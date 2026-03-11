# Bonus Module: Conversation Guide

How to talk to Claude Code when building a document search system
with Ollama.

---

## Getting Documents

### Downloading from SEC EDGAR

```
Download Roblox's most recent 10-K filing from SEC EDGAR and save it
as a clean text file in ~/ai-stock-tools/documents/RBLX-10K.txt.

Remove HTML tags and formatting junk. Keep the section headers
(Item 1, Item 1A, etc.) — they're important for organizing the search.
```

### Using your own files

```
I have a PDF at ~/Downloads/my-report.pdf. Can you convert it to a
text file at ~/ai-stock-tools/documents/my-report.txt?

Keep paragraph breaks and headings intact.
```

### If the text looks messy

```
The text file has a lot of junk — page numbers in the middle of
sentences, repeated headers, and broken words. Can you clean it up?
Remove the junk but keep section headers and paragraph breaks.
```

---

## Building the Search System

### Initial build

```
Build a document search system in rag_system.py that:
- Splits documents into sections (use headings like "Item 1:" as
  boundaries, not random chunk sizes)
- Creates search vectors using Ollama nomic-embed-text
- Saves the index as a JSON file
- Has a search function that returns top 5 matches with scores
- Has an answer function that sends matches to qwen3.5:4b

Use the ollama Python package. Keep it simple — JSON file, no database.
```

### If indexing is slow

```
The indexing step is taking forever. Can you add:
1. A progress indicator so I can see how far along it is
2. Skip re-indexing if the index file already exists
```

### If search results aren't good

```
The search results don't match my questions well. When I ask about
"risk factors" it returns sections about other stuff. Can you try
giving more weight to section titles when matching? The title is
often the best indicator of what a section is about.
```

### If answers are too generic

```
The answers sound like general knowledge, not like they're from the
document. Can you make the prompt stronger:
- "You MUST answer ONLY from the provided sections below"
- "Start each claim with the section it comes from, like:
  'According to Item 1A (Risk Factors), ...'"
- "If the information is not in these sections, say so"
```

---

## Making It an MCP Server

### Basic server

```
Turn the RAG system into an MCP server called rag_server.py with tools:
- index_document(file_path) - index a new document
- list_documents() - show indexed docs
- search_document(query, doc_name) - search one document
- ask_document(question, doc_name) - Q&A with citations
- get_rag_guide() - describe all tools

Set data_source to "local_ollama" on every return. If Ollama isn't
running, return a helpful error message instead of crashing.
```

### If you want to search multiple documents at once

```
Update ask_document so it can accept multiple document names. If
multiple docs are given, search all of them and merge the results.
Label each result with which document it came from.
```

---

## Testing in Claude Desktop

### Basic document Q&A

```
What documents do I have indexed?
```

```
What are Roblox's main risk factors according to their annual report?
```

### Testing citations

```
What does the annual report say about competition? Please cite
the specific section.
```

### Cross-document comparison

```
Compare Roblox's and Take-Two's risk factors related to user growth.
```

### Testing "I don't know"

```
What was Roblox's stock price on January 15th?
(This info isn't in an annual report — the system should say so)
```

---

## Troubleshooting

### Ollama not responding

```
I'm getting "connection refused" when the system tries to talk to
Ollama. Can you check if Ollama is running and add a startup check
that tests the connection before trying to index?
```

### Computer running slow

```
My computer is struggling with qwen3.5:4b. Can you switch to
qwen3.5:0.8b instead? It's smaller. Update both rag_system.py and
rag_server.py to use the smaller model.
```

### Search index seems broken

```
I'm getting errors when trying to search. Can you delete the index
file and re-index the document from scratch? Also add error handling
so a broken index gets rebuilt automatically.
```

---

## Tips

1. **Download models before starting.** The `ollama pull` commands can
   take a few minutes. Do them first.

2. **Start with one document.** Don't try to index a huge filing on
   your first try. Get it working with one document first.

3. **Test search before Q&A.** If the search function returns bad
   results, the Q&A answers will be bad too. Fix search first.

4. **Local models aren't as smart as Claude.** The answers won't be
   as polished as what Claude gives you. That's okay — the local model
   finds the relevant sections, and Claude Desktop does the sophisticated
   reasoning on top.

5. **The combo is powerful.** Local search (private) + Claude reasoning
   (smart) = the best of both worlds.
