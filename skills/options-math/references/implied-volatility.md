# Implied Volatility, Skew & Term Structure

## What IV is
The σ that makes the model price equal the observed market price. It's the market's
forward-looking estimate of volatility — *the* most information-rich number on the chain.
Solve it with `implied_vol()` (Newton-Raphson on vega, bisection fallback for the wings).

### Solving notes
- No real solution below intrinsic value (function returns NaN) — the price is stale/wrong.
- Newton can diverge for deep ITM/OTM (vega → 0); the bisection fallback handles those.
- Use mid-price (½(bid+ask)); wide spreads make IV noisy — note the spread.

## Skew and smile (one σ does not fit all strikes)
- **Equity index skew**: OTM puts trade at *higher* IV than OTM calls — crash insurance is
  bid. Plot IV vs strike (or vs delta): downward-sloping "smirk."
- **Smile**: both wings elevated (common in FX/commodities, single names around events).
- Quote skew by **delta** (25Δ put vs 25Δ call) for comparability across names/time.
- Rising put skew = rising fear/hedging demand; flattening = complacency.

## Term structure
IV across expiries for a fixed moneyness:
- **Contango** (upward): normal — longer-dated IV > short-dated. Calm regime.
- **Backwardation** (downward): short-dated IV > long — stress/event-driven (earnings,
  macro print). Mean-reverts after the event ⇒ basis for calendar trades.
- **Earnings**: the front expiry's IV is inflated by the expected one-day move; it
  **crushes** right after the report ("IV crush"). Estimate the implied move from the ATM
  straddle price ≈ `straddle / S` (or ≈ `0.8 × ATM straddle` for a tighter 1σ proxy).

## Regime gauges: IV Rank vs IV Percentile
Given a trailing window (e.g. 1y) of an underlying's ATM IV:
```
IV Rank       = (IV_now − IV_min) / (IV_max − IV_min)        # position in the range
IV Percentile = fraction of days with IV < IV_now            # how often it was lower
```
- High IV rank/percentile ⇒ options *relatively expensive* ⇒ favors **net-selling**
  premium (credit spreads, condors), accepting short-gamma risk.
- Low ⇒ options *relatively cheap* ⇒ favors **net-buying** (debit spreads, long gamma).
- These are *relative* gauges, not directional signals — pair with a thesis.

## Realized vs implied
- **Realized (historical) vol** = stdev of past log returns, annualized (×√252).
- IV − RV = the **variance risk premium**; persistently positive (options buyers overpay
  on average), which is why systematic premium-selling has an edge — and a fat left tail.
- Compare IV to recent RV to judge whether premium is rich or cheap *for this name*.
