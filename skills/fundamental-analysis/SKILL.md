---
name: fundamental-analysis
description: >
  Use for fundamental/valuation work on companies and for applying famous-investor
  rulesets — Warren Buffett, Peter Lynch, Bill Ackman, Tom Lee. Covers financial-statement
  analysis, valuation (DCF, owner earnings, multiples), quality/moat assessment, and
  scoring a stock against each investor's documented criteria. Holds the valuation toolkit
  and a reference file per investor.
---

> ⚠️ **Not financial advice.** This skill is educational and analytical tooling only.
> It presents math, valuation, scenarios, and risk — it never recommends buying or
> selling any security. Options carry substantial risk and are not suitable for all
> investors; you can lose more than you collect in premium. Verify every number against
> primary sources (filings, your broker, a data provider) and do your own due diligence.
> You are solely responsible for your trading decisions.

# Fundamental Analysis

Reference for valuing companies and applying investor playbooks in this repo.

## Two layers — keep them separate
1. **Mechanical (numbers).** Compute the quantitative checks yourself from the financial statements (see `references/valuation-toolkit.md`)
   (ROE, PEG, FCF margin, ROIC, leverage, etc.). Run these for hard pass/fail signals.
2. **Judgmental (the hard part).** Moat durability, management quality, the narrative,
   *why the market is wrong*, optionality, and reflexivity. The investor references below
   describe how each thinks — apply that judgment; don't reduce a great investor to a ratio.

## Workflow
1. **Understand the business** before any number: what it sells, to whom, the unit economics,
   the competitive position. If you can't explain it simply, say so (Buffett's circle of
   competence; Lynch's "know what you own").
2. **Read the statements**: revenue quality/growth, margins & their trend, ROE/ROIC,
   balance-sheet strength (leverage, interest coverage, liquidity), and **cash flow vs.
   reported earnings** (FCF, accruals — watch for earnings not backed by cash).
3. **Value it** with `references/valuation-toolkit.md` — DCF / owner earnings / multiples.
   Always give an intrinsic-value **range** and the key assumptions driving it.
4. **Apply the lens.** Load the relevant investor reference(s) and score against their
   explicit criteria and red flags. Attribute each rule ("Lynch caps PEG at 1.0…").
5. **Margin of safety.** Compare price to value; state the discount/premium. No edge without
   a gap between price and value.
6. **Write the bear case.** The strongest argument *against* the thesis, and what would
   change your mind.

## Investor references (read the one(s) you need)
- `references/warren-buffett.md` — quality + durable moat + honest management at a fair
  price; owner earnings; circle of competence; long holding period.
- `references/peter-lynch.md` — GARP, PEG, the six stock categories, "invest in what you
  know," ten-baggers, balance-sheet checks.
- `references/bill-ackman.md` — concentrated, simple, predictable, free-cash-flow
  compounders; capital-light high-ROIC; activist catalyst; quality at a reasonable price.
- `references/tom-lee.md` — top-down/macro + market-strategy framing; liquidity, demographics,
  earnings & valuation regime; sentiment as a contrarian tool; sizing the index/sector view.
- `references/valuation-toolkit.md` — DCF, owner earnings, multiples, ROIC vs WACC, the key
  ratios and what each tells you.

## Multi-investor comparisons
When asked to apply several investors, give a **scorecard**: each investor's verdict
(pass / fail / pass-with-caveats), their single most-binding criterion for this name, and
where they'd disagree. They genuinely disagree (e.g. Buffett's patience vs. Ackman's
activism vs. Lynch's growth tolerance vs. Lee's macro overlay) — surface the disagreement,
don't average it into mush.

## Honesty
Not investment advice — present thesis, valuation, and risks; the user decides. Don't
fabricate financials; if a number is missing, say what filing it comes from (10-K, 10-Q,
proxy, earnings call) and that you'd need it.
