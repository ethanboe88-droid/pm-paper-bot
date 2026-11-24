# Prediction Market Paper Bot — 2026-11-24 23:56 UTC

Fake money. Each strategy has its own fake bankroll. Win rate above breakeven in a price bucket = edge in that bucket.

## Strategy 1: AI forecasts

- Realized P&L: **$-15.06** (ROI -24.3% on $62 risked)
- Settled: 3 (won 1, 33%) | Open: 11 | Cash: $99,755.55 of $100,000
- Kalshi fees paid: $13.72 (included in all P&L above)

| Entry price | Trades | Win rate | Breakeven (incl. fees) | ROI |
|---|---|---|---|---|
| 0–15c | 1 | 0% | 14% | -100.0% |
| 40–60c | 2 | 50% | 47% | +14.8% |

## Strategy 2: Fade the longshot (rules only, no AI)

- Realized P&L: **$-59.81** (ROI -12.3% on $485 risked)
- Settled: 25 (won 21, 84%) | Open: 21 | Cash: $99,530.25 of $100,000
- Kalshi fees paid: $3.59 (included in all P&L above)

| Entry price | Trades | Win rate | Breakeven (incl. fees) | ROI |
|---|---|---|---|---|
| 85–100c | 25 | 84% | 95% | -12.3% |

## Is the AI smarter than the market?

Brier score (lower = better), 21 resolved predictions:

- AI: **0.1862**
- Market: **0.1876**
- AI is beating the market so far (too few results to mean anything yet — need ~100+)

### AI calibration

| AI said | Count | Actually YES |
|---|---|---|
| 0–20% | 10 | 30% |
| 20–40% | 1 | 0% |
| 40–60% | 4 | 100% |
| 60–80% | 2 | 100% |
| 80–100% | 4 | 100% |

Total AI predictions logged: 59

## Last 20 trades

| Date | Strat | Market | Side | Price | AI | Mkt | Status | P&L |
|---|---|---|---|---|---|---|---|---|
| 2026-11-24 | flb | BMW Australian PGA Championship: Cameron Smith wins | NO | 0.97 | - | 0.03 | open | - |
| 2026-11-24 | ai | Will the rate of CPI inflation be above 3.8% for the ye | YES | 0.07 | 0.32 | 0.07 | open | - |
| 2026-11-24 | ai | Hiroki Moriya wins | NO | 0.55 | 0.25 | 0.46 | open | - |
| 2026-11-24 | ai | Matteo Covato wins | NO | 0.28 | 0.12 | 0.72 | open | - |
| 2026-11-24 | flb | Nicolas Villalon Valdes wins | NO | 0.90 | - | 0.11 | won | 2.06 |
| 2026-11-24 | flb | Gabriela Agra Amorim wins | NO | 0.97 | - | 0.04 | won | 0.55 |
| 2026-11-24 | flb | BMW Australian PGA Championship: Min Woo Lee wins | NO | 0.96 | - | 0.06 | open | - |
| 2026-11-24 | flb | Will CPI rise more than 0.0% in November 2026? — Above  | NO | 0.93 | - | 0.07 | open | - |
| 2026-11-24 | ai | Will CPI rise more than 0.0% in November 2026? — Above  | YES | 0.08 | 0.42 | 0.07 | open | - |
| 2026-11-23 | flb | Will the rate of CPI inflation be above 3.8% for the ye | NO | 0.95 | - | 0.06 | open | - |
| 2026-11-23 | flb | Anastasiia Hnidets wins | NO | 0.97 | - | 0.04 | won | 0.55 |
| 2026-11-22 | flb | Will the upper bound of the federal funds rate be above | NO | 0.96 | - | 0.04 | open | - |
| 2026-11-21 | flb | The RSM Classic: Haotong Li wins | NO | 0.96 | - | 0.04 | won | 0.74 |
| 2026-11-21 | ai | Will the rate of CPI inflation be above 3.7% for the ye | YES | 0.37 | 0.94 | 0.36 | open | - |
| 2026-11-21 | flb | The RSM Classic: Rasmus Hojgaard wins | NO | 0.95 | - | 0.05 | won | 0.87 |
| 2026-11-21 | flb | The RSM Classic: Rasmus Neergaard-Petersen wins | NO | 0.91 | - | 0.09 | won | 1.76 |
| 2026-11-21 | flb | The RSM Classic: Adrien Dumont De Chassart wins | NO | 0.97 | - | 0.03 | won | 0.61 |
| 2026-11-20 | flb | The RSM Classic: Marco Penge wins | NO | 0.91 | - | 0.09 | lost | -19.31 |
| 2026-11-20 | flb | The RSM Classic: Harris English wins | NO | 0.95 | - | 0.05 | won | 0.85 |
| 2026-11-20 | flb | The RSM Classic: Jesper Svensson wins | NO | 0.97 | - | 0.03 | won | 0.59 |
