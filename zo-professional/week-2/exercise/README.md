# Exercise: Use SEC Filing RAG from Zo

## Goal

Use Zo to inspect and run the PageIndex RAG teaching server, then answer a company research question with citations.

## Source Server

Use the updated course server:

`professional/servers/page-index-rag-course`

This server includes pre-indexed BLK and HOOD filings so students can start with retrieval before fetching new documents.

## Steps

1. Open the PageIndex RAG course server folder.
2. Read the configuration file and the server entrypoint.
3. List the indexed documents.
4. Pick one BLK or HOOD filing.
5. Ask a question about risk factors, MD&A, revenue drivers, or business model changes.
6. Retrieve the source section before writing the answer.
7. Write a short answer with document and node citation.

## Prompts to Use

```text
Inspect the PageIndex RAG course server. Explain the ingestion, indexing, search, and section retrieval flow in the order a student should use it.
```

```text
Using the pre-indexed filings, answer this question with a source citation: what does the filing say about the main drivers of recent business performance?
```

## Checkpoint

You are done when:

- you can list indexed filings
- you can search for a topic
- you can retrieve source text
- your final answer cites the document and node
- you can explain why summaries are navigation aids, not the source of truth
