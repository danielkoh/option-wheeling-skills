# Peter Lynch — GARP & "Invest in What You Know"

Lynch ran Fidelity Magellan to ~29%/yr (1977–1990). Philosophy: **growth at a reasonable
price (GARP)**, found through everyday observation and verified in the financials. Hunt for
**ten-baggers** (10×) — a few big winners carry the portfolio.

## Core principles
1. **Invest in what you understand.** Edge comes from noticing great products/businesses in
   daily life *before* Wall Street, then doing the homework. "Know what you own and why."
2. **The story.** Be able to explain, in two minutes, why you own it — what has to go right.
   If the story changes (fundamentals deteriorate), sell; don't marry the position.
3. **Classify the company** — the expectation and exit differ by type:
   - **Slow growers** — large, mature, low growth; own for dividends, if at all.
   - **Stalwarts** — big, ~10–12% growth (Coca-Cola, P&G); good for 30–50% gains, recession
     defense; trim and rotate.
   - **Fast growers** — small/aggressive, 20–25%+ growth; *where the ten-baggers live*; the
     main hunting ground, but verify the growth is real and financeable.
   - **Cyclicals** — autos, airlines, steel; timing the cycle is everything; P/E signals are
     *inverted* (low P/E can be the top of the cycle).
   - **Turnarounds** — beaten-down recoveries; high risk, uncorrelated to market.
   - **Asset plays** — hidden value (real estate, cash, subsidiaries) the market misses.
4. **PEG is the core valuation gauge.** `PEG = P/E ÷ earnings growth%`. **< 1 is attractive**
   (you're paying less than the growth rate); ~2+ is expensive. A fairly priced growth
   company has P/E ≈ its growth rate.
5. **Balance-sheet discipline.** Prefer low debt, strong cash; check that **inventories
   aren't growing faster than sales** (a classic early warning); rising cash + falling debt
   is bullish.
6. **Ignore macro forecasting.** "If you spend 13 minutes a year on economics, you've wasted
   10." Bottom-up, company by company.

## What Lynch likes (bullish tells)
- Boring/disliked name, mundane or disagreeable business (less competition for the stock).
- Niche/franchise with repeat purchase; spin-offs; insider buying; company buying back shares.
- Fast grower with a long runway to **replicate a proven concept** in new markets.
- Institutions don't own it yet / analysts don't cover it.

## Red flags (Lynch avoids)
- "Hot" stocks in hot industries; the "next [famous company]"; diworsification (empire-
  building acquisitions outside the core).
- High P/E relative to growth (PEG ≫ 1); whisper/story stocks with no earnings.
- Inventories piling up faster than sales; rising debt.

## Quantitative checks (what `lynch_screen` encodes)
- **PEG < 1.0**.
- **EPS growth ~15–30%** (fast but sustainable; >50% is rarely durable).
- **Debt/Equity ≤ ~0.5**.
- **Inventory growth ≤ sales growth**.

## How to apply
Classify the company first (the bar differs by type), tell its two-minute story, compute PEG
and confirm growth is real and financed by the balance sheet, and check the Lynch tells/red
flags. For fast growers, the key question is **runway**: how many more "stores" can it open?
