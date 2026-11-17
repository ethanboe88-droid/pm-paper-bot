# Prediction Market Paper Bot — 2026-11-17 14:52 UTC

Fake money. Each strategy has its own fake bankroll. Win rate above breakeven in a price bucket = edge in that bucket.

## Strategy 1: AI forecasts

- Realized P&L: **$-21.11** (ROI -100.0% on $21 risked)
- Settled: 1 (won 0, 0%) | Open: 6 | Cash: $99,854.96 of $100,000
- Kalshi fees paid: $6.50 (included in all P&L above)

| Entry price | Trades | Win rate | Breakeven (incl. fees) | ROI |
|---|---|---|---|---|
| 0–15c | 1 | 0% | 14% | -100.0% |

## Strategy 2: Fade the longshot (rules only, no AI)

- Realized P&L: **$+0.00** (ROI +0.0% on $0 risked)
- Settled: 0 (won 0, 0%) | Open: 20 | Cash: $99,610.67 of $100,000
- Kalshi fees paid: $1.68 (included in all P&L above)

## Is the AI smarter than the market?

Brier score (lower = better), 4 resolved predictions:

- AI: **0.1003**
- Market: **0.0614**
- Market is beating the AI so far (too few results to mean anything yet — need ~100+)

### AI calibration

| AI said | Count | Actually YES |
|---|---|---|
| 40–60% | 1 | 100% |
| 60–80% | 1 | 100% |
| 80–100% | 2 | 100% |

Total AI predictions logged: 21

## Last 20 trades

| Date | Strat | Market | Side | Price | AI | Mkt | Status | P&L |
|---|---|---|---|---|---|---|---|---|
| 2026-11-17 | flb | The RSM Classic: Blades Brown wins | NO | 0.97 | - | 0.04 | open | - |
| 2026-11-17 | flb | The RSM Classic: Ben Kohles wins | NO | 0.98 | - | 0.04 | open | - |
| 2026-11-16 | flb | The RSM Classic: Michael Brennan wins | NO | 0.95 | - | 0.05 | open | - |
| 2026-11-16 | ai | Nitto ATP Singles Finals: Carlos Alcaraz wins | NO | 0.48 | 0.43 | 0.53 | open | - |
| 2026-11-16 | flb | The RSM Classic: Jackson Koivun wins | NO | 0.96 | - | 0.04 | open | - |
| 2026-11-16 | flb | Will the President sign more than 4 Executive Orders be | NO | 0.98 | - | 0.03 | open | - |
| 2026-11-15 | flb | Will BTC trimmed mean be above $90000.00 by 11:59 PM ET | NO | 0.97 | - | 0.04 | open | - |
| 2026-11-15 | flb | Will BTC trimmed mean be above $87500.00 by 11:59 PM ET | NO | 0.96 | - | 0.04 | open | - |
| 2026-11-14 | flb | Will BTC trimmed mean be above $85000.00 by 11:59 PM ET | NO | 0.98 | - | 0.03 | open | - |
| 2026-11-14 | ai | Will it be confirmed that a software or configuration e | NO | 0.40 | 0.35 | 0.61 | open | - |
| 2026-11-14 | flb | Will it be confirmed that accidental damage to a cable, | NO | 0.92 | - | 0.09 | open | - |
| 2026-11-14 | flb | Will it be confirmed that human error caused the FAA's  | NO | 0.87 | - | 0.14 | open | - |
| 2026-11-14 | flb | Will it be confirmed that an error by an AI system or A | NO | 0.92 | - | 0.09 | open | - |
| 2026-11-14 | flb | Will it be confirmed that a problem with the FAA's SMAR | NO | 0.93 | - | 0.07 | open | - |
| 2026-11-13 | flb | Will the unemployment rate (U-3) be above 4.2% in Novem | NO | 0.91 | - | 0.10 | open | - |
| 2026-11-13 | ai | Will Jensen Huang talk to Trump before Dec 1, 2026? | YES | 0.42 | 0.55 | 0.40 | open | - |
| 2026-11-13 | ai | Will Howard Lutnick be out as Commerce Secretary before | NO | 0.57 | 0.25 | 0.43 | open | - |
| 2026-11-13 | flb | Will Jensen Huang testify in front of Congress before D | NO | 0.88 | - | 0.12 | open | - |
| 2026-11-13 | flb | Hexed Rotten Tomatoes score? — Above 90 | NO | 0.95 | - | 0.06 | open | - |
| 2026-11-13 | flb | Will BTC trimmed mean be below $57500.00 by 11:59 PM ET | NO | 0.92 | - | 0.09 | open | - |
