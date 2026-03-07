# Bonus Exercise: Build a Private Document Q&A System

## What You'll Build

A system that lets you ask questions about company documents — running
entirely on your own computer. No data gets sent to the cloud. You'll
be able to ask Claude Desktop things like:

- "What does Apple say about AI risk in their annual report?"
- "Summarize the business overview from this filing"
- "Compare the risk factors in Apple's and Microsoft's reports"

...with the document search happening locally on your machine.

## Time: 45-60 minutes

This bonus module is longer than the regular weekly exercises because
it involves setting up Ollama and building a more complex system.

## What You Need

- Claude Code
- Claude Desktop
- Ollama installed with models downloaded (see `ollama_quickstart.md`)
- A company document to work with (we'll download one)

## Before You Start

Make sure Ollama is ready. Open your terminal:

```bash
ollama ls
```

You should see `nomic-embed-text` and your answer model. If not,
download them now (see `ollama_quickstart.md`):

```bash
ollama pull nomic-embed-text
ollama pull qwen3.5:4b        # 16GB RAM (most computers)
# ollama pull qwen3.5:0.8b    # 8GB RAM
# ollama pull qwen3.5:9b      # 32GB+ RAM
```

---

## Step 1: Get a Document (5 min)

You need a company document to work with. The easiest source is
SEC EDGAR — a government website where all public companies post
their annual reports (called 10-K filings). It's free, no account needed.

Ask Claude Code:

```
I want to download Apple's most recent 10-K filing from SEC EDGAR.
Can you write a script that:
1. Downloads the filing from EDGAR
2. Cleans up the HTML into plain text
3. Saves it as ~/ai-stock-tools/documents/AAPL-10K.txt

Keep the section headers intact (Item 1, Item 1A, etc.) — they're
important for organizing the search index.
```

If you have your own documents (PDFs, reports, etc.), you can use
those instead:

```
I have a PDF at ~/Downloads/my-report.pdf. Can you convert it to a
text file at ~/ai-stock-tools/documents/my-report.txt?
```

## Step 2: Build the Search System (10 min)

Tell Claude Code to build the document indexing and search system:

```
I want to build a document search system that uses Ollama (running
locally on my computer). Please create a file called rag_system.py that:

1. READS a text document and splits it into sections.
   - Try to split on natural section boundaries (headings like
     "Item 1:", "PART I", etc.)
   - If no clear sections exist, split into chunks of about 500 words
   - Keep track of each section's title

2. CREATES SEARCH VECTORS for each section using Ollama's
   nomic-embed-text model.
   - Call Ollama's local API at http://localhost:11434

3. SAVES the index to a JSON file so we don't have to redo this
   every time.

4. Has a SEARCH function that:
   - Takes a question
   - Finds the 5 most relevant sections
   - Returns the sections with their titles and relevance scores

Use the ollama Python package. Keep it simple — save everything in
a JSON file, no database needed.
```

Then test it:

```
Can you run the indexer on the AAPL-10K.txt file? Show me how many
sections it found and how long it took.
```

## Step 3: Add a Q&A Function (10 min)

```
Add a function to rag_system.py called answer_question that:

1. Takes a question
2. Searches the index for the 5 most relevant sections
3. Sends those sections plus the question to Ollama's qwen3.5:4b model
4. The prompt should tell the model:
   "Answer the question based ONLY on the provided document sections.
   Say which section each piece of information comes from.
   If the answer isn't in the sections, say so."
5. Returns the answer with section citations

Also add a way to test from the command line:
  uv run python rag_system.py --ask "What are Apple's main risk factors?"
```

Test with a few questions:

```
Run these queries and show me the results:
1. "What are the main risk factors?"
2. "What does the company say about competition?"
3. "What was the stock price on January 15th?"
```

Check that:
- Answers mention which section the info comes from
- Answers are based on the document, not general knowledge
- For question 3, it says the info isn't in the document (stock prices
  aren't in annual reports)

## Step 4: Make It an MCP Server (10 min)

```
Turn rag_system.py into an MCP server. Create rag_server.py with
these tools:

1. index_document(file_path) - Index a document. Returns how many
   sections were found. If already indexed, say so.

2. list_documents() - Show all indexed documents with section counts.

3. search_document(query, doc_name) - Search a document. Returns
   top 5 matching sections with titles and relevance scores.

4. ask_document(question, doc_name) - Ask a question about a document.
   Returns an answer with citations.

5. get_rag_guide() - Describes all tools. Include a note that
   everything runs locally — no data leaves the computer.

Every tool returns a dict with data_source set to "local_ollama".
If Ollama isn't running, return a helpful error message instead of
crashing.
```

## Step 5: Connect to Claude Desktop (5 min)

```
Add this RAG server to my Claude Desktop config alongside my stock
tracker server. Show me the updated config.
```

After restarting Claude Desktop, test:

```
What documents do I have indexed?
```

```
What does Apple say about AI and machine learning risks in their
annual report?
```

## Step 6: Add Another Document and Compare (10 min)

Download a second company's filing:

```
Download Microsoft's most recent 10-K from SEC EDGAR and save it to
my documents folder. Then index it using my RAG system.
```

Now try cross-document questions in Claude Desktop:

```
Compare Apple's and Microsoft's biggest risk factors.
```

```
How do Apple and Microsoft describe their competitive advantages?
```

Claude Desktop will call your RAG tools for both documents and combine
the answers — with the document searching happening locally.

---

## What You Learned

- How to run AI on your own computer with **Ollama**
- How **document search (RAG)** works: index, search, answer
- How **vectors** (lists of numbers) capture the meaning of text
- How to build a **private Q&A system** that keeps data on your machine
- How to make local tools available to Claude Desktop via **MCP**
- That **local search + cloud reasoning** is a powerful combination

## If You Get Stuck

- **"Ollama connection refused"** — Run `ollama serve` in a separate
  terminal window, or make sure the Ollama app is running (llama icon
  in menu bar)
- **Indexing is very slow** — The first time is slow because the model
  loads into memory. After that it's faster. A full 10-K takes 1-3
  minutes.
- **Answers are generic, not from the document** — Check that the
  prompt says "Answer ONLY from the provided sections." Also check
  that the search is finding relevant sections.
- **Computer is slow or freezing** — Close other apps. If still bad,
  switch to a smaller model. Tell Claude Code: "Switch the text model
  to qwen3.5:0.8b — my computer doesn't have enough memory."
