# Week 1: Connecting AI to Real Data

## 1.1 What Is a Stock, and Why Does AI Need Help?

Let's start with the basics.

A **stock** is a tiny piece of ownership in a company. When you buy a
share of Apple stock, you own a small fraction of Apple. If Apple does
well and makes more money, your share becomes worth more. If Apple does
poorly, your share loses value.

Every stock has a **ticker symbol** — a short code used to identify it.
Apple is "AAPL". Nike is "NKE". Tesla is "TSLA". You'll use these
codes throughout the course.

The **stock price** is what one share costs right now. It changes
constantly during trading hours (9:30 AM to 4:00 PM Eastern, Monday
through Friday). After hours, the price stays at whatever it closed at.

Now here's the thing about AI: **Claude doesn't know what any stock
costs right now.** Claude was trained on text from the internet, but
that training happened months ago. It doesn't have a live connection
to the stock market. If you ask Claude "What's Apple's stock price?",
it might give you a number — but it's probably wrong, because it's
guessing from old information.

That's what you're going to fix this week. You'll build a tool that
lets Claude look up the actual, current stock price whenever it needs to.

---

## 1.2 How AI Connects to Data: The Tool-Use Pattern

When you chat with Claude normally, here's what happens:

```
You ask a question → Claude thinks about it → Claude responds
```

Claude's response is based entirely on what it learned during training.
For general knowledge, that's usually fine. But for stock prices? Useless.

The **tool-use pattern** adds a step:

```
You ask a question → Claude checks its tools → Claude calls a tool
→ The tool fetches real data → Claude gets the data back → Claude responds
```

Now Claude's response is based on actual, current data. The difference
is huge.

Here's a concrete example. Say you ask Claude Desktop "How is Apple
doing today?" Without tools, Claude might say "I don't have access to
current stock data." With your tool connected, Claude:

1. Recognizes this is a stock question
2. Calls your `get_stock_snapshot("AAPL")` tool
3. Gets back real data: price $195.20, up 0.85% today
4. Responds: "Apple is up 0.85% today at $195.20"

**Your data stays on your computer.** Claude doesn't store your stock
data. It asks your tool for data, gets an answer, and uses it. Your
tool runs on your machine.

---

## 1.3 What Is an MCP Server?

**MCP** stands for Model Context Protocol. It's a standard (created by
Anthropic, the company that makes Claude) that defines how AI connects
to tools.

Think of it like a USB port. USB is a standard that lets you plug any
device (mouse, keyboard, phone charger) into any computer. MCP is a
standard that lets any AI connect to any tool. Your tools use MCP, so
Claude Desktop knows how to use them.

An **MCP server** is a program that provides tools. You'll build one
this week. It runs on your computer and gives Claude Desktop access to
stock data.

The word "server" might sound intimidating, but it's just a program
that answers questions. When Claude Desktop asks "What's Apple's price?",
your server looks it up and sends back the answer.

### What's Inside an MCP Tool?

Each tool has four parts:

1. **A name** — like `get_stock_snapshot`. This is how Claude refers to it.
2. **Inputs** — what information the tool needs. For a stock tool, that's
   the ticker symbol (like "AAPL").
3. **A description** — a sentence explaining what the tool does. Claude
   reads this to decide when to use it.
4. **A return** — the data that comes back. This is structured information
   (price, daily change, volume, etc.), not just a blob of text.

You don't need to understand how to write these in code. Claude Code
will write them for you. But understanding these four parts helps you
describe what you want.

---

## 1.4 Designing Good Tools: Three Rules

Not all tools are created equal. Here are three rules that separate
good tools from bad ones.

### Rule 1: Do the Math in the Tool, Not in the AI

This is the most important rule. AI is great at language but surprisingly
bad at math. If you give AI two prices and ask it to calculate the
percentage change, it might get it wrong.

The fix: calculate everything in the tool and give the AI the finished
answer.

```
BAD tool return:
  "previous_close": 193.55
  "current_price": 195.20
  (AI has to calculate: 195.20 - 193.55 = 1.65, then 1.65/193.55 = 0.85%)

GOOD tool return:
  "previous_close": 193.55
  "current_price": 195.20
  "daily_change": 1.65
  "daily_change_pct": 0.85
  (Math is already done! AI just reports the number.)
```

### Rule 2: Tell the AI Where the Data Came From

Always include a `data_source` field (like "yahoo_finance") and an
`as_of` timestamp (like "2026-03-15 4:05 PM"). This way, the AI can
say "According to Yahoo Finance data as of 4:05 PM..." instead of
presenting information without context.

This matters because:
- If the data is from yesterday (because the market is closed), the AI
  should say so
- If the data comes from a free source (which might be slightly delayed),
  the AI should mention that
- If something goes wrong and the data is missing, the AI knows something
  is off

### Rule 3: Include a Guide Tool

A **guide tool** is a special tool that describes all the other tools.
It's like a menu at a restaurant — the AI reads it first to understand
what's available.

Without a guide tool, Claude has to figure out your tools from their
names and descriptions alone. With a guide tool, Claude knows exactly
what to call and in what order. For example:

```
"Start with get_watchlist_summary() for the big picture,
 then use get_stock_snapshot(ticker) to drill into one stock,
 then use get_stock_comparison(ticker1, ticker2) to compare two."
```

---

## 1.5 What You'll Build This Week

Your MCP server will have four tools:

| Tool | What It Does |
|------|-------------|
| `get_stock_snapshot` | Look up one stock — price, daily change, volume, etc. |
| `get_watchlist_summary` | Overview of all your watched stocks |
| `get_stock_comparison` | Compare two stocks side by side |
| `get_strategy_guide` | Menu of all tools for Claude to read first |

You'll use **yfinance** as your data source. It's a free library that
pulls stock data from Yahoo Finance. No account needed, no credit card,
no API key. Claude Code will install it for you automatically.

Your default watchlist will include companies you probably know:
**AAPL** (Apple), **NKE** (Nike), **DIS** (Disney), **TSLA** (Tesla),
**NFLX** (Netflix). But you can change these to whatever companies
interest you.

---

## Key Takeaways

1. **Stocks** are pieces of company ownership with ticker symbols and
   prices that change throughout the day
2. **AI can't look up stock prices by itself** — you need to build
   tools that fetch real data
3. **MCP** is the standard that connects AI to tools (like USB connects
   devices to computers)
4. **Do the math in the tool**, not in the AI — AI is bad at math
5. **Tell the AI where data came from** — include data source and
   timestamp in every tool return
6. **Include a guide tool** — give the AI a menu of what's available
