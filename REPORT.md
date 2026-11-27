# Prediction Market Paper Bot — 2026-11-27 13:05 UTC

Fake money. Each strategy has its own fake bankroll. Win rate above breakeven in a price bucket = edge in that bucket.

## Strategy 1: AI forecasts

- Realized P&L: **$+58.00** (ROI +28.0% on $207 risked)
- Settled: 10 (won 5, 50%) | Open: 9 | Cash: $99,870.97 of $100,000
- Kalshi fees paid: $17.56 (included in all P&L above)

| Entry price | Trades | Win rate | Breakeven (incl. fees) | ROI |
|---|---|---|---|---|
| 0–15c | 2 | 0% | 14% | -100.0% |
| 15–40c | 4 | 75% | 35% | +119.3% |
| 40–60c | 4 | 50% | 47% | +1.5% |

## Strategy 2: Fade the longshot (rules only, no AI)

- Realized P&L: **$-55.99** (ROI -10.7% on $524 risked)
- Settled: 27 (won 23, 85%) | Open: 28 | Cash: $99,396.99 of $100,000
- Kalshi fees paid: $4.32 (included in all P&L above)

| Entry price | Trades | Win rate | Breakeven (incl. fees) | ROI |
|---|---|---|---|---|
| 85–100c | 27 | 85% | 95% | -10.7% |

## Is the AI smarter than the market?

Brier score (lower = better), 38 resolved predictions:

- AI: **0.1950**
- Market: **0.1893**
- Market is beating the AI so far (too few results to mean anything yet — need ~100+)

### AI calibration

| AI said | Count | Actually YES |
|---|---|---|
| 0–20% | 14 | 29% |
| 20–40% | 5 | 20% |
| 40–60% | 8 | 75% |
| 60–80% | 5 | 60% |
| 80–100% | 6 | 100% |

Total AI predictions logged: 76

## Last 20 trades

| Date | Strat | Market | Side | Price | AI | Mkt | Status | P&L |
|---|---|---|---|---|---|---|---|---|
| 2026-11-27 | flb | BMW Australian PGA Championship: Alex Noren wins | NO | 0.97 | - | 0.04 | open | - |
| 2026-11-27 | flb | Aoi Ito wins | NO | 0.91 | - | 0.10 | won | 1.76 |
| 2026-11-26 | flb | BMW Australian PGA Championship: Kazuma Kobori wins | NO | 0.94 | - | 0.06 | open | - |
| 2026-11-26 | ai | Real Madrid wins | NO | 0.63 | 0.27 | 0.38 | open | - |
| 2026-11-26 | ai | Nadia Podoroska wins | YES | 0.34 | 0.45 | 0.34 | lost | -20.64 |
| 2026-11-26 | flb | BMW Australian PGA Championship: Haydn Barron wins | NO | 0.94 | - | 0.06 | open | - |
| 2026-11-26 | flb | Diego Duran wins | NO | 0.90 | - | 0.10 | won | 2.06 |
| 2026-11-26 | flb | BMW Australian PGA Championship: Nicolai Hojgaard wins | NO | 0.97 | - | 0.04 | open | - |
| 2026-11-25 | flb | BMW Australian PGA Championship: Elvis Smylie wins | NO | 0.97 | - | 0.04 | open | - |
| 2026-11-25 | ai | What will Jensen Huang say during NVIDIA GTC Washington | YES | 0.55 | 0.82 | 0.54 | open | - |
| 2026-11-25 | ai | Jason Kubler wins | NO | 0.39 | 0.33 | 0.61 | won | 30.26 |
| 2026-11-25 | ai | Luis Guto Miguel wins | YES | 0.33 | 0.50 | 0.33 | won | 39.27 |
| 2026-11-25 | flb | BMW Australian PGA Championship: Marc Leishman wins | NO | 0.97 | - | 0.03 | open | - |
| 2026-11-25 | flb | BMW Australian PGA Championship: Lucas Herbert wins | NO | 0.94 | - | 0.06 | open | - |
| 2026-11-24 | flb | BMW Australian PGA Championship: Cameron Smith wins | NO | 0.97 | - | 0.03 | open | - |
| 2026-11-24 | ai | Will the rate of CPI inflation be above 3.8% for the ye | YES | 0.07 | 0.32 | 0.07 | open | - |
| 2026-11-24 | ai | Hiroki Moriya wins | NO | 0.55 | 0.25 | 0.46 | won | 15.57 |
| 2026-11-24 | ai | Matteo Covato wins | NO | 0.28 | 0.12 | 0.72 | won | 50.11 |
| 2026-11-24 | flb | Nicolas Villalon Valdes wins | NO | 0.90 | - | 0.11 | won | 2.06 |
| 2026-11-24 | flb | Gabriela Agra Amorim wins | NO | 0.97 | - | 0.04 | won | 0.55 |
