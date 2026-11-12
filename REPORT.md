# Prediction Market Paper Bot — 2026-11-12 17:03 UTC

Fake money. Each strategy has its own fake bankroll. Win rate above breakeven in a price bucket = edge in that bucket.

## Strategy 1: AI forecasts

- Realized P&L: **$-21.11** (ROI -100.0% on $21 risked)
- Settled: 1 (won 0, 0%) | Open: 0 | Cash: $99,978.89 of $100,000
- Kalshi fees paid: $1.22 (included in all P&L above)

| Entry price | Trades | Win rate | Breakeven (incl. fees) | ROI |
|---|---|---|---|---|
| 0–15c | 1 | 0% | 14% | -100.0% |

## Strategy 2: Fade the longshot (rules only, no AI)

- Realized P&L: **$+0.00** (ROI +0.0% on $0 risked)
- Settled: 0 (won 0, 0%) | Open: 2 | Cash: $99,960.53 of $100,000
- Kalshi fees paid: $0.12 (included in all P&L above)

## Is the AI smarter than the market?

Brier score (lower = better), 1 resolved predictions:

- AI: **0.2025**
- Market: **0.0156**
- Market is beating the AI so far (too few results to mean anything yet — need ~100+)

### AI calibration

| AI said | Count | Actually YES |
|---|---|---|
| 40–60% | 1 | 100% |

Total AI predictions logged: 2

## Last 20 trades

| Date | Strat | Market | Side | Price | AI | Mkt | Status | P&L |
|---|---|---|---|---|---|---|---|---|
| 2026-11-12 | flb | Will Pete Hegseth be out as Secretary of Defense before | NO | 0.95 | - | 0.06 | open | - |
| 2026-11-12 | flb | What will be Aaron Rodgers's next team? — Retires / No  | NO | 0.97 | - | 0.04 | open | - |
| 2026-11-12 | ai | Will Jensen Huang leave as Nvidia CEO before Dec 1, 202 | NO | 0.13 | 0.55 | 0.88 | lost | -21.11 |
