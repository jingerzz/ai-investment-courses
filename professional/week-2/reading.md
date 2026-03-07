# Week 2: AI Reasoning Over Financial Data

## 2.1 Structured Data In, Reasoned Analysis Out

Last week you learned how to make data AI-accessible through tools. This week is
about what happens *after* the AI calls those tools — how it reasons across
multiple data sources to produce analysis that would take a human analyst
significant effort.

### The Synthesis Pattern

The most valuable AI pattern in finance isn't answering a single question — it's
synthesizing across multiple tools into a coherent narrative.

Consider a morning briefing. A human analyst would:
1. Check the regime / macro signal
2. Pull key price levels and technicals
3. Review risk exposure
4. Cross-reference these into a trade plan

With MCP tools, the AI does the same thing:

```
AI calls: get_current_signal()     → {color: "Blue", signal: "T2_STRONG_BLUE", exposure: 1.5}
AI calls: get_es_levels()          → {pivot: 5420, r1: 5455, s1: 5385, atr: 45}
AI calls: get_risk_report()        → {posture: "HEDGED", es_contracts: 2, bond_position: "LONG"}

AI synthesizes:
"We're in a Blue regime (flight-to-safety) with a Tier 2 signal suggesting
1.5x exposure. ES pivot is 5420 with support at 5385. Current posture is
HEDGED with 2 ES contracts and a long bond position — the bond leg is
providing the expected hedge. If ES dips toward S1 (5385), that's a
mean-reversion entry aligned with the Blue signal."
```

The AI didn't compute any numbers. It *interpreted* pre-computed results and
*connected* them into a narrative that would take 10-15 minutes to write manually.

### Why This Beats Dashboards

Dashboards show you data. AI tells you what the data *means in combination*.

A dashboard can display the regime color, the price levels, and the risk report
side by side. But it can't say "the bond leg is providing the expected hedge" —
that requires understanding that Blue regimes imply TLT should rise, and that a
HEDGED posture with long bonds is *consistent* with the signal.

This cross-referencing across data sources is where AI reasoning adds genuine value.

---

## 2.2 RAG for Financial Documents

### The Problem with Standard RAG

Retrieval-Augmented Generation (RAG) gives AI access to documents it wasn't
trained on. The standard approach:

1. Split document into chunks (e.g., 500 tokens each)
2. Embed each chunk as a vector
3. When user asks a question, embed the question
4. Find the most similar chunks via vector similarity
5. Feed those chunks to the AI as context

This works well for unstructured text (research notes, earnings call transcripts,
news articles). It fails for **structured documents** like:

- SEC filings (10-K, 10-Q, 8-K)
- Credit agreements and indentures
- Prospectuses and offering memoranda
- Regulatory submissions

Why? These documents have **hierarchical structure** that matters. Item 1A (Risk
Factors) in a 10-K isn't just text — it's a specific section with regulatory
significance. When you chunk it into 500-token pieces, you lose:

- Which section a chunk belongs to
- The relationship between sections
- The document's logical flow

### Structure-First RAG (The PageIndex Approach)

An alternative that works dramatically better for structured documents:

**Step 1: Preserve the hierarchy**

Instead of chunking, parse the document into a tree:

```
10-K Filing
├── Item 1: Business
│   ├── Overview
│   ├── Products and Services
│   └── Competition
├── Item 1A: Risk Factors
│   ├── Market Risk
│   ├── Regulatory Risk
│   └── Operational Risk
├── Item 7: MD&A
│   ├── Results of Operations
│   ├── Liquidity
│   └── Critical Estimates
└── Item 8: Financial Statements
    ├── Balance Sheet
    ├── Income Statement
    └── Cash Flow Statement
```

Each node stores: title, summary (AI-generated), full raw text, and child nodes.

**Step 2: Two-stage retrieval**

```
Stage 1 — Keyword search (fast):
  Score each node's title + summary against the query
  If top score >= threshold → return those sections

Stage 2 — LLM tree navigation (fallback):
  If keyword search is weak, ask the AI to navigate the tree
  AI reads summaries at each level, decides which branches to explore
  Walks down to the relevant leaf nodes
```

**Step 3: The critical rule**

> Use summaries for *navigation*. Use raw text for *answers*.

This means the AI uses summaries to decide *where* to look (like reading a table
of contents), but always reads the full original text before answering.

Result: **98.7% accuracy on FinanceBench** (a benchmark for financial document QA),
compared to ~70% for naive chunk-and-embed RAG.

### When to Use Which

| Approach | Best For | Why |
|----------|----------|-----|
| Vector RAG | Research notes, news, transcripts | Unstructured, no hierarchy to preserve |
| Structure-first RAG | SEC filings, legal docs, regulatory | Hierarchy is semantically meaningful |
| Hybrid | Large doc collections with mixed types | Use structure for filings, vectors for notes |

---

## 2.3 Where AI Reasoning Adds Value (and Where It Doesn't)

### High-Value AI Tasks in Finance

**Cross-signal synthesis:** Combining macro regime + technicals + risk exposure
into a coherent view. No dashboard does this automatically.

**Natural language trade plans:** Turning structured levels (pivot, R1, S1) and
signals (Blue, Tier 2) into "if price does X, do Y because Z." Saves analysts
from translating between data and action.

**Pattern explanation:** "The last 5 times we saw this Blue streak pattern in a
bull regime, SPY recovered within 2 days 80% of the time." The AI queries
historical data and narrates the pattern.

**Document Q&A:** "Does Apple's latest 10-K mention any new risk factors related
to AI regulation?" The AI navigates the filing structure and provides cited answers.

**Anomaly narration:** "Portfolio risk contribution from XOM jumped from 8% to
15% — this is because energy sector correlation increased during the recent
volatility spike." The AI explains *why*, not just *what*.

### Low-Value AI Tasks (Keep in Python)

**Numerical computation:** Never let the AI calculate P&L, returns, position
sizes, or Greeks. It will hallucinate numbers. Pre-compute in Python.

**Precise pricing:** The AI should never state a price it didn't receive from a
tool. Pre-formatted templates with Python-inserted numbers prevent this.

**Backtesting:** Run backtests in code, return summary stats to the AI. The AI
interprets results, doesn't run the backtest.

**Order execution:** The AI should never directly call a broker API. It proposes
trades; a separate execution layer (with human approval) handles the rest.

### The Pre-Formatted Template Pattern

For critical outputs where numerical accuracy is non-negotiable:

```python
@mcp.tool()
async def get_trade_briefing() -> dict[str, Any]:
    """Returns a pre-formatted trade briefing with all numbers computed
    by Python. The AI should present this directly, not recompute."""
    signal = compute_signal()
    levels = compute_levels()

    # Python builds the narrative with exact numbers inserted
    briefing = f"""## Trade Briefing — {datetime.now().strftime('%Y-%m-%d')}

**Signal:** {signal.name} ({signal.color}, Tier {signal.tier})
**Target Exposure:** {signal.exposure}x

### Key Levels
| Level | Price |
|-------|-------|
| R2 | {levels.r2:.2f} |
| R1 | {levels.r1:.2f} |
| Pivot | {levels.pivot:.2f} |
| S1 | {levels.s1:.2f} |
| S2 | {levels.s2:.2f} |

### Plan
- **Entry zone:** {levels.s1:.2f} - {levels.pivot:.2f} (mean-reversion dip)
- **Stop:** {levels.s2:.2f} ({levels.pivot - levels.s2:.1f} pts risk)
- **Target 1:** {levels.r1:.2f} (1:1 R:R)
- **Target 2:** {levels.r2:.2f} (1:2 R:R)
"""
    return {
        "briefing_markdown": briefing,
        "signal": signal.name,
        "regime": signal.color,
    }
```

The AI receives a fully-formed briefing. It can add context or caveats, but all
the numbers are Python-computed. Zero chance of hallucinated prices.

---

## 2.4 Prompt Engineering for Financial AI

### Tool Docstrings Are Prompts

The most impactful "prompt engineering" in an MCP system isn't the user's
question — it's the tool docstrings. These tell the AI *when* and *how* to use
each tool.

```python
# Weak docstring — AI might call this at the wrong time
@mcp.tool()
async def get_risk_data() -> dict:
    """Get risk data."""

# Strong docstring — AI knows exactly when to use it
@mcp.tool()
async def get_risk_check() -> dict:
    """Check current portfolio against risk limits. Returns any breaches
    or warnings for position concentration and sector limits.

    Call during morning review or before placing a trade. Returns 'OK',
    'WARNING', or 'BREACH' status with specific details.

    Does NOT return individual position data — use get_position_detail()
    for that."""
```

The strong docstring tells the AI:
- What the tool does (checks against limits)
- When to call it (morning review, pre-trade)
- What the output means (OK/WARNING/BREACH)
- What it does NOT do (doesn't return position detail)

### Return Field Names Are Prompts

The keys in your return dict shape how the AI talks about results:

```python
# Weak — AI might say "the value is 0.82"
return {"value": 0.82}

# Strong — AI will say "confidence is 82%"
return {"confidence_pct": 82.0}

# Even stronger — AI contextualizes the number
return {
    "confidence_pct": 82.0,
    "confidence_label": "HIGH",  # LOW/MEDIUM/HIGH/VERY_HIGH
    "reasoning": "3 of 4 indicators aligned with historical pattern",
}
```

---

## Key Takeaways

1. **AI's value is synthesis** — connecting multiple data sources into narrative
2. **Structure-first RAG** beats vector RAG for structured financial documents
3. **Summaries for navigation, raw text for answers** — the key RAG rule
4. **Pre-compute all numbers** — AI interprets, Python calculates
5. **Pre-formatted templates** prevent hallucinated prices in critical outputs
6. **Tool docstrings are your most important prompts** — they guide when/how the AI uses each tool
7. **Return field names shape AI language** — `confidence_pct` beats `value`
