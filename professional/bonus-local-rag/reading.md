# Bonus Module: Local RAG with Ollama — Private Document Q&A

## Why Local Models?

In Week 2, you learned about RAG — giving AI access to documents it wasn't
trained on. In that module, we used cloud AI (Claude) for everything. That
works well for public data like stock prices, but what about:

- **Proprietary research notes** your firm doesn't want leaving the building
- **Client portfolio reports** with PII and account details
- **Internal strategy memos** with non-public investment theses
- **Compliance documents** that must stay on-premises

Local models solve this. Instead of sending documents to a cloud API, you
run the AI model on your own machine. The data never leaves your computer.

### When to Use Local vs. Cloud

| Use Case | Best Choice | Why |
|----------|------------|-----|
| Public SEC filings | Either | Data is public anyway |
| Stock prices, market data | Cloud (Claude) | Better reasoning |
| Proprietary research notes | Local (Ollama) | Data stays private |
| Client reports | Local (Ollama) | Regulatory requirement |
| Complex multi-step analysis | Cloud (Claude) | Needs stronger reasoning |
| High-volume document search | Local (Ollama) | No API costs |

The sweet spot: **use local models for document search and retrieval, cloud
models for complex reasoning.** Your MCP server can use Ollama for finding
the right passages, then Claude Desktop interprets them.

---

## What Is Ollama?

Ollama is a tool that runs AI models locally on your Mac (or PC). It's like
having a private AI that runs entirely on your hardware.

Key concepts:

- **Models** are the AI brains. Different models have different strengths.
  Some are good at general text; others are specialized for embeddings
  (converting text to searchable vectors).

- **Pulling** a model downloads it to your machine. Models range from 1GB
  to 50GB+ depending on capability.

- **Serving** means Ollama runs in the background, ready to process requests.
  Your Python code talks to it via a local API (no internet needed).

### Recommended Models for Finance RAG

Pick the text model that matches your machine. Everyone uses the same
embedding model (`nomic-embed-text`).

**Embedding model (required for all setups):**

| Model | Disk | RAM | Notes |
|-------|------|-----|-------|
| `nomic-embed-text` | ~275MB | ~300MB | Converts text to searchable vectors. Small and fast. |

**Text model (pick one based on your machine):**

| Your Machine | Model | Disk | RAM | Quality |
|-------------|-------|------|-----|---------|
| 8GB RAM | `qwen3.5:0.8b` | ~1GB | ~1GB | Good — handles basic Q&A and summaries |
| 16GB RAM | `qwen3.5:4b` | ~3.4GB | ~3-4GB | Great — strong reasoning, accurate citations |
| 32GB+ RAM | `qwen3.5:9b` | ~7GB | ~6-7GB | Excellent — near cloud-quality for local use |

**Our default recommendation is `qwen3.5:4b`** — it hits the sweet spot
for most participants. All Qwen 3.5 models share the same capabilities:
256K context window (ideal for long financial documents like 10-K filings),
multimodal support (can process images and charts), and strong performance
on structured/technical content. Larger models give better answers but
use more resources.

**How to choose:**
- If your machine has **8GB RAM**, use `qwen3.5:0.8b`. It won't produce
  answers as polished as the 4B model, but it runs smoothly and the
  hybrid approach helps — Claude Desktop does the sophisticated reasoning
  on top of what the local model retrieves.
- If your machine has **16GB RAM** (most participants), use `qwen3.5:4b`.
  This leaves ~8-10GB free for the OS, Claude Desktop, and your browser.
- If your machine has **32GB+ RAM**, try `qwen3.5:9b` for noticeably
  better answer quality. You can also run both the 4B (for fast search)
  and 9B (for final answers) side by side if you want speed + quality.

---

## How RAG Works (The Simple Version)

RAG has two phases:

### Phase 1: Indexing (done once per document)

```
Your document (e.g., a 10-K filing)
       ↓
Split into chunks (paragraphs or sections)
       ↓
Each chunk → Ollama embedding model → vector (list of numbers)
       ↓
Store chunks + vectors in a local file
```

Think of this like building an index for a textbook. You do it once, then
you can look things up quickly.

### Phase 2: Querying (done every time you ask a question)

```
Your question: "What are Apple's main risk factors?"
       ↓
Question → Ollama embedding model → vector
       ↓
Find chunks with the most similar vectors (cosine similarity)
       ↓
Top 5 most relevant chunks → Ollama text model
       ↓
"Based on these passages, Apple's main risk factors are..."
```

The embedding model finds the relevant sections. The text model reads them
and answers your question. Both run locally — nothing leaves your machine.

---

## Structure-First RAG: A Better Approach for Financial Documents

The simple chunk-and-embed approach works for unstructured text like news
articles or research notes. But financial documents have structure that
matters.

A 10-K filing has sections like:
- Item 1: Business
- Item 1A: Risk Factors
- Item 7: Management's Discussion and Analysis
- Item 8: Financial Statements

If you blindly chunk this into 500-token pieces, you lose which section
each chunk came from. When the AI says "revenues increased 12%," you can't
tell if that's from the MD&A (management's analysis) or the actual financial
statements.

**Structure-first RAG preserves this hierarchy:**

1. Parse the document into sections (Item 1, Item 1A, Item 7, etc.)
2. Create embeddings for each section (not random chunks)
3. When searching, the results include which section they came from
4. The AI can cite specific sections: "According to Item 1A (Risk Factors)..."

This gives you citation-grade answers — essential for investment research
and compliance.

---

## Key Takeaways

1. **Local models** keep sensitive documents on your machine — nothing goes to the cloud
2. **Ollama** makes running local models simple — download, run, done
3. **Embeddings** convert text to searchable vectors — this is how RAG finds relevant passages
4. **Structure-first RAG** preserves document hierarchy — critical for financial filings where section identity matters
5. **Local for search, cloud for reasoning** — the practical hybrid approach
