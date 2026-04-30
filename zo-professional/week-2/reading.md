# Week 2: SEC Filing RAG on Zo

The second workflow is primary-source document analysis with SEC filings.

The teaching server lives at:

`professional/servers/page-index-rag-course`

It is aligned with the production SEC-RAG architecture but remains small enough for students to run locally. It includes pre-indexed filings and a controlled retrieval flow.

## Why RAG Matters for Investment Work

Models can sound confident while misquoting filings. That is unacceptable in research.

The correct pattern is:

1. fetch the filing
2. parse it into sections
3. index the structure
4. search for relevant passages
5. retrieve source text
6. answer with citations

The model helps navigate and synthesize. The filing text remains the source of truth.

## What the Course Server Teaches

The PageIndex RAG course server teaches:

- document ingestion
- filing metadata
- structured section retrieval
- keyword and reasoning-assisted search
- citation discipline
- configurable LLM backends
- intentional divergence from production

The pre-indexed BLK and HOOD filings make the first experience fast. Students can see the workflow before waiting on new filings.

## The Citation Standard

For investment research, a useful answer must be traceable.

Acceptable:

> The filing says revenue increased because of higher transaction-based revenues. Source: document ID and node ID.

Not acceptable:

> Management seems optimistic about growth.

The second answer may be directionally plausible, but it is not research-grade unless it points back to source text.
