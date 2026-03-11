# Glossary

Key terms used in this course, explained in plain language.

---

## Investing Terms

**Stock**
A tiny piece of ownership in a company. If you buy one share of Roblox
stock, you own a very small fraction of Roblox. If Roblox does well, your
share becomes worth more.

**Ticker symbol**
A short code for a company's stock. Roblox is "RBLX", Spotify is "SPOT",
Snapchat is "SNAP". You'll use these codes when asking Claude about stocks.

**Stock price**
What one share of a company costs right now. Roblox's stock price might
be $60, meaning one share costs $60. Prices change throughout the
trading day.

**Market cap (market capitalization)**
The total value of all a company's shares combined. If a company has
1 million shares and each is worth $100, the market cap is $100 million.
It tells you how big a company is.

**P/E ratio (Price-to-Earnings ratio)**
A way to measure if a stock is expensive or cheap relative to how much
money the company makes. A P/E of 15 means investors are paying $15 for
every $1 of earnings. Higher P/E can mean investors expect more growth —
or that the stock is overpriced.

**Dividend**
Money a company pays to its shareholders, usually every three months.
Not all companies pay dividends. It's like getting a small paycheck
just for owning the stock.

**Volume**
How many shares of a stock were bought and sold in a day. High volume
means lots of people are trading it. Unusually high volume can signal
big news.

**52-week high / low**
The highest and lowest price a stock has reached in the past year. If
a stock is near its 52-week high, it's been doing well. Near the low,
not so much.

**Portfolio**
All the investments you own. If you have shares of Roblox, Spotify, and
Disney, those three stocks are your portfolio.

**Watchlist**
A list of stocks you're keeping an eye on, even if you don't own them.
Like a wish list for investments.

**YTD return (Year-to-Date return)**
How much a stock has gone up or down since January 1st of the current
year, shown as a percentage.

**Earnings**
The profit a company makes. Companies report their earnings every three
months (quarterly). When Roblox reports earnings, the stock often moves
a lot because investors are reacting to whether the company did better
or worse than expected.

**Stock split**
When a company divides its existing shares into more shares. If you own
1 share worth $500 and the company does a 10-for-1 split, you now own
10 shares worth $50 each. Your total value hasn't changed — there are
just more pieces. Netflix did this, which is why its share price went
from around $700 to around $70.

**Profitable**
A company is profitable when it makes more money than it spends. Crocs
is highly profitable — it earns money on every pair of foam clogs it
sells. Snapchat has never been profitable despite having 400 million
users. Being profitable and being popular aren't the same thing.

**10-K filing**
A detailed annual report that public companies must file with the
government (the SEC). It includes information about the business,
financials, and risks. Used in the bonus module.

**SEC (Securities and Exchange Commission)**
The government agency that regulates the stock market in the United
States. Companies that sell stock to the public must file reports with
the SEC.

---

## AI and Technology Terms

**AI (Artificial Intelligence)**
Computer software that can understand language, find patterns, and
make decisions. Claude is an AI. When you chat with Claude, you're
talking to an AI.

**LLM (Large Language Model)**
The type of AI that powers Claude, ChatGPT, and similar tools. It's
trained on huge amounts of text and learns to understand and generate
language. "Large" refers to the billions of patterns it learned.

**API (Application Programming Interface)**
A way for two programs to talk to each other. When your tool fetches
stock prices from Yahoo Finance, it uses Yahoo's API. Think of it as
a drive-through window — you make a request, and you get back exactly
what you asked for.

**Claude Code**
A tool from Anthropic that you use in your terminal. You type
instructions in plain English, and it creates files, writes code, and
runs commands on your computer. It's how you build everything in
this course.

**Claude Desktop**
Anthropic's AI assistant app. Once you connect your tools to Claude
Desktop, it can look up real stock data when answering your questions
instead of guessing.

**Context window**
The amount of text an AI can process at once. Think of it as the AI's
short-term memory. A bigger context window means it can handle longer
documents and more complex conversations.

**Embedding**
A way to turn text into a list of numbers that captures its meaning.
Similar sentences produce similar numbers. This is how the bonus
module's search system finds relevant sections in a document — it
compares the "meaning numbers" of your question against each section.

**FastMCP**
The Python tool kit for building MCP servers. Claude Code uses this
behind the scenes. You don't need to understand it — just know that
it's what makes your tools work.

**Guardrail**
A safety check built into an AI tool. Examples: calculating numbers in
code so the AI doesn't do math wrong, adding warnings when data is
old, formatting output so the AI doesn't rephrase exact figures.

**Guide tool**
A special tool that describes all the other tools on your server. The
AI calls this first to understand what's available. Like giving someone
a menu before they order.

**Hallucination**
When AI makes something up and presents it as fact. For example, AI
might say a stock is up 5% when it actually has no idea what the price
is. Guardrails help prevent this.

**MCP (Model Context Protocol)**
A standard created by Anthropic that lets AI connect to external tools
and data. Think of it as a universal adapter. Your tools use MCP so
Claude Desktop can call them.

**MCP Inspector**
A testing page for your tools. Run `uv run mcp dev server.py` to open
it. You can click each tool, try it out, and see what it returns before
connecting everything to Claude Desktop.

**MCP Server**
A program that provides tools via MCP. You build these throughout the
course. Each server runs on your computer and gives Claude Desktop
access to specific data.

**Ollama**
A tool that runs AI models on your own computer. Used in the bonus
module so you can process documents privately without sending data
to the internet.

**Pre-computed value**
A number calculated by code before the AI sees it. Instead of giving
the AI two prices and hoping it calculates the change correctly, you
calculate the change in code and give the AI the finished answer.

**RAG (Retrieval-Augmented Generation)**
A technique that lets AI answer questions about documents it wasn't
trained on. The system searches your documents for relevant parts,
then gives those parts to the AI along with your question. Used in
the bonus module.

**Terminal**
The text-based window on your computer where you type commands. Also
called the command line or command prompt. This is where you run
Claude Code.

**Tool (MCP)**
A function that AI can call. Each tool has a name and returns structured
data. For example, `get_stock_snapshot("RBLX")` is a tool that returns
Roblox's current stock information.

**uv**
A behind-the-scenes tool that Claude Code uses to manage Python
libraries. You install it once and then forget about it.

**Vector**
A list of numbers that represents the meaning of text. Used in the
bonus module for searching documents. You don't need to understand
the math — the code handles it.

**yfinance**
A free tool that provides stock market data from Yahoo Finance. Used
throughout the course. No account needed.
