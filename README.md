# Prediction Market Paper Bot

Claude forecasts live Kalshi markets and paper-trades the ones it disagrees with. **No real money and no Kalshi account.** It uses only Kalshi's public market data.

## How it works
- **Hourly light run (free):** settles finished markets, places fade-the-longshot trades, updates the report. No AI calls.
- **Daily full run (about 7am Pacific):** everything above plus the AI forecasts, which are the part that costs money.

Steps:
1. **Settle:** checks Kalshi for resolved markets and scores past predictions and trades.
2. **Scan:** finds up to 25 markets with **$50K+ traded in the last 24h** and a spread of 4c or less, that close in 1–21 days. Claude researches each one with web search (prediction market sites are blocked) and gives a probability **without seeing the market price**.
3. **Trade:** if Claude's number beats the price by 8+ points, it buys $20 of YES or NO at the ask, paying Kalshi's taker fee. **Longshot rule:** anything priced under 15c needs a 10+ point edge.
4. **Benchmark strategy (no AI, free):** "Fade the longshot" buys NO on up to 10 liquid markets priced 3–15c YES. This is based on Kalshi research showing cheap contracts lose most of their money. It has its own $1,000 fake bankroll, so you can see whether the AI beats a dumb rule.
5. **Report:** writes `REPORT.md` with P&L, win rate, ROI, calibration, and **Brier score of AI vs. market**. The Brier score is the stat that matters.

All data is saved in `data/predictions.csv` (every forecast, traded or not) and `data/trades.csv`.

## Setup (about 10 minutes)
1. Create a new **private** GitHub repo and upload these files. Keep the `.github/workflows/` folder path exactly as it is.
2. Get an Anthropic API key at console.anthropic.com and add a few dollars of credit.
3. In the repo, go to **Settings → Secrets and variables → Actions → New repository secret**. Name it `ANTHROPIC_API_KEY` and paste the key.
4. Go to **Actions** → **Prediction market paper bot** → **Run workflow** to test it now. After that it runs every day by itself.
5. Open `REPORT.md` in the repo to see the scoreboard.

## Settings (optional)
Set these under **Settings → Secrets and variables → Actions → Variables**:

| Variable | Default | What it does |
|---|---|---|
| `MAX_MARKETS_PER_RUN` | 25 | Markets checked per day. This is the main cost lever. |
| `MIN_EDGE` | 0.08 | How far Claude has to disagree with the price before it trades |
| `MODEL` | claude-sonnet-5-5 | Change to `claude-haiku-5-5` for a cheaper test |
| `MIN_VOLUME_24H` | 10000 | Minimum 24h volume (≈ dollars). Lower it if the log says 0 markets were picked. |
| `STARTING_BANKROLL` | 100000 | Fake bankroll per strategy |
| `STAKE_PER_TRADE` | 20 | Fake $ per trade |
| `FLB_MAX_PER_RUN` | 1 | Longshot trades per run (25 runs/day = 25 max/day) |
| `FLB_ENABLED` | 1 | Set to 0 to turn off the fade-the-longshot strategy |

## Cost
Each market is roughly 1 Claude call plus up to 3 web searches ($0.01 each). Expect about **$0.50–1.50/day** at 8 markets. Check your Anthropic console after the first run and adjust.

## Reading the results
- **Ignore P&L for the first ~100 resolved predictions.** With a small sample, it's mostly luck.
- **Brier score AI < Market** over 100+ resolved predictions means the AI has a real edge. **AI > Market** means the market is smarter, which is the normal result.
- Check the **entry price tables**. If the win rate is above breakeven in a bucket, the strategy has an edge there. Check them monthly.
- Check the calibration table. When the AI says 70%, those events should happen about 70% of the time.

## Run locally
```
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-...
python bot.py run        # or: settle | scan | report
```
