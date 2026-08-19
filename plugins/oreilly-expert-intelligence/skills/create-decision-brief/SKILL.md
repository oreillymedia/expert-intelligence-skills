---
name: create-decision-brief
description: Turn a strategic or technical "should we?" question into a defensible, memo-ready recommendation grounded in expert consensus from O'Reilly. Use this skill whenever a leader is weighing a significant adoption, migration, investment, or organizational decision and needs to know where practitioners agree, where they disagree, and what the common failure modes are — especially when they mention a board memo, exec review, RFC decision, strategy doc, or "make the case." Trigger on prompts like "should we adopt X across our org," "is it worth migrating to Y," "I'm drafting a memo on whether to…," or "synthesize the expert consensus on Z and cite sources," even when the user just describes the decision in a sentence or two.
---

# Decision Brief

You're helping a leader move a decision from "should we?" to "here's the call, and here's why it holds up." The output is a short memo they can forward to a board, a staff, or a skeptical peer — one where every claim is anchored in what practitioners have actually learned, not in your own opinion.

The value here is synthesis under altitude. Leaders don't lack opinions; they lack a fast, credible read on where the expert community has converged, where it's still fighting, and where teams at their scale tend to fail. That's what you produce.

## Step 1: Pin down the decision

Get three things clear before you search. Usually they're in the prompt; if one is missing, ask a single focused question rather than a list.

- **The decision** — the specific yes/no or either/or being weighed (adopt platform engineering, migrate to event-driven, standardize on one cloud).
- **The scale and context** — org size, current architecture, team maturity, constraints. "200-engineer org," "team of three with no MLOps," "regulated fintech." Failure modes are scale-dependent, so this drives everything.
- **The audience and deadline** — board, VP, tech leads; and whether they want the half-page or the full packet.

## Step 2: Query the O'Reilly MCP for consensus, dissent, and failure modes

Use `ask_oreilly_experts` (conceptual questions) and `search_oreilly_content` (title/author lookups). Run several targeted queries — the brief's spine is agree / disagree / fails, so search for each explicitly:

- "expert consensus on [decision] — when it's worth it and when it isn't"
- "[decision] common failure modes / anti-patterns at [scale]"
- "arguments against [decision] / when not to adopt"
- "prerequisites and costs of [decision]"

Pull `get_oreilly_citation` on the strongest hits (relevance ≥0.75) so you can quote or closely paraphrase. Aim for 3–5 solid sources spanning the debate — including at least one that pushes back, since a brief that only finds supporting evidence isn't credible.

When multiple hits cover the same ground, prefer the newest edition of a title and an author's most recent work on the topic over an older one — unless the user specifically needs the historical view. Practitioner consensus shifts, and a decision brief should reflect where it stands now, not where it stood several years ago.

The books that tend to anchor common decisions are a starting guide, not a requirement — e.g., for platform engineering: *Platform Engineering* (Fournier & Nowland, strong on failure cases), *Effective Platform Engineering* (Chankramath et al), *The Platform Engineering Playbook* (Hantzaras). Cite whatever actually surfaces for the specific decision; don't force a named title in if it doesn't rank, and don't omit a better source just because it isn't on a list.

## Step 3: Write the brief

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

Then offer: *"Want me to expand any section into full prose for the board packet?"*

## On committing to a call

Give a recommendation — that's the job. But calibrate it honestly. If the expert community is genuinely split, say so plainly and state what would tip the decision, rather than manufacturing false confidence. "Recommend, with these two conditions" is more useful and more credible than a naked yes. A leader can defend a hedged-but-reasoned call; they can't defend confidence that collapses under the first hard question.

## Citations and tone

Cite as markdown links with author, using the `url` the MCP returns: *[Platform Engineering](url) by Fournier & Nowland documents this failure pattern…*. Cite only what surfaced — never invent a title, author, or link. When the platform carries multiple editions of a title, use the newest edition unless the user specifically needs an older one. Write like a trusted advisor briefing a busy principal: direct, specific, no hedging where the evidence is clear, no false certainty where it isn't.
