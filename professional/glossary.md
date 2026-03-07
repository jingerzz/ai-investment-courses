# Glossary

Key terms used throughout this course, explained for a non-technical audience.

---

**API (Application Programming Interface)**
A way for two pieces of software to talk to each other. When your MCP server
fetches stock prices from Yahoo Finance, it uses Yahoo's API. Think of it
as a structured request-and-response system between programs.

**Audit trail**
A chronological record of every action a system takes. In Week 4, your
monitoring agent logs every check, every alert, and every approval
decision — creating an audit trail that compliance can review.

**Claude Code**
Anthropic's command-line AI tool. You type instructions in plain English,
and it creates files, writes code, and runs commands on your computer.
This is how you build MCP servers throughout the course.

**Claude Desktop**
Anthropic's desktop AI assistant application. Once you connect MCP servers
to Claude Desktop, it can call your tools to access real data when
answering questions.

**Context window**
The amount of text an AI model can process at once. Measured in tokens
(roughly 1 token = 3/4 of a word). A 256K context window can handle
about 190,000 words — enough for most financial documents.

**Cosine similarity**
A mathematical measure of how similar two vectors are. In RAG, it's used
to find which document sections are most relevant to your question. You
don't need to understand the math — the code handles it.

**Embedding**
A way to convert text into a list of numbers (a vector) that captures its
meaning. Similar text produces similar numbers. This is how RAG systems
find relevant document sections — they compare the "meaning numbers" of
your question against the "meaning numbers" of each section.

**Fallback (data provider)**
A backup data source used when the primary one is unavailable. For
example, if a real-time feed goes down, the system falls back to a
delayed data source and warns the user.

**FastMCP**
The Python framework for building MCP servers. Claude Code uses this
when it creates your tools. You describe what you want; Claude Code
writes the FastMCP implementation.

**Guardrail**
A design pattern that prevents AI from making mistakes. Examples include
pre-computing numbers (so the AI doesn't do math wrong), stale data
warnings (so the AI doesn't present old data as current), and verbatim
sections (so the AI doesn't rephrase exact figures).

**Guide tool**
A special MCP tool that describes all the other tools on a server. The
AI calls this first to understand what's available and how to use it.
Like giving a new analyst a cheat sheet for your desk's systems.

**Human-in-the-loop**
A design principle where AI proposes actions but a human must approve
them before execution. Critical in finance for regulatory compliance
and risk management.

**MCP (Model Context Protocol)**
An open standard created by Anthropic that lets AI models connect to
external tools and data sources. Think of it as a universal adapter
between AI and your systems. Your MCP servers expose tools; Claude
Desktop calls them.

**MCP Inspector**
A testing interface for MCP servers. Run `uv run mcp dev server.py` to
open it. You can call each tool individually and see what it returns
before connecting to Claude Desktop.

**MCP Server**
A program that exposes tools via the MCP protocol. You build these
throughout the course. Each server runs on your computer and provides
Claude Desktop with access to specific data or capabilities.

**OAuth 2.1**
An authentication standard used when MCP servers run in the cloud.
Handles user login, token management, and access control. Not used in
this course (all servers run locally) but covered conceptually in Week 3.

**Ollama**
A tool that runs AI models locally on your computer. Used in the bonus
module to process documents privately without sending data to the cloud.

**Pre-computed value**
A number calculated by your code (Python) before the AI sees it. For
example, instead of giving the AI raw prices and expecting it to
calculate a return, you calculate the return in code and give the AI
the finished number. This prevents math errors.

**RAG (Retrieval-Augmented Generation)**
A technique that gives AI access to documents it wasn't trained on. The
system searches your documents for relevant sections, then feeds those
sections to the AI along with your question. The AI answers based on
your documents, not its training data.

**Structure-first RAG**
A RAG approach that preserves a document's natural structure (sections,
chapters, items) instead of blindly splitting it into chunks. Especially
important for financial documents like SEC filings where section identity
(Item 1A: Risk Factors) matters.

**Stale data warning**
A field in a tool's return that tells the AI the data isn't fresh. For
example, if the market is closed, the warning says "Prices are from
the most recent trading session." The AI then includes this caveat in
its response to the user.

**Terminal**
The text-based interface on your computer where you type commands. Also
called the command line, command prompt (Windows), or shell. This is
where you run Claude Code.

**Tool (MCP)**
A function exposed by an MCP server that AI can call. Each tool has a
name, parameters, and returns structured data. For example,
`get_stock_snapshot("AAPL")` is a tool that returns Apple's current
stock data.

**Tool-use pattern**
The approach where AI doesn't access data directly — instead, it calls
structured tools that you define. Your data stays in your systems; the
AI sends requests and receives responses.

**uv**
A fast Python package manager. Claude Code uses uv behind the scenes
to install Python libraries and run your MCP servers. You don't interact
with it directly.

**Vector**
A list of numbers that represents the meaning of a piece of text. Used
in RAG for searching documents. You don't need to understand the math —
the embedding model creates vectors, and the search code compares them.

**Verbatim section**
A pre-formatted piece of output (usually a table or summary) that the
AI should display exactly as returned by a tool, without rephrasing or
recalculating. A key guardrail pattern for financial data accuracy.

**yfinance**
A free Python library that provides stock market data from Yahoo Finance.
Used throughout the course as the primary data source. No API key or
account needed.
