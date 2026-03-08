# Week 2: Building Your Own AI Tools with Claude Code

## 2.1 From User to Builder

Last week you installed a pre-built MCP server, connected it to Claude
Desktop, and experienced what it feels like to have a conversation with
live market data. You saw the SPY/TLT strategy server answer questions,
cross-reference signals with technical levels, and present pre-computed
trade briefings.

This week, you build your own.

The tool is **Claude Code** — a CLI-based coding agent that reads your
instructions, writes code, runs tests, and iterates until the server
works. You describe what you want in plain English; Claude Code produces
a working MCP server.

This is not a prompt engineering trick. Claude Code has access to your
filesystem, your terminal, and the full context of your project. When
you say "add a tool that returns today's sector performance sorted by
daily return," it reads your existing server code, writes the new tool
function, installs any missing dependencies, and tests it — all in one
conversation.

### The Development Loop

Building with Claude Code follows a tight loop:

```
1. Describe what you want (in English)
2. Claude Code writes the code
3. You test it (MCP inspector or Claude Desktop)
4. You describe what to fix or improve
5. Repeat until it works
```

Each iteration takes 1-3 minutes. A simple MCP server with 5-6 tools
can be built and tested in under 30 minutes.

### What Makes a Good Prompt for Claude Code

Be specific about:
- **What data** the tool should return (fields, types, format)
- **What the AI should NOT compute** — pre-compute in Python instead
- **What metadata** to include (data source, staleness, confidence)
- **What the tool does NOT do** — prevents confusion with other tools

You don't need to specify implementation details. Claude Code knows
how to use `yfinance`, `pandas`, `mcp`, and standard Python libraries.
Focus on the *what*, not the *how*.

---

## 2.2 Designing Effective MCP Tools

The SPY/TLT server you used last week was designed with specific
patterns. Now that you're building your own server, you need to
understand these patterns well enough to apply them.

### Tool Docstrings Are Your Most Important Prompts

The docstring on each `@mcp.tool()` function is the primary way the AI
decides *when* and *how* to use your tool. Weak docstrings lead to the
AI calling tools at the wrong time or misinterpreting results.

```python
# Weak — AI might call this at the wrong time
@mcp.tool()
async def get_risk_data() -> dict:
    """Get risk data."""

# Strong — AI knows exactly when to use it
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

When you describe tools to Claude Code, include these four elements.
Claude Code will write the docstring for you, but only if you give it
the right information.

### Return Field Names Shape AI Language

The keys in your return dict shape how the AI talks about results:

```python
# Weak — AI might say "the value is 0.82"
return {"value": 0.82}

# Strong — AI will say "confidence is 82%"
return {"confidence_pct": 82.0}

# Even stronger — AI contextualizes the number
return {
    "confidence_pct": 82.0,
    "confidence_label": "HIGH",
    "reasoning": "3 of 4 indicators aligned with historical pattern",
}
```

Semantic field names like `confidence_pct`, `stale_data_warning`, and
`data_source` help the AI qualify its statements naturally. Compare
the SPY/TLT server's `get_current_signal()` — every field name tells
the AI what the value means: `spy_pct_change`, `target_exposure`,
`signal`, `tier`.

### The Return Contract

A hard rule for financial AI tools: **never raise exceptions from
tools.** When a tool crashes, the AI receives a generic error and can't
reason about what went wrong. When a tool returns a structured error,
the AI can explain the issue and suggest alternatives.

```python
# WRONG — AI receives an opaque crash
@mcp.tool()
async def get_signal() -> dict:
    data = fetch_data()       # might throw
    return compute_signal(data)

# RIGHT — AI receives actionable information
@mcp.tool()
async def get_signal() -> dict:
    try:
        data = fetch_data()
        return {"signal": data.signal, "confidence": data.confidence}
    except DataUnavailableError:
        return {"error": "Market data unavailable. Try refresh_data() first."}
```

Every tool in the SPY/TLT server follows this pattern. When you build
with Claude Code, tell it: "All tools should return dicts, never raise.
Use an error field for failures."

---

## 2.3 Guardrails: Preventing AI Math Errors

The most dangerous failure mode in financial AI is **hallucinated
numbers**. An AI that invents a portfolio return of 12% when it's
actually 1.2% is worse than no AI at all.

Three patterns prevent this.

### Pattern 1: Pre-Compute Everything

Python does math. The AI interprets. This was Principle 1 from Week 1,
and it applies to every tool you build.

When you describe tools to Claude Code, say: "Pre-compute everything.
The AI should never need to do math." This applies to returns, averages,
ratios, position sizes, risk metrics — anything numerical.

### Pattern 2: Pre-Formatted Templates

For critical outputs where numerical accuracy is non-negotiable, build
the entire narrative in Python with exact numbers inserted:

```python
@mcp.tool()
async def get_trade_briefing() -> dict:
    """Returns a pre-formatted trade briefing. Present the
    formatted_section verbatim — do not reformat or recompute."""
    signal = compute_signal()
    levels = compute_levels()

    briefing = f"""## Trade Briefing — {date.today()}

**Signal:** {signal.name} ({signal.color}, Tier {signal.tier})
**Target Exposure:** {signal.exposure}x

### Key Levels
| Level | Price |
|-------|-------|
| R1 | {levels.r1:.2f} |
| Pivot | {levels.pivot:.2f} |
| S1 | {levels.s1:.2f} |

### Plan
- **Entry zone:** {levels.s1:.2f} – {levels.pivot:.2f}
- **Stop:** {levels.s2:.2f} ({levels.pivot - levels.s2:.1f} pts risk)
"""
    return {
        "formatted_section": briefing,
        "present_verbatim": True,
        "ai_interpretation_notes": "Elaborate on signal meaning and risk context",
    }
```

The AI receives a fully-formed briefing. The `present_verbatim` flag
and the docstring tell it to present the formatted section as-is. It
can add context, but all numbers are Python-computed.

The SPY/TLT server's `get_trade_briefing()` uses exactly this pattern —
you saw it in action last week.

### Pattern 3: Stale Data Warnings

Every tool should signal when its data isn't fresh:

```python
return {
    "signal": "T2_STRONG_BLUE_NEGCORR",
    "stale_data_warning": None,  # or "Data from 2026-03-06. Call refresh_data()."
}
```

Without this, stale data looks identical to fresh data. The SPY/TLT
server includes `stale_data_warning` in every tool that returns market
data. When you build your own server, add this field to every tool that
touches prices or derived calculations.

### Finding Guardrail Gaps

Even with these patterns, gaps emerge. In the exercise, you'll discover
one: if you ask "What's my portfolio's total return today?" the AI might
add up individual stock returns — which is mathematically wrong (you
can't just add percentages across different position sizes).

The fix: pre-compute the correct aggregate in Python and return it as a
field. The AI uses the pre-computed number instead of doing bad math.

This is the iterative nature of guardrail design: test, find a gap,
pre-compute the answer, repeat.

---

## 2.4 Running AI Locally with Ollama

So far, everything has used cloud AI — Claude processes your questions,
Claude Code writes your code. But what about data that shouldn't leave
your machine?

- **Proprietary research notes** your firm doesn't want in the cloud
- **Client portfolio reports** with PII and account details
- **Internal strategy memos** with non-public investment theses
- **Compliance documents** that must stay on-premises

**Ollama** solves this. It runs AI models locally on your machine — the
data never leaves your computer.

### How Ollama Works

Ollama manages AI models on your hardware:

- **Pull** a model: downloads it (1-8GB depending on size)
- **Serve**: Ollama runs in the background, exposing a local API
- **Use**: Your Python code calls `http://localhost:11434` — no internet

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh   # Mac/Linux

# Pull a model
ollama pull qwen3.5:0.8b     # ~1GB, runs on any machine with 8GB RAM

# It's now available at localhost:11434
```

### Choosing a Model

For the course, we use the smallest model that works — so everyone can
run it regardless of hardware. All Qwen 3.5 models share the same
architecture with a 256K context window, which is ideal for long
financial documents.

| Your Machine | Model | Disk | RAM | Quality |
|-------------|-------|------|-----|---------|
| 8GB RAM | `qwen3.5:0.8b` | ~1GB | ~1GB | Good — handles basic Q&A and summaries |
| 16GB RAM | `qwen3.5:4b` | ~3.4GB | ~3-4GB | Great — strong reasoning, accurate citations |
| 32GB+ RAM | `qwen3.5:9b` | ~7GB | ~6-7GB | Excellent — near cloud-quality for local use |

**The course default is `qwen3.5:0.8b`** — it won't produce answers as
polished as larger models, but it runs on any machine and the hybrid
approach helps: Ollama handles document search and retrieval, Claude
Desktop does the sophisticated reasoning on top.

### Local vs. Cloud: The Hybrid Approach

The sweet spot: **use local models for document search, cloud models
for reasoning.**

| Use Case | Best Choice | Why |
|----------|------------|-----|
| Public SEC filings | Either | Data is public |
| Stock prices, market data | Cloud (Claude) | Better reasoning |
| Proprietary research notes | Local (Ollama) | Data stays private |
| Client reports | Local (Ollama) | Regulatory compliance |
| Complex multi-step analysis | Cloud (Claude) | Needs stronger reasoning |
| High-volume document search | Local (Ollama) | No API costs |

Your MCP server can use Ollama for finding the right passages in
documents, then Claude Desktop interprets and synthesizes the results.
This is exactly how the page-index-rag server works — you'll set it
up in the exercise.

---

## 2.5 Structure-First RAG for Financial Documents

### Why Standard RAG Fails on Filings

Standard RAG splits documents into fixed-size chunks (e.g., 500 tokens),
embeds each chunk as a vector, and retrieves the most similar chunks
when you ask a question.

This works for unstructured text — research notes, earnings call
transcripts, news articles. It fails for **structured documents** like
SEC filings, credit agreements, and regulatory submissions.

Why? These documents have **hierarchical structure** that matters.
Item 1A (Risk Factors) in a 10-K isn't just text — it's a specific
section with regulatory significance. When you chunk it into 500-token
pieces, you lose:

- Which section a chunk belongs to
- The relationship between sections
- The ability to cite specific sections in your answer

### The PageIndex Approach

Structure-first RAG preserves the document hierarchy:

**Step 1: Parse into a tree (not chunks)**

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
```

Each node stores: title, summary (AI-generated), full raw text, and
child nodes.

**Step 2: Two-stage retrieval**

```
Stage 1 — Keyword search (instant):
  Score each node's title + summary against the query
  If top score >= threshold → return those sections

Stage 2 — LLM reasoning (fallback, 5-10 seconds):
  If keyword search is weak, ask the AI to navigate the tree
  AI reads summaries at each level, decides which branches to explore
  Walks down to the relevant leaf nodes
```

**Step 3: The critical rule**

> Use summaries for *navigation*. Use raw text for *answers*.

The AI uses summaries to decide *where* to look (like reading a table
of contents), but always reads the full original text before answering.

Result: **98.7% accuracy on FinanceBench** (a benchmark for financial
document QA), compared to ~70% for naive chunk-and-embed RAG.

### The Vectorless Architecture

A key insight: the PageIndex approach doesn't require embeddings at all.
Keyword matching on section titles and summaries handles most queries
instantly. The LLM reasoning fallback handles the rest.

This means:
- No embedding model required by default
- No separate vector database
- Much smaller data footprint
- Works offline once documents are indexed

The page-index-rag server you'll set up in the exercise uses this
architecture. It includes 14 tools for fetching SEC filings from EDGAR,
indexing them into trees, searching across multiple filings, and
retrieving specific sections with citations.

### When to Use Which RAG Approach

| Approach | Best For | Why |
|----------|----------|-----|
| Vector RAG | Research notes, news, transcripts | Unstructured, no hierarchy |
| Structure-first RAG | SEC filings, legal docs, regulatory | Hierarchy is semantically meaningful |
| Hybrid | Large doc collections with mixed types | Structure for filings, vectors for notes |

---

## 2.6 Where AI Reasoning Adds Value

You experienced this last week with the SPY/TLT server — now you need
to design for it in your own tools.

### High-Value AI Tasks

**Cross-signal synthesis:** Combining regime signal + technical levels +
sector performance into a coherent view. Ask for a morning briefing and
the AI calls multiple tools, then connects them: "We're in a Blue
regime with a Tier 2 signal. SPY is near S1 support. Energy is today's
weakest sector — your XOM position is exposed."

No dashboard does this automatically. The AI reads structured data from
multiple sources and produces a narrative that would take an analyst
10-15 minutes to write.

**Natural language trade plans:** Turning structured levels and signals
into "if price does X, do Y because Z." Saves analysts from mentally
translating between data grids and action.

**Pattern explanation:** "The last 66 times we saw a Blue→Red→Blue
sequence, SPY was up 66.7% of the time the next day." The AI queries
historical data and narrates the pattern in context.

**Document Q&A:** "Does BlackRock's latest 10-K mention any new risk
factors related to digital assets?" The AI navigates the filing
structure, finds the relevant section, and provides a cited answer.

### Low-Value Tasks (Keep in Python)

**Numerical computation:** Never let the AI calculate P&L, returns,
position sizes, or risk metrics. Pre-compute in Python.

**Precise pricing:** The AI should never state a price it didn't receive
from a tool. Pre-formatted templates prevent this.

**Order execution:** The AI should never directly call a broker API.
It proposes; a separate system with human approval executes. We'll
cover this in Week 4.

---

## Key Takeaways

1. **Claude Code writes your MCP server** — describe what you want in
   English, iterate until it works.

2. **Tool docstrings are your most important prompts** — they tell the
   AI when, how, and why to use each tool.

3. **Return field names shape AI language** — `confidence_pct` beats
   `value`.

4. **Three guardrail patterns** prevent hallucinated numbers:
   pre-compute everything, pre-formatted templates, stale data warnings.

5. **Guardrail design is iterative** — test, find gaps, pre-compute the
   answer, repeat.

6. **Ollama runs AI locally** — use it for sensitive documents that
   can't go to the cloud.

7. **Structure-first RAG** preserves document hierarchy for citation-
   grade answers on SEC filings (98.7% accuracy vs ~70% for vector RAG).

8. **Local for search, cloud for reasoning** — the practical hybrid
   approach for financial document Q&A.
