# Black-Scholes-Merton

## The formulas (European, continuous dividend yield q)

```
d1 = [ ln(S/K) + (r − q + σ²/2)·T ] / (σ·√T)
d2 = d1 − σ·√T

Call = S·e^(−qT)·N(d1) − K·e^(−rT)·N(d2)
Put  = K·e^(−rT)·N(−d2) − S·e^(−qT)·N(−d1)
```
`N(·)` = standard normal CDF. At/after expiry (T ≤ 0), value = intrinsic:
`max(S−K, 0)` for a call, `max(K−S, 0)` for a put.

### Interpretation of the pieces
- `N(d2)` ≈ risk-neutral probability the option finishes ITM.
- `S·e^(−qT)·N(d1)` = present value of receiving the stock if exercised.
- `K·e^(−rT)·N(d2)` = present value of paying the strike if exercised.

## Assumptions (and how reality breaks them)
1. **Lognormal returns / constant σ** → real markets have volatility *skew* and *smile*;
   a single σ doesn't fit all strikes. Use the IV *per strike*, not one number.
2. **No jumps / continuous hedging** → gaps and earnings moves violate this; tails are fat.
3. **European exercise** → American options can be exercised early; see below.
4. **Constant r, frictionless, no taxes** → fine as a first approximation.

## Put-call parity (your #1 sanity check)
```
C − P = S·e^(−qT) − K·e^(−rT)
```
If your computed C and P violate this, an input is wrong. Parity also defines the
synthetic relationships: long call + short put (same K, T) = synthetic long forward.

## American options & early exercise
- **American call on a non-dividend stock**: never optimal to exercise early ⇒ equals the
  European call. With dividends, early exercise just before ex-div can be optimal if the
  dividend exceeds the remaining time value.
- **American put**: can be optimal to exercise early (deep ITM, high rates) ⇒ worth ≥ European.
- When early-exercise value matters, prefer a **binomial (CRR) tree** or finite-difference
  solver over BSM. State the method you used.

## Cox-Ross-Rubinstein binomial (when you need American/dividends)
```
u = e^(σ√Δt),  d = 1/u,  p = (e^((r−q)Δt) − d) / (u − d)
```
Back-induct from expiry payoffs, taking `max(continuation, intrinsic)` at each node for
American exercise. ~200–500 steps converges to BSM for European cases (good cross-check).

## Greeks live in `greeks.md`; IV/skew in `implied-volatility.md`.
