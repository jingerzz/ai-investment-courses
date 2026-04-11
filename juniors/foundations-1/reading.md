# Foundations 1: Understanding Claude -- Your AI Study Partner

## F1.1 What AI Actually Is

Imagine a study partner who read every textbook ever written -- every
history book, every science paper, every business article, every
financial report published online. This study partner can explain
almost anything, connect ideas across different subjects, and help
you think through problems.

Now imagine that this study partner has no phone and no internet.
They can't look anything up. Everything they know comes from what
they read during their training -- and that training ended months
ago. They can reason about what they've seen, but they have no idea
what happened in the world yesterday.

That's what Claude is.

Claude is a large language model (LLM). During training, it
processed billions of documents and learned patterns -- what good
writing looks like, how to reason through problems, what financial
analysis involves. It didn't memorize a list of facts like
flashcards. Instead, it learned the *relationships* between ideas
by seeing them appear over and over across millions of examples.

This makes Claude genuinely useful. Ask it to explain how a company
makes money, what a P/E ratio means, or how interest rates affect
the stock market, and you'll get a clear, thoughtful answer.

But there are hard limits. Claude does not have access to current
stock prices, today's news, or live data of any kind. It cannot
look something up. When it tells you a number -- a stock price, a
company's revenue, who the CEO is -- it's pulling from training
data that may be months or years old. It has no way to check
whether that information is still correct.

This is the key tension: Claude is a strong *reasoning* tool with
a *data* gap. The reasoning capabilities are powerful for the right
tasks -- understanding concepts, comparing ideas, building
frameworks. But you should never trust a specific number or fact
from Claude without checking it yourself.

---

## F1.2 How AI Gets Things Wrong

This is the most important section in today's reading. Before you
start using AI for anything related to investing, you need to
understand exactly how it fails. These aren't rare glitches -- these
are patterns you *will* encounter. Recognizing them is a skill, and
it might be the most valuable skill in this entire course.

### Failure Mode 1: Stale Magnitude

You ask Claude: "What's Tesla's stock price?"

Claude confidently answers: "$180."

But Tesla is actually trading at $280. What happened? Claude's
training data is from an earlier period when $180 was the right
answer. The format looks correct -- it's a plausible stock price,
not some obviously wrong number like $18,000. That's what makes it
dangerous. You won't get a number that screams "I'm wrong." You'll
get a number that *was* right a while ago.

This applies to any number Claude gives you: stock prices, index
levels, GDP figures, company revenue. If the number matters, verify
it.

### Failure Mode 2: Confabulated Facts

You ask Claude about Nike, and it confidently tells you the CEO is
someone who actually left the company years ago. The language is
smooth and authoritative -- there's nothing in the tone that says
"I'm making this up."

This is called *hallucination*, and it's built into how language
models work. Claude generates text that sounds plausible. Most of
the time, plausible text is also correct. But sometimes plausible
text is completely wrong, and Claude delivers it with the exact same
confidence.

Company facts that are especially risky: CEO names, board members,
recent acquisitions, product launches, and earnings dates. These
change over time, and Claude's information may be outdated or simply
fabricated.

### Failure Mode 3: Hallucinated Reasoning

This is the most dangerous one.

You ask Claude to analyze the streaming industry, and it says:
"Since Disney acquired Netflix in 2024, the combined entity now
dominates the streaming market..."

Disney never acquired Netflix. That never happened. But Claude
states it as fact and then builds a detailed, logical-sounding
analysis on top of it. The reasoning *after* the false premise
might actually be clever and insightful -- "the combined content
library gives them pricing power" and so on. It sounds great. But
the entire foundation is made up, so the conclusion is worthless.

This is the hardest failure to catch because the logic *feels*
right. Your brain follows the reasoning and nods along, and you
might not stop to question the premise it's built on. Always ask
yourself: "Is the starting fact actually true?"

### Failure Mode 4: Numerical Plausibility

You ask Claude about Apple's annual revenue, and it says "$300
billion." The actual number is around $390 billion. Close enough
that it doesn't set off alarm bells, but wrong enough to matter.

This is different from the stale magnitude problem. Sometimes
Claude generates numbers that were never exactly right -- they're
just in the right neighborhood. A stock's P/E ratio might be off
by 30%. A company's market cap might be wrong by $100 billion.
These errors survive casual review because they *feel* reasonable.

If you're making any decision based on a number, look it up
yourself.

### Failure Mode 5: The Core Problem -- No Uncertainty Signal

Here's what ties all of these together, and it's the thing that
makes AI genuinely risky if you don't understand it:

**A hallucinated fact and a correct fact look identical.**

When Claude says "Apple's headquarters is in Cupertino, California"
(true) and "Disney acquired Netflix in 2024" (completely false), it
uses the same confident, matter-of-fact tone for both. There is no
"I'm guessing" flag. There is no yellow highlight on the uncertain
parts. There is no difference in how it presents reliable
information versus total fabrications.

This means verification is 100% your job. AI won't tell you when
it's wrong. You have to develop the habit of checking important
facts, especially numbers, names, dates, and claims about what
companies have done.

### Why This Matters for Investing

Investing is one of the areas where getting facts wrong costs real
money. If you use an AI-generated stock price to make a buy
decision, and that price is months old, you could be making a
mistake. If you believe a company made an acquisition it never made,
your entire analysis falls apart.

Throughout this course, you'll learn tools and techniques that help
solve these problems -- ways to give Claude access to real data, ways
to verify what it tells you, templates that lock in accurate
numbers. But the tools only work if you also build the habit of
questioning what AI tells you. The tools are the first line of
defense. You are the second.

---

## F1.3 The Context Window

Every conversation with Claude has a context window -- think of it
as Claude's short-term memory. Everything you type, everything
Claude types back, and any documents you share all take up space in
this window. When it fills up, the oldest parts of the conversation
start getting forgotten.

How big is it? Claude's context window is about 200,000 tokens.
A token is roughly three-quarters of a word, so that's approximately
150,000 words -- about the length of two Harry Potter books.

What does this mean in practice?

**You can paste in long articles.** If you find a great article
about a company and want Claude to analyze it, just paste the whole
thing into the chat. It fits.

**Long conversations eventually lose their beginning.** If you have
a really long session where you analyze Apple, then Nike, then
Disney, then Tesla, Claude remembers all of it -- until the
conversation gets so long that the earliest messages start falling
out. If Claude seems to forget something you discussed earlier,
start a fresh conversation and bring over the key points.

**Specific questions get better answers.** "Tell me about Apple" will
get you a generic overview. "What are the two biggest risks to
Apple's iPhone business?" will get you a focused, useful answer.
It's like asking a friend a specific question versus saying "talk
to me about stuff."

**You control what Claude knows about.** Claude can only work with
what's in the conversation. If you give it an article about Nike
and then ask about Nike, it can reference the article. If you don't
give it the article, it only has its training data. What you include
in the conversation shapes the quality of the answers you get.

---

## F1.4 Custom Instructions

When you use Claude at [claude.ai](https://claude.ai), you can set
up custom instructions that apply to every conversation. These tell
Claude who you are and how you want it to respond.

Without custom instructions, Claude doesn't know if you're a
professional investor, a college student, or someone who just heard
about the stock market for the first time. It defaults to
general-purpose answers that try to help everyone -- which means
they're not specifically helpful to *you*.

Custom instructions fix this. Here's what good instructions look
like for a high school student interested in investing:

```
You are helping a high school student who is learning about the
stock market and investing.

When explaining things:
- Use clear, simple language -- not Wall Street jargon
- If you use a finance term, explain what it means
- Give examples using companies I know (Apple, Nike, Disney,
  Tesla, Netflix)
- Be honest when you're not sure about something

When I ask about stocks or companies:
- Remind me that your data might be outdated
- Explain your reasoning step by step
- Tell me both the good and bad sides of any company
- Keep responses concise -- I'll ask for more if I need it
```

See what this does? It tells Claude your level (learning), your
preferences (simple language, examples from familiar companies),
and your expectations (honest about uncertainty, concise). Every
response Claude gives will be shaped by these instructions.

Without this, you'd need to say "remember, I'm a student, keep it
simple" in every other message. With custom instructions, you say it
once and it sticks.

You can update your instructions anytime as you learn more and
figure out what works for you.

---

## F1.5 Projects in Claude

A Claude project is like a folder for your conversations. It has its
own custom instructions and its own set of uploaded documents.

Why does this matter? Because you might use Claude for different
things, and each one needs different context:

- **Stock Research** -- instructions focused on analyzing companies,
  comparing stocks, understanding financial data
- **School Stock Club** -- instructions for preparing presentations
  or discussions for your investment club
- **Learning Investing** -- instructions focused on explaining
  concepts clearly, with lots of examples
- **Homework Help** -- general academic instructions (not investing-
  specific, but useful to have separate)

Each project has two key features:

**Project instructions** work like the custom instructions from F1.4,
but they only apply inside that project. Your Stock Research project
might say "I'm researching tech stocks." Your School Stock Club
project might say "Help me prepare talking points for my club
meeting."

**Project knowledge** lets you upload documents that Claude can
reference in every conversation within the project. Upload an article
about Tesla, and Claude can reference it whenever you ask questions
in that project. Upload your stock club's portfolio list, and Claude
can help you analyze it.

To create a project:

1. Go to [claude.ai](https://claude.ai)
2. Look for "Projects" in the left sidebar
3. Click "Create project" (or the + icon)
4. Give it a name and write your project instructions
5. Optionally, upload documents to the project knowledge base

Every conversation you start inside that project will automatically
have access to those instructions and documents.

---

## F1.6 Artifacts

When Claude creates something substantial -- a comparison table, a
formatted summary, a structured report -- it can put it in an
artifact. An artifact appears in a separate panel next to the chat,
so it's easy to read, copy, or reference without scrolling through
messages.

Think of it like the difference between someone explaining something
out loud versus handing you a printed page. The explanation is
useful in the moment. The printed page is something you can keep,
mark up, and share.

For stock research, artifacts are great for:

**Comparison tables.** Ask Claude to compare Apple and Nike -- their
revenue, how fast they're growing, what their stock costs -- and
it'll produce a clean table you can actually use. Way better than
the same information buried in a paragraph.

**Research summaries.** Ask Claude to write a one-page summary of
a company, with sections for what the company does, how it makes
money, what the risks are, and what could go well. You can copy
this for your stock club or your own notes.

**Checklists.** Ask Claude to create a checklist for researching
a new stock -- what to look up, what questions to answer, what
data to find. Then use it every time you research a new company.

Artifacts appear automatically when Claude decides the content
deserves a standalone format. You can also ask for them explicitly:
"Put that in a table" or "Create an artifact with that summary."

Not everything needs to be an artifact. Quick answers and
back-and-forth conversation are better as regular chat. Artifacts
are for things you want to keep or share.

---

## F1.7 Prompting Basics

You'll hear a lot of advice about "prompt engineering" -- fancy
techniques for getting better answers from AI. Most of it boils
down to a few simple ideas that actually matter.

### Be specific

"Tell me about Nike" is vague. Claude has to guess what you want.

"Compare Nike and Disney -- which company grew revenue faster over
the last three years?" is specific. Claude knows exactly what
you're asking and can give you a focused answer.

The more specific your question, the more useful the answer.

### Ask for reasoning

"Is Tesla a good stock to buy?" gives you a conclusion you can't
really evaluate.

"Walk me through the bull case and the bear case for Tesla. What
are the strongest arguments on each side?" gives you reasoning you
can think about, agree with, or push back on.

Asking for reasoning is especially important with AI because it
lets you see *where* the logic is strong and *where* Claude might
be working from outdated information.

### Push back

Claude's first answer isn't always its best answer. Treat it like
a first draft.

"That's interesting, but you didn't mention competition from
Adidas. How does that change the picture for Nike?"

Claude doesn't get defensive. It doesn't forget what you already
discussed. It takes your feedback and gives you a better answer.
Some of the best analysis comes from going back and forth three
or four times, not from a single perfect question.

### Iterate

If the first answer is too long, say "make it shorter." If it's
too general, say "be more specific about X." If it missed something,
say "you forgot to consider Y."

Think of it as a conversation, not a search engine query. You're
working *with* Claude to get to a good answer, not hoping to get
lucky on the first try.

### Say what you don't want

"Don't give me generic stuff that applies to every company. Focus
on what makes Netflix different from other streaming companies."

This prevents Claude from padding its response with filler that
isn't useful to you.

---

## Key Takeaways

- **AI is a reasoning tool, not a fact database.** Claude can
  analyze, explain, and compare, but every specific number or fact
  it gives you might be outdated or wrong. Think of it as a
  brilliant study partner with no internet access.

- **AI fails silently -- verification is your responsibility.** This
  is the single most important lesson. Claude presents hallucinated
  facts with the same confidence as correct ones. Any stock price,
  company fact, or specific claim from AI needs to be checked
  against a real source before you trust it.

- **The context window is Claude's memory.** About 150,000 words
  (two Harry Potter books). You can paste in articles and documents,
  but specific questions always get better answers than vague ones.

- **Custom instructions make Claude work for you.** Tell Claude your
  level, your interests, and how you want responses. Say it once
  and it applies to every message.

- **Projects keep your work organized.** Different projects for
  different purposes, each with their own instructions and
  documents.

- **Good prompts are specific prompts.** Say exactly what you want
  to know. Ask for reasoning. Push back. Iterate. The best answers
  come from conversations, not single questions.
