# Prompts: Week 2

Use these prompts while working with the PageIndex RAG course server.

## Inspect the RAG Flow

```text
Inspect the PageIndex RAG course server. Explain the ingestion, indexing, search, and section retrieval flow in the order a student should use it.
```

```text
List the indexed documents available in the course server. For each document, identify the company, filing type, filing date, and document ID if available.
```

## Search and Retrieve

```text
Search the pre-indexed filings for management discussion of revenue drivers. Return the most relevant document/node candidates before writing any answer.
```

```text
Retrieve the source section for the best candidate. Quote only from the raw section text, and cite the document ID and node ID.
```

## Answer with Discipline

```text
Using only retrieved source text, answer this question: what does the filing say about the main drivers of recent business performance? Include the citation and avoid unsupported inference.
```

```text
Review this draft answer for citation quality. Flag any sentence that is not supported by the retrieved filing section.
```
