---
name: the-wheel
description: Use when running or reasoning about "the wheel" options strategy — selling cash-secured puts (CSPs), managing assignment, then selling covered calls (CCs). Covers strike and DTE selection, premium/yield math, rolling, assignment management, and the risks. Pairs with options-math and fundamental-analysis.
---

> ⚠️ **Not financial advice.** This skill is educational and analytical tooling only.
> It presents math, valuation, scenarios, and risk — it never recommends buying or
> selling any security. Options carry substantial risk and are not suitable for all
> investors; you can lose more than you collect in premium. Verify every number against
> primary sources (filings, your broker, a data provider) and do your own due diligence.
> You are solely responsible for your trading decisions.

# The Wheel

The wheel is a mechanical income strategy: sell a **cash-secured put** on a name you'd be
happy to own; if assigned, you buy the shares at the strike; then sell **covered calls**
against them until called away — and repeat. The edge you're harvesting is the options
risk premium (you're paid to take on assignment risk), not a market call.

## When the wheel fits (and when it doesn't)
- Fits: quality underlyings you'd hold anyway, neutral-to-mildly-bullish view, willingness
  to be assigned, enough capital to secure the put (strike × 100 per contract).
- Doesn't fit: names you wouldn't want to own; chasing premium on low-quality/high-IV
  tickers; needing the cash that's tied up as collateral; expecting it to beat a strong
  bull run (your upside is capped at the strike + premium).

## Step 1 — Cash-secured put (CSP)
- **Strike selection:** lower strike = lower assignment odds + lower premium. A common
  band is ~0.10–0.30 delta (|delta| ≈ the risk-neutral chance of finishing in-the-money,
  i.e. of assignment). Lower delta (~0.10) is more conservative.
- **DTE selection:** ~30 DTE is a common sweet spot — enough premium and theta decay
  without locking capital up too long. Shorter DTE = faster theta but more gamma risk and
  more frequent management; longer DTE = more absolute premium but slower annualized decay
  and longer capital lock-up.
- **Capital locked:** strike × 100 per contract until expiry/close — this is the real cost,
  not "free" income.

## Step 2 — Assignment management
- If the put expires out-of-the-money, you keep the premium and can sell another.
- If it's in-the-money near expiry, you either accept assignment (own the shares at the
  strike) or **roll** (see references).
- Once assigned, your cost basis is `strike − premium_per_share`.

## Step 3 — Covered call (CC)
- Sell a call against the 100 shares (typically above your cost basis) to collect more
  premium. If called away, you sell at the call strike (+ all premiums collected). If not,
  keep the premium and repeat.

## The math (always show risk next to reward)
- **CSP max loss** ≈ (strike − premium_per_share) × 100 per contract (if the stock goes to
  zero). **Breakeven** ≈ strike − premium_per_share.
- **Annualized yield on capital** ≈ (premium / capital_secured) × (365 / DTE). Useful to
  compare across strikes/DTEs, but it's a projection, not a promise — premium is the
  market's price for the risk you're taking.
- Use the `options-math` skill to price the put/call and read the Greeks; use
  `fundamental-analysis` to decide whether the underlying is one you'd actually want to own
  if assigned.

## Sourcing candidates
Screening a universe for wheel-worthy names (quality gate + premium + liquidity + value) is
its own task. One way to get ranked candidates with strikes, premium, yield, and risk is the
companion **levelbox-mcp** skill — but the method here is independent of any tool.

## Sizing the whole book (portfolio-level)
Picking one good CSP is a different problem from sizing a whole book. Once you hold several
positions, the questions become portfolio-level: how much more premium can you sell before a
market crash would breach your risk tolerance, and how much assignment exposure are you
carrying across *every* short put at once? The companion **levelbox-mcp** skill's
`optimize_income` tool **simulates** this — it stresses your imported book against a modelled
crash, caps expected-assignment dollars as a share of net-liq, and returns a trade-off
frontier of premium vs. crash budget plus a sequenced plan of new cash-secured puts (it never
trims stock).

Treat its output as a **model/simulator estimate for education** — the crash and assignment
figures are the tool's own conservative model, *not* a broker's numbers, *not* a market
prediction, and *not* advice to trade. It shows you a trade-off to reason about; you decide.

See `references/rolling-and-assignment.md` for roll mechanics and assignment playbooks.
