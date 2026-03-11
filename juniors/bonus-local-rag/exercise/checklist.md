# Bonus Module: Did It Work? Checklist

---

## Ollama Setup

- [ ] **Ollama is running.** `ollama ls` shows `nomic-embed-text` and
  your answer model (`qwen3.5:0.8b`, `qwen3.5:4b`, or `qwen3.5:9b`
  depending on your computer's RAM).

- [ ] **Models respond.** `ollama run <your-model>` opens a chat and
  you can ask a question and get a response.

## Document Preparation

- [ ] **Document downloaded and cleaned.** A text file exists in your
  documents folder with readable content and section headers.

- [ ] **Section boundaries visible.** The text file has clear section
  markers (Item 1, Item 1A, PART I, etc.) that the indexer can use.

## Indexing

- [ ] **Indexer runs successfully.** The document is split into sections
  and each section gets its search vector from Ollama.

- [ ] **Index file created.** A JSON file exists with the section text
  and vectors stored.

- [ ] **Reasonable section count.** An annual report should produce
  roughly 15-40 sections (not 500 tiny pieces or 3 enormous ones).

- [ ] **Re-indexing is skipped.** Running the indexer again on the same
  document detects the existing index and skips re-processing.

## Search Quality

- [ ] **Relevant results.** Searching "risk factors" returns sections
  from Item 1A, not random business description paragraphs.

- [ ] **Scores make sense.** The top result has a higher relevance
  score than the 5th result. Scores are between 0 and 1.

- [ ] **Section titles included.** Each result shows which section of
  the document it came from.

## Q&A Quality

- [ ] **Answers cite sections.** The answer mentions which section
  (e.g., "According to Item 1A...") the information comes from.

- [ ] **Answers are from the document.** The answer is based on the
  document content, not general knowledge. Test by asking something
  specific that only this filing would mention.

- [ ] **"Not found" works.** Asking something not in the document
  (e.g., "What is the stock price?") returns a response saying the
  information isn't in the indexed sections.

## MCP Server

- [ ] **Server runs without errors.** The MCP inspector shows all
  tools available.

- [ ] **Error handling for Ollama.** Stop Ollama, then call a tool.
  It should return a helpful error message, not crash.

- [ ] **list_documents works.** Shows all indexed documents with
  section counts.

- [ ] **Connected to Claude Desktop.** Claude Desktop can call your
  RAG tools alongside your stock tracker tools.

## Claude Desktop Integration

- [ ] **Claude uses RAG tools.** Ask Claude Desktop about a document —
  it calls your RAG server, not its own training data.

- [ ] **Citations carry through.** Claude's answer includes section
  references from the RAG tool results.

- [ ] **Cross-server works.** Ask Claude Desktop something that
  combines document data with stock data from your Week 1 server:
  "What does Roblox's annual report say about their business, and how
  is RBLX doing today?"

## Privacy

- [ ] **All processing is local.** The `data_source` field says
  "local_ollama" — confirming no cloud service was used for document
  processing.

- [ ] **No document content in the cloud.** When Claude Desktop reads
  the RAG results, it sees excerpts from your tools — the full document
  was never uploaded anywhere.
