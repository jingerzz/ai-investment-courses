# AI Investment Academy

**Build AI-powered investment tools — no coding required.**

Two parallel courses that teach you to direct Claude to build real financial tools using plain English. You describe what you want. Claude builds it. You connect it to real market data. Every week produces a working tool.

---

## Two Courses, One Approach

### [AI-Powered Investment Management](professional/) — for finance professionals

For investment analysts, portfolio managers, and IT managers at investment firms. Assumes deep finance knowledge. Teaches AI tool-building patterns used in production trading systems.

> "The AI received pre-computed risk metrics from your tool. It didn't calculate portfolio VaR — Python did. The AI's contribution was connecting the risk posture to the current regime and explaining why the hedge is working."

### [AI-Powered Investing for Juniors](juniors/) — for high school students

For curious 8th-10th graders interested in investing and AI. No assumed knowledge of finance or programming. Same technology, same patterns — adapted language and relatable examples.

> "Tesla is your standout today — up 3.21% with more than double its normal trading volume, even while the overall market is slightly down. That kind of strength against a weak market is worth paying attention to."

---

## What You'll Build

| Module | Professional | Core Pattern |
|--------|-------------|-------------|
| Foundations 1 | Understanding Claude — LLMs, tokens, prompting | How AI works and where it fails |
| Foundations 2 | Desktop and Mobile workspace setup | Cross-device projects and attachments |
| Week 1 | Install a pre-built SPY/TLT or SEC filing server | AI calls tools for real data |
| Week 2 | Build your own MCP server with Claude Code | AI presents pre-computed numbers honestly |
| Week 3 | Multi-server architecture design | Separate concerns, connect with Claude |
| Week 4 | Agent workflow with audit trail | AI watches and suggests, humans decide |

Every tool uses real market data from Yahoo Finance and SEC EDGAR. No toy examples. The tools keep working after the course ends.

---

## The Approach

**You will not write a single line of code.**

You use [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — Anthropic's CLI for Claude — to build everything. Your skill is knowing what to ask for, checking whether it's correct, and improving it through conversation.

What you learn:
1. **Describe** workflows in plain English that produce working tools
2. **Evaluate** whether AI-built tools are correct
3. **Iterate** when the first version isn't right
4. **Design** systems worth building — with guardrails, audit trails, and human oversight

These skills transfer to any domain. Finance is the vehicle.

---

## Getting Started

**Time commitment:** 30 min reading + 30 min hands-on per week, for 4 weeks.

**Prerequisites:**
- [Claude Desktop](https://claude.ai/download)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code/getting-started)
- A Mac or PC (model recommendations tiered by RAM for the bonus module)

**Pick your course:**
- Finance professional? Start with [`professional/introduction.md`](professional/introduction.md)
- High school student? Start with [`juniors/introduction.md`](juniors/introduction.md)

Each course has its own detailed prerequisites and setup guide.

---

## Course Structure

Both courses share the same structure:

```
course/
├── introduction.md                    # Start here
├── prerequisites.md                   # Setup guide
├── week-N/
│   ├── reading.md                     # Concepts (30 min)
│   └── exercise/
│       ├── README.md                  # Step-by-step exercise
│       ├── conversation_guide.md      # Example prompts for Claude Code
│       ├── checklist.md               # Self-assessment
│       └── reference_solution.md      # Annotated good result
├── bonus-local-rag/                   # Optional: local AI with Ollama
├── conclusion.md                      # What you built, what's next
└── glossary.md                        # Every term defined
```

---

## Key Principles

**AI proposes, humans decide.** Every tool follows this pattern. AI surfaces information and suggests actions. Humans interpret and approve. The monitoring tools never execute trades — that's a permanent design choice, not a limitation.

**Guardrails are the point, not the caveat.** Pre-computed values prevent AI math errors. Stale data warnings prevent confident-sounding answers based on old information. Verbatim sections prevent creative rewriting of numbers. These patterns come from a production trading platform.

**Real data, not toy examples.** Yahoo Finance for stock prices, SEC EDGAR for filings, StockAnalysis.com for fundamentals. Free data sources, no paid subscriptions required.

---

## Repository Structure

```
ai-investment-courses/
├── professional/          # Course for finance professionals
├── juniors/               # Course for high school students
├── brand/                 # Visual identity and design guidelines
│   ├── shared.md          # Parent brand (typography, layout, tokens)
│   ├── professional.md    # Institutional finance aesthetic
│   └── juniors.md         # Modern fintech education aesthetic
├── SYNC_GUIDE.md          # How to keep courses aligned
└── .github/workflows/     # CI: structure sync check
```

The two courses teach the same technology with different voices. See [SYNC_GUIDE.md](SYNC_GUIDE.md) for how changes propagate between them.

---

## Technology

- **[Model Context Protocol (MCP)](https://modelcontextprotocol.io/)** — the open standard for connecting AI to external tools
- **[FastMCP](https://github.com/jlowin/fastmcp)** — Python framework for building MCP servers
- **[Claude Code](https://docs.anthropic.com/en/docs/claude-code)** — Anthropic's CLI that builds the tools from natural language
- **[Claude Desktop](https://claude.ai/download)** — where you use the tools in conversation
- **[Ollama](https://ollama.com/)** — local AI model runner (bonus module only)
- **[yfinance](https://github.com/ranaroussi/yfinance)** — free stock market data

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of course updates, fixes, and new content.

---

## Contributing

Found an error? Have a suggestion? Open an issue or PR. If your change affects one course, check [SYNC_GUIDE.md](SYNC_GUIDE.md) to see if the other course needs a corresponding update.

---

## License

This project is licensed under the [MIT License](LICENSE).
