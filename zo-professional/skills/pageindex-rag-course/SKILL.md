---
name: pageindex-rag-course
description: SEC filing analysis (10-K / 10-Q / 8-K / proxy / S-1 / Forms 3-4-144 / 20-F) for the AI Investing course (Week 2+) using the PageIndex vectorless RAG MCP server. Invoke whenever the student asks about a public company's risk factors, MD&A, revenue drivers, year-over-year changes, executive compensation, insider transactions, or anything that requires reading the actual text of a SEC filing. Backed by a local Ollama + gemma4:e2b model — no cloud LLM calls. Ships with BLK + HOOD pre-indexed so the centerpiece exercises work out of the box; `fetch_company_filings` is fully available from Week 2 for any ticker the student wants to research.
compatibility: Created for Zo Computer
metadata:
  author: jing.zo.computer
  course: zo-professional
  week: 2
---

# pageindex-rag-course

Agent guidance for the **course edition** of the PageIndex RAG MCP server. The student installs and registers it via the `course-setup` skill; this skill explains how to use it once it's live.

## Server fingerprint

- **Server name (in Zo MCP registry):** `page-index-rag-course`
- **Tool count:** 14
- **Source:** `professional/servers/page-index-rag-course/`
- **Entry point:** `uv run rag-server`
- **LLM backend:** local Ollama at `http://localhost:11434/v1`, model `gemma4:e2b`
- **Pre-indexed filings:** BLK (10-K + 10-Q × 2) and HOOD (10-K + 10-Q × 3) — at least 7 documents

If the indexed-filing count is 0, route the student back to the `course-setup` skill — Ollama or the model is likely missing.

## When to invoke

The student's question requires reading the text of a public-company SEC filing — financials, risk factors, MD&A, exec comp, ownership, legal, segments. Examples:

- "What are BLK's biggest risk factors in the latest 10-K?"
- "Did HOOD's MD&A discussion change from Q2 to Q3?"
- "What does management say about revenue drivers?"
- "Compare BLK and HOOD on regulatory risk."

**Do not invoke** for: real-time stock price, breaking news, anything not in a filing. Use the SPY/TLT skill or web search for those.

## Pre-indexed starter filings

BLK and HOOD ship pre-indexed (≥7 filings total) so the Week 2 centerpiece exercises work the moment the server is registered — no SEC fetch required, no waiting for indexing. Use them as the default examples.

For any other ticker, `fetch_company_filings` is fully available from day one. Heads-up to share with the student before they fetch:

- Indexing a full 10-K with `gemma4:e2b` summaries on a Zo box takes **~2–5 minutes per filing** — `fetch_company_filings` returns immediately with a `batch_id`; poll `check_indexing_status` until `COMPLETE` before searching.
- SEC EDGAR rate limit is ~10 req/s; PageIndex stays under that, but back-to-back fetches across many tickers can still hit it. If you do, wait 10 minutes.

## PageIndex philosophy — memorize this

```
┌─ REASONING PHASE (uses summaries for navigation) ──────────────┐
│  LLM reads tree structure + section summaries, picks node_ids  │
└────────────────────────────────────────────────────────────────┘
┌─ RETRIEVAL PHASE (uses raw text for answers) ──────────────────┐
│  Fetch full raw text for selected node_ids                     │
│  Use raw text to answer — NEVER use summaries as the answer    │
└────────────────────────────────────────────────────────────────┘
```

- **Summaries** = navigation aid only ("where should I look?")
- **Keyword search** = fast baseline; LLM reasoning kicks in only when keyword score is weak
- **Raw text** = the sole source of truth for any number, date, or legal phrasing you quote back to the student

## The 6-step workhorse pattern

Every research question follows this. Memorize it — it's the centerpiece of Weeks 2–4.

1. `list_documents` — see what's on the shelf. Note the doc_ids.
2. `get_document_overview(doc_id)` — read the table of contents for the filing you'll search.
3. `search_with_citations(query, doc_id=DOC_ID, max_results=5)` — find candidate sections. Show the student the top 3 with previews.
4. Pick the best candidate. Tell the student why (relevance to the question, not gut feel).
5. `get_document_section(doc_id, node_id)` — pull the **full raw text** for that node.
6. Quote the relevant 2–4 sentences verbatim. Write a one-paragraph answer that cites doc_id and node_id.

## Critical rules

- **Raw text is the only answer source.** Summaries are for navigation. Never quote a summary as if it were a financial statement.
- **Cite every claim with doc_id + node_id.** Inline format: `(BLK_10-K_20260225_..., node 0023)`.
- **`list_documents` first, every session.** The student needs to see what's available before you pick.
- **`check_company_indexed` before `fetch_company_filings`.** Avoids redundant SEC downloads and rate-limit hits.

## Tools at a glance

| Tool | Purpose |
| --- | --- |
| `list_documents` | List indexed filings. Call FIRST. |
| `get_document_overview(doc_id)` | Table of contents for one filing. |
| `search_with_citations(query, doc_id?, max_results?)` | Find relevant sections. Returns `node_id` candidates. |
| `get_document_section(doc_id, node_id)` | Full raw text — the sole answer source. |
| `batch_query(query, doc_ids)` | Same question across multiple filings (BLK vs HOOD, year-over-year, etc.). |
| `check_company_indexed(ticker)` | Check if a ticker is indexed. Call before `fetch_company_filings` to avoid redundant downloads. |
| `fetch_company_filings(ticker, forms, max_filings)` | Download + index filings from SEC EDGAR for any ticker. Returns immediately; indexing runs in background (~2–5 min/filing on a Zo box). |
| `check_indexing_status(batch_id)` | Poll background indexing. Call after `fetch_company_filings` until status is `COMPLETE`. |
| `ingest_drop_folder` | Index files dropped into `data/drop/`. Rarely needed in the course. |
| `remove_document(doc_id)` | Delete an indexed document. |
| `embed_documents(doc_ids)` | Generate semantic-search embeddings. Optional — disabled by default in the course. |

## Citation format

**Inline:**
> According to BLK's 2026 10-K (`BLK_10-K_20260225_000119312526071966_e6f23f33`, node 0015 — Item 1A Risk Factors), the company identifies fee-pressure as a key risk…

**End-of-response block:**
```
Sources:
- [1] BLK_10-K_20260225_..., node 0015 — Item 1A: Risk Factors
- [2] BLK_10-K_20260225_..., node 0023 — Item 7: MD&A
```

## Course context

Week 2 reading at `zo-professional/week-2/reading.md` motivates *why* primary-source citation beats LLM-summarized answers; the exercise at `zo-professional/week-2/exercise/README.md` walks the student through the 6-step pattern on a real BLK research question.

Production divergence: the production SEC-RAG server has additional tooling for live SEC monitoring, alerting, and cross-portfolio queries. The course server keeps the core workflow but trims production-only operational concerns. See `zo-professional/SERVER_CONTEXT.md` for the divergence registry.
