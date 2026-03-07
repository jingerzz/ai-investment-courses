# Week 2: Conversation Guide

How to talk to Claude Code when building multi-tool systems with guardrails.

---

## Building on Existing Code

When you open Claude Code in your project folder, it can see the files from
Week 1. You don't need to re-explain everything.

**Good:**
```
I have a server.py from last week with stock snapshot and watchlist tools.
I want to add market overview and sector heatmap tools. Can you add them
to the existing file?
```

**Less effective:**
```
[Re-describing everything from scratch]
```

Claude Code remembers the context of files in your project. It will read
`server.py` and understand what's there before adding to it.

---

## Describing Guardrails

### The pre-formatted template pattern

```
I want a tool that returns a pre-built markdown table with exact numbers.
The AI should display this table exactly as returned — no rounding, no
recalculating. The tool should have a field called "present_verbatim"
set to true so the AI knows not to modify it.
```

### The stale data warning pattern

```
Every tool should check if the market is currently open. If it's closed
(weekend, holiday, after hours), add a "stale_data_warning" field with
a message like "Data from last trading session (2026-03-15)". If the
market is open, set this to null.
```

### The no-compute rule

```
The AI should never calculate percentages, averages, or P&L from raw
numbers. Pre-compute everything in the tool. For example, don't return
individual stock returns and expect the AI to average them — return the
pre-computed average.
```

---

## When the AI Gets Something Wrong

This is the most important skill in Week 2: identifying when the AI
misuses your tools and fixing it through conversation with Claude Code.

### The AI makes up numbers

```
When I asked Claude Desktop for my portfolio performance, it said my
average return was 2.3%, but I can see from the tool output that the
individual returns don't average to that. The AI is doing math wrong.

Can you add a pre-computed "average_daily_return_pct" field to the
get_watchlist_movers tool so the AI doesn't need to calculate it?
```

### The AI ignores the formatted section

```
My get_briefing_formatted tool returns a markdown table, but the AI
is rewriting the numbers in its own words instead of showing the table.
Can you update the get_strategy_guide tool to explicitly say: "Always
present the formatted_section from get_briefing_formatted as-is. Do not
paraphrase or reformat the numbers."
```

### The AI doesn't cross-reference

```
The briefing mentions that XOM is down 3% but doesn't connect it to the
fact that the Energy sector (XLE) is down overall. Can you add a field
to get_watchlist_movers that shows each stock's sector and whether the
stock is outperforming or underperforming that sector? That should help
the AI make the connection.
```

---

## Testing Prompts for Claude Desktop

After building your briefing tools, try these in Claude Desktop:

**Basic briefing:**
```
Give me my morning briefing.
```

**Probing for guardrail gaps:**
```
What's my total portfolio return today?
(Watch if AI calculates or uses pre-computed value)
```

**Stale data test (try after market hours):**
```
How are my stocks doing right now?
(Should include stale data warning)
```

**Cross-reference test:**
```
Which of my stocks is most aligned with today's sector trends?
(Should connect stock performance to sector heatmap)
```

**Error handling test:**
```
How is INVALID_TICKER doing today?
(Should gracefully report the error, not crash)
```

---

## Tips for Week 2

1. **Build incrementally.** Add one tool, test it, then add the next. Don't
   ask Claude Code to build 5 tools at once — if something breaks, you won't
   know which tool caused it.

2. **Test with Claude Desktop, not just the inspector.** The MCP inspector
   shows you raw tool output. Claude Desktop shows you how the AI *interprets*
   that output. Both matter.

3. **Guardrails are about tool design, not prompting.** The best guardrail
   is a tool that returns data the AI can't misinterpret — not a prompt that
   says "please don't make mistakes."

4. **The guide tool is your strongest guardrail.** It tells the AI the rules.
   If the AI isn't following a rule, check if the guide tool mentions it.
