# Prediction Market Paper Bot — 2026-11-28 13:34 UTC

Fake money. Each strategy has its own fake bankroll. Win rate above breakeven in a price bucket = edge in that bucket.

## Strategy 1: AI forecasts

- Realized P&L: **$+11.37** (ROI +3.9% on $291 risked)
- Settled: 14 (won 6, 43%) | Open: 10 | Cash: $99,803.61 of $100,000
- Kalshi fees paid: $22.38 (included in all P&L above)

| Entry price | Trades | Win rate | Breakeven (incl. fees) | ROI |
|---|---|---|---|---|
| 0–15c | 3 | 0% | 14% | -100.0% |
| 15–40c | 6 | 50% | 33% | +45.8% |
| 40–60c | 5 | 60% | 49% | +17.1% |

## Strategy 2: Fade the longshot (rules only, no AI)

- Realized P&L: **$-54.82** (ROI -10.1% on $544 risked)
- Settled: 28 (won 24, 86%) | Open: 31 | Cash: $99,339.10 of $100,000
- Kalshi fees paid: $4.83 (included in all P&L above)

| Entry price | Trades | Win rate | Breakeven (incl. fees) | ROI |
|---|---|---|---|---|
| 85–100c | 28 | 86% | 95% | -10.1% |

## Is the AI smarter than the market?

Brier score (lower = better), 44 resolved predictions:

- AI: **0.1906**
- Market: **0.1755**
- Market is beating the AI so far (too few results to mean anything yet — need ~100+)

### AI calibration

| AI said | Count | Actually YES |
|---|---|---|
| 0–20% | 14 | 29% |
| 20–40% | 8 | 12% |
| 40–60% | 11 | 64% |
| 60–80% | 5 | 60% |
| 80–100% | 6 | 100% |

Total AI predictions logged: 85

## Last 20 trades

| Date | Strat | Market | Side | Price | AI | Mkt | Status | P&L |
|---|---|---|---|---|---|---|---|---|
| 2026-11-28 | flb | Semen Pankin wins | NO | 0.90 | - | 0.10 | open | - |
| 2026-11-28 | flb | BMW Australian PGA Championship: Tom McKibbin wins | NO | 0.89 | - | 0.12 | open | - |
| 2026-11-27 | flb | Rivoli / Souza wins | NO | 0.94 | - | 0.07 | won | 1.17 |
| 2026-11-27 | ai | Will 3 mg THC beverages be federally legal to sell on D | NO | 0.33 | 0.40 | 0.68 | open | - |
| 2026-11-27 | ai | Rivoli / Souza wins | YES | 0.12 | 0.43 | 0.11 | lost | -21.15 |
| 2026-11-27 | ai | Omar Jasika wins | NO | 0.54 | 0.37 | 0.47 | won | 16.37 |
| 2026-11-27 | ai | Blaise Bicknell wins | YES | 0.25 | 0.46 | 0.24 | lost | -21.05 |
| 2026-11-27 | ai | Victor Pagotto wins | NO | 0.31 | 0.47 | 0.69 | lost | -20.8 |
| 2026-11-27 | flb | BMW Australian PGA Championship: Daniel Hillier wins | NO | 0.92 | - | 0.09 | open | - |
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
