# option-wheeling-skills

Open-source, self-contained **options-wheeling skills** for Claude and other AI assistants.
Install once, then ask your assistant to price an option, value a company, read the
technicals, or reason about running the wheel.

> ⚠️ **Not financial advice.** This skill is educational and analytical tooling only.
> It presents math, valuation, scenarios, and risk — it never recommends buying or
> selling any security. Options carry substantial risk and are not suitable for all
> investors; you can lose more than you collect in premium. Verify every number against
> primary sources (filings, your broker, a data provider) and do your own due diligence.
> You are solely responsible for your trading decisions.

## Skills

| Skill | What it does |
|---|---|
| `options-math` | Black-Scholes pricing, Greeks, implied vol, vol surface, multi-leg payoff/risk. Ships a small MIT reference implementation (`references/bsm.py`). |
| `fundamental-analysis` | Valuation (DCF, owner earnings, multiples), quality/moat, and the Buffett / Lynch / Ackman / Tom Lee playbooks. |
| `technical-analysis` | Indicators/signals (Wilder-smoothed RSI/ATR/ADX), support/resistance, chart patterns. |
| `the-wheel` | The wheel playbook: CSP → assignment → covered call, strike/DTE selection, premium/yield math, rolling, and risk. |
| `levelbox-mcp` | Optional companion to pull real, ranked wheel candidates from [levelbox.ai](https://levelbox.ai) over MCP. |

## Install (Claude Code plugin)

```
/plugin marketplace add danielkoh/option-wheeling-skills
/plugin install option-wheeling-skills
```

## Install (manual / other agents)

Skills are plain markdown — copy any `skills/<name>/` folder into your agent's skills
directory (e.g. `~/.claude/skills/`).

## License

MIT © 2026 Daniel Koh
