# Week 1: Market Regime Tools on Zo

## 1.1 The First Real Workflow

Your first investment workflow is a market-context tool: a small piece of code that looks at how stocks and Treasury bonds moved today and tells you what kind of day the market just had. By the end of this week, you will be able to ask the AI "what is today's signal?" and get an answer based on real market data, not the model's training memory.

The tool is the **SPY/TLT course server**, and it lives in the course repository at:

```
professional/servers/spy-tlt-course
```

It is a teaching version of a larger production system. The production version has 37 tools and is wired into [Jing's](/about) actual investment workflow. The course version has 14 tools and is small enough that you can read its source code in an afternoon. Both follow the same architecture; the course version just stops earlier.

> **You do not need to read the source code to use the server.** The exercise this week walks you through running it. Reading the source is an optional bonus.

## 1.2 Why SPY and TLT?

SPY tracks the S&P 500. TLT tracks long-dated US Treasury bonds. When you watch the two together, you get a surprisingly rich read on what the market is doing.

The basic idea: investors move money between stocks and bonds depending on how much risk they want to take. When stocks rise and bonds rise together, money is flowing into the market broadly. When stocks rise but bonds fall, equity holders are confident enough that they do not want safety. When stocks fall and bonds rise, money is fleeing risk and seeking shelter. When both fall, everyone is selling everything.

Those four combinations are the **color days**:

| Color | SPY | TLT | What It Means |
| --- | --- | --- | --- |
| Green | Up | Up | Risk-on. Money flowing in everywhere. |
| Orange | Up | Down | Equity strength, no demand for safety. Often complacent. |
| Blue | Down | Up | Flight to safety. Classic risk-off. |
| Red | Down | Down | Capitulation. No safe haven bid. |

The exact strategy that uses these labels is interesting on its own merits, but it is not the point of this module. The point is that **a small piece of code can classify the day deterministically**, and the AI's job is to explain what the classification means — not to invent it.

## 1.3 What the Course Server Actually Does

The teaching server exposes 14 named tools. Each one answers a specific question. Here is what they cover, grouped by purpose:

**Orientation**
- `get_strategy_guide` — explains the whole strategy in one call. The AI should call this first in any session.

**Live state**
- `get_current_signal` — what color day is today, and what does the strategy say about exposure?
- `get_recent_history` — the last N trading days as a table
- `get_trading_levels` — key support and resistance levels
- `get_trade_briefing` — a pre-formatted human-readable summary

**Reference data**
- `get_signal_list` — the full list of named signals the strategy can produce
- `explain_signal` — what does signal name X mean, and when does it fire?
- `get_backtest_summary` — historical performance of the strategy

**Analysis**
- `analyze_pattern` — historical odds after a specific color sequence
- `spy_extreme_moves` — biggest up and down days
- `spy_streaks` — runs of consecutive up or down days
- `spy_seasonal` — average returns by month or weekday
- `spy_summary` — combined extremes plus streaks

**Data hygiene**
- `refresh_data` — pull the latest prices

You do not need to memorize this list. The point is that **the server is a set of small, named answers**, not one big "tell me everything" function. When the AI needs the regime, it calls `get_current_signal`. When you ask for support levels, it calls `get_trading_levels`. Each tool returns a structured object, and the AI puts the result into prose for you.

## 1.4 What a Tool Output Actually Looks Like

Here is the kind of object `get_current_signal` returns. The exact numbers will be different on the day you run it.

```json
{
  "date": "2026-04-30",
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
  "stale_data_warning": null
}
```

Three things to notice:

**Every number is computed by code.** The AI does not produce `678.50`. It receives that number from the tool. If you ask "what did SPY close at?", and the AI answers `678.50`, you can be confident that value is from the tool, not a guess.

**The output is self-describing.** The fields are named in plain English (`color`, `tier`, `target_exposure`). The AI reads them and can say "we are in a Blue regime with a Tier 2 signal" without doing any reasoning of its own.

**There is a stale-data field.** When data is fresh, it is `null`. When the data is behind, it contains a sentence explaining how far behind. The AI should pass that warning along to you. If a tool's output looks too clean, look for that field.

This is the **tool-use pattern**: code computes a structured result, the AI explains it.

## 1.5 The Professional Standard

A market-regime tool that is good enough for actual investment work should be able to answer all of these without you having to ask twice:

1. **What is the regime right now?** A clear label, not a hedge.
2. **What data went into that classification?** Prices, dates, sources.
3. **How fresh is the data?** With an explicit stale-data warning if it is not fresh.
4. **Which levels matter?** Support, resistance, moving averages.
5. **What would invalidate the signal?** A specific level or condition that would flip the call.
6. **What is the human supposed to decide?** A clearly framed decision, not a recommendation to act.

If an AI answer about the market skips any of these, it is not yet investment-grade. The course server tries to answer all six. When you build your own regime tool later, this list is the spec.

## 1.6 Where AI Adds Value (and Where It Does Not)

The AI is doing real work in this workflow, but it is doing the right work.

**Where the AI helps:**

- Explaining what `T2_STRONG_BLUE_NEGCORR` means in language a colleague can use
- Deciding which tool to call given an open-ended question ("what should I be watching today?")
- Synthesizing across tools when more than one is needed
- Highlighting a stale-data warning that a glance might miss

**Where the AI should not be involved:**

- Calculating any of the numbers in the output. That is the script's job.
- Making the call on whether to act. That is yours.
- Quoting any historical price it was not handed by a tool.
- "Refreshing data" by remembering what it last saw — there is a real `refresh_data` tool for that.

When you run the exercise this week, watch for these boundaries. If the AI ever gives you a number it did not get from a tool, that is a bug in your prompt. Tighten it.

## 1.7 Common Failure Modes (Week 1 Edition)

Each of these has caught careful users. Recognizing them is half the work.

**The phantom price.** AI tells you SPY closed at 681.45. The tool says 678.50. Both sound plausible. The phantom price is the one the AI made up; the tool's price is the right one. Always favor the tool's value.

**The forgotten refresh.** The tool was last refreshed two days ago. The AI happily reports a "current" signal anyway. The fix is to call `refresh_data` first; the better fix is for your prompt to require it.

**The confidence collapse.** The tool returns a Blue day. The AI hedges: "it might be Blue, or it might be Red — markets are uncertain." That is a bug in the AI's voice, not the data. Push back: ask it to report the tool's output verbatim before adding any commentary.

**The signal-meaning hallucination.** The AI explains `T2_STRONG_BLUE_NEGCORR` from its training memory rather than calling `explain_signal`. Sometimes it gets close. Sometimes it gets it embarrassingly wrong. The fix is to use `explain_signal`, not memory.

## Key Takeaways

- **The course server is a small, focused MCP server.** 14 tools, each answering one question, all backed by deterministic Python.
- **Color days are a simple way to classify market state.** Green, Orange, Blue, Red. Each is a SPY/TLT combination.
- **Tools return structured objects.** The AI's job is to explain them, not to invent the numbers.
- **The professional standard is six questions.** Regime, data, freshness, levels, invalidation, human decision.
- **AI should call tools, not remember.** If the AI is reciting a price from memory, your guardrail failed.
