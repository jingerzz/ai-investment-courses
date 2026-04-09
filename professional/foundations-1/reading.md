# Foundations 1: Understanding Claude --- Your AI Research Partner

## F1.1 What Large Language Models Actually Are

Imagine hiring an analyst who has read every investing textbook ever
written, every earnings call transcript from the last twenty years,
every macro research note published in English, and most of the
financial press. This analyst can synthesize across all of it, draw
connections between disparate ideas, and explain complex topics clearly.

Now imagine that this analyst has no Bloomberg terminal. No market data
feed. No access to EDGAR. Everything they know comes from what they
read during training --- and that training ended months ago. They can
reason brilliantly about what they've seen, but they cannot tell you
what happened in the market yesterday.

That's a large language model.

LLMs like Claude are pattern-matching engines trained on enormous
amounts of text. During training, the model processes billions of
documents and learns the statistical relationships between words,
sentences, and ideas. It learns what good financial analysis looks
like by reading thousands of examples. It learns how to reason about
risk by absorbing decades of research. It learns accounting standards,
valuation frameworks, and regulatory language --- not because someone
programmed those rules in, but because the patterns appeared over and
over in the training data.

This produces something genuinely useful: a system that can reason
about finance at a high level, explain complex concepts clearly, and
synthesize across multiple frameworks. Ask Claude to compare DCF and
comparable company analysis for a specific situation, and it will give
you a thoughtful answer that reflects real understanding of both
methods.

But there are hard limits. Claude does not have access to current
prices, recent filings, or live data of any kind. It cannot look
something up. When it states a number --- a stock price, a GDP figure,
an earnings result --- it is drawing from training data that may be
months or years old. It has no way to know whether that number is
still accurate.

This is the fundamental tension of using AI for investment work: the
reasoning is strong, but the data connection is missing. The rest of
this course is about solving that problem. But first, you need to
understand how Claude works well enough to use it effectively even
without live data --- because the reasoning capabilities alone are
remarkably powerful for the right tasks.

### How AI Gets Things Wrong

Before we go further, you need a mental model for the specific ways AI
fails in investment contexts. These aren't theoretical — they're
patterns you will encounter, and recognizing them is a core skill.

**Stale magnitude errors.** AI may quote the S&P 500 index in the
5,000s when it's actually trading in the 6,000s. This happens because
the model's training data reflects an earlier period. The format looks
correct — it's a plausible number for an index level — which makes it
dangerous. You won't get a 6-digit number that's obviously wrong. You'll
get a 4-digit number that *was* right six months ago.

**Confabulated company facts.** AI will confidently state that a company
made an acquisition that never happened, name a wrong CEO, or cite a
financial metric that doesn't match reality. The language is fluent and
authoritative — there's nothing in the tone that signals "I'm making
this up." This is called *hallucination*, and it's an inherent property
of how language models work: they generate plausible text, and sometimes
plausible text is wrong.

**Hallucinated reasoning chains.** This is the most dangerous failure
mode. The AI builds an investment thesis on a premise that is simply
false — "Given that Company X recently acquired Y..." when no such
acquisition happened. The logic from that point forward is internally
consistent and may even be insightful. But the foundation is fabricated,
and the conclusion is worthless. The reasoning *quality* masks the data
*quality* problem.

**Numerical plausibility traps.** The AI generates numbers that are in
the right ballpark but wrong — revenue of $4.2B when it's actually
$6.8B, or a P/E ratio of 18 when it's actually 28. These are close
enough to not trigger alarm bells, but wrong enough to change an
investment decision. Unlike a blatant error, a plausible-but-wrong
number can survive casual review.

**The core problem:** AI does not signal uncertainty the way humans do.
A hallucinated fact and a correct fact are presented with identical
confidence. There is no "I'm guessing" flag. This means the burden of
verification falls entirely on you, and you need to know where to look.

Throughout this course, you'll learn engineering solutions to many of
these problems — tools that feed live data to AI, guardrails that
prevent it from doing math, templates that lock in exact numbers. But
the engineering only works if you also develop the habit of critical
verification. The tools are the first line of defense. You are the
second.

---

## F1.2 The Context Window

Every conversation with Claude has a context window --- think of it as
Claude's working memory. Everything you say, everything Claude says,
and any documents you share all occupy space in this window. When the
window fills up, the oldest parts of the conversation start dropping
out.

Claude's context window holds roughly 200,000 tokens. A token is
roughly three-quarters of a word, so 200K tokens is approximately
150,000 words --- about the length of two full-length books, or a
stack of 10-K filings from three or four mid-cap companies.

This has practical implications for investment work:

**Long documents work.** You can paste an entire earnings transcript
or a 50-page research report into a conversation and ask Claude to
analyze it. The document fits comfortably in the context window, and
Claude can reference specific sections, compare different parts, and
draw conclusions across the whole thing.

**Conversations have memory --- until they don't.** In a long
conversation, Claude remembers everything you've discussed. If you
analyzed Apple in the first message and Microsoft in the fifth, you can
ask Claude to compare them in the tenth message. But in an extremely
long session, early messages may fall out of context. If you notice
Claude forgetting something you discussed earlier, start a new
conversation and bring forward the key points.

**Focused questions get better answers.** A question like "What are
the three biggest risks in this 10-K?" will get a sharper answer than
"Tell me everything about this filing." Not because Claude can't
process the whole document, but because a focused question directs
Claude's attention to the most relevant patterns. Think of it like
giving an analyst a specific assignment versus telling them to "look
into it."

**You control what's in the window.** Every piece of text you include
is text Claude can reference. Every piece you leave out is invisible.
This means you can shape Claude's analysis by choosing what context to
provide. Give Claude your investment thesis before asking it to
evaluate a company, and the analysis will be framed around your thesis.
Skip the thesis, and you'll get a generic overview.

---

## F1.3 System Prompts and Custom Instructions

When you start a conversation with Claude, you can provide instructions
that persist throughout the entire session. These are called custom
instructions (on claude.ai) or system prompts (in the API). They tell
Claude who you are, how you work, and how you want it to respond.

Without custom instructions, Claude has no idea whether you're a
retail investor asking about your first stock purchase or a portfolio
manager running a multi-billion dollar fund. It defaults to
general-purpose responses that try to be helpful to everyone --- which
means they're not specifically helpful to you.

Custom instructions change this. They shape every response Claude
gives, without you having to repeat yourself in every message. Here's
what good custom instructions look like for an investment professional:

```
You are assisting a senior equity analyst at a long/short hedge fund.
I cover US technology stocks with a focus on enterprise software.

When analyzing companies:
- Frame everything in terms of competitive moat and unit economics
- I care about Rule of 40 (revenue growth + FCF margin) as a quality metric
- Always note the bull and bear case, even if one seems obvious
- Use specific numbers from filings, not generalizations

When responding:
- Be direct. Skip disclaimers about "this is not financial advice"
- If you're uncertain about a data point, say so explicitly
- Use the terminology I'd use with my PM, not retail language
- Keep responses concise --- I'll ask for more detail if I need it
```

Notice what these instructions accomplish. They tell Claude your role
(senior equity analyst), your domain (enterprise software), your
analytical framework (moat, unit economics, Rule of 40), and your
communication preferences (direct, concise, no disclaimers). Every
response Claude gives in this session will be calibrated to this
context.

Compare that to a conversation without instructions, where you'd need
to say "Remember, I'm an equity analyst who cares about unit
economics" in every other message. Custom instructions say it once and
it sticks.

You can update your custom instructions at any time. As you work with
Claude more, you'll develop a feel for what makes your instructions
more effective. Start simple and add specifics as you discover what
you want Claude to do differently.

---

## F1.4 Projects in Claude

A Claude project is a workspace where you can organize conversations
around a specific topic. Think of it as a folder with persistent
context --- its own custom instructions and its own knowledge base.

Why does this matter? Because different types of investment work
require different contexts. Your equity research needs different
instructions than your macro analysis, which needs different
instructions than your compliance review. Without projects, you'd
either maintain one giant set of instructions that tries to cover
everything (and covers nothing well) or rewrite your instructions
for every new conversation.

Projects solve this by letting you create separate workspaces:

- **Equity Research** --- instructions focused on fundamental analysis,
  your coverage universe, your valuation framework
- **Macro / Asset Allocation** --- instructions focused on regime
  analysis, cross-asset correlations, your firm's allocation process
- **Compliance Review** --- instructions focused on regulatory
  language, your firm's policies, disclosure requirements
- **Earnings Season** --- instructions focused on transcript analysis,
  estimate revisions, management tone

Each project has two key features:

**Project instructions** work like the custom instructions described
in F1.3, but they apply only to conversations within that project.
Your Equity Research project might say "Focus on enterprise software
and SaaS metrics." Your Macro project might say "I trade SPY and TLT
as my primary instruments. Analyze everything through a regime lens."

**Project knowledge** lets you upload documents that Claude can
reference in every conversation within the project. Upload your firm's
investment process document to a project, and Claude can reference it
when you ask "How would our process evaluate this opportunity?" Upload
a set of earnings transcripts, and Claude can compare them across
conversations.

To create a project:

1. Go to [claude.ai](https://claude.ai)
2. Look for "Projects" in the left sidebar
3. Click "Create project" (or the + icon)
4. Give it a name and write your project instructions
5. Optionally, upload documents to the project knowledge base

Every conversation you start within that project will have access to
those instructions and documents automatically. You don't need to
re-upload or re-explain anything.

---

## F1.5 Artifacts

When Claude produces a substantial, standalone piece of content --- a
comparison table, a formatted report, a structured analysis --- it can
create an artifact. An artifact appears in a separate panel alongside
the conversation, making it easy to read, copy, or reference without
scrolling through chat messages.

Think of the difference between an analyst explaining something
verbally at your desk versus handing you a printed summary. The
explanation is useful in the moment. The printed summary is something
you can take with you, mark up, and share. Artifacts are the printed
summary.

For investment work, artifacts are particularly useful for:

**Comparison tables.** Ask Claude to compare the financial profiles of
five companies, and it can produce a clean table with revenue growth,
margins, valuation multiples, and key metrics --- formatted and ready
to reference. This is far more useful than the same information buried
in a paragraph of text.

**Structured reports.** Ask Claude to write a brief investment memo on
a company, and it can produce a formatted document with sections for
thesis, key metrics, risks, and catalysts. You can copy this directly
into your workflow.

**Checklists and frameworks.** Ask Claude to create a due diligence
checklist for evaluating SaaS acquisitions, and it produces a
structured document you can reuse across multiple deals.

Artifacts appear automatically when Claude determines the content
warrants a standalone format. You can also ask explicitly: "Create a
table comparing these companies" or "Put that analysis in an artifact
I can reference later."

Not everything should be an artifact. Quick answers, clarifications,
and back-and-forth discussion work better as regular conversation.
Artifacts are for outputs you want to keep, reference, or share.

---

## F1.6 Prompting for Investment Work

Generic prompt engineering advice --- "be specific," "provide
context," "ask step by step" --- applies to finance, but it misses
what makes financial prompting different. Your domain has its own
vocabulary, its own analytical frameworks, and its own standards for
what constitutes a useful answer. Here are the practices that matter
most.

### Be specific about timeframes, instruments, and analysis type

Finance is full of ambiguity that natural language makes worse.
"How is Apple doing?" could mean the stock price, the business
fundamentals, the competitive position, or the technical setup.
Claude will guess, and it might guess wrong.

Instead: "Analyze Apple's enterprise services segment over the last
three fiscal years, focusing on revenue growth and margin expansion."
This eliminates ambiguity and gets you an answer you can actually use.

### Tell Claude what role to play

"You are a sell-side analyst writing a note for institutional
clients" produces very different output than "You are helping a
retail investor understand their portfolio." The role shapes the
depth, the terminology, and the assumptions Claude makes about what
you already know.

For investment professionals, useful roles include: equity research
analyst, credit analyst, risk manager, macro strategist, compliance
officer. Each one changes how Claude frames its analysis.

### Provide context about your analytical framework

If you care about free cash flow yield more than P/E, say so. If
your firm uses a specific scoring model, describe it. Claude can't
read your mind about which metrics matter to you, but it's very good
at adapting once you tell it.

"Evaluate this company using our quality framework: sustainable
revenue growth above 15%, gross margins above 60%, and FCF
conversion above 20% of revenue. Flag any metric that falls short."

### Ask Claude to show its reasoning

"Walk me through how you'd evaluate the bull case for this stock"
produces a more useful response than "Is this stock a buy?" The
first gives you reasoning you can agree with, challenge, or build on.
The second gives you a conclusion you can't evaluate.

This is especially important because Claude doesn't have current
data. When it shows its reasoning, you can see where the logic is
sound (based on enduring principles) and where it's working from
potentially stale information (specific numbers or recent events).

### Push back and iterate

Claude's first answer is rarely its best answer. Treat it like a
draft from a junior analyst. "That's a reasonable framework, but
you're not considering the impact of their pricing power on margins.
Redo the analysis with that factor included."

This kind of iteration is where Claude becomes genuinely valuable.
It doesn't get defensive. It doesn't forget the prior context. It
incorporates your feedback and produces a better version. The best
investment analysis with Claude comes from three or four rounds of
refinement, not from a single perfect prompt.

### State what you don't want

"Don't include generic risk factors that apply to every company.
Focus on the two or three risks specific to this business model."
This prevents the kind of padding that makes AI output feel like
a compliance document rather than useful analysis.

---

## Key Takeaways

- **LLMs are powerful reasoning engines with no live data.** Claude
  can analyze, synthesize, and explain financial concepts at a high
  level, but every specific number it quotes comes from training data
  that may be outdated.

- **The context window is your working memory.** At ~200K tokens, you
  can fit entire filings and transcripts, but focused questions get
  better answers than open-ended ones.

- **Custom instructions eliminate repetition.** Define your role, your
  framework, and your preferences once, and Claude applies them to
  every response in the session.

- **Projects organize your work.** Separate projects for different
  types of analysis keep your instructions focused and your documents
  accessible.

- **Prompting for finance is about precision.** Specify timeframes,
  instruments, and analysis types. Tell Claude your framework. Ask it
  to show its reasoning so you can evaluate where the logic is sound
  and where the data might be stale.

- **AI fails silently — verification is your responsibility.** AI
  presents hallucinated facts with the same confidence as correct ones.
  Any specific number, date, name, or claim from AI output should be
  verified against a primary source before you act on it. This habit
  matters more than any technical feature.
