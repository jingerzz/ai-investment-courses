# Glossary

Plain-English definitions of every technical term used in the course. If you forget one mid-module, come back here.

## Agent

A scheduled or event-driven AI workflow that runs a narrow task and produces an output. An agent is what you build when you want something to happen every weekday at 4:30 PM without you having to be there. Examples: a post-close market brief, a filing monitor, a portfolio drift checker.

## Artifact

A file produced by a workflow that you keep — a markdown report, a chart image, a CSV. Artifacts are how you remember what an AI actually did, instead of relying on chat history that may scroll away.

## Audit Trail

A record of what ran, what data was used, what output was produced, and what decision followed. The investment-grade version answers six questions: when, what tools, what data, what changed, what was recommended, and what the human decided.

## Color Day

A label the SPY/TLT teaching server applies to each trading day, based on whether SPY and TLT closed up or down. Green, Orange, Blue, and Red days each describe a different combination of equity and bond behavior. See Week 1 for the full table.

## Dashboard

A hosted page that shows the current state of something — a strategy, a portfolio, a watchlist — in a way a human can read at a glance. Dashboards are read-only by design; they do not place trades.

## Deterministic Tool

A piece of code that gives the same answer for the same inputs, every time. Used for prices, signals, levels, and metrics. A model that "explains" a number is non-deterministic; a script that calculates the number is deterministic. The course uses deterministic tools for anything that has to be exact.

## Filing RAG

A workflow that lets an AI answer questions about SEC filings by **retrieving** the actual filing text and then **generating** an answer based on that retrieved text. RAG stands for retrieval-augmented generation. In plain English: the AI looks the answer up before writing it.

## Guardrail

A rule, check, or piece of code that prevents the AI from doing something unsafe. Examples: a stale-data warning that flags when prices are out of date; a citation requirement that prevents quoting from a summary; an approval prompt before sending an external message.

## Hallucination

A confident but wrong statement from an AI model. The dangerous part is that hallucinations sound exactly like correct answers. Most of the course is about engineering the AI's environment so hallucinations get caught early.

## Human Decision Loop

The design principle that AI may observe, compute, retrieve, and recommend, but a human decides whenever capital or publication risk is involved. The loop is: AI proposes → tools compute → sources substantiate → human decides → system records.

## MCP

Model Context Protocol. A standard way for an AI assistant to talk to external tools. You can think of it as a common language: as long as a tool speaks MCP, almost any modern AI can call it. Anthropic published the protocol; it is open and not Claude-specific.

## MCP Server

A program that exposes one or more tools through the MCP protocol. The two course servers (`spy-tlt-course` and `page-index-rag-course`) are MCP servers. Each one offers a small set of named functions the AI can call.

## PageIndex

A way of preparing a long document — a 10-K, a 10-Q, a research report — so it can be searched section by section. Instead of treating the document as one long string, PageIndex builds a navigable structure with summaries at each level. The AI uses the summaries to find the right section, then quotes from the raw text.

## Regime

A label for what kind of market we are in. "Risk-on", "risk-off", "trending", and "choppy" are all loose regime labels. The SPY/TLT course server uses a more specific regime model based on color days. Regime matters because the same price action can mean different things in different regimes.

## Service

A long-running program that lives on Zo and answers requests. The course MCP servers are services. So is a hosted dashboard, a webhook receiver, or a small API. Services are what you build when you want something to keep running between conversations.

## Stale Data

Data that is technically loaded but no longer current. A price from yesterday's close at 3 PM today is stale. The course teaches tools to flag stale data with a warning rather than silently presenting it as live.

## Tool Boundary

The line between what code computes and what the AI explains. Good systems keep this line explicit: numbers come from code, narrative comes from the AI. Bad systems blur it, which is when models start inventing prices.

## Workspace

The set of folders and files that make up your project on Zo. Your workspace is the AI's working environment. A clean, predictable workspace makes the AI useful; a messy one makes it brittle.

## Zo Computer

A personal cloud computer where files, tools, services, hosted pages, integrations, and AI workflows all live together. Unlike a chat-only AI app, Zo gives the AI an actual computer to work on. That is why the course is built around it.
