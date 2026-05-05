# Exercise: Read a Filing With Zo

## Goal

By the end of this exercise, you will have asked Zo a real research question about a real SEC filing — and gotten back an answer with a citation you can verify in 10 seconds. You will also have caught the AI in at least one citation slip and corrected it.

Time: about 25–35 minutes. Server install is handled by the prerequisites; this exercise focuses on the research-and-citation workflow itself.

## What You Will Use

- **The course repository** — same repo as Week 1 ([github.com/jingerzz/ai-investment-courses](https://github.com/jingerzz/ai-investment-courses)), but a different folder.
- **Zo terminal** — to install and run the new server.
- **Zo chat** — to ask questions and watch the AI navigate the filings.

## Steps

### 1. Confirm the PageIndex server is ready

If you completed the [prerequisites](../../prerequisites.md), the PageIndex RAG course server is already installed, registered, and pre-indexed with BLK and HOOD filings. Ollama is running locally with the `gemma4:e2b` model that powers the server's section summaries. Confirm in Zo chat:

```text
List the MCP servers registered in this workspace. Specifically confirm
that page-index-rag-course is registered. Then call list_documents on
it and tell me how many BLK and HOOD filings are indexed.
```

You should see at least 7 indexed filings (BLK 10-K + 2x 10-Q, HOOD 10-K + 3x 10-Q). If the server is missing, the tool count is wrong, or `list_documents` returns nothing, ask:

```text
Use the course-setup skill to verify and repair my course setup.
```

That re-runs the bootstrap (Ollama, model, server install) and prints the registration prompt at the end. Do not move on until `list_documents` returns the BLK and HOOD filings.

### 2. Take inventory

Before asking a research question, see what is on the shelf:

```text
Call list_documents on the PageIndex server. For each indexed filing,
give me the company, filing type, filing date, and doc_id in a table.
```

Write the doc_ids down — you will use them in the next steps.

### 3. Look at the structure of one filing

A 10-K is a big document. Before searching, get the table of contents:

```text
Call get_document_outline on the most recent BLK 10-K (use the doc_id
from the previous answer). Show me the top-level sections and a few
notable sub-sections. This is the map I will use to navigate.
```

You should see familiar 10-K sections: business description, risk factors, MD&A, financial statements. The outline is structured the same way the SEC document is structured, because the indexer follows the document's own headings.

### 4. Ask the centerpiece research question

Pick a real question. Here is a good first one:

```text
Using the PageIndex server, answer this research question about the
most recent BLK 10-K: what does management say are the main drivers of
recent revenue performance?

Use this exact flow:
  1. Call search with a focused query, scoped to BLK's doc_id.
  2. Show me the top 3 candidates with their node_ids and previews.
  3. Pick the best candidate. Tell me why.
  4. Call get_section on that candidate.
  5. Quote the relevant 2–4 sentences verbatim.
  6. Write a one-paragraph answer that cites doc_id and node_id.
```

This is the workhorse pattern. You will reuse this six-step flow on every research question for the rest of the course.

A good response will:

- Show all 3 candidates, not just one
- Quote the chosen section verbatim before paraphrasing
- Cite both the `doc_id` and `node_id`
- Distinguish between what the filing literally says and what the AI infers

### 5. Stress-test against the failure modes

Pick at least two of these. They are designed to catch the failure modes from the reading.

**The summary stand-in test.**

```text
Show me the previews for the top 3 search results. Then retrieve the
full text of the top result. Compare them — what is in the section that
was not in the preview?
```

If the AI insists "the preview was enough," push back. The preview is for navigation; the section is the source.

**The phantom citation test.**

```text
You said earlier that BLK's revenue grew by [some number]. Show me the
exact tool call (search → get_section), the doc_id, the node_id, and
the verbatim sentence in the filing where that number appears.
```

If the AI cannot show you the call and the verbatim sentence, the number was a phantom. Make it redo the answer with a real retrieval.

**The cross-filing test.**

```text
Compare what the most recent BLK 10-K and the most recent HOOD 10-K
say about competitive pressure. For each one, give me the doc_id,
node_id, and a verbatim quote.
```

This tests whether the AI scopes its searches by company. You should see two distinct citations, not a blended summary.

### 6. (Optional) Index a new filing

If you have time, ask the server to fetch and index something fresh:

```text
Use index_filing to fetch and index NVDA's most recent 10-Q. Tell me
the doc_id when it is ready, and confirm with get_index_status.
```

Once it is indexed, you can run the same six-step flow on it. This is the bridge from "course content" to "your own research."

## Checkpoint

You are done when:

- The PageIndex course server is registered and the AI can call its tools
- You have run the six-step research flow at least once on a BLK or HOOD filing
- Every claim in your final answer has a `doc_id` / `node_id` citation
- You have caught the AI in at least one citation slip and corrected it
- You can explain in one sentence why the search preview is not the answer

If any of these are still rough, repeat the relevant step before moving on. Week 3 is where you start combining Week 1 and Week 2 into a single workflow.
