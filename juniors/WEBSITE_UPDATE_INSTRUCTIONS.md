# Website Update Instructions — Juniors Course

These instructions describe the changes made to the juniors course
materials that need to be reflected on the website at `jing.zo.space`.

---

## Summary of Changes

The juniors course content has been updated with a **new company
universe** designed for middle school and high school students. Every
ticker example, price reference, JSON output block, and scenario has
been rewritten to use companies teenagers actually know and care about.

Three new **"Investing 101" sidebars** have been added to teach
fundamental concepts through relatable examples.

### Old Company Universe
- AAPL (Apple), NKE (Nike), DIS (Disney), TSLA (Tesla), NFLX (Netflix)

### New Company Universe

**Primary 5 (used in all weekly exercises):**

| Ticker | Company | Why Students Know It | Price* |
|--------|---------|---------------------|--------|
| RBLX | Roblox | Gaming platform | ~$60 |
| SNAP | Snapchat | Social media | ~$5 |
| SPOT | Spotify | Music streaming | ~$517 |
| DUOL | Duolingo | Language learning app | ~$97 |
| CROX | Crocs | Footwear/fashion | ~$80 |

**Extended 3 (used in comparisons and bonus module):**

| Ticker | Company | Why Students Know It | Price* |
|--------|---------|---------------------|--------|
| TTWO | Take-Two | GTA, NBA 2K | ~$210 |
| NFLX | Netflix | Streaming | ~$95 |
| DIS | Disney | Theme parks, streaming | ~$101 |

*Prices as of March 2026. Website should use live or recent prices.

---

## New "Investing 101" Sidebars

Three teaching sidebars were added to weekly readings. These should be
rendered as highlighted callout boxes (distinct from regular content).

### 1. "Share Price vs. Company Value" (Week 1 reading)

**Location:** After the "How do stock prices work?" section

**Content:** Uses SNAP ($5) vs SPOT ($517) to teach that a cheaper
stock price does not mean a smaller company. Introduces market cap
with simple multiplication: SNAP at $5 x 1.6B shares = $8B, while
showing that price alone is misleading.

**Why it matters:** Students instinctively think "$5 stock = cheap
company." This is the most common beginner misconception.

### 2. "What Does 'Profitable' Mean?" (Week 2 reading)

**Location:** After the stale data / Saturday example section

**Content:** Contrasts CROX (profitable, $1B+ revenue, makes more
than it spends) with SNAP (400M daily users but has never made a
yearly profit). Introduces the idea that growth companies often lose
money on purpose.

**Why it matters:** Students assume popular = profitable. Snapchat
is a perfect counterexample they can relate to.

### 3. "The GTA Effect" (Week 3 reading)

**Location:** After the annual report / multi-source section

**Content:** Uses Take-Two (TTWO) and the GTA VI announcement to
explain why stock prices move on announcements before products ship.
An announcement is new information that changes what investors think
the company is worth.

**Why it matters:** Students understand game hype cycles. This
connects something they experience (game announcements) to market
mechanics.

---

## Files Changed

### Top-level files:

| File | Website Page | What Changed |
|------|-------------|--------------|
| `introduction.md` | intro page | Apple → Roblox in opening example and company list |
| `COURSE_BRIEF.md` | (metadata) | Updated ticker comparison table and default watchlist |
| `glossary.md` | glossary page | Updated 5 term examples + added 3 new terms (Earnings, Stock split, Profitable) |
| `conclusion.md` | conclusion page | Nike/Adidas/Under Armour → Roblox/Take-Two/EA comparison |

### Week 1 (heaviest changes):

| File | Website Page | What Changed |
|------|-------------|--------------|
| `week-1/reading.md` | week-1.html | All price/ticker examples rewritten. Added "Share Price vs. Company Value" sidebar. Math examples use RBLX ($58.83→$59.80 = 1.65%). |
| `week-1/exercise/README.md` | week-1.html (exercise) | All prompt examples, test tickers, Claude Desktop prompts updated |
| `week-1/exercise/conversation_guide.md` | (reference) | Starter prompts, error examples, troubleshooting tickers |
| `week-1/exercise/checklist.md` | (reference) | Price verification: Apple/$195 → Roblox/$60 |
| `week-1/exercise/reference_solution.md` | (reference) | **All 4 JSON example blocks completely rewritten** with new tickers, prices, and market data |
| `week-1/exercise/setup.md` | setup page | No changes (software setup only) |

### Week 2 (moderate changes):

| File | Website Page | What Changed |
|------|-------------|--------------|
| `week-2/reading.md` | week-2.html | Price examples, pre-formatted table, sector analysis example. Added "Profitable" sidebar. |
| `week-2/exercise/README.md` | week-2.html (exercise) | Cross-reference example: Disney → Snapchat |
| `week-2/exercise/conversation_guide.md` | (reference) | Sector example updated |
| `week-2/exercise/reference_solution.md` | (reference) | Formatted report and Claude Desktop response rewritten |

### Week 3 (moderate changes):

| File | Website Page | What Changed |
|------|-------------|--------------|
| `week-3/reading.md` | week-3.html | Annual report example Apple → Roblox. Added "GTA Effect" sidebar. |
| `week-3/exercise/README.md` | week-3.html (exercise) | Watchlist and cross-server test prompts |
| `week-3/exercise/conversation_guide.md` | (reference) | Claude Desktop test prompts |
| `week-3/exercise/checklist.md` | (reference) | Cross-server example |
| `week-3/exercise/reference_solution.md` | (reference) | Cross-server question examples |
| `week-3/exercise/architecture_template.md` | (reference) | No changes (generic template) |

### Week 4 (moderate changes):

| File | Website Page | What Changed |
|------|-------------|--------------|
| `week-4/reading.md` | week-4.html | Apple → Roblox, Tesla → Snapchat in examples |
| `week-4/exercise/README.md` | week-4.html (exercise) | All ticker lists, BLOCKED example: Tesla → Snapchat |
| `week-4/exercise/conversation_guide.md` | (reference) | Ticker lists and test prompts |
| `week-4/exercise/reference_solution.md` | (reference) | **All monitor output, audit log JSON, summary stats, MCP tool JSON, and Claude Desktop response rewritten.** Key scenario: SNAP -8.1% URGENT, RBLX +3.8% ALERT. |

### Bonus RAG module:

| File | Website Page | What Changed |
|------|-------------|--------------|
| `bonus-local-rag/reading.md` | bonus.html | Apple → Roblox in RAG explanation and search examples |
| `bonus-local-rag/exercise/README.md` | bonus.html (exercise) | 10-K download AAPL → RBLX, all question examples, cross-document: Microsoft → Take-Two |
| `bonus-local-rag/exercise/conversation_guide.md` | (reference) | EDGAR download, risk factors, cross-document comparison |
| `bonus-local-rag/exercise/checklist.md` | (reference) | Cross-server test: Apple/AAPL → Roblox/RBLX |
| `bonus-local-rag/exercise/reference_solution.md` | (reference) | **All JSON examples rewritten** with Roblox-specific content (user safety, child protection, COPPA risk factors). File references: AAPL-10K → RBLX-10K. |
| `bonus-local-rag/exercise/ollama_quickstart.md` | (reference) | No changes needed |

### Files NOT changed (no ticker references):
- `prerequisites.md` — software setup only, no company examples
- `week-1/exercise/setup.md` — software setup only

---

## Glossary Page — Specific Changes

### Updated examples in existing terms:

| Term | Old Example | New Example |
|------|------------|-------------|
| Stock | "...a tiny piece of Apple" | "...a tiny piece of Roblox" |
| Ticker Symbol | "AAPL, NKE, DIS" | "RBLX, SPOT, SNAP" |
| Stock Price | "$195.50" | "$59.80" |
| Portfolio | "Apple, Nike, and Disney" | "Roblox, Spotify, and Disney" |
| Tool | "AAPL" | "RBLX" |

### Three new terms added:

1. **Earnings** — Explains quarterly reports using Roblox example.
   "If Roblox earns more than expected, the price usually goes up."

2. **Stock split** — Uses Netflix 7-for-1 split as a teaching moment.
   "Like cutting a pizza into more slices — same amount of pizza."

3. **Profitable** — Contrasts Crocs (profitable) with Snapchat
   (400M users, never made a yearly profit). Teaches that popular
   does not always mean profitable.

---

## Week 1 Reference Solution — JSON Blocks

The reference solution contains 4 JSON example blocks that were
completely rewritten. These are important because they show students
what correct tool output looks like.

### `get_stock_snapshot` example:
- RBLX at $59.80, market cap $38.2B
- pe_ratio: null (Roblox is not yet profitable)
- notable: "Elevated volume — 1.5x 30-day average"
- Math walkthrough: (59.80 - 58.83) / 58.83 * 100 = 1.65%

### `get_watchlist_summary` example:
- RBLX: hot (+1.65%), DUOL: steady (+0.38%), CROX: steady (+0.12%)
- SPOT: steady (-0.45%), SNAP: cold (-2.21%)

### `get_stock_comparison` example:
- RBLX vs SPOT with market caps ($38.2B vs $103.5B)
- pe_ratio: null vs 85.3 (demonstrates profitability contrast)

### `get_strategy_guide` example:
- Lists all 5 primary tickers in overview

---

## Week 4 Reference Solution — Monitor Scenario

The monitor scenario was rewritten to use a dramatic, relatable event:

- **URGENT:** SNAP down -8.1% on 2.5x average volume
  - Suggested action: "Big drop with high volume — check for news"
- **ALERT:** RBLX up +3.8%
  - Suggested action: "Medium-sized move, worth keeping an eye on"
- **All clear:** SPOT, DUOL, CROX

Claude Desktop response example references "URGENT: Snapchat down
8.1% on high volume" and "ALERT: Roblox up 3.8%".

---

## Bonus RAG Reference Solution — Document Content

All RAG examples now use Roblox-specific annual report content:

- Company description: online entertainment platform, user-generated
  experiences, virtual currency (Robux)
- Risk factors: user safety, child protection, COPPA compliance,
  content moderation at scale
- Hybrid pattern example: RAG search for Roblox risk factors combined
  with live RBLX stock price data

---

## Hosted MCP Server (Future)

A pre-built MCP server will be hosted at `jing.zo.space` so students
can connect in Week 1 without building anything first. This follows
the "use before you build" pedagogy.

**Student connection command:**
```bash
claude mcp add --transport http stock-tracker https://jing.zo.space/api/mcp/stock-tracker
```

**Tools available:**
- `get_stock_snapshot(ticker)` — single stock data
- `get_watchlist_summary(tickers)` — multiple stocks at once
- `get_stock_comparison(ticker1, ticker2)` — side-by-side comparison
- `get_market_overview()` — broad market context
- `get_strategy_guide()` — describes all available tools

**Default tickers:** RBLX, SNAP, SPOT, DUOL, CROX

This server is not yet built. When ready, Week 1 exercise instructions
will need to include the connection step, and the prerequisites page
may need a note about the hosted server option.

---

## Navigation / Table of Contents

The juniors course structure is unchanged (4 weeks + bonus). Update
the navigation to reflect the new company theme:

- Introduction: "Build AI tools for tracking stocks you actually know"
- Week 1: "Your First AI Stock Tracker" (RBLX, SNAP, SPOT, DUOL, CROX)
- Week 2: "Making Your Tracker Smarter"
- Week 3: "Connecting Multiple AI Tools"
- Week 4: "Building a Stock Monitor"
- Bonus: "Private Document Search with Ollama"
- Glossary, Conclusion

---

## Interactive Demo Update (Optional)

Consider updating any website demo to use the new tickers. A
`get_stock_snapshot("RBLX")` returning Roblox at ~$60 is more
engaging for the target audience than an Apple example.

The SNAP vs SPOT price contrast ($5 vs $517) also makes a compelling
visual for explaining market cap vs share price.

---

## What NOT to Change

- The overall site layout and design direction are unchanged
- The course structure (4 weeks + bonus) is unchanged
- Prerequisites content was not modified in this update
- The `ollama_quickstart.md` guide is unchanged
- The `architecture_template.md` is unchanged
- Brand/visual identity follows `brand/juniors.md` (light code blocks,
  bright blue + amber palette)
