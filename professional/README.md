# AI-Powered Investment Management — 4-Week Course

## Overview

This course teaches finance professionals how to build AI-powered tools for
investment management — using Claude as your builder. You don't need to know
how to code. You'll describe what you want in plain English, and Claude will
build it for you.

**Audience:** Investment analysts, portfolio managers, IT managers at investment firms
**Format:** 30 min reading + 30 min hands-on with Claude per week (4 weeks)
**Prerequisites:** Claude Desktop and Claude Code installed (see Week 1 setup guide)

## What You'll Learn

This is NOT a coding course. You'll learn to:
- **Describe** financial workflows to Claude in a way that produces useful tools
- **Evaluate** whether what Claude built is correct and complete
- **Iterate** when the first version isn't quite right
- **Connect** your tools to Claude Desktop so AI has access to real market data

## Weekly Progression

| Week | Focus | What You'll Build |
|------|-------|-------------------|
| 1 | Getting started with Claude Code | An MCP server that gives Claude access to your stock watchlist data |
| 2 | AI reasoning and guardrails | A morning briefing tool that cross-references multiple data sources |
| **Bonus** | **Local RAG with Ollama (optional)** | **A private document Q&A system for SEC filings using local AI models** |
| 3 | System design and architecture | A multi-server system design for your organization |
| 4 | Autonomous agents and controls | An agent workflow with approval rules and audit trail |

The bonus module is optional and recommended after Week 2. It works on any
Mac or PC — model recommendations are tiered by RAM (8GB / 16GB / 32GB+).

## Prerequisites

See `prerequisites.md` for the complete setup guide (accounts, software,
hardware requirements, and troubleshooting).

Quick version — install these before Week 1:
1. **Claude Desktop** — [claude.ai/download](https://claude.ai/download)
2. **Claude Code** — See `week-1/exercise/setup.md` for step-by-step instructions

## Data Sources

This course uses free data sources with no paid subscriptions required:
- **Yahoo Finance** (via yfinance library) — stock prices, fundamentals, options
- **StockAnalysis.com** — financial statements, screener, analyst ratings
- **FRED** (Federal Reserve Economic Data) — macro indicators, interest rates
- **SEC EDGAR** — public company filings (10-K, 10-Q, 8-K)

## Structure

Each week contains:
```
week-N/
├── reading.md                      # Concepts (30 min read)
└── exercise/
    ├── README.md                   # Step-by-step exercise guide
    ├── conversation_guide.md       # Example prompts for Claude Code
    ├── checklist.md                # How to evaluate what Claude built
    └── reference_solution.md       # Annotated walkthrough of a good result
```

Special files:
- `introduction.md` — Why this course matters (opening chapter)
- `conclusion.md` — What you've built and what's next (closing chapter)
- `prerequisites.md` — Complete setup guide with troubleshooting
- `glossary.md` — All technical terms defined for a non-technical audience
- `COURSE_BRIEF.md` — Metadata and design direction for book production
- `week-1/exercise/setup.md` — First-time installation guide (terminal, Claude Code, uv)
- `bonus-local-rag/exercise/ollama_quickstart.md` — Ollama CLI reference and model setup
