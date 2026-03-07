# Week 1: Making Your Data AI-Accessible — The Tool-Use Pattern

## 1.1 How LLMs Actually Work With Data

Large language models like Claude are powerful reasoners, but they have a fundamental
limitation: they only see what's in their context window. They don't have access to
your Bloomberg terminal, your risk system, or your proprietary signal models.

The **tool-use pattern** bridges this gap. You define structured functions — tools —
that the AI can call on demand. The AI decides *when* to call a tool, *what parameters*
to pass, and *how to interpret* the results.

This is a critical architectural distinction:

```
Traditional approach:
  Dump all data into prompt → AI reasons over giant context → output

Tool-use approach:
  AI sees tool descriptions → decides what data it needs → calls specific tools
  → receives structured results → reasons and synthesizes → output
```

Why this matters for finance:

- **Your data stays in your systems.** The AI calls into your infrastructure; you
  don't ship your portfolio to an AI provider.
- **The AI only fetches what it needs.** Instead of 10,000 rows of position data,
  it calls `get_portfolio_summary()` for a high-level view, then drills into
  specific positions.
- **You control the interface.** The tool defines exactly what data is exposed and
  in what format. Your proprietary models stay proprietary — the AI sees outputs,
  not internals.

**Mental model:** Think of AI as a new analyst who just joined your desk. They're
smart and can synthesize information quickly, but they need access to your systems.
MCP tools are the equivalent of giving them a login to your terminals.

---

## 1.2 Model Context Protocol (MCP) — The Standard Interface

MCP is an open protocol (created by Anthropic) that standardizes how AI models
interact with external tools and data sources. Think of it as a USB-C port for AI:
any model that speaks MCP can use any tool that implements it.

### Anatomy of a Tool

An MCP tool has four components:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("portfolio-server")

@mcp.tool()
async def get_position_summary(ticker: str) -> dict:
    """Get current position details including P&L, weight, and risk metrics.

    Args:
        ticker: Stock ticker symbol (e.g., "AAPL")

    Returns:
        Position summary with current value, unrealized P&L, portfolio weight,
        and risk contribution.
    """
    position = await load_position(ticker)
    return {
        "ticker": ticker,
        "shares": position.shares,
        "avg_cost": position.avg_cost,
        "current_price": position.current_price,
        "unrealized_pnl": position.unrealized_pnl,
        "portfolio_weight_pct": position.weight * 100,
        "risk_contribution_pct": position.risk_contribution * 100,
        "data_source": "portfolio_system",
    }
```

The four components:

1. **Name** (`get_position_summary`) — How the AI refers to the tool
2. **Parameters** (`ticker: str`) — Typed inputs with descriptions
3. **Docstring** — Natural language description the AI reads to decide when to use it
4. **Return value** — Structured dict with semantic field names

### The Return Contract

This is a hard rule for financial AI tools: **never raise exceptions from tools.**

```python
# WRONG — AI receives an opaque error
@mcp.tool()
async def get_signal(ticker: str) -> dict:
    data = fetch_data(ticker)       # might throw
    return compute_signal(data)     # might throw

# RIGHT — AI receives actionable error information
@mcp.tool()
async def get_signal(ticker: str) -> dict:
    try:
        data = fetch_data(ticker)
        signal = compute_signal(data)
        return {
            "ticker": ticker,
            "signal": signal.name,
            "confidence": signal.confidence,
            "reasoning": signal.reasoning,
        }
    except DataUnavailableError:
        return {"error": f"Market data unavailable for {ticker}"}
    except Exception as e:
        return {"error": f"Signal computation failed: {e}"}
```

Why? When a tool raises an exception, the AI sees a generic error message and can't
reason about what went wrong. When a tool returns `{"error": "..."}`, the AI can
explain the issue to the user, try alternative tools, or adjust its approach.

### Transport Modes

MCP servers run in two modes:

- **stdio** (local): The AI app launches your server as a subprocess. Zero
  network overhead, used during development.
- **streamable-http** (cloud): Your server runs as an HTTP service. Supports
  authentication, multiple clients, cloud deployment.

The same tool code works in both modes — the transport layer is configured separately.

---

## 1.3 Designing Tools for AI Consumption

A good MCP tool is different from a good REST API endpoint. APIs are designed for
programmatic consumers that know exactly what they want. AI tools are designed for
a *reasoning* consumer that needs context to make decisions.

### Principle 1: Pre-Compute Everything

The AI should interpret results, not compute them. Python handles the math — the
AI handles the narrative.

```python
# BAD — AI must compute P&L, might hallucinate the math
@mcp.tool()
async def get_trades(ticker: str) -> dict:
    return {"trades": [
        {"date": "2026-01-15", "action": "BUY", "shares": 100, "price": 150.00},
        {"date": "2026-03-20", "action": "SELL", "shares": 50, "price": 175.00},
    ]}

# GOOD — Python computed everything, AI just interprets
@mcp.tool()
async def get_position_pnl(ticker: str) -> dict:
    return {
        "ticker": "AAPL",
        "total_invested": 15000.00,
        "current_value": 17500.00,
        "unrealized_pnl": 2500.00,
        "return_pct": 16.67,
        "holding_period_days": 65,
    }
```

This is especially critical for financial data. An AI that hallucinates a portfolio
return of 12% when it's actually 1.2% is worse than no AI at all.

### Principle 2: Return Context, Not Just Data

Include metadata that helps the AI qualify its statements:

```python
return {
    "signal": "RISK_OFF",
    "confidence": 0.82,
    "reasoning": "4 consecutive flight-to-safety days with declining volume",
    "data_source": "live_feed",           # vs "delayed_15min" or "end_of_day"
    "as_of": "2026-03-15T16:00:00Z",
    "stale_data_warning": None,           # or "Data is 3 hours old"
}
```

When the AI sees `stale_data_warning`, it can tell the user "Note: this is based
on data from 3 hours ago" — without this field, it might present stale data as
current.

### Principle 3: One Tool Per Decision-Relevant Question

Don't build a single `get_everything()` tool. Break it into the questions an
analyst actually asks:

```
get_current_signal()        → "What's the regime right now?"
get_risk_report()           → "What's my risk exposure?"
get_position_size(params)   → "How big should this trade be?"
get_trade_plan(signal)      → "What's the specific entry/exit plan?"
```

This lets the AI call only what it needs for the current conversation. If a user
asks "what's the signal?", the AI calls one tool — not five.

### Principle 4: The Guide Tool Pattern

Every MCP server should include a tool that describes its own capabilities:

```python
@mcp.tool()
async def get_strategy_guide() -> dict:
    """Explains all available tools, when to use each one, and recommended
    call sequences. Call this first when starting a new conversation."""
    return {
        "overview": "This server provides SPY/TLT regime signals and ES futures trade plans.",
        "tools": {
            "get_current_signal": "Start here. Returns today's regime color and signal tier.",
            "get_es_trade_plan": "Call after get_current_signal. Returns entry/stop/target levels.",
            "get_risk_report": "Call when user asks about exposure or position sizing.",
        },
        "recommended_flow": [
            "1. get_current_signal() — understand the regime",
            "2. get_es_levels() — see key price levels",
            "3. get_es_trade_plan() — get the actionable plan",
        ],
    }
```

This is like giving the new analyst a cheat sheet for your desk's systems. Without
it, the AI might call tools in a suboptimal order or miss relevant tools entirely.

---

## Key Takeaways

1. **AI doesn't access your data directly** — you expose it through structured tools
2. **MCP is the standard** for connecting AI to external systems (like USB-C for AI)
3. **Tools return dicts, never raise** — errors are data, not exceptions
4. **Pre-compute results** — Python does math, AI does interpretation
5. **Include context** — data source, freshness, confidence help the AI qualify its statements
6. **One tool per question** — granular tools let the AI fetch only what it needs
7. **Guide tools orient the AI** — describe your server's capabilities in a tool the AI calls first
