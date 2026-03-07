# Bonus Module: Conversation Guide

How to talk to Claude Code when building a RAG system with Ollama.

---

## Getting Documents

### Downloading from SEC EDGAR

```
Download Apple's most recent 10-K filing from SEC EDGAR and save it as
a clean text file in ~/ai-finance-tools/documents/AAPL-10K.txt.

Strip out HTML tags, navigation elements, and formatting artifacts.
Keep the section headers (Item 1, Item 1A, etc.) intact — they're
important for structuring the RAG index.
```

### Using your own PDFs

```
I have a PDF at ~/Downloads/research-report.pdf. Can you convert it
to a text file at ~/ai-finance-tools/documents/research-report.txt?

Use PyMuPDF (fitz) for the conversion. Preserve paragraph breaks and
section headings as much as possible.
```

### If the text extraction is messy

```
The text file has a lot of junk — page numbers in the middle of
sentences, headers repeated on every page, and broken words from
column layouts. Can you clean it up? Remove:
- Repeated headers/footers
- Page numbers
- Artifacts from multi-column layouts
Keep section headers and paragraph structure.
```

---

## Building the RAG System

### Initial build

```
Build a RAG system in rag_system.py that:
- Splits documents into sections (prefer natural boundaries like
  "Item 1:" over arbitrary chunk sizes)
- Embeds each section using Ollama nomic-embed-text
- Stores the index as a JSON file
- Has a search function that returns top 5 matches with scores
- Has an answer function that sends matches to qwen3.5:4b

Use the ollama Python package. Keep it simple — JSON file storage,
no vector database.
```

### If embeddings are slow

```
The embedding step is taking a long time. Can you add:
1. A progress bar that shows how many sections have been embedded
2. Batch processing (send multiple sections at once if the API supports it)
3. Skip re-embedding if the index file already exists — only embed
   new or changed sections
```

### If search quality is poor

```
The search results aren't very relevant. When I ask about "risk factors"
it returns sections about "business overview." Can you try:
1. Embedding the section title + first 200 chars together (not just
   the full text) as a separate "title embedding"
2. Combining title similarity and content similarity with title
   weighted higher (70% title, 30% content)
This might help match queries to the right section headers.
```

### Improving answer quality

```
The answers are too generic. They sound like the model is using its
training data instead of the document. Can you make the prompt stronger:
- "You MUST answer ONLY from the provided sections below"
- "If the information is not in these sections, say 'This information
  is not found in the indexed sections of this document.'"
- "Start each claim with the section it comes from, like:
  'According to Item 1A (Risk Factors), ...'"
```

---

## Making It an MCP Server

### Basic server setup

```
Turn the RAG system into an MCP server called rag_server.py with tools:
- index_document(file_path) - index a new document
- list_documents() - show indexed docs
- search_document(query, doc_name) - search one document
- ask_document(question, doc_name) - Q&A with citations
- get_rag_guide() - describe all tools

Set data_source to "local_ollama" on every return. If Ollama isn't
running, return {"error": "Ollama is not running. Start it with
'ollama serve' or launch the Ollama app."} instead of crashing.
```

### Adding multi-document support

```
Update ask_document to accept an optional list of doc_names instead
of just one. If multiple docs are provided, search all of them and
merge the top results. Label each result with which document it
came from so the AI can cite properly.
```

### Handling large documents

```
Some of my documents are very long (200+ pages). The indexing works but
search returns too many low-relevance results. Can you:
1. Only return results with similarity score above 0.5 (or a configurable threshold)
2. Add a "confidence" field: "high" if score > 0.7, "medium" if > 0.5, "low" otherwise
3. Sort by score descending
4. In ask_document, only send "high" and "medium" confidence chunks
   to the LLM — don't waste context on low-relevance matches
```

---

## Testing Prompts for Claude Desktop

### Basic document Q&A

```
What documents do I have indexed in my RAG system?
```

```
What are Apple's main risk factors according to their latest 10-K?
```

### Specific section queries

```
What does Item 7 (Management's Discussion and Analysis) say about
revenue growth?
```

### Cross-document comparison

```
Compare Apple's and Microsoft's competitive positioning based on
their 10-K filings.
```

### Testing citation quality

```
What does the 10-K say about foreign currency risk? Please cite
the specific section.
```

### Testing the "I don't know" boundary

```
What was Apple's stock price on January 15th?
(This shouldn't be in a 10-K — the system should say it's not found)
```

---

## Troubleshooting

### Ollama not responding

```
I'm getting "connection refused" when the RAG system tries to call
Ollama. Can you check:
1. Is Ollama running? (ollama ps)
2. Is it listening on the right port? (default is 11434)
3. Can you add a startup check that tests the connection before
   trying to embed?
```

### Out of memory

```
The qwen3.5:4b model is using too much RAM and my system is slow.
Can you switch to qwen3.5:2b instead? It's smaller. Update both
the rag_system.py and rag_server.py to use the 2b model.
```

If 2b is still too heavy (8GB machines), try `qwen3.5:0.8b`:

```
Switch to qwen3.5:0.8b — I only have 8GB of RAM.
```

### Index file corrupted

```
The index JSON file seems corrupted — I'm getting JSON parse errors.
Can you:
1. Delete the bad index file
2. Re-index the document from scratch
3. Add error handling so a corrupted index is detected and rebuilt
   automatically
```

---

## Tips for This Module

1. **Pull models before starting.** `ollama pull nomic-embed-text` and
   your text model can take a few minutes. Do this first. See
   `ollama_quickstart.md` for which model to pick based on your RAM.

2. **Start with one short document.** Don't try to index a 300-page
   filing on your first attempt. Start with a shorter document or
   just one section of a filing.

3. **Test search before Q&A.** The search function should return
   relevant chunks. If search is bad, Q&A will be bad too — fix search
   first.

4. **Local models are less capable than Claude.** The answers from
   local models won't be as polished as Claude's. That's fine — the
   value is privacy and cost, not answer quality. Claude Desktop does
   the final interpretation. This is true even for the 9B model.

5. **The hybrid approach is powerful.** Your RAG server finds relevant
   passages locally (private), then Claude Desktop in the conversation
   does the sophisticated reasoning. Best of both worlds.
