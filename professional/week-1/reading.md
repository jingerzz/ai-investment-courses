# Week 1: Making Your Data AI-Accessible — The Tool-Use Pattern

## 1.1 A Working Strategy — Your First AI Tool

Most AI courses start with theory. This one starts with a working
investment strategy connected to live market data through Claude.

By the end of this chapter's exercise, you'll have installed a
pre-built AI tool on your machine. You'll open Claude Desktop, ask
"What's today's signal?", and get a real answer — based on a real
strategy — computed from real market data. No code written, no API
keys, no subscriptions.

But first, you need to understand what the tool is doing. The strategy
behind it matters — not just because it's an interesting approach to
tactical allocation, but because understanding the strategy will help
you see *why* the AI tools are designed the way they are.

---

## 1.2 The SPY/TLT Color Strategy

> **You don't need to memorize any of this.** The server handles all the
> signal logic automatically. You're reading this so you can understand
> what the tools are doing under the hood — and so you can evaluate
> AI tool design when you build your own in Week 2. Skim the signal
> details; focus on the overall structure.

### The Core Idea

The strategy classifies every trading day into one of four **colors**
based on a simple observation: what happened to stocks (SPY) and bonds
(TLT) today?

| Color | SPY | TLT | What It Means |
|-------|-----|-----|---------------|
| **Green** | Up | Up | Risk-on rally. Both equities and Treasuries rise. Money is flowing in broadly. |
| **Orange** | Up | Down | Equity strength, but bonds are being sold. Markets are complacent — no demand for safety. |
| **Blue** | Up | Up | Flight to safety. Equities sold, Treasuries bought. Classic risk-off. |
| **Red** | Down | Down | Capitulation. Both equities and bonds decline. No safe haven bid. |

Why SPY and TLT specifically? Because the relationship between equities
and long-term Treasuries captures something fundamental about market
sentiment. When investors get nervous, they sell stocks and buy bonds
(Blue days). When panic exhausts itself, both decline together (Red
days). The color tells you *what kind* of market day it was — not just
whether stocks went up or down.

### Signals: When to Act

The strategy maintains a permanent 1x long SPY position — it's always
in the market. The question isn't *whether* to own equities, but
*how much*. On certain color patterns, the strategy adds tactical
leverage (up to 2x) for a limited number of days.

Nine signals are organized into three conviction tiers:

**Tier 1 — Maximum conviction (2.0x exposure):**

- **T1_BOTH_STRONG_BLUE:** SPY down >1% *and* TLT up >1% on the same
  day. Acute risk-off shock — both legs are moving with force. Hold
  the boost for 3 days.
- **T1_STRONG_HIVOL_RED:** Red day with SPY down >1% and volume >1.5x
  its 20-day average. Capitulation-style selling with high participation.
  3-day hold.
- **T1_STRONG_RED_STREAK:** Three or more consecutive Red days with at
  least two showing strong SPY declines. Clustered panic — 1-day hold
  targeting the immediate bounce.

**Tier 2 — High conviction (1.5x exposure):**

- **T2_STRONG_BLUE_NEGCORR:** Strong Blue day when the 20-day SPY/TLT
  correlation is below −0.3. The negative correlation confirms that
  flight-to-safety mechanics are working normally. 3-day hold.
- **T2_WEAK_RED_EXHAUSTION:** Three or more Red days in a row, but none
  with a strong SPY decline. Selling pressure is shallow and may be
  exhausting. 1-day hold.
- **T2_GREEN_MOMENTUM:** Three or more consecutive Green days. Orderly
  risk-on behavior may continue. Upgrades to 2.0x when SPY is above
  both its 50-day and 200-day moving averages. Held while the Green
  streak continues.
- **T2_SPY_DOWN_STREAK:** SPY closes down four or more days in a row.
  Mean-reversion trade — 1-day hold.

**Tier 3 — Moderate conviction (1.25x exposure):**

- **T3_WEAK_BLUE_NEGCORR:** Blue day with a mild SPY decline (≤1%) and
  negative correlation. Supportive structure, but not a strong signal.
  3-day hold.
- **T3_ORANGE_GRIND:** Three or more consecutive Orange days. Equity
  strength despite bond weakness — modest continuation bet. Held while
  the streak continues.

Signals are evaluated **top-down in priority order** each day at close.
The first match wins. If no signal triggers, the strategy holds its
base 1x position.

### Safety Rules

Two mechanisms protect capital:

**Danger state:** If Blue days stack up consecutively, the strategy
interprets this as sustained selling pressure that isn't bouncing.

- In a **bull regime** (SPY above its 200-day SMA): 4+ consecutive Blue
  days trigger a full exit to cash. Sit out for 2 days, then re-enter
  at 1x.
- In a **bear regime** (SPY below its 200-day SMA): the threshold
  tightens to 3+ Blue days with a 3-day sit-out. Bear markets are more
  dangerous, so the strategy exits earlier and stays out longer.

**Greed trim:** If the 5-day cumulative magnitude of up-move days
reaches 6.0%, any active boost is closed. The market has moved
significantly in the strategy's favor — take the win.

### How It Has Performed

Over a backtest spanning 2002–2026 (roughly 5,900 trading days):

| Metric | Strategy | SPY Buy & Hold |
|--------|----------|----------------|
| CAGR | 15.6% | 9.0% |
| Total Return | ~3,000% | ~660% |
| Max Drawdown | −35.4% | −56.5% |
| Sharpe Ratio | 0.74 | — |

The strategy outperforms because it **scales position size based on
conviction signals** — adding exposure when risk-off events are
likeliest to mean-revert, while protecting capital during sustained
downtrends via the danger rule.

Standard caveats apply: this backtest assumes fractional exposure
compounding with no transaction costs, slippage, or margin interest.
Past performance does not predict future results. The point here isn't
to convince you to trade this strategy — it's to give you a concrete
example of the kind of systematic logic that AI tools can make
accessible.

---

## 1.3 From Spreadsheet to AI Tool

You could implement this strategy in a spreadsheet. Pull SPY and TLT
prices, compute the colors, check the signal rules, look up the
current regime. Analysts do this kind of work daily.

But here's what changes when you connect this strategy to Claude
through structured tools:

**You can ask questions in natural language.** Instead of scanning rows
in a spreadsheet, you ask Claude: "What's today's signal and what does
it mean?" Claude calls `get_current_signal()`, reads the result, and
explains it — including why this signal fired, what the exposure
recommendation is, and what risks to watch.

**You get cross-referenced analysis.** Ask for a trade briefing and
Claude calls multiple tools: the current signal, the pivot levels, the
trade plan. It synthesizes these into a narrative: "We're in a Blue
regime with a Tier 2 signal. SPY is near S1 support. The trade plan
suggests buying the dip toward S1 with a stop at S2."

**The AI doesn't do math.** Every number Claude reports — the signal
tier, the pivot levels, the risk/reward ratio — was computed by Python
and handed to Claude as a finished result. Claude interprets and
explains. It doesn't calculate.

This is the **tool-use pattern**: you define structured tools that the
AI can call on demand. The AI decides *when* to call a tool, *what
parameters* to pass, and *how to interpret* the results. Your data
stays in your systems. The AI sees only what you explicitly expose.

---

## 1.4 Model Context Protocol (MCP) — The Standard Interface

The tool-use pattern needs a standard way to describe tools so any AI
model can understand them. That standard is **Model Context Protocol
(MCP)**, an open protocol created by Anthropic.

Think of MCP as USB-C for AI. Just as USB-C lets any device connect to
any charger or display, MCP lets any AI model connect to any tool.

### Anatomy of a Tool

> **You'll see Python code in this section.** You don't need to
> understand it — it shows how the tools work internally. You won't
> write or edit this code. Focus on the four labeled components
> (name, parameters, docstring, return value) and what each one does.

Every MCP tool has four components. Here's a real tool from the
SPY/TLT server you'll install in the exercise:

```python
@mcp.tool()
async def get_current_signal() -> dict:
    """Get today's strategy signal, color classification, and recommended action.

    Returns the latest day's signal evaluation including color, signal name,
    tier, target exposure, and recommended action. Includes stale data
    warning if data needs refreshing.
    """
    # ... Python code computes the result ...
    return {
        "date": "2026-03-06",
        "color": "Blue",
        "signal": "T2_STRONG_BLUE_NEGCORR",
        "tier": 2,
        "target_exposure": 1.5,
        "action": "Add SPY to 1.50x at next open",
        "spy_close": 678.50,
        "spy_pct_change": -1.23,
        "tlt_close": 91.15,
        "tlt_pct_change": 0.87,
        "data_source": "yfinance + local CSV",
        "stale_data_warning": None,
    }
```

The four components:

1. **Name** (`get_current_signal`) — How the AI refers to the tool.
   Descriptive names help the AI decide when to call it.
2. **Parameters** — Typed inputs the tool accepts. This tool takes no
   parameters, but others take `days`, `sequence`, `signal_name`, etc.
3. **Docstring** — Natural language description the AI reads before
   deciding whether to call the tool. This is your most powerful lever
   for shaping AI behavior (more on this below).
4. **Return value** — A structured dictionary with semantic field names.
   The AI reads these fields to formulate its response.

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

Every tool in the SPY/TLT server follows this pattern. You'll never
see the server crash — if something goes wrong, you'll see an `error`
field with a message you can act on.

### Transport Modes

MCP servers run in two modes:

- **stdio** (local): Claude Desktop launches the server as a process on
  your machine. Fast, secure, no network. This is what we use in the
  course.
- **streamable-http** (cloud): The server runs on a remote machine.
  Supports authentication, multiple users, cloud deployment. Used in
  production environments.

The same tool code works in both modes — only the transport configuration
changes.

---

## 1.5 Four Design Principles for AI Tools

The SPY/TLT server implements four design principles that make AI tools
effective for finance. As you use the server in the exercise, watch for
these patterns — they'll guide you when you build your own tools in
Week 2.

### Principle 1: Pre-Compute Everything

The AI should interpret results, not compute them. Python handles the
math — the AI handles the narrative.

When you ask the SPY/TLT server for a trade briefing, every number in
the response was computed by Python: the pivot levels, the risk/reward
ratios, the position sizing. The AI presents them and explains what they
mean. It never adds, divides, or averages numbers on its own.

This is critical for finance. An AI that hallucinates a portfolio return
of 12% when it's actually 1.2% is worse than no AI at all. The
`get_trade_briefing()` tool returns a fully formatted markdown section
with Python-inserted prices — the AI presents it verbatim.

### Principle 2: Return Context, Not Just Data

Every tool return includes metadata that helps the AI qualify its
statements:

```python
return {
    "signal": "T2_STRONG_BLUE_NEGCORR",
    "tier": 2,
    "target_exposure": 1.5,
    "data_source": "yfinance + local CSV",
    "stale_data_warning": None,       # or "Data is 1 day behind. Call refresh_data()."
}
```

When the AI sees a `stale_data_warning`, it tells the user: "Note: this
analysis is based on yesterday's close — the market has been open for
3 hours." Without this field, stale data looks identical to fresh data.

The `data_source` field serves a similar purpose. When a tool falls back
to a secondary data provider, the AI can say "this uses delayed data"
instead of silently presenting lower-quality information as if it were
live.

### Principle 3: One Tool Per Decision-Relevant Question

Don't build a single `get_everything()` tool. The SPY/TLT server has
14 tools, each answering a specific question:

```
get_current_signal()    → "What's the regime right now?"
get_trading_levels()    → "Where are the key support/resistance levels?"
get_backtest_summary()  → "How has this strategy performed historically?"
analyze_pattern()       → "What happened the last 66 times we saw Blue→Red→Blue?"
```

When a user asks "What's the signal?", the AI calls one tool — not
five. When they ask for a full briefing, the AI (or the briefing tool)
calls several and synthesizes them. Granular tools give the AI
flexibility to fetch only what's needed.

### Principle 4: The Guide Tool Pattern

The SPY/TLT server has a tool called `get_strategy_guide()` — and it's
the first tool the AI should call in any session. It returns:

- A catalog of all 14 tools with descriptions
- Recommended workflows (morning briefing, signal check, research)
- Strategy concepts (color definitions, signal tiers, key rules)
- Critical rules ("ALWAYS call `refresh_data()` before any analysis")

This is like giving a new analyst a cheat sheet for your desk's
systems. Without it, the AI might call tools in a suboptimal order or
miss relevant tools entirely. With it, the AI knows to call
`refresh_data()` before querying signals — because the guide told it to.

---

## 1.6 How AI Adds Value (and Where It Doesn't)

### High-Value AI Tasks

**Cross-signal synthesis:** The AI calls multiple tools — signal,
levels, trade plan — and connects them: "Blue regime with a Tier 2
signal. SPY is near S1 support. The trade plan suggests buying the dip."
No dashboard does this automatically.

**Natural language trade plans:** Instead of scanning a grid of numbers,
the AI says: "Entry zone is 676–681. Stop at 671. Target 1 is 686 for
a 1.5:1 R:R." It translates structured data into actionable language.

**Pattern explanation:** "The last 66 times we saw a Blue→Red→Blue
sequence, SPY was up 66.7% of the time the next day, with an average
gain of 0.4%." The AI queries historical data and narrates the pattern.

**Context for non-specialists:** A PM asks "What does T2_STRONG_BLUE_NEGCORR
mean?" The AI calls `explain_signal()` and returns a clear explanation
of the trigger, the logic, the sizing rationale, and the risks.

### Low-Value Tasks (Keep in Python)

**Numerical computation:** Never let the AI calculate returns, position
sizes, or risk metrics. It will hallucinate numbers. Pre-compute in
Python and return the result.

**Precise pricing:** The AI should never state a price it didn't receive
from a tool. The `get_trade_briefing()` tool solves this by returning a
pre-formatted section with all prices Python-inserted.

**Order execution:** The AI should never directly place trades. It
proposes; a separate system (with human approval) executes. We'll cover
this in Week 4.

### Why These Patterns Exist: Connecting Back to AI Failure Modes

In Foundations 1, you learned the specific ways AI gets things wrong in
investment contexts — stale magnitudes, confabulated facts, hallucinated
reasoning chains, numerical plausibility traps. The tool-use patterns
you learned this week are direct engineering responses to those failure
modes:

| Failure Mode | Tool Design Response |
|---|---|
| Stale magnitude errors (SPX in 5,000s vs 6,000s) | Tools call live APIs — AI never relies on training-data prices |
| Confabulated company facts | Tools return structured data from authoritative sources — AI interprets, doesn't invent |
| Hallucinated numbers (12% vs 1.2%) | Python pre-computes all math — AI never calculates |
| Plausible-but-wrong numbers | Pre-formatted templates lock in exact figures — AI presents them verbatim |
| Stale data presented as current | `stale_data_warning` field flags when data isn't fresh |

This isn't accidental. Every design principle in this course exists
because of a specific failure mode that was observed in practice. When
you build your own tools in Week 2, you'll implement these patterns
yourself.

---

## Key Takeaways

1. **The SPY/TLT strategy** classifies each trading day by color (based
   on SPY and TLT returns), then applies 9 tiered signals to tactically
   adjust exposure between 0x and 2x.

2. **Tool-use is the pattern** that connects AI to your data. You define
   structured tools; the AI decides when to call them and how to interpret
   the results.

3. **MCP is the standard** for describing tools to AI models — like
   USB-C for AI.

4. **Tools return dicts, never raise** — errors are data, not exceptions.

5. **Pre-compute results** — Python does math, AI does interpretation.
   This prevents hallucinated numbers in financial outputs.

6. **Include context** — `data_source`, `stale_data_warning`, and
   semantic field names help the AI qualify its statements.

7. **One tool per question** — granular tools let the AI fetch only what
   it needs for the current conversation.

8. **Guide tools orient the AI** — describe your server's capabilities
   so the AI calls tools in the right order.
