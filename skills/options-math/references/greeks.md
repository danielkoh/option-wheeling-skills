# The Greeks

First/second-order sensitivities of option value. They are **local** — valid for small
moves; re-price for large ones. Greeks are **additive across legs** (multiply by
position sign and contract multiplier, usually ×100 shares).

## First order

### Delta (Δ) — ∂V/∂S
- Call: `e^(−qT)·N(d1)` ∈ (0, 1). Put: `−e^(−qT)·N(−d1)` ∈ (−1, 0).
- Intuition: share-equivalent exposure. Δ0.60 call ≈ long 60 shares per contract.
- ATM ≈ ±0.5; deep ITM → ±1; deep OTM → 0. Also ≈ risk-neutral P(finish ITM).
- **Hedging**: short Δ·100 shares per long call to be delta-neutral.

### Vega (𝜈) — ∂V/∂σ
- `S·e^(−qT)·φ(d1)·√T`, same for calls and puts (always positive for long options).
- Per 1.00 (100 vol-pts) change in σ here; divide by 100 for "per vol point."
- Largest for ATM, longer-dated options. Long options = long vega (want IV up).

### Theta (Θ) — ∂V/∂t (time decay)
- Negative for long options (value bleeds as expiry approaches). Reported per **year**;
  divide by 365 for per-calendar-day.
- Accelerates as expiry nears for ATM options; OTM theta is small and flattish.
- The vega/theta trade-off is the core of every calendar/income strategy.

### Rho (ρ) — ∂V/∂r
- Call: `K·T·e^(−rT)·N(d2)` > 0. Put: `−K·T·e^(−rT)·N(−d2)` < 0.
- Per 1.00 change in r; usually the least important Greek except for LEAPS / high rates.

## Second order

### Gamma (Γ) — ∂Δ/∂S = ∂²V/∂S²
- `e^(−qT)·φ(d1) / (S·σ·√T)`, always positive for long options.
- Δ's rate of change. Peaks ATM and **explodes near expiry** for ATM options ("gamma
  week"). Long gamma = convexity (gains from big moves either way) but pays theta for it.
- **Long gamma / short theta** vs **short gamma / long theta** is the central tension.

### Vanna — ∂Δ/∂σ (≈ ∂vega/∂S)
- How delta shifts as vol moves; matters for skew trading and large risk-reversals.

### Vomma / Volga — ∂vega/∂σ
- Convexity of vega; why far-OTM options gain disproportionately when IV spikes.

### Charm — ∂Δ/∂t
- Delta decay over time; matters for hedging into expiry/weekends.

## Practical reporting
For any position, give **net delta, gamma, vega, theta** (and rho if rates-sensitive).
Translate to dollars: `$ exposure = net_delta × multiplier × $ move`. Example phrasing:
"Net Δ +120 (≈ long 120 shares), Γ +8 (delta rises ~8/$1 up-move), 𝜈 +$45/vol-pt,
Θ −$22/day — a long-gamma, long-vega, time-decay-paying book."
