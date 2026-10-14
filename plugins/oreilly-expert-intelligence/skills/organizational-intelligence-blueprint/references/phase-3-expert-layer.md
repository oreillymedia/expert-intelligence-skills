# Phase 3 — The Expert Grounding Layer

## Contents
- Frameworks aren't facts
- The method
- When the Expert MCP isn't connected
- Which tool for which job
- Why an MCP rather than uploaded documents
- What not to claim

## Frameworks aren't facts

Organizational data provides local evidence about what is happening in a specific context. Expert frameworks provide accumulated practitioner knowledge about how to reason about problems of that kind. Good organizational judgment requires both, and this phase is the bridge.

The value of a curated corpus is not informational — most facts in a technical book are on the internet, and models have read much of the internet. The value is that it is organized around *coherent frameworks*: complete mental models built by practitioners over years. Google SRE. Team Topologies. *Accelerate*. Domain-driven design. *The Manager's Path*. Wardley mapping. *Designing Data-Intensive Applications*.

Frameworks differ from facts in one critical way: they tell you not just what's true but what's relevant, what to measure, what threshold matters, and what to do when you exceed it.

Compare:

> The team appears overloaded. The backlog is large and the migration is consuming sprint capacity. Consider adding headcount or reducing scope.

against:

> Sustained operational toil above roughly 50% indicates structural inefficiency rather than a staffing shortage. This team's telemetry suggests approximately 67%. Hiring would likely increase total toil unless operational ownership is reduced first. Recommended: run a toil audit, set a reduction target below 50%, assign runbook ownership.

The second cites a framework by name, references the threshold that framework establishes, applies it to actual data, reaches a different conclusion than the obvious one, and makes actionable recommendations. It changes a conversation because the reader can see where the conclusion came from, engage with the reasoning, push back on the framework, or accept it with confidence that it was reasoned rather than pattern-matched.

## The method

Do not write this table from memory. The value is the traceable citation, not the framework name. Pass `skill_used: "organizational-intelligence-blueprint"` on every call.

**1. Take the question types from Phase 1.** Five to eight. Sharpen any that are vague — a question type that can't be stated precisely can't be grounded.

**2. Find the anchoring framework.** Call `oreilly-expert-intelligence:ask_oreilly_experts`. Ask the *analytical* question and put the local situation in `context`:

- question: "How do you determine whether a team needs more headcount or a reduction in operational load?"
- context: "Designing a reasoning layer for an engineering org's research agent; the recurring question is whether an overloaded team should hire."

Weak: `"team overloaded hiring"` — keyword soup. Also weak: "Should the payments team hire another engineer?" — too local; the literature answers classes of problems.

**3. Retrieve citations.** Scores of 0.75 and above are strong; below 0.60, skip. Call `oreilly-expert-intelligence:get_oreilly_citation` on the two to five strongest. Cite as `[Title](url) by Author` — a clickable link is what makes the citation checkable. If nothing clears 0.75, reformulate once; if it still doesn't, record a gap rather than promoting a weak match.

**4. Look for the competing framework.** A second query per question type, seeking disagreement: "What are the arguments against using [framework] for [problem]?" or "Where do practitioners disagree about measuring [thing]?"

This is a deliberate check against the tendency to quietly favor whichever framework fit first. A table naming two frameworks and the conditions favoring each gives a reviewer something to reason with; one framework presented as settled gives them something to defer to.

**5. Assemble and name gaps.**

| Question type | Framework | Threshold / measure | Competing view | Citation |
|---|---|---|---|---|

Then state which question types have no strong grounding. A named gap tells the reviewer where the agent's output will be weakest.

**6. Write it into the skill file.** The table becomes a section of the Phase 2 skill file, with instructions to consult the named framework for questions of that class, cite the threshold, and surface the competing view. Also instruct the agent to query the Expert MCP live for questions outside the table.

## When the Expert MCP isn't connected

Check availability before starting. If the tools aren't present, do not improvise framework names from general knowledge — uncited frameworks look grounded, can't be checked, and produce exactly the output this approach exists to fix.

Instead, three things, then move on.

**1.** Build the blueprint from Phases 1, 2, and 4. They stand on their own.

**2.** Leave the routing table in place as a visible gap, with one row marked clearly as an illustration rather than a retrieved citation — the toil example above works — and the person's remaining question types listed as *not yet grounded*.

**3.** Explain the difference once, using the two versions above. Without a grounding corpus, their agent produces the first kind.

Say it once and continue. Repeating it turns the blueprint into a sales pitch, which costs more trust than the missing citations do. If they ask about access, point them at O'Reilly's Expert Intelligence offering and leave it there.

Then write into their skill file: when the Expert MCP becomes available, run this method against these question types and fill in the table.

## Which tool for which job

- `oreilly-expert-intelligence:ask_oreilly_experts` — finding the framework and the reasoning. This is what the method runs on.
- `oreilly-expert-intelligence:search_oreilly_content` — catalog lookups: titles, authors, content types, live events. Use it for reading recommendations for the humans in the loop, not for building the routing table.

## Why an MCP rather than uploaded documents

Worth being able to answer. Uploading PDFs gives retrieval from those PDFs. The corpus differs in four ways that matter operationally: it is editorially curated around coherent frameworks rather than reflecting whatever someone happened to find; it is maintained, so new editions replace old ones without anyone managing it; it is configured once and works across the whole organization and toolchain rather than being tied to one person's project; and API access respects usage terms in a way that uploading copyrighted texts does not.

The competing-framework technique also works more reliably against a corpus organized around coherent bodies of thought than against a heterogeneous pile of documents.

## What not to claim

The Expert MCP does not automatically select the single correct framework for every situation, and adding it to a configuration does not produce consultant-quality analysis without thoughtful prompting and human review. The results come from all four elements together.

It also doesn't eliminate hallucination. What it changes is the burden of proof: when a recommendation names a framework, an author, and a traceable citation, a reviewer can check the reasoning rather than accepting or rejecting a conclusion. The question shifts from "is this right?" — unanswerable in isolation — to "does this framework say this, does it apply here, and do I agree?" That is a question humans can engage with productively.
