# Strategy Cheat-Sheet

For each structure: construction, directional/vol bias, net Greeks, max profit / max loss
/ breakeven(s), and the dominant risk. Aggregate Greeks by summing legs (× sign × 100).
"Credit" = you receive premium; "debit" = you pay.

## Single legs
| Structure | View | Δ | 𝜈 | Θ | Max profit | Max loss | Breakeven |
|---|---|---|---|---|---|---|---|
| Long call | bullish | + | + | − | unbounded | premium | K + premium |
| Long put | bearish | − | + | − | K − premium | premium | K − premium |
| Short call (naked) | bearish/neutral | − | − | + | premium | unbounded | K + premium |
| Short put (naked) | bullish/neutral | + | − | + | premium | K − premium | K − premium |

## Income / premium-selling (short vega, short gamma, positive theta)
- **Covered call** = long 100 shares + short 1 OTM call. Caps upside at K, collects
  premium, small downside cushion. Max profit `(K−cost)+prem`; breakeven `cost−prem`.
- **Cash-secured put** = short put backed by cash. Synthetic "buy the dip at K−prem."
- **Credit spread** (bull put / bear call) = sell near + buy far OTM. Defined risk.
  Max profit = net credit; max loss = width − credit; one breakeven at short strike ± credit.
- **Iron condor** = bull put spread + bear call spread. Neutral, range-bound, **short
  gamma/vega, positive theta**. Profit if price stays between short strikes. Best in
  *high IV rank*; the killer is a fast move through a wing near expiry (gamma).
- **Iron butterfly** = condor with the shorts at the same (ATM) strike — bigger credit,
  narrower profit zone.

## Debit / directional with defined risk
- **Vertical debit spread** (bull call / bear put) = buy near + sell far. Caps profit at
  width − debit; max loss = debit; cheaper than the outright, lower vega.
- **Long straddle** = long ATM call + long ATM put. Long vol/gamma, pays theta. Profits on
  a **big move either way** or an IV spike. Breakevens = K ± total premium. Use when IV is
  cheap into an expected catalyst.
- **Long strangle** = OTM call + OTM put. Cheaper, needs a bigger move. Wider breakevens.

## Vol / time structure
- **Calendar (time) spread** = short near-dated + long far-dated, same strike. **Long
  vega, profits from theta differential** (near decays faster). Wants the underlying to
  pin the strike and/or front IV to crush relative to back. Max loss = net debit.
- **Diagonal** = calendar with different strikes (directional tilt). "Poor man's covered
  call" = long deep-ITM LEAPS call + short near OTM call.

## Hedging
- **Protective put** = long stock + long put (insurance; floors downside at K − premium).
- **Collar** = long stock + long put + short call (finance the put by capping upside).
  Near-zero cost; defines a band.
- **Risk reversal** = short put + long call (or vice-versa); expresses skew + direction.

## Picking by regime (combine with `implied-volatility.md`)
- **High IV rank** → net-sell premium (condors, credit spreads, CSPs). Short vega.
- **Low IV rank** → net-buy (debit spreads, straddles, calendars). Long vega/gamma.
- **Expected catalyst, cheap IV** → long straddle/strangle before; beware IV crush after.
- Always size to **max loss**, not to premium collected — short-premium tails are fat.
