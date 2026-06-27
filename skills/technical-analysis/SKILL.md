---
name: technical-analysis
description: >
  Use for technical analysis of price/volume: trend, momentum, mean-reversion and
  volatility indicators (moving averages, RSI, MACD, Bollinger Bands, ATR, stochastics,
  ADX, OBV/VWAP), support/resistance, chart patterns, and signal construction/backtest
  framing. Holds exact indicator formulas and honest caveats about what TA can and
  can't do.
---

> ⚠️ **Not financial advice.** This skill is educational and analytical tooling only.
> It presents math, valuation, scenarios, and risk — it never recommends buying or
> selling any security. Options carry substantial risk and are not suitable for all
> investors; you can lose more than you collect in premium. Verify every number against
> primary sources (filings, your broker, a data provider) and do your own due diligence.
> You are solely responsible for your trading decisions.

# Technical Analysis

Reference for indicator math and price-action reading in this skill.

## Stance (be honest)
TA describes **supply/demand and crowd behavior in price**, not company value. Treat
indicators as **probabilistic, context-dependent** tools, not predictions. The dominant
factor is almost always **trend/regime**: the same RSI=30 means "buy the dip" in an
uptrend and "catch a falling knife" in a downtrend. Always state the regime first.

## Workflow
1. **Establish regime/trend** (e.g. price vs 50/200-day MA; ADX for trend strength;
   higher-highs/higher-lows). Pick the right *family* of indicator for that regime:
   - **Trending** → trend/momentum tools (MA crossovers, MACD, ADX). Mean-reversion
     oscillators give false "overbought" sells in strong trends.
   - **Ranging** → mean-reversion tools (RSI, Bollinger Bands, stochastics).
2. **Confirm, don't stack-redundantly.** Combine *independent* signals (e.g. momentum +
   volume), not three flavors of the same momentum. Beware multicollinearity.
3. **Define levels**: support/resistance, prior swing highs/lows, round numbers, VWAP.
4. **Risk first**: where's the invalidation (stop)? Size off ATR, not gut. State R:R.
5. **Backtest framing** when asked for a signal: specify entry/exit rules, look-ahead-bias
   avoidance, transaction costs, and that in-sample fit ≠ out-of-sample edge.

## Compute it properly
Implement indicators on a pandas Series (or any ordered price series). Use **Wilder's smoothing** for RSI/ATR/ADX — not a simple moving average.
Use the **exact** definitions in `references/indicators.md` — getting the smoothing method wrong silently corrupts signals.

## References
- `references/indicators.md` — formulas: SMA/EMA, RSI, MACD, Bollinger, ATR, stochastics,
  ADX/DMI, OBV, VWAP, plus default parameters and reading notes.
- `references/patterns.md` — support/resistance, classic patterns, candlesticks, divergence,
  and the caveats (subjectivity, base rates, confirmation).

## Hard caveats to always surface
- Indicators **lag** (they're functions of past price). Crossovers confirm late.
- **Overfitting**: any parameter set looks great in-sample. Insist on out-of-sample/walk-
  forward and realistic costs before claiming an "edge."
- Patterns are **subjective** and have unimpressive unconditional base rates; they work
  best as *risk-definition* tools (clear invalidation), not crystal balls.
- TA ≠ fundamentals. For value/quality questions, use the `fundamental-analysis` skill.
