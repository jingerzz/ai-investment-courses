# Foundations 1: Zo as an AI Operating Environment

AI becomes more useful when it has a durable place to work.

A normal chat app remembers a conversation. Zo gives the AI a computer: files, terminal, services, automations, integrations, browser access, and hosted pages. That changes the shape of the work.

## The Core Mental Model

Think of Zo as four layers:

| Layer | What It Holds | Investment Example |
| --- | --- | --- |
| Files | Markdown, code, data, notes | research memos, watchlists, strategy docs |
| Tools | Scripts, MCP servers, APIs | SPY/TLT signals, SEC filing search |
| Surfaces | Sites, dashboards, reports | regime dashboard, research page |
| Agents | Scheduled workflows | post-close market brief, filing monitor |

The AI sits across these layers. It can read files, run tools, edit code, publish pages, and schedule future work when you allow it.

## Why This Matters in Finance

Investment work is not a single prompt. It is a chain:

1. collect data
2. clean data
3. compute metrics
4. retrieve source documents
5. reason about context
6. produce an output
7. review and decide
8. archive the decision trail

If the chain lives only in a chat window, it is fragile. If it lives on a computer you control, it becomes inspectable and repeatable.

## The Guardrail Pattern

The course uses a simple rule:

AI should explain and orchestrate. Deterministic tools should compute.

For example:

- A Python tool calculates signal levels.
- A RAG tool retrieves exact filing text.
- A dashboard renders the current state.
- The AI explains what changed and why it matters.

This reduces the chance that a model invents a price, misquotes a filing, or silently changes methodology.

## What Good Looks Like

A useful AI investment workflow should be:

- grounded in real data
- easy to re-run
- explicit about stale inputs
- clear about sources
- narrow enough to audit
- designed for human approval before capital is put at risk

That is the standard for every hands-on module.

