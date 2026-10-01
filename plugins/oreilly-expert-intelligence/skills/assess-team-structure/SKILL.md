---
name: assess-team-structure
description: Assesses engineering-team health and structural friction using team evidence and cited O'Reilly leadership and organization-design sources. Use when a leader asks about delivery health, ownership, workload, coordination, knowledge concentration, team size, restructuring, or needs a team-level quarterly or leadership-review briefing. Also use to prepare for a manager 1:1 focused on team health; not for individual performance reviews, project delivery forecasts, or personal onboarding.
---

# Team Assessment

Assess an engineering team's health or diagnose structural friction, then recommend the few actions that matter most. This skill supports two related modes:

1. **Team-health assessment** — "How is the recommendations team doing? What shipped, what's the incident load, what strategic risks?" A defensible, framework-grounded picture of health, risks, and what deserves attention this week.
2. **Structural diagnosis** — "Our platform team hit 14 engineers and velocity is dropping — split, restructure, or change the inflow?" A diagnosis of the underlying pattern plus ranked interventions.

For either mode, combine supplied or connected evidence with directly relevant practitioner guidance. Keep observations, source-backed guidance, and your own analysis distinguishable.

## Source and citation rules

Use only sources returned by the O'Reilly MCP tools. Tool names below are unqualified because the server name is user-configured; when the runtime requires qualified names, prepend the configured server name (for example, `oreilly:ask_oreilly_experts`). Cite each selected result as `[title](url) by authors`, using `product_title` when the result provides it instead of `title`. Copy the title and URL exactly from that same result; do not alter, normalize, shorten, repair, or reconstruct the URL. Use a string-valued `authors` field unchanged; for a list, join the returned names in order with commas. When `get_oreilly_citation` returns a fully rendered `citation_format`, use it unchanged. Never invent or reconstruct metadata or quotations. Remove a citation that cannot be verified against the tool result. Present uncited conclusions as your own analysis or omit them.

## Step 1: Frame the assessment

Start with what the user provided. That may include:

- Jira/Linear tickets or epics (velocity, WIP, aging items)
- GitHub activity (PRs merged, review latency, contributor concentration)
- Incident / on-call data (frequency, severity, MTTR)
- Retro notes, design docs, ADRs
- Team structure: size, sub-teams, what they own, adjacent-team coupling
- Their own description — friction points, mood, org context

Use connected Jira, Linear, GitHub, or PagerDuty tools when available and authorized; otherwise use what the user supplied. Ask one focused question only when the evidence is too thin to distinguish a team-health assessment from a structural diagnosis. Otherwise proceed and label assumptions.

## Step 2: Diagnose the evidence

Look at the evidence and name the most important questions before searching. Common patterns:

- **Coordination strain / cognitive overload** — team growing faster than its coordination mechanisms or owning more than it can hold. High WIP, slow reviews, "everything is priority one."
- **Reactive overload** — incident/support load crowding out investment work.
- **Knowledge concentration** — single points of failure; one person owns too much.
- **Structural mismatch** — team shape wrong for what it owns: too broad, too narrow, too coupled to adjacent teams (a Conway's Law problem).
- **Scaling threshold** — the team has crossed a size where the old structure stops working (~7–9+, and again past ~12–15), raising split/restructure questions.
- **Delivery risk** — scope creep, unclear priorities, slipping timelines.
- **Morale / attrition signals** — retro tone, disengagement, flight risk.

Focus on patterns that the evidence actually supports. Separate temporary load from persistent structure: remove known one-off incidents, migrations, or retiring systems from the steady-state picture where possible. Test competing explanations instead of treating correlated signals as causal; for example, check whether the same people handling incidents are also the review bottleneck. For a structural question, go deep on the one or two patterns that best explain the slowdown.

## Step 3: Research the diagnostic questions

Research in this order:

1. Turn the diagnostic questions into targeted research questions.
2. Use `ask_oreilly_experts` and/or `search_oreilly_content` as appropriate for the research need, following their tool descriptions.
3. Select only results that directly support a material finding or recommendation.
4. Draft from the verified evidence. If no directly relevant source surfaces, state the evidence gap instead of citing a weaker source.

One query per diagnostic question is a good rhythm. Examples:

- "signs a team has grown beyond its coordination mechanisms Team Topologies"
- "when to split an engineering team / team size thresholds"
- "team cognitive load and team API"
- "manager response when incident load crowds out investment work"
- "org structure and Conway's law when restructuring teams"
- "evaluating team velocity and delivery risk engineering manager"

Aim for a small set of sources covering the actual patterns, not a generic leadership bibliography. Useful anchors may include *Engineering Manager's Handbook*, *The Engineering Executive's Primer*, *Leading Effective Engineering Teams*, *Team Topologies*, *Platform Engineering*, and *Building Microservices*; cite them only if they surface and fit the evidence. Search the patterns the evidence actually shows. Do not force a named title into the assessment or omit a stronger result because it is unfamiliar.

Core org-design frameworks (Team Topologies, Conway's law) are durable reference points and don't need to be current to apply well. But leadership practice around remote/hybrid teams, scaling norms, and what "good" looks like shifts — where a newer book revisits the same pattern, prefer it over an older one covering the same ground.

## Step 4: Draft the assessment

Be direct — the leader needs to make decisions, not collect information. Keep it fairly brief. Use headers and bullets, but let findings breathe with a sentence of reasoning rather than bare bullets.

---

### [Team Name] — Assessment ([Date])

**Snapshot**
2–3 sentences on what the evidence shows, plainly. No hedging if the picture is clear.

**Findings**
For each (aim for 2–4 — more means you haven't prioritized):
- **[Finding / pattern name]** — what the team evidence shows and what practitioner guidance says about it. Cite the selected result following the source and citation rules above, then explain how the source applies.

**Recommended actions**
Give no more than three ranked interventions. Each should name the action, timing or owner when known, the hypothesis it tests, and its main trade-off. Prefer cheap, reversible interventions before a reorganization when they can distinguish a flow problem from a structural one. For a team-health assessment, make these priority actions for the near term rather than generic advice.

**Watch for**
- Name the leading and lagging indicators that would show improvement or deterioration.
- For a structural decision, state what observed threshold or result would change the recommendation.

---

## Step 5: Verify the assessment

Before responding:

1. Check that every finding maps to supplied team evidence and distinguishes steady-state signals from temporary noise.
2. Remove or label causal claims the evidence cannot support.
3. Confirm that actions are prioritized, specific, limited to three, and include a way to tell whether they worked.
4. Compare every citation with the MCP result — title, author, edition, and URL must match exactly — and remove any citation you cannot verify rather than repairing it. Prefer the newest applicable edition when sources cover the same ground.

If any check fails, revise the draft and run these checks again. Do not respond until all of them pass.

## Principles

Write as a thoughtful advisor. If evidence is thin, say so plainly rather than manufacturing confidence — a short honest read beats a padded one. Don't recap what the leader already told you; jump to interpretation. For structural questions, don't hide behind "it depends": name the most likely pattern and lead with the intervention you'd back, while being honest about what would change the call.

Prefer the newest applicable edition when sources cover the same practice; for durable organization-design frameworks, relevance may outrank recency.
