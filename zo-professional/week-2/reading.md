# Week 2: Reading SEC Filings With Zo

## 2.1 The Second Real Workflow

Last week's tool answered "what is the market doing today?" This week's tool answers a different question: **"what does this company actually say about itself, in its own filings, in its own words?"**

That second question is the heart of fundamental research. Earnings calls and analyst summaries can drift; a 10-K is the company's signed statement to the SEC. If you can read those documents at scale and quote them accurately, you can build an opinion that holds up.

The tool you will use this week is the **PageIndex RAG course server**, in the course repository at:

```
professional/servers/page-index-rag-course
```

It is a teaching version of the production SEC research server. The production version downloads, indexes, and searches every filing for hundreds of tickers. The course version ships with a few BLK and HOOD filings already indexed so you can skip the wait and start asking questions on day one.

> **You are not going to read full 10-Ks for fun.** The point is to learn how the AI navigates them so you can later ask "what did this company say about X?" and trust the answer.

## 2.2 Why You Cannot Just Hand a 10-K to an AI

A natural first instinct is "the model is smart, I will just paste the filing in and ask my question." There are three reasons this does not work for investment research:

**Filings are too long.** A typical 10-K is 150–300 pages of dense PDF. Even with large context windows, paying to send the full filing on every question is expensive and slow.

**Models drift on long documents.** When everything is dumped in one block, the model sometimes "remembers" things from training that look right but are not actually in the document. You have no way to tell.

**You cannot cite a paste.** A research note that says "the company mentioned supply-chain risk" is worthless without a page or section reference. You need the exact source text behind every claim.

The fix is **retrieval-augmented generation**, or RAG. Instead of pasting the whole filing, you let a dedicated system store the filing in a structured way, search it for the right section, and feed only that section to the AI. The AI's job becomes "explain this short, real piece of text" — not "remember the whole document."

## 2.3 What "RAG" Actually Means in Six Steps

RAG sounds technical. The mechanics are simple:

1. **Fetch** the filing from EDGAR (the SEC's public archive).
2. **Parse** it into sections — risk factors, MD&A, financial statements, etc.
3. **Index** the sections so each one has a stable ID and can be searched.
4. **Search** the index when a question comes in. Return the best-matching sections as candidates.
5. **Retrieve** the actual source text for the best candidate.
6. **Answer** the question by quoting from the retrieved text, with the document and section ID attached as a citation.

The AI is involved in steps 4 and 6. The other four steps are handled by code. That separation matters: the parts of the workflow that need to be exact are exact, and the parts that need to be flexible (deciding which section is relevant, writing the prose) are the parts the AI is good at.

## 2.4 What the Course Server Gives You

The PageIndex course server exposes a small set of tools:

**Inventory**
- `list_documents` — every filing currently indexed, with company, type, and filing date

**Navigation**
- `get_document_outline` — the section structure of a single filing, like a table of contents
- `get_section` — the full raw text of one section, by ID

**Search**
- `search` — keyword search across one filing or all filings, returns ranked candidates
- `reasoning_search` — same, but uses the AI to rephrase the query first (catches paraphrases)

**Bookkeeping**
- `index_filing` — fetch and index a new filing on demand
- `get_index_status` — has the indexing job finished yet?

The course server ships with BLK and HOOD filings already indexed. That means you can skip `index_filing` for the first hour and just explore the data that is already there. (Indexing a new filing takes minutes; pre-indexed filings let the workflow feel snappy on first contact.)

## 2.5 What a Tool Output Actually Looks Like

When the AI calls `search`, it gets back ranked candidates that look roughly like this:

```json
[
  {
    "doc_id": "BLK_10K_2024",
    "node_id": "item_1a_risk_factors_3",
    "section_title": "Risk Factors — Operational risks",
    "score": 0.91,
    "preview": "Our investment performance and the success of our products depend on..."
  },
  {
    "doc_id": "BLK_10K_2024",
    "node_id": "item_7_mdna_revenue",
    "section_title": "MD&A — Revenue analysis",
    "score": 0.78,
    "preview": "Revenue increased $X.XB year over year, driven primarily by..."
  }
]
```

Three things to notice:

**Every candidate has a stable ID.** `BLK_10K_2024` and `item_7_mdna_revenue` will not change if you re-run the search. You can save them in research notes and come back to them later.

**The preview is not the answer.** It is bait — a few words to help the AI (and you) decide which candidate is worth retrieving in full.

**The score is relative.** A 0.91 next to a 0.78 says "this one is a better match." It does not say "this one is true." Truth comes from the retrieved text in step 5, not from the search score.

After the AI picks a candidate, it calls `get_section(doc_id, node_id)` and gets the full source text. **That** is what gets quoted.

## 2.6 The Citation Standard

Every claim that comes out of this workflow must be traceable back to a `(doc_id, node_id)` pair. That is the single rule.

**Acceptable:**

> BLK's 2024 10-K describes its operational risk profile as concentrated in technology platforms and key personnel.
> *Source: BLK_10K_2024 / item_1a_risk_factors_3*

**Not acceptable:**

> BlackRock seems concerned about technology and people risk this year.

The first answer points back to a section. You can pull up that section in 10 seconds, read it, and either confirm or push back. The second answer is just vibes — directionally maybe correct, but useless as research.

When you write a research note from this workflow, every quoted line needs a citation. When the AI returns an answer without one, that is a bug — make it redo the call.

## 2.7 Where AI Adds Value (and Where It Does Not)

**Where the AI helps:**

- Rephrasing a vague question ("what's their growth story?") into a useful search query ("recent revenue drivers", "segment growth", "outlook")
- Picking the best candidate from a ranked search result based on the section titles and previews
- Reading the retrieved section and writing a plain-English summary
- Comparing the same topic across multiple filings (e.g., risk factors year over year)

**Where the AI should not be involved:**

- Quoting numbers it did not see in a retrieved section. (Phantom numbers from training memory.)
- Inferring tone or strategy from a section's headline alone. The full text matters.
- Deciding what a number means without the surrounding paragraphs.
- Skipping the citation. Ever.

## 2.8 Common Failure Modes (Week 2 Edition)

**The summary stand-in.** The AI quotes from the search preview instead of retrieving the section. The preview is 1–2 sentences and was meant for navigation, not for quoting. Always retrieve the full section before answering.

**The training-memory citation.** The AI confidently says "as stated in BLK's 10-K, revenue grew 12.3%" with no `doc_id` / `node_id`. That number may be from training data, last year's filing, or another company entirely. Force a tool call.

**The wrong filing.** Multiple filings are indexed. The AI searches without specifying `doc_id` and pulls a result from the wrong year or company. When in doubt, pin the search to a specific document.

**The "executive summary" trap.** A long retrieved section gets compressed to one sentence by the AI. Some of the nuance is dropped. For a research-grade answer, ask for both the verbatim quote *and* a one-sentence interpretation.

## Key Takeaways

- **RAG separates what the model is good at from what code should do.** Code fetches, parses, indexes. AI navigates and explains.
- **Every claim needs a citation.** A `(doc_id, node_id)` pair is the unit of evidence.
- **Search is not the answer; the retrieved section is.** Previews are bait — never quote them.
- **The course server ships with BLK and HOOD pre-indexed** so you can start asking questions immediately.
- **The AI's job is to navigate the filing.** Yours is to make the call.
