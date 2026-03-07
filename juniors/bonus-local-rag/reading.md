# Bonus Module: Running AI on Your Own Computer

## Why Run AI Locally?

In Weeks 1 and 2, all your tools sent requests to Claude over the
internet. Claude is powerful, but here's the thing: everything you type
and every document you share goes to Anthropic's servers in the cloud.

For public stock prices, that's totally fine. But what about private
documents? Companies have internal reports, financial plans, and
strategy memos that they absolutely cannot share with anyone outside the
company. A law firm has confidential client files. A school might have
private student records.

**Local AI** solves this. Instead of sending your documents to the
cloud, you run an AI model right on your own computer. The data never
leaves your machine. Nobody else can see it.

### When to Use Local vs. Cloud

| What You're Doing | Best Choice | Why |
|-------------------|------------|-----|
| Looking up stock prices | Cloud (Claude) | Public data, Claude is smarter |
| Reading public SEC filings | Either works | Data is public anyway |
| Searching private documents | Local (Ollama) | Data stays on your computer |
| Complex analysis and reasoning | Cloud (Claude) | Claude is much better at this |
| Learning how AI works under the hood | Local (Ollama) | You can see everything happening |

The smart approach: **use local AI to search through documents, then let
Claude (in the cloud) do the complex thinking.** Your private documents
stay on your computer, but you still get Claude's intelligence for the
final answer.

---

## What Is Ollama?

**Ollama** is an app that runs AI models on your own Mac or PC. It's
like having a mini version of ChatGPT that lives entirely on your
computer.

Here's how it works:

- **Models** are the AI brains. You download them to your computer.
  Different models are different sizes — bigger models give better
  answers but need more computer memory (RAM).
- **Pulling** a model means downloading it. You do this once.
- **Running** a model means it's active and ready to answer questions.
  Your code talks to it through a local connection (no internet needed).

### Which Model Should You Use?

You need two models: one for **searching** (finding relevant parts of
a document) and one for **answering** (reading those parts and
responding to your question).

**Search model (everyone uses the same one):**

| Model | Size | What It Does |
|-------|------|-------------|
| `nomic-embed-text` | ~275MB | Converts text into searchable numbers. Small and fast. |

**Answer model (pick based on your computer):**

| Your Computer | Model | Size | Quality |
|--------------|-------|------|---------|
| 8GB RAM | `qwen3.5:0.8b` | ~1GB | Good — handles basic questions |
| 16GB RAM | `qwen3.5:4b` | ~3.4GB | Great — accurate, detailed answers |
| 32GB+ RAM | `qwen3.5:9b` | ~7GB | Excellent — best quality |

**Most people should use `qwen3.5:4b`.** All three models do the same
thing — bigger ones just give better answers. The 0.8b model works
fine for this exercise because Claude Desktop (the cloud AI) does the
heavy thinking on top of what the local model finds.

Not sure how much RAM your computer has?
- **Mac:** Click the Apple menu > About This Mac > look for "Memory"
- **Windows:** Right-click Start button > System > look for "Installed RAM"

---

## How Document Search Works (RAG)

**RAG** stands for Retrieval-Augmented Generation. That's a fancy name
for a simple idea: **help AI answer questions by first finding the
relevant parts of a document.**

Without RAG, if you ask an AI "What are Apple's biggest risks?", it
would have to guess based on its training data (which might be old).

With RAG, the system:
1. Searches through Apple's actual annual report
2. Finds the sections about risks
3. Gives those sections to the AI
4. The AI reads them and gives you a specific, accurate answer

### Phase 1: Indexing (Done Once)

Before you can search a document, you need to "index" it — like
building a table of contents.

```
Your document (Apple's annual report)
       |
Split into sections (Risk Factors, Business Overview, etc.)
       |
Each section gets turned into a list of numbers (called a "vector")
       |
Save everything in a file for later
```

The list of numbers (vector) captures the *meaning* of each section.
Sections about similar topics produce similar numbers. This is what
makes searching by meaning possible — not just searching for exact words.

### Phase 2: Searching (Every Time You Ask)

```
Your question: "What are Apple's main risks?"
       |
Your question gets turned into numbers (same way as the sections)
       |
Compare your question's numbers to each section's numbers
       |
Find the 5 sections with the most similar numbers
       |
Send those sections to the AI model
       |
AI reads them and answers your question
```

The searching happens locally on your computer. No internet needed.
No data sent anywhere.

---

## Why Document Structure Matters

Company annual reports (called 10-K filings) have a specific structure:
- **Item 1:** Business overview
- **Item 1A:** Risk factors
- **Item 7:** Management's discussion
- **Item 8:** Financial statements

When you search for "risk factors," you want results from Item 1A —
not random paragraphs from the business overview that happen to
mention the word "risk."

**Structure-first indexing** preserves this organization. Instead of
chopping the document into random pieces, it splits along the natural
section boundaries. When the AI answers your question, it can say
"According to Item 1A (Risk Factors)..." — which is much more useful
than "According to some paragraph somewhere in the document..."

---

## Key Takeaways

1. **Local AI** keeps your documents private — nothing goes to the cloud
2. **Ollama** is the app that runs AI on your computer — download it,
   pull some models, and you're ready
3. **RAG** helps AI answer questions by finding relevant document
   sections first
4. **Vectors** (lists of numbers) capture the meaning of text — that's
   how the search finds relevant sections
5. **Structure-first indexing** preserves document organization so the
   AI can cite specific sections
6. **Local for search, cloud for thinking** — the best approach combines
   both
