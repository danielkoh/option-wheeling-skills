# Valuation Toolkit

## 1. Discounted Cash Flow (DCF)
Intrinsic value = present value of future free cash flows.
```
FCF (to firm)   = EBIT·(1−tax) + D&A − CapEx − ΔNWC
FCF (to equity) = Net income + D&A − CapEx − ΔNWC + net borrowing
EV = Σ_t  FCF_t / (1+WACC)^t  +  TerminalValue / (1+WACC)^N
Terminal value (Gordon) = FCF_{N+1} / (WACC − g)        # g = perpetual growth, < WACC
Equity value = EV − net debt;  per share = / shares out.
```
- **WACC** = `E/V·Re + D/V·Rd·(1−tax)`; `Re` via CAPM = `Rf + β·ERP`.
- DCF is *garbage-in-garbage-out* and dominated by terminal value. Always run a
  **sensitivity table** over (growth, discount rate, margin). Quote a **range**, not a point.
- Use a conservative `g` (≤ long-run GDP/inflation, ~2–3%). If small changes in g flip the
  verdict, the DCF isn't telling you much — lean on other methods.

## 2. Owner Earnings (Buffett)
```
Owner earnings = Net income + D&A + non-cash charges − maintenance CapEx − ΔNWC
```
The cash an owner could extract without impairing the business. Distinguish **maintenance**
CapEx (to sustain) from **growth** CapEx (to expand) — only maintenance is subtracted. This
is usually a better "real earnings" figure than reported net income.

## 3. Multiples (relative valuation)
| Multiple | Use / caveat |
|---|---|
| **P/E** | Quick, but distorted by leverage, one-offs, accounting. Compare to growth (PEG) and peers. |
| **PEG** = P/E ÷ growth% | Lynch's core gauge; < 1 = growth cheap relative to earnings. |
| **EV/EBITDA** | Capital-structure-neutral; good cross-company/sector. Ignores capex intensity. |
| **EV/EBIT** | Better than EV/EBITDA for capital-heavy firms (counts D&A). |
| **P/FCF, EV/FCF** | Hardest to fake; cash is king. |
| **P/B** | Useful for financials/asset-heavy; meaningless for asset-light/IP businesses. |
| **P/S** | For unprofitable growth; pair with a path-to-margin. |
| **FCF yield** = FCF/EV | Compare to bond yields; the owner's cash return. |

Multiples are *relative* — they price a company against peers/history, not against value.
A whole sector can be mispriced. Cross-check with a DCF.

## 4. Quality & returns on capital
- **ROE** = Net income / equity. **ROIC** = NOPAT / invested capital. The headline quality
  metric: **a business creates value only when ROIC > WACC**, and compounds value when it
  can *reinvest* at high ROIC. Decompose ROE (DuPont): margin × turnover × leverage — make
  sure high ROE isn't just leverage.
- Durable high ROIC ≈ evidence of a **moat** (see Buffett ref).

## 5. Balance-sheet & cash health
- Leverage: Debt/Equity, **Net debt/EBITDA** (<3 generally safe, sector-dependent).
- **Interest coverage** = EBIT/interest (want ≥ 4–5×).
- Liquidity: current & quick ratios.
- **Accruals check**: if net income ≫ operating cash flow over time, earnings quality is
  suspect (aggressive revenue recognition, ballooning receivables/inventory).

## 6. Margin of safety
`MoS = (intrinsic value − price) / intrinsic value`. Demand a discount sized to your
uncertainty (Graham/Buffett: wider for harder-to-predict businesses). No gap ⇒ no edge.

## Sanity discipline
- Triangulate: DCF **and** multiples **and** owner-earnings/FCF yield. If they wildly
  disagree, find out why before trusting any one.
- Normalize for cycles (use mid-cycle margins for cyclicals), one-offs, SBC dilution, and
  off-balance-sheet items.
