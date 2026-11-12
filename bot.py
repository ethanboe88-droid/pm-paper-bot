"""
Prediction market paper trading bot (Kalshi data + Claude forecasts).

No real money. Every run:
  1. settle  - checks open paper trades / predictions against Kalshi results
  2. scan    - picks liquid markets, asks Claude for a BLIND probability
               (it never sees the market price), paper-trades if the edge is big enough
  3. report  - writes REPORT.md: bankroll, ROI, win rate, and the key stat:
               Brier score of Claude vs. the market

Usage:
  python bot.py run       # settle + AI scan + FLB + report (daily)
  python bot.py light     # settle + FLB + report, no AI calls (hourly, free)
  python bot.py settle
  python bot.py scan      # AI strategy
  python bot.py flb       # rules-only fade-the-longshot strategy
  python bot.py report
"""

import csv
import json
import math
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

# ----------------------------------------------------------------------------
# Config (override any of these with environment variables / GitHub secrets)
# ----------------------------------------------------------------------------
KALSHI_BASE = os.getenv("KALSHI_BASE", "https://api.elections.kalshi.com/trade-api/v2")
ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "")
MODEL = os.getenv("MODEL", "claude-sonnet-5-5")

STARTING_BANKROLL = float(os.getenv("STARTING_BANKROLL", "1000"))
STAKE_PER_TRADE = float(os.getenv("STAKE_PER_TRADE", "20"))      # $ per paper trade
MIN_EDGE = float(os.getenv("MIN_EDGE", "0.08"))                  # model must beat price by 8 pts
MAX_MARKETS_PER_RUN = int(os.getenv("MAX_MARKETS_PER_RUN", "8"))  # controls API cost
MIN_DAYS_TO_CLOSE = float(os.getenv("MIN_DAYS_TO_CLOSE", "1"))
MAX_DAYS_TO_CLOSE = float(os.getenv("MAX_DAYS_TO_CLOSE", "21"))  # short = fast feedback
# Kalshi volume is in contracts; each matched contract = $1 of face value,
# so 50000 ≈ $50K traded in the last 24h
MIN_VOLUME_24H = float(os.getenv("MIN_VOLUME_24H", "50000"))
MAX_SPREAD = float(os.getenv("MAX_SPREAD", "0.04"))
MIN_PRICE, MAX_PRICE = 0.05, 0.95                                 # AI only forecasts 5-95% markets
# Favorite-longshot rule: buying anything under 15c needs a bigger edge
LONGSHOT_PRICE = float(os.getenv("LONGSHOT_PRICE", "0.15"))
LONGSHOT_MIN_EDGE = float(os.getenv("LONGSHOT_MIN_EDGE", "0.10"))
# Rules-only "fade the longshot" strategy (no AI, no API cost) as a benchmark
FLB_ENABLED = os.getenv("FLB_ENABLED", "1") == "1"
FLB_MAX_PER_RUN = int(os.getenv("FLB_MAX_PER_RUN", "10"))
FLB_MIN_MID, FLB_MAX_MID = 0.03, LONGSHOT_PRICE                   # longshots to fade
WEB_SEARCHES_PER_MARKET = int(os.getenv("WEB_SEARCHES_PER_MARKET", "3"))

DATA = Path(os.getenv("DATA_DIR", "data"))
PRED_FILE = DATA / "predictions.csv"
TRADE_FILE = DATA / "trades.csv"
REPORT_FILE = Path(os.getenv("REPORT_FILE", "REPORT.md"))

PRED_COLS = ["ts", "ticker", "event_ticker", "question", "close_time",
             "yes_bid", "yes_ask", "market_mid", "model_p", "confidence",
             "reasoning", "model", "action", "outcome", "settled_ts"]
TRADE_COLS = ["id", "strategy", "ts", "ticker", "question", "side", "price", "contracts",
              "cost", "fee", "model_p", "market_mid", "edge", "status",
              "payout", "pnl", "settled_ts"]


# ----------------------------------------------------------------------------
# CSV helpers
# ----------------------------------------------------------------------------
def load(path, cols):
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return [{c: r.get(c, "") for c in cols} for r in csv.DictReader(f)]


def save(path, rows, cols):
    DATA.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)


def now():
    return datetime.now(timezone.utc)


def f(x, default=None):
    try:
        return float(x)
    except (TypeError, ValueError):
        return default


# ----------------------------------------------------------------------------
# Kalshi (public market data, no account needed)
# ----------------------------------------------------------------------------
def kalshi_get(path, params=None):
    for attempt in range(4):
        r = requests.get(f"{KALSHI_BASE}{path}", params=params, timeout=30)
        if r.status_code == 429:
            time.sleep(2 ** attempt)
            continue
        r.raise_for_status()
        return r.json()
    r.raise_for_status()


def fetch_open_markets(max_pages=5):
    t = now()
    params = {
        "status": "open",
        "limit": 1000,
        "mve_filter": "exclude",  # skip parlay/combo markets
        "min_close_ts": int((t + timedelta(days=MIN_DAYS_TO_CLOSE)).timestamp()),
        "max_close_ts": int((t + timedelta(days=MAX_DAYS_TO_CLOSE)).timestamp()),
    }
    markets, cursor = [], None
    for _ in range(max_pages):
        if cursor:
            params["cursor"] = cursor
        data = kalshi_get("/markets", params)
        markets += data.get("markets", [])
        cursor = data.get("cursor")
        if not cursor:
            break
    return markets


def question_text(m):
    title = (m.get("title") or "").strip()
    sub = (m.get("yes_sub_title") or m.get("subtitle") or "").strip()
    return f"{title} — {sub}" if sub and sub.lower() not in title.lower() else title


def liquid(m):
    bid, ask = f(m.get("yes_bid_dollars")), f(m.get("yes_ask_dollars"))
    if m.get("market_type", "binary") != "binary" or bid is None or ask is None:
        return None
    if bid <= 0 or ask >= 1 or ask - bid > MAX_SPREAD:
        return None
    if f(m.get("volume_24h_fp"), 0) < MIN_VOLUME_24H:
        return None
    return (bid + ask) / 2


def pick_candidates(markets, already_seen, lo=MIN_PRICE, hi=MAX_PRICE, limit=MAX_MARKETS_PER_RUN, one_per_event=True):
    picked, seen_events = [], set()
    good = []
    for m in markets:
        mid = liquid(m)
        if mid is None or not (lo <= mid <= hi) or m["ticker"] in already_seen:
            continue
        good.append((f(m.get("volume_24h_fp"), 0), m))
    good.sort(key=lambda x: x[0], reverse=True)
    for _, m in good:
        ev = m.get("event_ticker")
        if one_per_event and ev in seen_events:  # one market per event = more variety
            continue
        seen_events.add(ev)
        picked.append(m)
        if len(picked) >= limit:
            break
    return picked


# ----------------------------------------------------------------------------
# Claude forecast (blind: never shown the market price)
# ----------------------------------------------------------------------------
PROMPT = """You are a careful forecaster. Today is {today} (UTC).

Question: {question}
Market closes: {close_time}

Resolution rules:
{rules}

Research the question with web search if useful, then estimate the probability
that this resolves YES. Think about base rates, the latest news, and exactly how
the rules define YES. Do not look up prediction market or betting odds for this question.

End your answer with ONLY this JSON on the last line:
{{"probability": <0.01-0.99>, "confidence": "low|medium|high", "reasoning": "<one or two sentences>"}}"""


def ask_claude(m):
    if not ANTHROPIC_KEY:
        raise RuntimeError("ANTHROPIC_API_KEY is not set")
    rules = (m.get("rules_primary") or "") + "\n" + (m.get("rules_secondary") or "")
    messages = [{"role": "user", "content": PROMPT.format(
        today=now().strftime("%Y-%m-%d %H:%M"),
        question=question_text(m),
        close_time=m.get("close_time"),
        rules=rules.strip()[:4000] or "(none provided)",
    )}]
    tools = []
    if WEB_SEARCHES_PER_MARKET > 0:
        tools = [{
            "type": "web_search_20250305",
            "name": "web_search",
            "max_uses": WEB_SEARCHES_PER_MARKET,
            # keep it from just copying the market's price
            "blocked_domains": ["kalshi.com", "polymarket.com", "manifold.markets",
                                "predictit.org", "metaculus.com"],
        }]
    text = ""
    for _ in range(3):  # handle pause_turn on long searches
        body = {"model": MODEL, "max_tokens": 2000, "messages": messages}
        if tools:
            body["tools"] = tools
        r = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={"x-api-key": ANTHROPIC_KEY,
                     "anthropic-version": "2023-06-01",
                     "content-type": "application/json"},
            json=body, timeout=180,
        )
        r.raise_for_status()
        resp = r.json()
        text += "".join(b.get("text", "") for b in resp["content"] if b.get("type") == "text")
        if resp.get("stop_reason") != "pause_turn":
            break
        messages.append({"role": "assistant", "content": resp["content"]})
    return parse_forecast(text)


def parse_forecast(text):
    matches = re.findall(r"\{[^{}]*\"probability\"[^{}]*\}", text, re.S)
    if not matches:
        raise ValueError(f"No forecast JSON in response: {text[-300:]}")
    d = json.loads(matches[-1])
    p = min(max(float(d["probability"]), 0.01), 0.99)
    return p, str(d.get("confidence", "")), str(d.get("reasoning", ""))[:500]


# ----------------------------------------------------------------------------
# Paper trading
# ----------------------------------------------------------------------------
_fee_mult_cache = {}


def fee_multiplier(m):
    """Some Kalshi series carry a non-standard fee multiplier (M). Default 1."""
    series = (m.get("event_ticker") or m.get("ticker") or "").split("-")[0]
    if series not in _fee_mult_cache:
        mult = 1.0
        try:
            s = kalshi_get(f"/series/{series}").get("series", {})
            mult = f(s.get("fee_multiplier"), 1.0) or 1.0
        except Exception:
            pass
        _fee_mult_cache[series] = mult
    return _fee_mult_cache[series]


def kalshi_fee(contracts, price, mult=1.0):
    # Kalshi taker fee: round up(M * 0.07 * C * P * (1-P)) to the cent. No settlement fee.
    return math.ceil(round(mult * 0.07 * contracts * price * (1 - price) * 100, 6)) / 100


def decide(model_p, m):
    yes_ask = f(m.get("yes_ask_dollars"))
    no_ask = f(m.get("no_ask_dollars")) or (1 - f(m.get("yes_bid_dollars")))
    yes_edge = model_p - yes_ask
    no_edge = (1 - model_p) - no_ask
    need = lambda price: LONGSHOT_MIN_EDGE if price < LONGSHOT_PRICE else MIN_EDGE
    if yes_edge >= need(yes_ask) and yes_edge >= no_edge:
        return "YES", yes_ask, yes_edge
    if no_edge >= need(no_ask):
        return "NO", no_ask, no_edge
    return None, None, max(yes_edge, no_edge)


def strat(t):
    return t.get("strategy") or "ai"


def cash_available(trades, strategy="ai"):
    cash = STARTING_BANKROLL
    for t in trades:
        if strat(t) != strategy:
            continue
        cash -= f(t["cost"], 0) + f(t["fee"], 0)
        cash += f(t["payout"], 0)
    return cash


def scan():
    preds = load(PRED_FILE, PRED_COLS)
    trades = load(TRADE_FILE, TRADE_COLS)
    seen = {p["ticker"] for p in preds}
    markets = fetch_open_markets()
    picks = pick_candidates(markets, seen)
    print(f"{len(markets)} open markets in window -> {len(picks)} picked")

    for m in picks:
        q = question_text(m)
        try:
            model_p, conf, why = ask_claude(m)
        except Exception as e:
            print(f"  skip {m['ticker']}: {e}")
            continue
        bid, ask = f(m["yes_bid_dollars"]), f(m["yes_ask_dollars"])
        mid = round((bid + ask) / 2, 4)
        side, price, edge = decide(model_p, m)
        action = "none"

        if side:
            contracts = int(STAKE_PER_TRADE // price)
            cost = round(contracts * price, 2)
            fee = kalshi_fee(contracts, price, fee_multiplier(m))
            if contracts > 0 and cash_available(trades) >= cost + fee:
                action = f"BUY {side}"
                trades.append({
                    "id": f"{m['ticker']}-{int(time.time())}", "strategy": "ai",
                    "ts": now().isoformat(timespec="seconds"),
                    "ticker": m["ticker"], "question": q, "side": side,
                    "price": price, "contracts": contracts, "cost": cost, "fee": fee,
                    "model_p": model_p, "market_mid": mid, "edge": round(edge, 4),
                    "status": "open", "payout": "", "pnl": "", "settled_ts": "",
                })
            else:
                action = f"{side} (skipped: no cash)"

        preds.append({
            "ts": now().isoformat(timespec="seconds"),
            "ticker": m["ticker"], "event_ticker": m.get("event_ticker", ""),
            "question": q, "close_time": m.get("close_time", ""),
            "yes_bid": bid, "yes_ask": ask, "market_mid": mid,
            "model_p": model_p, "confidence": conf, "reasoning": why,
            "model": MODEL, "action": action, "outcome": "", "settled_ts": "",
        })
        print(f"  {q[:70]:70} mkt {mid:.2f} | AI {model_p:.2f} | {action}")
        # save after each market so a crash never loses paid-for forecasts
        save(PRED_FILE, preds, PRED_COLS)
        save(TRADE_FILE, trades, TRADE_COLS)


def flb_scan():
    """Rules-only benchmark: buy the favorite side of liquid longshot markets."""
    trades = load(TRADE_FILE, TRADE_COLS)
    seen = {t["ticker"] for t in trades if strat(t) == "flb"}
    picks = pick_candidates(fetch_open_markets(), seen, FLB_MIN_MID, FLB_MAX_MID,
                            FLB_MAX_PER_RUN, one_per_event=False)
    print(f"FLB: {len(picks)} longshots to fade")
    for m in picks:
        bid = f(m["yes_bid_dollars"])
        price = f(m.get("no_ask_dollars")) or round(1 - bid, 2)
        contracts = int(STAKE_PER_TRADE // price)
        cost, fee = round(contracts * price, 2), kalshi_fee(contracts, price, fee_multiplier(m))
        if contracts <= 0 or cash_available(trades, "flb") < cost + fee:
            print("  FLB out of cash"); break
        mid = round((bid + f(m["yes_ask_dollars"])) / 2, 4)
        trades.append({
            "id": f"{m['ticker']}-flb-{int(time.time())}", "strategy": "flb",
            "ts": now().isoformat(timespec="seconds"), "ticker": m["ticker"],
            "question": question_text(m), "side": "NO", "price": price,
            "contracts": contracts, "cost": cost, "fee": fee, "model_p": "",
            "market_mid": mid, "edge": "", "status": "open", "payout": "",
            "pnl": "", "settled_ts": "",
        })
        print(f"  FLB NO @ {price:.2f}  {question_text(m)[:70]}")
    save(TRADE_FILE, trades, TRADE_COLS)


def settle():
    preds = load(PRED_FILE, PRED_COLS)
    trades = load(TRADE_FILE, TRADE_COLS)
    pending = {p["ticker"] for p in preds if not p["outcome"]}
    pending |= {t["ticker"] for t in trades if t["status"] == "open"}
    results = {}
    for tk in pending:
        try:
            m = kalshi_get(f"/markets/{tk}")["market"]
        except Exception as e:
            print(f"  could not check {tk}: {e}")
            continue
        res = (m.get("result") or "").lower()
        if res in ("yes", "no"):
            results[tk] = res
        elif m.get("status") in ("finalized", "determined") and res == "":
            results[tk] = "void"
    ts = now().isoformat(timespec="seconds")
    for p in preds:
        if not p["outcome"] and p["ticker"] in results:
            p["outcome"], p["settled_ts"] = results[p["ticker"]], ts
    for t in trades:
        if t["status"] == "open" and t["ticker"] in results:
            res = results[t["ticker"]]
            if res == "void":
                payout = f(t["cost"])  # refunded
                t["status"] = "void"
            else:
                won = res == t["side"].lower()
                payout = float(t["contracts"]) if won else 0.0
                t["status"] = "won" if won else "lost"
            t["payout"] = round(payout, 2)
            t["pnl"] = round(payout - f(t["cost"]) - f(t["fee"]), 2)
            t["settled_ts"] = ts
    save(PRED_FILE, preds, PRED_COLS)
    save(TRADE_FILE, trades, TRADE_COLS)
    print(f"Settled {len(results)} markets")


# ----------------------------------------------------------------------------
# Report
# ----------------------------------------------------------------------------
def money_section(trades, name, label):
    ts = [t for t in trades if strat(t) == name]
    closed = [t for t in ts if t["status"] in ("won", "lost")]
    open_ = [t for t in ts if t["status"] == "open"]
    realized = sum(f(t["pnl"], 0) for t in ts if t["status"] in ("won", "lost", "void"))
    risked = sum(f(t["cost"], 0) + f(t["fee"], 0) for t in closed)
    wins = sum(t["status"] == "won" for t in closed)
    fees = sum(f(t["fee"], 0) for t in ts)
    out = [f"## {label}", "",
           f"- Realized P&L: **${realized:+,.2f}** "
           f"(ROI {(realized / risked * 100) if risked else 0:+.1f}% on ${risked:,.0f} risked)",
           f"- Settled: {len(closed)} (won {wins}, {(wins / len(closed) * 100) if closed else 0:.0f}%)"
           f" | Open: {len(open_)} | Cash: ${cash_available(trades, name):,.2f} of ${STARTING_BANKROLL:,.0f}",
           f"- Kalshi fees paid: ${fees:,.2f} (included in all P&L above)", ""]
    if closed:
        out += ["| Entry price | Trades | Win rate | Breakeven (incl. fees) | ROI |", "|---|---|---|---|---|"]
        for lo, hi in [(0, .15), (.15, .40), (.40, .60), (.60, .75), (.75, .85), (.85, 1.01)]:
            b = [t for t in closed if lo <= f(t["price"]) < hi]
            if not b:
                continue
            w = sum(t["status"] == "won" for t in b)
            pnl = sum(f(t["pnl"]) for t in b)
            risk = sum(f(t["cost"]) + f(t["fee"]) for t in b)
            avg_p = risk / sum(f(t["contracts"]) for t in b)  # cost per contract incl. fee
            out.append(f"| {lo * 100:.0f}–{min(hi, 1) * 100:.0f}c | {len(b)} | {w / len(b) * 100:.0f}% | "
                       f"{avg_p * 100:.0f}% | {pnl / risk * 100:+.1f}% |")
        out.append("")
    return out


def report():
    preds = load(PRED_FILE, PRED_COLS)
    trades = load(TRADE_FILE, TRADE_COLS)
    resolved = [p for p in preds if p["outcome"] in ("yes", "no")]

    lines = [f"# Prediction Market Paper Bot — {now():%Y-%m-%d %H:%M} UTC", "",
             "Fake money. Each strategy has its own fake bankroll. "
             "Win rate above breakeven in a price bucket = edge in that bucket.", ""]
    lines += money_section(trades, "ai", "Strategy 1: AI forecasts")
    if FLB_ENABLED or any(strat(t) == "flb" for t in trades):
        lines += money_section(trades, "flb", "Strategy 2: Fade the longshot (rules only, no AI)")

    lines += ["## Is the AI smarter than the market?", ""]
    if resolved:
        o = [1.0 if p["outcome"] == "yes" else 0.0 for p in resolved]
        ai = [f(p["model_p"]) for p in resolved]
        mk = [f(p["market_mid"]) for p in resolved]
        b_ai = sum((a - y) ** 2 for a, y in zip(ai, o)) / len(o)
        b_mk = sum((a - y) ** 2 for a, y in zip(mk, o)) / len(o)
        verdict = "AI is beating the market" if b_ai < b_mk else "Market is beating the AI"
        lines += [f"Brier score (lower = better), {len(resolved)} resolved predictions:", "",
                  f"- AI: **{b_ai:.4f}**",
                  f"- Market: **{b_mk:.4f}**",
                  f"- {verdict} so far" + (" (too few results to mean anything yet — need ~100+)" if len(resolved) < 100 else ""),
                  "", "### AI calibration", "", "| AI said | Count | Actually YES |", "|---|---|---|"]
        for lo in range(0, 100, 20):
            b = [y for a, y in zip(ai, o) if lo / 100 <= a < (lo + 20) / 100 or (lo == 80 and a == 1)]
            if b:
                lines.append(f"| {lo}–{lo + 20}% | {len(b)} | {sum(b) / len(b) * 100:.0f}% |")
    else:
        lines.append("No predictions have resolved yet.")
    lines += ["", f"Total AI predictions logged: {len(preds)}", ""]

    if trades:
        lines += ["## Last 20 trades", "", "| Date | Strat | Market | Side | Price | AI | Mkt | Status | P&L |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for t in trades[-20:][::-1]:
            ai_p = f"{f(t['model_p']):.2f}" if t["model_p"] else "-"
            lines.append(f"| {t['ts'][:10]} | {strat(t)} | {t['question'][:55]} | {t['side']} | {f(t['price']):.2f} | "
                         f"{ai_p} | {f(t['market_mid']):.2f} | {t['status']} | {t['pnl'] or '-'} |")
    REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:20]))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "run"
    if cmd in ("settle", "run", "light"):
        settle()
    if cmd in ("scan", "run"):
        scan()
    if cmd in ("flb", "run", "light") and FLB_ENABLED:
        flb_scan()
    if cmd in ("report", "run", "light"):
        report()
