# Week 1 Conversation Guide — Stock Research Track

How to explore the page-index-rag server with Claude Desktop. These
prompts demonstrate different aspects of document-backed AI analysis.

---

## Getting Oriented

**Discover available tools:**
```
What document analysis tools do you have? Give me a quick overview
of what each one does.
```

*Why it works: The guide tool gives Claude the full catalog. You'll
see 14 tools organized by function.*

**See what's indexed:**
```
List all indexed documents. For each one, tell me the company,
filing type, and document ID.
```

*Why it works: You need the document IDs to target specific filings
in later queries.*

---

## Single-Document Analysis

**Structural exploration:**
```
Show me the table of contents for BlackRock's 10-K. What are the
major sections?
```

*Why it works: Understanding document structure helps you ask more
targeted questions.*

**Targeted search:**
```
Search BlackRock's 10-K for their discussion of fee rates and
pricing pressure. What trends do they describe?
```

*Why it works: Specific, targeted queries produce better citations
than broad questions.*

**Section deep-dive:**
```
Pull the full Management Discussion and Analysis section from the
Robinhood 10-K. Summarize the key points and highlight any numbers
they report.
```

*Why it works: Reading a full section gives Claude more context than
a keyword search.*

---

## Cross-Document Analysis

**Comparative analysis:**
```
Compare how BlackRock and Robinhood describe their competitive
advantages. What does each company claim sets them apart?
```

*Why it works: Cross-document synthesis is where AI adds the most
value — it would take an analyst hours to read both filings and
extract these comparisons.*

**Revenue model comparison:**
```
How does BlackRock make money versus how Robinhood makes money?
Use the 10-K filings to compare their revenue breakdowns.
```

*Why it works: Specific questions about business model differences
produce well-structured, citation-backed analysis.*

**Risk factor comparison:**
```
What regulatory risks does each company disclose? Are there any
risks that appear in both filings?
```

*Why it works: Regulatory risk is concrete and well-documented in
10-Ks, making it ideal for RAG-backed analysis.*

---

## Due Diligence Workflows

**Investment thesis:**
```
I'm evaluating BlackRock as a long-term investment. Based on their
10-K, what are the top 3 bull arguments and top 3 bear arguments?
Cite specific sections for each.
```

*Why it works: Forcing citations keeps the AI grounded in the filing
rather than generating opinions from training data.*

**Red flag scan:**
```
Search Robinhood's 10-K for any mentions of litigation, regulatory
actions, or material weaknesses. Summarize what you find.
```

*Why it works: These are specific disclosure categories that every
10-K addresses, making searches precise and comprehensive.*

**Forward-looking statements:**
```
What does BlackRock say about their growth strategy and outlook?
Pull from the Management Discussion section.
```

*Why it works: Combining a topic search with a section target gives
Claude both breadth and precision.*

---

## Tips for Effective Document Analysis

1. **Use document IDs for precision.** "Search BLK's 10-K for..." is
   better than "What does BlackRock say about..." because it targets a
   specific filing.

2. **Ask for citations explicitly.** "Cite the specific section" forces
   Claude to reference the filing rather than paraphrase from memory.

3. **Start broad, then narrow.** "What are the risk factors?" gives you
   an overview. "Tell me more about the interest rate risk they
   describe" digs into a specific finding.

4. **Compare across documents.** The most valuable analysis comes from
   cross-referencing multiple filings — something that's tedious
   manually but natural for AI with the right tools.

5. **Verify the citations.** The AI provides section and page references.
   Spot-check a few to build confidence in the system. This is how you
   calibrate trust in RAG-backed analysis.
