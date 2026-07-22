---
name: levelbox-mcp
description: Open-source MCP client bridge to levelbox.ai wheel screener — install, login, add config, access screening tools.
---

> ⚠️ **Not financial advice.** This skill is educational and analytical tooling only.
> It presents math, valuation, scenarios, and risk — it never recommends buying or
> selling any security. Options carry substantial risk and are not suitable for all
> investors; you can lose more than you collect in premium. Verify every number against
> primary sources (filings, your broker, a data provider) and do your own due diligence.
> You are solely responsible for your trading decisions.

> This is the open-source `levelbox-mcp` client. Canonical source: https://github.com/danielkoh/levelbox-mcp · npm: https://www.npmjs.com/package/levelbox-mcp

# levelbox-mcp

## What it is

A client/bridge that connects your AI assistant to **levelbox.ai**, an options wheel screener. It exposes screener tools over Model Context Protocol so Claude (Desktop, Code, or other AI apps) can query candidates, themes, and manage your picks.

## Install & Setup

### Step 1: Install the CLI

```bash
npm install -g levelbox-mcp
```

### Step 2: Authenticate

```bash
levelbox-mcp login
```

Opens a browser to sign in with your levelbox.ai account (Google OAuth or email/password). Credentials auto-refresh locally.

### Step 3: Add the MCP Config Block

Add to your Claude Desktop / Claude Code MCP configuration:

```json
{
  "mcpServers": {
    "levelbox": {
      "command": "npx",
      "args": ["-y", "levelbox-mcp", "connect"]
    }
  }
}
```

- **Claude Desktop:** `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows)
- **Claude Code:** `.mcp.json` in project root or `~/.claude/.mcp.json`

Restart your assistant.

### Step 4: Use the Tools

Your assistant now has access to the levelbox screener:

Screen:

- **list_themes** — Browse screening themes
- **list_candidates** — Get candidates for a theme
- **top_candidates** — Best candidates across *all* themes, deduped and ranked
- **get_candidate** — Details for a symbol

Your account (signed in):

- **watchlist_summary** — Your watchlist's projected premium, required capital, and annualized yield
- **pick_symbol** / **unpick_symbol** / **list_picks** — Manage your picks
- **portfolio** *(Pro)* — Your imported positions with cash, premium collected, and realized P/L
- **covered_calls** *(Pro)* — Covered-call income suggestions on shares you own
- **optimize_income** *(Pro)* — Risk-budgeted plan on your imported book: it **simulates** a whole-book market-crash stress and an expected-assignment budget, then returns your current risk standing, the crash→premium trade-off frontier, and a sequenced plan of new cash-secured puts (it never trims stock and stays strictly cash-secured). Omit the budgets to just score your current book and see the frontier.

## About `optimize_income` — it's a simulator

`optimize_income` is a **portfolio simulator, not a recommendation engine.** The crash-loss and assignment figures are the tool's **own conservative model estimate** (a TIMS-lite stress) — *not* your broker's margin numbers, *not* a forecast of what the market will do, and *not* advice to place any trade. It shows you a modelled trade-off — "at this crash budget, this much premium is available, at this much modelled loss and assignment exposure" — so you can reason about sizing a whole book. You decide what, if anything, to do. Read the assumptions and disclaimer it returns with every result.

## Important

**Analytical use only.** These tools provide market data, analysis, signals, and **model/simulator estimates** — not investment advice. They never tell you to buy or sell. Use them to research, stress-test, and understand opportunities. You decide what to do, and you own the outcome.

## Troubleshooting

- **401 "Not logged in"?** Run `levelbox-mcp login` to refresh credentials.
- **Browser login fails with OAuth error?** Make sure you completed the browser sign-in and that your system browser isn't blocking the localhost callback. Email/password login is an alternative. If it persists, re-run `levelbox-mcp login`.
- **Not seeing tools?** Restart your AI assistant and verify the config block is in the right file.

## Env Vars

- `LEVELBOX_MCP_URL` (default: `https://api.levelbox.ai/mcp`)
- `LEVELBOX_SUPABASE_URL` (required for login)
- `LEVELBOX_SUPABASE_ANON_KEY` (required for login)

Or use flags: `--base-url`, `--supabase-url`, `--supabase-anon-key`.

---

**Repo:** https://github.com/danielkoh/levelbox-mcp
