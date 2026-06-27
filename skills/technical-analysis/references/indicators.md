# Indicator Formulas

Defaults in parentheses. Implement on pandas Series; mind **Wilder's smoothing** where noted.

## Moving averages
- **SMA(n)** = mean of last `n` closes.
- **EMA(n)** = `EMA_t = α·P_t + (1−α)·EMA_{t−1}`, `α = 2/(n+1)`. Reacts faster, less lag.
- Use: trend filter (price vs SMA50/SMA200), the **golden cross** (50 over 200) / **death
  cross** (50 under 200). MAs are trend tools — useless/whipsawy in ranges.

## RSI (14) — momentum oscillator, 0–100
```
RS = (Wilder-smoothed avg gain) / (Wilder-smoothed avg loss)
RSI = 100 − 100/(1 + RS)
```
**Wilder smoothing** (not SMA): `avg_t = (avg_{t−1}·(n−1) + current_t)/n`.
- >70 overbought, <30 oversold — **but** in strong uptrends RSI rides 40–90 and "overbought"
  is bullish continuation. Best signal: **divergence** (price new high, RSI lower high).

## MACD (12, 26, 9)
```
MACD line   = EMA12 − EMA26
Signal line = EMA9 of MACD line
Histogram   = MACD − Signal
```
- Cross above signal = bullish momentum; histogram = momentum acceleration. Lagging;
  whipsaws in chop. Zero-line cross = trend-direction confirmation.

## Bollinger Bands (20, 2σ)
```
Mid = SMA20;  Upper/Lower = Mid ± 2·stdev(close,20)
%b = (price − lower)/(upper − lower);  Bandwidth = (upper − lower)/mid
```
- Mean-reversion in ranges (tags of the band fade back to mid). A **squeeze** (low
  bandwidth) precedes volatility expansion — direction unknown until the break.

## ATR (14) — Average True Range (volatility, in price units)
```
TR = max(high−low, |high−prev_close|, |low−prev_close|)
ATR = Wilder-smoothed average of TR over n
```
- Not directional. Use for **stops and position sizing** (e.g. stop = entry − 1.5·ATR;
  size so `risk_$ = shares × stop_distance`). Normalizes risk across symbols.

## Stochastic oscillator (14, 3, 3)
```
%K = 100·(close − lowest_low_n)/(highest_high_n − lowest_low_n)
%D = SMA3 of %K
```
- 0–100; >80 overbought, <20 oversold. Mean-reversion tool; same trend caveat as RSI.

## ADX / DMI (14) — trend *strength* (not direction)
```
+DI, −DI from smoothed directional movement; ADX = Wilder-smoothed |+DI − −DI|/(+DI + −DI)·100
```
- ADX <20 = no trend (use mean-reversion tools); >25 = trending (use trend tools); rising
  ADX = strengthening. +DI over −DI = up-trend bias.

## Volume
- **OBV** = running sum of signed volume (`+vol` on up-closes, `−vol` on down). Confirms/
  diverges from price; rising OBV supports an up-move.
- **VWAP** = `Σ(typical_price·vol)/Σvol` (intraday). Institutional fair-value benchmark;
  price above VWAP = buyers in control intraday. Anchored VWAP from a key event is useful.

## Reading notes
- Match the indicator family to the regime (see SKILL.md). Confirm with *independent*
  signals (momentum + volume), not redundant ones. Everything here **lags** price.
