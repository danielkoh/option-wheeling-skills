---
name: options-math
description: >
  Use when pricing options, computing or interpreting Greeks, solving implied
  volatility, reasoning about the vol surface (skew/term structure), or analyzing
  the payoff and net risk of single- and multi-leg structures (spreads, straddles,
  strangles, butterflies, condors, calendars, collars, covered calls). Holds the
  exact formulas, conventions, and the repo's pricing engine.
---

> ⚠️ **Not financial advice.** This skill is educational and analytical tooling only.
> It presents math, valuation, scenarios, and risk — it never recommends buying or
> selling any security. Options carry substantial risk and are not suitable for all
> investors; you can lose more than you collect in premium. Verify every number against
> primary sources (filings, your broker, a data provider) and do your own due diligence.
> You are solely responsible for your trading decisions.

# Options Math

Authoritative reference for derivatives pricing and risk in this repo. **When a
number is requested, prefer the implemented engine over hand calculation**, then
sanity-check.

## The reference implementation
`references/bsm.py` is a small, self-contained Black-Scholes-Merton implementation
(stdlib only, MIT) you can run to check any number:
- `price(S, K, T, r, sigma, right, q=0)` — option price
- `greeks(S, K, T, r, sigma, right, q=0)` — dict: `price, delta, gamma, vega, theta, rho`
- `implied_vol(target_price, S, K, T, r, right, q=0)` — IV by bisection

```bash
python3 -c "import sys; sys.path.insert(0,'references'); from bsm import greeks; print(greeks(100,100,0.25,0.04,0.20,'C'))"
```

**Conventions (fixed):** `T` in years; `sigma`/`r`/`q` annualized; `r` continuously-compounded;
`q` dividend yield; **vega per 1.00 vol**; **theta per year**. Prefer the reference
implementation over hand calculation, then sanity-check.

## Conventions (do not deviate without saying so)
- `T` is in **years** (calendar days / 365, or trading days / 252 for vol work — state which).
- `r` is the continuously-compounded annual risk-free rate; supplied by the caller.
- `q` is the continuous dividend yield (0 for non-dividend names/indices priced ex-div).
- `sigma` is annualized (0.25 = 25%).
- `vega` is per 1.00 change in sigma (÷100 for per vol-point); `theta` is per **year**
  (÷365 for per-day); `rho` is per 1.00 change in r (÷10000 for per-1bp, since 1bp = 0.0001).

## Workflow for any options question
1. Pin down all inputs (S, K, T, r, q, sigma, right, American/European). Fill gaps with
   project defaults and **say so**.
2. Compute with the engine. For multi-leg, compute each leg then aggregate Greeks
   (they're additive) and build the payoff at expiry.
3. Report: price/cost, **net Greeks**, **max profit / max loss / breakeven(s)**, and the
   dominant risk (direction, vol, time, assignment/pin).
4. Sanity checks: put-call parity `C − P = S·e^{-qT} − K·e^{-rT}`; `0 ≤ call delta ≤ 1`,
   `-1 ≤ put delta ≤ 0`; deep ITM ≈ intrinsic; IV ≥ intrinsic floor.

## Caveats to surface when relevant
- Black-Scholes assumes European exercise, constant vol, lognormal returns, no jumps.
  Real markets show skew/smile and fat tails. For American options with dividends (esp.
  early-exercise of ITM calls before ex-div, or ITM puts), BSM is an approximation —
  note it; use binomial if precision matters.
- Greeks are local first/second-order sensitivities; they drift as spot/vol/time move
  (gamma and "vega of vega"/vanna/vomma). For big moves, re-price, don't extrapolate.

## Deep references (read the one you need)
- `references/black-scholes.md` — model, formulas, assumptions, parity, binomial note.
- `references/greeks.md` — every Greek: definition, sign, intuition, hedging use.
- `references/implied-volatility.md` — IV solving, skew, term structure, IV rank/percentile.
- `references/strategies.md` — payoff/Greek/risk cheat-sheet for the common structures.
