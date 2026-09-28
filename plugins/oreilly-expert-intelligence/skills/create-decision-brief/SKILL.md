---
name: create-decision-brief
description: Creates a memo-ready recommendation for a significant adoption, migration, investment, or organization decision using cited O'Reilly consensus, dissent, prerequisites, and failure modes. Use when the primary task is a decision-maker-facing "should we?", "which option?", or "under what conditions?" decision, including when an existing proposal or architecture provides context. For proposal-wide critique and approval readiness, use review-technical- proposal; for detailed evaluation of underlying system-design trade-offs, use review-architecture-decision.
---

# Decision Brief

Produce a short, decision-maker-facing memo that recommends a course of action and shows the supporting consensus, credible dissent, prerequisites, and failure modes.

## Source and citation rules

Use only sources returned by the O'Reilly MCP tools. Tool names below are unqualified because the server name is user-configured; when the runtime requires qualified names, prepend the configured server name (for example, `oreilly:ask_oreilly_experts`). Cite each selected result as `[title](url) by authors`, using `product_title` when the result provides it instead of `title`. Copy the title and URL exactly from that same result; do not alter, normalize, shorten, repair, or reconstruct the URL. Use a string-valued `authors` field unchanged; for a list, join the returned names in order with commas. When `get_oreilly_citation` returns a fully rendered `citation_format`, use it unchanged. Never invent or reconstruct metadata or quotations. Remove a citation that cannot be verified against the tool result. Present uncited conclusions as your own analysis or omit them.

## Step 1: Frame the decision

Get three things clear before you search. Usually they're in the prompt; if one is missing, ask a single focused question rather than a list.

- **The decision** — the specific yes/no or either/or being weighed (adopt platform engineering, migrate to event-driven, standardize on one cloud).
- **The scale and context** — org size, current architecture, team maturity, constraints. "200-engineer org," "team of three with no MLOps," "regulated fintech." Failure modes are scale-dependent, so this drives everything.
- **The audience and deadline** — board, VP, tech leads; and whether they want the half-page or the full packet.

## Step 2: Research consensus, dissent, and failure modes

Research in this order:

1. Turn the decision, credible countercase, prerequisites, and failure modes into targeted questions.
2. Use `ask_oreilly_experts` and/or `search_oreilly_content` as appropriate for the research need, following their tool descriptions.
3. Select only results that directly support a material part of the recommendation or countercase.
4. Draft from the verified evidence. If no directly relevant source surfaces, state the evidence gap instead of citing a weaker source.

Run several targeted queries — the brief's spine is agree / disagree / fails, so search for each explicitly:

- "expert consensus on [decision] — when it's worth it and when it isn't"
- "[decision] common failure modes / anti-patterns at [scale]"
- "arguments against [decision] / when not to adopt"
- "prerequisites and costs of [decision]"

Use a small set of sources spanning the debate, including credible counterevidence; a brief that searches only for support is not defensible.

When multiple hits cover the same ground, prefer the newest edition of a title and an author's most recent work on the topic over an older one — unless the user specifically needs the historical view. Practitioner consensus shifts, and a decision brief should reflect where it stands now, not where it stood several years ago.

The books that tend to anchor common decisions are a starting guide, not a requirement — e.g., for platform engineering: *Platform Engineering* (Fournier & Nowland, strong on failure cases), *Effective Platform Engineering* (Chankramath et al), *The Platform Engineering Playbook* (Hantzaras). Search the decision actually being made. Do not force a named title into the brief or omit a stronger result because it is unfamiliar.

## Step 3: Draft the brief

Lead with the recommendation. Default to **half a page, bulleted, scannable in under two minutes** — a leader should get the answer and its backbone at a glance, then follow citations or ask you to expand any section.

Use this structure:

---

### [Decision] — Recommendation

**Recommendation:** [One or two sentences. The call, plus a confidence signal — "recommend, with caveats," "recommend against at your current scale," "too close to call without X."]

**Where experts agree**
- [Point] — cited.
- [Point] — cited.

**Where they disagree**
- [The live debate, and which side the evidence leans toward for *this* context] — cited.

**Failure modes at your scale**
- [The specific ways teams like theirs get burned] — cited.

**What it costs / what has to be true first**
- [Prerequisites, investment, org readiness.]

**What would change this recommendation**
- [The condition or evidence that would flip the call.]

---

## Step 4: Verify the brief

Before responding:

1. Confirm that the recommendation answers the stated decision and fits the audience and context.
2. Check that the brief covers supporting evidence, credible dissent, failure modes, prerequisites, and what would change the recommendation.
3. Compare every citation with the MCP result — title, author, edition, and URL must match exactly — and remove any citation you cannot verify rather than repairing it.
4. Remove claims that are unsupported or irrelevant to the decision.

If any check fails, revise the brief and run these checks again. Do not respond until all of them pass.

## Principles

Give a recommendation — that's the job. But calibrate it honestly. If the expert community is genuinely split, say so plainly and state what would tip the decision, rather than manufacturing false confidence. "Recommend, with these two conditions" is more useful and more credible than a naked yes. A leader can defend a hedged-but-reasoned call; they can't defend confidence that collapses under the first hard question.

Prefer the newest applicable edition when sources cover the same decision. Write for a busy decision-maker: direct where evidence is clear, explicit about dissent, and calibrated where it is not.
