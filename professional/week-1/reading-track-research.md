# Week 1 — Stock Research Track: Section 1.2 Alternative

> This section replaces "1.2 The SPY/TLT Color Strategy" for the Stock
> Research track. Sections 1.1 and 1.3–1.6 are shared across both tracks.

## 1.2 A Document Intelligence System — Analyzing SEC Filings

> **You don't need to memorize any of this.** The server handles all the
> document processing automatically. You're reading this so you can
> understand what the tools are doing under the hood — and so you can
> evaluate AI tool design when you build your own in Week 2. Skim the
> technical details; focus on the overall structure.

### The Core Idea

Every public company tells its story in SEC filings. The 10-K annual
report, the 10-Q quarterly update, the 8-K material event disclosure —
these documents contain the ground truth about a company's finances,
risks, and strategy. Professional investors read them. But they're long,
dense, and hard to search across.

The page-index-rag server solves this: it takes SEC filings (or any
document), builds a structured index of every section, and lets Claude
search and cite specific passages. You ask a question in natural
language; Claude finds the exact paragraph in the filing that answers
it — with a citation you can verify.

This is **Retrieval-Augmented Generation (RAG)** — a pattern where the
AI retrieves relevant information from your documents before generating
a response. Instead of answering from training data (which may be
outdated or wrong), the AI answers from the actual filing.

### What Makes This RAG Different

Most RAG systems use vector search: they convert text into numerical
representations (embeddings) and find passages that are mathematically
similar to your question. This works but has failure modes. It can miss
passages that use different terminology, or return passages that are
superficially similar but not actually relevant.

The page-index-rag server uses a **structure-first approach** called
PageIndex. Instead of embedding chunks of text, it builds a hierarchical
index of the document's structure — sections, subsections, tables, and
key passages. When you search, the system navigates this structure to
find relevant sections, then reads them in context.

Think of it as the difference between searching a book with Ctrl-F
versus using the table of contents and index. Both work, but the
structural approach understands *where* information lives in the
document — not just which words appear near each other.

### Pre-Indexed Companies

The course server comes with filings pre-indexed for two companies:

| Company | Ticker | Filings | Why These Companies |
|---------|--------|---------|---------------------|
| **BlackRock** | BLK | 10-K, 10-Q | World's largest asset manager. Filings cover AUM trends, fee dynamics, iShares growth, regulatory risks. |
| **Robinhood** | HOOD | 10-K, 10-Q | Retail brokerage disruptor. Filings cover PFOF revenue, crypto exposure, user growth, regulatory challenges. |

These represent two very different business models in financial services.
BlackRock is an institutional asset manager with $10T+ AUM. Robinhood is
a consumer fintech platform. Comparing their filings — risk factors,
revenue composition, regulatory language — gives you a concrete feel for
what document-backed AI analysis can do.

You can also index your own documents later (in Week 2). Any PDF, HTML,
or CSV file can be indexed.

### The 14 Tools

The page-index-rag server exposes 14 tools to Claude. The most important
ones for your first session:

| Tool | What It Does |
|------|-------------|
| `get_rag_guide()` | Describes all tools and recommended workflows |
| `list_documents()` | Shows all indexed documents with their IDs |
| `search_with_citations(query, doc_id)` | Searches a document for relevant passages, returns text with citations |
| `batch_query(query, doc_ids)` | Searches across multiple documents at once |
| `get_document_overview(doc_id)` | Shows the structural outline of a document |
| `get_document_section(doc_id, node_id)` | Reads a specific section of a document |
| `fetch_company_filings(ticker, forms)` | Downloads new filings from SEC EDGAR |
| `check_company_indexed(ticker)` | Checks if a company's filings are already indexed |

The remaining tools handle indexing status, document management, and
batch operations. You'll see them in the guide tool output.

### How It Works in Practice

When you ask Claude "What are BlackRock's biggest risk factors?", here's
what happens:

1. Claude calls `search_with_citations("risk factors", doc_id="BLK-10K")`
2. The server searches the filing's structure for the Risk Factors section
3. It returns the relevant passages with page and section citations
4. Claude synthesizes the passages into a clear answer
5. You can verify every claim by checking the citation

The AI never invents financial information. Every statement it makes
about a company comes from the actual filing, with a citation you can
trace back to the source. This is the fundamental difference between
RAG-backed analysis and asking a chatbot questions from its training
data.

---
