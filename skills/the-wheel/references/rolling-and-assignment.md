> ⚠️ **Not financial advice.** This skill is educational and analytical tooling only.
> It presents math, valuation, scenarios, and risk — it never recommends buying or
> selling any security. Options carry substantial risk and are not suitable for all
> investors; you can lose more than you collect in premium. Verify every number against
> primary sources (filings, your broker, a data provider) and do your own due diligence.
> You are solely responsible for your trading decisions.

# Rolling and Assignment — Reference

This document covers the mechanical decisions that arise once a CSP or covered call is
on the board: when and how to roll, when to accept assignment, how to manage a covered call
as the stock moves, the early-assignment edge case, and the discipline to walk away when
the thesis breaks.

---

## Rolling a Cash-Secured Put

A roll means buying back the existing short put and selling a new one in a single spread
order, keeping the position open instead of closing it outright.

**Why roll.** If the underlying has declined and your short put is now in-the-money (or
getting close) with expiry approaching, you face a choice: accept assignment or extend the
trade. Rolling gives you more time for the stock to recover while still collecting
incremental premium. The mechanics: buy to close the near-term put (at a debit) and sell
to open a new put that is further out in time (roll out), at a lower strike (roll down), or
both (roll out-and-down). The goal is to execute this as a single spread for a **net
credit** — meaning the new premium you receive exceeds the cost to close the old position.

**Net-credit discipline.** A roll done for a net debit means you are paying to extend
assignment risk — that is usually not the right trade. If no net-credit roll is available,
it is a signal that the market is pricing in significant continued downside; the roll may
not make economic sense. In that case, accepting assignment (if your thesis on the
underlying still holds) or closing the position outright at a loss are the cleaner options.

**Rolling down** reduces your strike, which lowers assignment risk and lowers your maximum
loss if the stock keeps falling, but also lowers the premium you can collect in future
cycles. Rolling repeatedly on a deteriorating name still leaves you with a cost basis above
the current market price — the cumulative credits collected rarely offset a large decline,
and you've committed more capital and time in the process.

**The trap: rolling indefinitely.** Rolling buys time, but it does not fix a broken thesis.
If you roll a CSP on a stock that has declined 30% and then another 20%, you are extending
a position on a name that the market is marking down significantly. Every roll on a
deteriorating underlying increases the total capital commitment and extends the period over
which your cash is locked up. Roll once or twice if the decline looks temporary and the
fundamental thesis is intact. If the thesis is broken — the company missed guidance badly,
the sector has re-rated, or you would not sell a new put today if you had no existing
position — stop rolling and take the assignment or the loss.

**Practical mechanics.** Most brokers allow you to enter a roll as a single multi-leg order
(a calendar spread for the same strike, or a diagonal if you're also changing strike). This
reduces slippage versus legging in separately. Target a net credit of at least $0.10–$0.15
per share (≥ $10–$15 per contract) to make the roll economically meaningful rather than
just paying to delay.

---

## Accepting Assignment

Assignment on a short put means the counterparty exercises their right to sell you the
stock at the strike. On American-style options this can happen at any time the put is
in-the-money, though in practice early assignment before expiry is uncommon on puts (see
the early-assignment section below). Standard assignment happens at or near expiry.

**Mechanics.** At assignment your broker debits your account `strike × 100` per contract
and credits you with 100 shares. The premium you collected when selling the put is already
yours — it is not returned. Your effective cost basis is therefore:

```
cost_basis = strike − premium_per_share
```

For example: sold a $50 put for $1.50/share → cost basis = $48.50/share. If the stock is
trading at $46 when assigned, you own shares that are $2.50 below your cost basis. That
is a paper loss, but it is also $1.50 better (exactly the premium you collected) than if
you had simply bought the stock at $50 the day you sold the put.

**When assignment is fine.** If you sold the CSP on a name you genuinely wanted to own at
or below the strike, assignment is the strategy working as designed. You now have a stock
position, and the next step is to sell covered calls above your cost basis to collect
additional premium while you hold. The total return on the wheel includes every dollar of
premium collected on the way in (CSP) and on the way out (CCs), plus any capital gain or
loss when the shares are eventually called away or sold.

**When assignment is uncomfortable.** If the stock has moved sharply lower and you no longer
believe in the underlying, owning 100 shares at a cost basis well above the current price
is a real loss position — not a "paper" one you can simply ignore. The covered-call
income from here is bounded by how high the stock might recover; if it does not recover,
you are slowly collecting premium on a depreciating asset. Sizing matters enormously here:
never sell a CSP for more contracts than you can absorb into your portfolio without it
becoming a dangerously concentrated position.

---

## Rolling a Covered Call

Once you own shares from an assignment (or from an existing long position), you sell covered
calls to collect premium. The same rolling logic applies when the stock rallies toward your
short call strike and you want to avoid being called away prematurely.

**Rolling up and out.** If the stock has moved up toward your call strike, the call is now
closer to at-the-money and has higher delta — meaning you are more likely to be called away
at expiry. If total return to the strike plus premiums already collected meets your target,
being called away is fine. If you would like to hold the shares longer — because you believe
further upside remains, or because being called away would trigger an unfavorable tax event
— you can roll the call up and out: buy to close the existing call and sell a new call at
a higher strike and/or later expiry for a net credit.

**The trade-off.** Rolling the covered call up-and-out always involves a trade: you receive
a net credit (good) but you extend the time during which your shares are encumbered by the
call (cost) and you cap your upside at the new, higher strike (still a cap). If the stock
continues rallying well past your new strike, you will have surrendered significant upside
and will face the same decision again.

**Accepting being called away.** When the covered call expires in-the-money at expiry, your
shares are sold at the strike. Your total return on the position is:

```
total_return = (call_strike − CSP_strike) + total_premiums_collected
```

where `CSP_strike` is the raw (original) put strike at which you were assigned, and
`total_premiums_collected` is the sum of every premium received: the CSP premium collected
when you opened the wheel plus every covered-call premium collected while holding the shares.
Note that `CSP_strike` is the gross strike, not the reduced cost basis — using the raw strike
here avoids double-counting the CSP premium that is already included in `total_premiums_collected`.

This is the intended outcome of the wheel if the stock recovered to and past your cost
basis. Evaluate it as a complete trade: did the annualized return on capital deployed make
sense for the risk you absorbed? That evaluation informs whether to start the wheel again
on the same name.

---

## Early Assignment

American-style options can be exercised at any time, so a short call or put can be
assigned before expiry. In practice, early assignment on short puts is rare because a put
holder loses extrinsic (time) value by exercising early — they would generally be better
off selling the put in the market. The main exception is deep in-the-money puts with little
extrinsic value remaining, but this is uncommon in a wheel context where you typically
start near-the-money.

**Early assignment on covered calls around ex-dividend.** The most common real-world
early-assignment scenario for wheel traders is on short covered calls around ex-dividend
dates. A call holder may exercise early the day before ex-dividend if doing so allows them
to capture the dividend. The condition: the dividend must exceed the extrinsic value
remaining in the call. If your short call is deep in-the-money heading into ex-dividend
with little extrinsic value left, early assignment is a real possibility.

**How to manage it.** If you are not willing to be called away early — for example, because
the short-term capital gain would have adverse tax treatment, or because you want to
collect the dividend yourself — consider buying back the covered call before ex-dividend
and re-evaluating. Weigh the cost of the buyback against the dividend amount and any
premium you might lose. There is no universal answer; the math depends on the specific
position, your tax situation, and your view on the stock. When in doubt, confirm the
ex-dividend date and calculate the extrinsic value of the short call a few days prior.

---

## Bear-Case Discipline and Invalidation

The wheel strategy has a structural vulnerability: it is long the underlying. When you sell
a CSP, you are exposed to downside below the breakeven (`strike − premium`). When you own
shares after assignment, you are exposed to the stock continuing to fall. Covered calls
provide premium income but do not meaningfully hedge a large decline — the call premium
you collect is far smaller than the potential loss on the stock if it drops 20–30%.

**The strategy underperforms in sharp declines.** If you are wheeling a name that drops
40% after an earnings miss, acquisition failure, or sector-wide repricing, the covered-call
premium you collect over subsequent months will barely offset the paper loss, and the stock
may not recover to your cost basis for a very long time — if ever. This is not a flaw in
execution; it is the inherent nature of the strategy. The wheel returns the options risk
premium; it does not protect against large drawdowns on the underlying.

**The strategy caps your upside in a rally.** If you are wheeling a stock that doubles, you
will be called away at your covered-call strike and miss most of the gain. Premium collected
softens the blow, but the wheel structurally underperforms in strong bull markets. This is
the other side of the same coin: you are selling optionality, and the market sometimes pays
out on that optionality in a large way.

**State the invalidation before entering.** Before selling any CSP, write down — explicitly —
the conditions under which you would stop wheeling this name. Examples:
- Fundamental thesis break: revenue growth reverses, a key product fails, management
  credibility is damaged.
- Technical invalidation: the stock closes below a meaningful structural support that
  suggests the trend has changed.
- Valuation re-rating: the sector multiple compresses and the stock is no longer cheap
  even at the strike.
- Position size breach: assignment would make this position too large a percentage of
  your portfolio.

**If the thesis breaks, stop.** Rolling a CSP or selling another covered call on a name
where your original thesis no longer holds means you are collecting premium in exchange
for carrying a position you no longer believe in. The premium rarely compensates for the
risk of continued downside on a broken story. Close the position, take the loss, and
redeploy capital to a name where the thesis is intact. The discipline to walk away is the
most important risk management tool in a wheel strategy — more important than any
particular delta target or DTE choice.
