# AI-Powered Investment Management — 4-Week Course

## Overview

This course teaches finance professionals how to build AI-powered tools for
investment management — using Claude as your builder. You don't need to know
how to code. You'll describe what you want in plain English, and Claude will
build it for you.

**Audience:** Investment analysts, portfolio managers, IT managers at investment firms
**Format:** 30 min reading + 30 min hands-on per week (4 weeks)
**Prerequisites:** Claude Desktop installed (see Week 1 setup guide)

## What You'll Learn

This is NOT a coding course. You'll learn to:
- **Experience** what good AI tools feel like — before building your own
- **Describe** financial workflows to Claude in a way that produces useful tools
- **Evaluate** whether what Claude built is correct and complete
- **Connect** your tools to Claude Desktop so AI has access to real market data

## Weekly Progression

| Week | Focus | What You'll Do |
|------|-------|----------------|
| 1 | The tool-use pattern | Install a pre-built SPY/TLT strategy server. Experience AI answering questions backed by real market data. Learn MCP, design principles, and guardrail patterns. |
| 2 | Building your own AI tools | Use Claude Code to build a watchlist server from scratch. Set up Ollama and a private document Q&A system for SEC filings. |
| 3 | System design and architecture | Design a multi-server system for your organization. Learn separation of concerns, shared libraries, and deployment. |
| 4 | Autonomous agents and controls | Build an agent workflow with approval rules and audit trail. |

## Prerequisites

See `prerequisites.md` for the complete setup guide (accounts, software,
hardware requirements, and troubleshooting).

Quick version — install these before Week 1:
1. **Claude Desktop** — [claude.ai/download](https://claude.ai/download)
2. **A terminal application** — Terminal (Mac) or PowerShell (Windows)
3. **Claude Code** (recommended) — `curl -fsSL https://claude.ai/install.sh | bash` (Mac/Linux) or `irm https://claude.ai/install.ps1 | iex` (Windows)

Week 2 additionally requires:
4. **Ollama** — `brew install ollama` (Mac) or [ollama.com/download](https://ollama.com/download)

## Included Servers

The course includes pre-built MCP servers in the `servers/` directory:

| Server | Used In | Description |
|--------|---------|-------------|
| `spy-tlt-course` | Week 1 | SPY/TLT color strategy with 14 tools (signals, levels, patterns, briefings) |
| `page-index-rag-course` | Week 2 | SEC filing Q&A with 14 tools. Includes 7 pre-indexed BLK and HOOD filings. |
| `my-watchlist` | Week 2 | Students build this themselves with Claude Code |

## Data Sources

This course uses free data sources with no paid subscriptions required:
- **Yahoo Finance** (via yfinance library) — stock prices, technicals
- **SEC EDGAR** — public company filings (10-K, 10-Q, 8-K)
- **Ollama** — local AI models for document search (free, open-source)

## Structure

```
professional/
├── introduction.md                 # Opening chapter
├── conclusion.md                   # Closing chapter
├── prerequisites.md                # Setup guide
├── glossary.md                     # Technical terms defined
├── COURSE_BRIEF.md                 # Metadata for book production
├── week-1/
│   ├── reading.md                  # SPY/TLT strategy, MCP, design principles
│   └── exercise/
│       └── README.md               # Install and explore pre-built servers
├── week-2/
│   ├── reading.md                  # Claude Code, guardrails, Ollama, RAG
│   └── exercise/
│       └── README.md               # Part A: build server; Part B: set up RAG
├── week-3/
│   ├── reading.md                  # System design and architecture
│   └── exercise/
│       └── README.md               # Architecture design exercise
├── week-4/
│   ├── reading.md                  # Autonomous agents and controls
│   └── exercise/
│       └── README.md               # Agent workflow exercise
└── servers/
    ├── spy-tlt-course/             # Pre-built strategy server (Week 1)
    ├── page-index-rag-course/      # Pre-built RAG server (Week 2)
    └── my-watchlist/               # Built by student (Week 2)
```
