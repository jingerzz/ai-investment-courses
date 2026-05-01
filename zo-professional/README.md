# AI-Powered Investment Management on Zo Computer

Build and operate AI-native investment workflows on your own cloud computer.

This is the Zo-centric professional track of AI Investment Academy. It teaches investment professionals, founders, executives, and independent capital allocators how to use Zo Computer as the operating environment for research, trading tools, dashboards, and controlled AI agents.

The course uses the latest teaching versions of the SPY/TLT strategy server and SEC filing RAG server from this repo:

- `professional/servers/spy-tlt-course`
- `professional/servers/page-index-rag-course`

Those servers are intentionally smaller than the production systems running on Jing's Zo Computer, but they preserve the core architecture students need to understand.

## Positioning

The Claude-centric course remains available as a supported track. This track leads with Zo:

- Zo Computer is the home base for files, services, datasets, automations, hosted pages, and AI work.
- Claude Code and Codex are optional power tools inside the Zo workflow.
- Students should be able to complete the hands-on work with a strong coding model for build steps and a free-tier chat model for ordinary interaction.
- The required prerequisite is a Zo Computer account. Use Jing's referral link: https://zo-computer.cello.so/8dcc6g0vZVs

## Audience

This track is for:

- Investment analysts, portfolio managers, and research leads
- Founders and executives who want to apply AI to capital allocation and operating leverage
- Independent investors who want durable tooling instead of newsletter subscriptions
- AI-forward finance teams evaluating internal research and trading infrastructure

## What You Build

| Module | Output | Pattern |
| --- | --- | --- |
| Foundations 1 | Mental model for Zo as an AI operating environment | Files + tools + models + hosted services |
| Foundations 2 | Personal investment workspace setup | Workspace structure, secrets, channels, browser, terminal |
| Foundations 3 | Persistent context for investment AI | Memory files, USER.md, AGENTS.md, session continuity |
| Week 1 | SPY/TLT regime workflow on Zo | AI calls tools backed by real market data |
| Week 2 | SEC filing RAG workflow on Zo | AI answers from indexed primary-source filings |
| Week 3 | Multi-server investment architecture | Separate concerns across services, datasets, dashboards, and agents |
| Week 4 | Controlled investment agent workflow | Scheduled runs, audit trail, approvals, human decision loop |

## Course Structure

```
zo-professional/
├── introduction.md
├── prerequisites.md
├── foundations-1/
│   ├── reading.md
│   └── exercise/README.md
├── foundations-2/
│   ├── reading.md
│   └── exercise/README.md
├── foundations-3/
│   ├── reading.md
│   └── exercise/README.md
├── week-1/
│   ├── reading.md
│   └── exercise/README.md
├── week-2/
│   ├── reading.md
│   └── exercise/README.md
├── week-3/
│   ├── reading.md
│   └── exercise/README.md
├── week-4/
│   ├── reading.md
│   └── exercise/README.md
├── conclusion.md
└── glossary.md
```

## Design Principle

AI does not become useful in investment management because it writes clever prose. It becomes useful when it can safely use the right tools, read the right files, cite the right sources, and leave an audit trail. Zo is the environment where those pieces live together.
