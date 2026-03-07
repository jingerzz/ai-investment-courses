# Bonus Exercise: Build a Local Document Q&A System

## What You'll Build

A RAG system that runs entirely on your Mac — no cloud APIs needed for
the document processing. You'll be able to drop in a PDF (an SEC filing,
a research report, any financial document) and ask Claude Desktop questions
about it, with the document search happening locally via Ollama.

When you're done:
- "What does Apple say about AI risk in their latest 10-K?"
- "Summarize the revenue trends from this earnings report"
- "Compare the risk factors between these two filings"

...with citations pointing to the exact section of the document.

## Time: 45-60 minutes

This is a bonus module — it's longer than the regular weekly exercises
because it involves setting up Ollama and building a more complex system.

## What You Need

- Claude Code
- Claude Desktop
- Ollama installed with models pulled (see `ollama_quickstart.md`)
- A financial document to work with (we'll download one from SEC EDGAR)

## Prerequisites

Before starting, make sure Ollama is ready. Open your terminal:

```bash
ollama ls
```

You should see `nomic-embed-text` and your chosen text model. If not,
pull them now (see `ollama_quickstart.md` for how to pick the right
model for your machine):

```bash
ollama pull nomic-embed-text
ollama pull qwen3.5:4b        # 16GB RAM (most participants)
# ollama pull qwen3.5:0.8b    # 8GB RAM
# ollama pull qwen3.5:9b      # 32GB+ RAM
```

---

## Step 1: Get a Document (5 min)

You need a financial document to index. The easiest source is SEC EDGAR
(free, no account needed).

Ask Claude Code:

```
I want to download Apple's most recent 10-K filing from SEC EDGAR.
Can you write a Python script that:
1. Downloads the filing from EDGAR
2. Saves it as a text file in ~/ai-finance-tools/documents/

If the HTML is messy, clean it up to plain text. Save it as
AAPL-10K.txt.
```

Alternatively, if you have your own documents (PDF research reports,
internal memos, etc.), copy them to `~/ai-finance-tools/documents/`.

```
I have a PDF file I want to use instead. Can you write a script that
converts ~/ai-finance-tools/documents/my-report.pdf to a text file?
Use a Python PDF library like PyMuPDF.
```

## Step 2: Build the Indexer (10 min)

Tell Claude Code to build the document indexing system:

```
I want to build a RAG system that uses Ollama for local embeddings.
Please create a file called rag_system.py that:

1. READS a text document and splits it into sections.
   - Try to split on natural section boundaries (headings,
     "Item 1:", "PART I", etc.)
   - If no clear sections are found, split into chunks of about
     500 words each with 50 words of overlap
   - Store each chunk with its section title (if available)

2. EMBEDS each section using Ollama's nomic-embed-text model.
   - Call Ollama's local API at http://localhost:11434
   - Use the /api/embeddings endpoint
   - Store the embeddings alongside the text

3. SAVES the index to a JSON file (documents/AAPL-10K-index.json)
   so we don't have to re-embed every time.

4. Has a SEARCH function that:
   - Takes a question string
   - Embeds the question using the same model
   - Finds the top 5 most similar chunks (cosine similarity)
   - Returns the chunks with their section titles and similarity scores

Use the ollama Python package for the API calls. Keep it simple —
no vector database needed, just a JSON file with embeddings.
```

Then test it:

```
Can you run the indexer on the AAPL-10K.txt file? Show me how many
sections it found and how long the indexing takes.
```

## Step 3: Add a Q&A Function (10 min)

```
Add a function to rag_system.py called answer_question that:

1. Takes a question string
2. Searches the index for the top 5 relevant chunks
3. Sends those chunks + the question to Ollama's qwen3.5:4b model
4. The prompt should say:
   "Answer the question based ONLY on the provided document sections.
   Cite which section each piece of information comes from.
   If the answer isn't in the provided sections, say so."
5. Returns the answer with citations

Also add a simple command-line interface so I can test:
  uv run python rag_system.py --ask "What are Apple's main risk factors?"
```

Test with a few questions:

```
Run these queries and show me the results:
1. "What are the main risk factors?"
2. "What was the revenue for the most recent year?"
3. "What does the company say about competition?"
```

Check that:
- Answers cite specific sections
- Answers are based on the document, not general knowledge
- "I don't know" is returned for questions not in the document

## Step 4: Make It an MCP Server (10 min)

```
Now turn rag_system.py into an MCP server. Create a file called
rag_server.py with these tools:

1. index_document(file_path) - Index a document from the given path.
   Returns the number of sections found. If already indexed, return
   a message saying so.

2. list_documents() - Show all indexed documents with section counts
   and when they were indexed.

3. search_document(query, doc_name) - Search a specific document.
   Returns top 5 matching sections with titles, text excerpts (first
   200 chars), and similarity scores.

4. ask_document(question, doc_name) - Ask a question about a document.
   Uses the search + Ollama LLM to generate a cited answer.

5. get_rag_guide() - Describes all tools and the recommended flow.
   Include a note that all processing is local — no data leaves the
   machine.

Every tool returns a dict with data_source set to "local_ollama".
Error handling: if Ollama isn't running, return a helpful error message
telling the user to start it.
```

## Step 5: Connect to Claude Desktop (5 min)

```
Add this RAG server to my Claude Desktop config alongside my other
servers. Show me the updated config.
```

After restarting Claude Desktop, test:

```
What documents do I have indexed?
```

```
What does Apple say about AI and machine learning risks in their 10-K?
```

```
Summarize the business overview section of the Apple 10-K.
```

## Step 6: Add a Second Document and Compare (10 min)

Download another filing — either a different company or a different
year for the same company:

```
Download Microsoft's most recent 10-K from SEC EDGAR and save it
to my documents folder. Then index it using my RAG system.
```

Now test cross-document queries in Claude Desktop:

```
Compare Apple's and Microsoft's risk factors related to AI.
```

```
How do Apple and Microsoft differ in their revenue breakdown?
```

Claude Desktop will call your RAG tools for both documents and synthesize
the comparison — with the search running locally via Ollama.

---

## Optional: Structure-First Improvement (if time permits)

If the basic chunking approach misses section boundaries, ask Claude Code
to improve it:

```
The chunking is splitting sections in the middle. Can you improve the
document parser to:

1. First look for SEC filing section headers (Item 1, Item 1A, etc.)
2. Split on those headers to create structured sections
3. For very long sections (> 2000 words), split into sub-chunks but
   keep the parent section title
4. Store the hierarchy: section title → sub-chunks

This way search results always show which Item they came from.
```

This is the structure-first approach from Week 2's reading — preserving
the document's natural hierarchy instead of blindly chunking.

---

## What You Learned

- How to run local AI models with **Ollama** (pull, serve, run, ls, rm)
- How **embeddings** work: text → vector → similarity search
- How **RAG** works end-to-end: index → search → answer with citations
- The difference between **chunk-based** and **structure-first** RAG
- How to make a **local RAG system accessible via MCP** so Claude Desktop
  can use it
- That **local search + cloud reasoning** is a practical hybrid — sensitive
  document search stays on your machine, Claude provides the interpretation

## If You Get Stuck

- **"Ollama connection refused"** → Run `ollama serve` in a separate
  terminal window, or check that the Ollama app is running (llama icon
  in menu bar)
- **Indexing is very slow** → The first embedding call loads the model
  into RAM; subsequent calls are faster. On a Mac Mini, expect 1-3 minutes
  for a full 10-K filing.
- **Answers are generic, not from the document** → Check that the prompt
  says "Answer based ONLY on the provided sections." Also check that
  the search is returning relevant chunks (test with `--ask` first).
- **"Out of memory"** → Close other heavy apps. If still failing, drop
  to a smaller model: tell Claude Code "Switch the text model to
  `qwen3.5:2b`" or `qwen3.5:0.8b`. See `ollama_quickstart.md` for the
  full model tier list.
