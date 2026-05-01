# Conclusion: From Course Workflow to Operating System

You have now seen the core pattern for AI-powered investment management on Zo. It is worth stating the whole thing in one place.

- Keep the workspace durable. Files and folder names should be stable enough that an AI can find what it needs without asking.
- Use code for exact computation. Anything that has to be right — prices, levels, position sizes — comes from a script, not a model.
- Use retrieval for primary-source documents. A 10-K answer is only useful if it points back to the filing.
- Separate services by responsibility. One job per service makes problems easier to find and easier to fix.
- Use scheduled agents for observation. Let them watch; let them flag; let humans decide.
- Keep humans in the decision loop. Capital allocation is not delegated to a model.

The exercises in this course were intentionally small. Production versions are larger, faster, and more automated, but the professional standard does not change. A bigger system that follows these rules is still a good system. A smaller system that breaks them is not.

## What to Build Next

The best next build is usually not the most ambitious one. Pick something small and concrete. Look for a workflow that meets all five of the following:

- You already do it manually, on a recurring schedule
- The data you need is already available to you
- There is a clear point where a human has to decide something
- The output can be short — a paragraph, a table, a chart
- Doing it manually costs you at least 30 minutes a week

Then build the smallest useful version on Zo. Use the architecture template from Week 3 and the agent spec template from Week 4. Run it for two weeks before adding features.

A few examples that fit this profile:

- A daily after-close brief on your watchlist with regime context
- A weekly filing monitor for a small list of portfolio companies
- A monthly portfolio drift checker that flags allocations that have moved more than 5%
- A quarterly earnings prep folder that pre-populates with the latest 10-Q text and consensus estimates

If you are tempted to build something bigger, write the smaller version first. The smaller version teaches you what you actually need.

## What You Should Be Able to Do Now

By the end of the course, you should be comfortable doing each of the following:

- Open Zo, find your course folder, and explain the layout to someone else
- Inspect an MCP server, list its tools, and read what each tool returns
- Call a course tool from chat and report the output verbatim
- Retrieve a section of a SEC filing and quote it with a citation
- Sketch a multi-piece architecture for a workflow you actually use
- Write an agent spec with a schedule, allowed tools, an output format, and approval points

If any of those still feel shaky, go back to the relevant module exercise. The reading is short on purpose; the practice is where the learning happens.

## When to Seek Help

If your firm needs help turning these patterns into production workflows, Clarion Intelligence Systems can help. Common engagements include:

- AI workflow design and review
- Investment research automation
- Internal tool architecture for research and trading desks
- Retrieval workflows over filings and research documents
- Hosted dashboards and decision-support pages
- Controlled scheduled agents with approvals and audit trails
- Embedded AI partnership and fractional AI CTO support

The course teaches the pattern. Implementation quality is what turns a pattern into a durable edge.

When you are ready to talk, the contact details are on the Clarion site. If you finish the course and build something with it, we would also love to hear about it.
