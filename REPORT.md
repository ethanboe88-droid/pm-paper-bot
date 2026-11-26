# Prediction Market Paper Bot — 2026-11-26 01:10 UTC

Fake money. Each strategy has its own fake bankroll. Win rate above breakeven in a price bucket = edge in that bucket.

## Strategy 1: AI forecasts

- Realized P&L: **$+29.54** (ROI +23.7% on $124 risked)
- Settled: 6 (won 3, 50%) | Open: 11 | Cash: $99,800.65 of $100,000
- Kalshi fees paid: $16.13 (included in all P&L above)

| Entry price | Trades | Win rate | Breakeven (incl. fees) | ROI |
|---|---|---|---|---|
| 0–15c | 2 | 0% | 14% | -100.0% |
| 15–40c | 1 | 100% | 29% | +239.9% |
| 40–60c | 3 | 67% | 49% | +35.2% |

## Strategy 2: Fade the longshot (rules only, no AI)

- Realized P&L: **$-59.81** (ROI -12.3% on $485 risked)
- Settled: 25 (won 21, 84%) | Open: 25 | Cash: $99,452.25 of $100,000
- Kalshi fees paid: $3.83 (included in all P&L above)

| Entry price | Trades | Win rate | Breakeven (incl. fees) | ROI |
|---|---|---|---|---|
| 85–100c | 25 | 84% | 95% | -12.3% |

## Is the AI smarter than the market?

Brier score (lower = better), 27 resolved predictions:

- AI: **0.1963**
- Market: **0.1890**
- Market is beating the AI so far (too few results to mean anything yet — need ~100+)

### AI calibration

| AI said | Count | Actually YES |
|---|---|---|
| 0–20% | 12 | 33% |
| 20–40% | 3 | 0% |
| 40–60% | 5 | 100% |
| 60–80% | 2 | 100% |
| 80–100% | 5 | 100% |

Total AI predictions logged: 68

## Last 20 trades

| Date | Strat | Market | Side | Price | AI | Mkt | Status | P&L |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 | flb | BMW Australian PGA Championship: Nicolai Hojgaard wins | NO | 0.97 | - | 0.04 | open | - |
| 2026-11-25 | flb | BMW Australian PGA Championship: Elvis Smylie wins | NO | 0.97 | - | 0.04 | open | - |
| 2026-11-25 | ai | What will Jensen Huang say during NVIDIA GTC Washington | YES | 0.55 | 0.82 | 0.54 | open | - |
| 2026-11-25 | ai | Jason Kubler wins | NO | 0.39 | 0.33 | 0.61 | open | - |
| 2026-11-25 | ai | Luis Guto Miguel wins | YES | 0.33 | 0.50 | 0.33 | open | - |
| 2026-11-25 | flb | BMW Australian PGA Championship: Marc Leishman wins | NO | 0.97 | - | 0.03 | open | - |
| 2026-11-25 | flb | BMW Australian PGA Championship: Lucas Herbert wins | NO | 0.94 | - | 0.06 | open | - |
| 2026-11-24 | flb | BMW Australian PGA Championship: Cameron Smith wins | NO | 0.97 | - | 0.03 | open | - |
| 2026-11-24 | ai | Will the rate of CPI inflation be above 3.8% for the ye | YES | 0.07 | 0.32 | 0.07 | open | - |
| 2026-11-24 | ai | Hiroki Moriya wins | NO | 0.55 | 0.25 | 0.46 | won | 15.57 |
| 2026-11-24 | ai | Matteo Covato wins | NO | 0.28 | 0.12 | 0.72 | won | 50.11 |
| 2026-11-24 | flb | Nicolas Villalon Valdes wins | NO | 0.90 | - | 0.11 | won | 2.06 |
| 2026-11-24 | flb | Gabriela Agra Amorim wins | NO | 0.97 | - | 0.04 | won | 0.55 |
| 2026-11-24 | flb | BMW Australian PGA Championship: Min Woo Lee wins | NO | 0.96 | - | 0.06 | open | - |
| 2026-11-24 | flb | Will CPI rise more than 0.0% in November 2026? — Above  | NO | 0.93 | - | 0.07 | open | - |
| 2026-11-24 | ai | Will CPI rise more than 0.0% in November 2026? — Above  | YES | 0.08 | 0.42 | 0.07 | open | - |
| 2026-11-23 | flb | Will the rate of CPI inflation be above 3.8% for the ye | NO | 0.95 | - | 0.06 | open | - |
| 2026-11-23 | flb | Anastasiia Hnidets wins | NO | 0.97 | - | 0.04 | won | 0.55 |
| 2026-11-22 | flb | Will the upper bound of the federal funds rate be above | NO | 0.96 | - | 0.04 | open | - |
| 2026-11-21 | flb | The RSM Classic: Haotong Li wins | NO | 0.96 | - | 0.04 | won | 0.74 |
