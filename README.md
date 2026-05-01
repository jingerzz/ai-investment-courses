# AI Investment Academy

**Build AI-powered investment tools — no coding required.**

Three course tracks teach you to build real financial tools using plain English. The new Zo-centric track leads with Zo Computer as the operating environment; the existing Claude-centric professional and junior tracks remain available.

> **Deploying changes?** This repo is the canonical source of course
> content. The websites that publish it live in separate repos and
> require an explicit sync step. See [`DEPLOYMENT.md`](DEPLOYMENT.md)
> before pushing course updates.

---

## Course Tracks

### [AI-Powered Investment Management on Zo Computer](zo-professional/) — flagship Zo track

For investment professionals, founders, executives, and independent capital allocators who want AI-native investment workflows on a personal cloud computer. Uses Zo for files, services, hosted pages, automations, and AI orchestration. Claude Code and Codex are optional supported tools, not the center of the workflow.

### [AI-Powered Investment Management](professional/) — Claude-centric professional track

For investment analysts, portfolio managers, and IT managers at investment firms. Assumes deep finance knowledge. Teaches AI tool-building patterns used in production trading systems.

> "The AI received pre-computed risk metrics from your tool. It didn't calculate portfolio VaR — Python did. The AI's contribution was connecting the risk posture to the current regime and explaining why the hedge is working."

### [AI-Powered Investing for Juniors](juniors/) — junior track

For curious 8th-10th graders interested in investing and AI. No assumed knowledge of finance or programming. Same technology, same patterns — adapted language and relatable examples.

> "Tesla is your standout today — up 3.21% with more than double its normal trading volume, even while the overall market is slightly down. That kind of strength against a weak market is worth paying attention to."

---

## What You'll Build

| Module | Professional | Core Pattern |
|--------|-------------|-------------|
| Foundations 1 | Understanding the AI operating environment | How AI works with files, tools, and services |
| Foundations 2 | Workspace setup | Projects, secrets, channels, terminal, hosting |
| Week 1 | Use the SPY/TLT regime server | AI calls tools for real market data |
| Week 2 | Use SEC filing RAG | AI answers from primary-source filings |
| Week 3 | Multi-server architecture design | Separate concerns across services and datasets |
| Week 4 | Agent workflow with audit trail | AI watches and suggests, humans decide |

Every tool uses real market data from Yahoo Finance and SEC EDGAR. No toy examples. The tools keep working after the course ends.

---

## The Approach

**You do not need to write code by hand.**

In the Zo-centric track, Zo Computer is the home base for files, services, dashboards, automations, and AI interaction. Strong coding assistants such as Claude Code or Codex are optional accelerators inside that workflow.

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
- Zo-centric track: [Zo Computer](https://www.zo.computer/) account. Jing's referral link: https://zo-computer.cello.so/8dcc6g0vZVs
- [Claude Desktop](https://claude.ai/download)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code/getting-started)
- A Mac or PC (model recommendations tiered by RAM for the bonus module)

**Pick your course:**
- Zo-first professional track? Start with [`zo-professional/introduction.md`](zo-professional/introduction.md)
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
├── zo-professional/       # Zo-centric professional course
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
