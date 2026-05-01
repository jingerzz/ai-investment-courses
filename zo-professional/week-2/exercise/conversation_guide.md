# Prompts: Week 2

These prompts go with the PageIndex RAG exercise. Run them in Zo chat after the server is registered. A general-purpose model is fine; a coding-grade model is not required.

The prompts are grouped by what you are trying to do. Each one has a one-line note explaining what to expect from the AI's reply.

## Take Inventory

```text
Call list_documents on the PageIndex server. For each indexed filing,
show me the company, filing type, filing date, and doc_id in a table.
```

> A good answer is a clean table with at least the BLK and HOOD pre-indexed filings. If the table is empty, the registration is off.

```text
Call get_document_outline on the most recent BLK 10-K. Show me the
top-level sections and a few notable sub-sections. Use this as the map
I will navigate from.
```

> You should see standard 10-K sections: Item 1 Business, Item 1A Risk Factors, Item 7 MD&A, etc. If the outline looks chaotic, the document was parsed wrong — try a different filing.

## The Six-Step Research Flow

This is the workhorse pattern for every research question for the rest of the course.

```text
Using the PageIndex server, answer this question about the most recent
BLK 10-K: what does management say are the main drivers of recent
revenue performance?

Use this exact flow:
  1. Call search with a focused query, scoped to BLK's doc_id.
  2. Show me the top 3 candidates with their node_ids and previews.
  3. Pick the best candidate. Tell me why.
  4. Call get_section on that candidate.
  5. Quote the relevant 2–4 sentences verbatim.
  6. Write a one-paragraph answer that cites doc_id and node_id.
```

> If the AI skips a step, do not let it. Each step exists to keep the answer honest. Repeat the prompt with "you skipped step X" if needed.

```text
Same flow, different question: what does the filing say about the main
business risks the company is currently facing?
```

> Tests whether the AI can use the same flow for a different topic. Risk Factors is the obvious section; it should land there fast.

## Verify the Citation

```text
You cited doc_id [X] and node_id [Y]. Call get_section on that pair
again and show me the full text. I want to confirm the quote is
verbatim.
```

> Forces the AI to re-fetch and prove the quote. If the verbatim text differs from what was quoted earlier, the AI was paraphrasing — push back.

```text
Show me the previews for the top 3 search results. Then retrieve the
full text of the top result. List one fact that is in the section but
not in the preview.
```

> Trains the AI to never quote from a preview. The preview was for navigation only.

## Reasoning Search

```text
The keyword search for [topic] did not return useful candidates. Use
reasoning_search instead — let the model rephrase the query first —
and show me the new ranked candidates.
```

> Use this when keyword search misses because the filing uses different language than your question. Reasoning search is slower but catches paraphrases.

## Compare Across Filings

```text
Compare what the most recent BLK 10-K and the most recent HOOD 10-K
say about competitive pressure. For each company, give me the doc_id,
node_id, and a verbatim quote, and then a one-sentence comparison.
```

> Two companies, two citations, then a comparison sentence. If the AI returns one blended paragraph with no citations, it is paraphrasing from memory.

```text
Same comparison, but for revenue concentration risk. If one filing
does not have a clear section on this, say so explicitly rather than
inventing one.
```

> Trains the AI to admit when a filing does not address a topic. "We did not find this in the filing" is a research-grade answer.

## Probe the Boundaries

```text
You said earlier that [company] mentioned [specific point]. Show me
the exact (doc_id, node_id) and the verbatim sentence where that
appears in the filing.
```

> Use this any time the AI says something that sounds plausible but unfamiliar. Plausible-but-uncited is the most expensive failure mode in research.

```text
You retrieved section [node_id]. Read it again and tell me one nuance
in the section that your previous summary dropped. I want to know what
got compressed away.
```

> The "executive summary trap." Forces the AI to surface what it left out. The dropped nuance is often the most interesting part.

## A Note on Pushback

If the AI ever quotes a number or fact without a `(doc_id, node_id)` citation, treat it as a bug and tell it explicitly: *"That fact has no citation. Re-run with a search and get_section call, and quote the section verbatim."* Two or three rounds of this in your first session will train the rest of the week's behavior.
