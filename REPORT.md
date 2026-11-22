# Prediction Market Paper Bot — 2026-11-22 21:05 UTC

Fake money. Each strategy has its own fake bankroll. Win rate above breakeven in a price bucket = edge in that bucket.

## Strategy 1: AI forecasts

- Realized P&L: **$-41.51** (ROI -100.0% on $42 risked)
- Settled: 2 (won 0, 0%) | Open: 8 | Cash: $99,792.33 of $100,000
- Kalshi fees paid: $9.49 (included in all P&L above)

| Entry price | Trades | Win rate | Breakeven (incl. fees) | ROI |
|---|---|---|---|---|
| 0–15c | 1 | 0% | 14% | -100.0% |
| 40–60c | 1 | 0% | 50% | -100.0% |

## Strategy 2: Fade the longshot (rules only, no AI)

- Realized P&L: **$-37.75** (ROI -48.6% on $78 risked)
- Settled: 4 (won 2, 50%) | Open: 35 | Cash: $99,282.41 of $100,000
- Kalshi fees paid: $3.07 (included in all P&L above)

| Entry price | Trades | Win rate | Breakeven (incl. fees) | ROI |
|---|---|---|---|---|
| 85–100c | 4 | 50% | 95% | -48.6% |

## Is the AI smarter than the market?

Brier score (lower = better), 12 resolved predictions:

- AI: **0.1602**
- Market: **0.1446**
- Market is beating the AI so far (too few results to mean anything yet — need ~100+)

### AI calibration

| AI said | Count | Actually YES |
|---|---|---|
| 0–20% | 4 | 25% |
| 20–40% | 1 | 0% |
| 40–60% | 3 | 100% |
| 60–80% | 1 | 100% |
| 80–100% | 3 | 100% |

Total AI predictions logged: 47

## Last 20 trades

| Date | Strat | Market | Side | Price | AI | Mkt | Status | P&L |
|---|---|---|---|---|---|---|---|---|
| 2026-11-22 | flb | Will the upper bound of the federal funds rate be above | NO | 0.96 | - | 0.04 | open | - |
| 2026-11-21 | flb | The RSM Classic: Haotong Li wins | NO | 0.96 | - | 0.04 | open | - |
| 2026-11-21 | ai | Will the rate of CPI inflation be above 3.7% for the ye | YES | 0.37 | 0.94 | 0.36 | open | - |
| 2026-11-21 | flb | The RSM Classic: Rasmus Hojgaard wins | NO | 0.95 | - | 0.05 | open | - |
| 2026-11-21 | flb | The RSM Classic: Rasmus Neergaard-Petersen wins | NO | 0.91 | - | 0.09 | open | - |
| 2026-11-21 | flb | The RSM Classic: Adrien Dumont De Chassart wins | NO | 0.97 | - | 0.03 | open | - |
| 2026-11-20 | flb | The RSM Classic: Marco Penge wins | NO | 0.91 | - | 0.09 | open | - |
| 2026-11-20 | flb | The RSM Classic: Harris English wins | NO | 0.95 | - | 0.05 | open | - |
| 2026-11-20 | flb | The RSM Classic: Jesper Svensson wins | NO | 0.97 | - | 0.03 | open | - |
| 2026-11-20 | flb | The RSM Classic: Keith Mitchell wins | NO | 0.92 | - | 0.08 | open | - |
| 2026-11-19 | flb | The RSM Classic: Maverick McNealy wins | NO | 0.95 | - | 0.05 | open | - |
| 2026-11-19 | ai | Will CPI rise more than -0.1% in November 2026? — Above | YES | 0.41 | 0.62 | 0.41 | open | - |
| 2026-11-19 | ai | Violent Night 2 Rotten Tomatoes score? — Above 80 | YES | 0.09 | 0.27 | 0.09 | open | - |
| 2026-11-19 | flb | The RSM Classic: Max Greyserman wins | NO | 0.96 | - | 0.04 | open | - |
| 2026-11-19 | flb | Jackson Koivun leads at the end of Round 1 | NO | 0.98 | - | 0.03 | won | 0.42 |
| 2026-11-19 | flb | Will the Federal Reserve Hike rates by 0bps at their De | NO | 0.97 | - | 0.04 | open | - |
| 2026-11-18 | flb | Benjamin James leads at the end of Round 1 | NO | 0.97 | - | 0.03 | won | 0.5 |
| 2026-11-18 | flb | Will the Federal Reserve Hike rates by >25bps at their  | NO | 0.93 | - | 0.07 | open | - |
| 2026-11-18 | flb | CME Group Tour Championship: Jeeno Thitikul wins | NO | 0.91 | - | 0.10 | lost | -19.24 |
| 2026-11-18 | flb | The RSM Classic: Michael Thorbjornsen wins | NO | 0.97 | - | 0.03 | open | - |
