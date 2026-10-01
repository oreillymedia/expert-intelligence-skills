---
name: create-learning-plan
description: Creates a sequenced learning path from cited O'Reilly books, videos, courses, and live events, with practice activities and observable success markers. Use when the primary task is deciding what an individual or team should learn, in what order, and how to practice and demonstrate it—including curricula, study plans, career transitions, reading order, team skill development, and the learning track within onboarding. For a comprehensive 30-60-90 role ramp-up centered on stakeholder conversations, early contributions, and decisions to defer, use plan- domain-rampup.
---

# Learning Plan

Create a sequenced learning path with cited content, practice activities, and observable success markers. For a cohort, emphasize shared milestones and manager check-ins; for an individual, emphasize realistic pacing and transferable practice.

## Source and citation rules

Use only sources returned by the O'Reilly MCP tools. Tool names below are unqualified because the server name is user-configured; when the runtime requires qualified names, prepend the configured server name (for example, `oreilly:ask_oreilly_experts`). Cite each selected result as `[title](url) by authors`, using `product_title` when the result provides it instead of `title`. Copy the title and URL exactly from that same result; do not alter, normalize, shorten, repair, or reconstruct the URL, including its `orm_source=mcp` parameter. Use a string-valued `authors` field unchanged; for a list, join the returned names in order with commas. When `get_oreilly_citation` returns a fully rendered `citation_format`, use it unchanged. Preserve a returned live-event date, and never invent or reconstruct metadata, dates, or quotations. Remove a citation that cannot be verified against the tool result. Present uncited conclusions as your own analysis or omit them.

## Working checklist

Track this checklist while working; do not include it in the final deliverable.

- [ ] Frame the transition, audience, timeframe, and weekly capacity.
- [ ] Identify the competencies the transition requires.
- [ ] Research suitable books, videos or courses, and live events.
- [ ] Capture every selected source using its exact MCP citation.
- [ ] Sequence phases with a realistic workload.
- [ ] Give every phase a practice activity and observable success marker.
- [ ] Verify citations, event dates, editions, and `orm_source=mcp`.
- [ ] Remove redundant resources and recheck the time budget.

## Step 1: Frame the learning goal

Get clear on:

- **The transition** — from what, to what (senior → staff, backend → ML, new-hire → productive on our stack).
- **The timeframe** — 3 months, 6 months, a quarter of onboarding.
- **The audience** — designing for others (cohort/role) or for themselves.
- **Any constraints** — hours/week available, existing knowledge to skip, in-house priorities.

Ask one focused question only when the missing timeframe, audience, or available effort would materially change the sequence. Otherwise state a reasonable assumption.

## Step 2: Research across relevant content types

A good path mixes formats. Research in this order:

1. Turn the target competencies and transition needs into targeted questions.
2. Use `ask_oreilly_experts` and/or `search_oreilly_content` as appropriate for the research need, following their tool descriptions.
3. Select only results that directly support a phase, practice activity, or success marker.
4. Draft from the verified evidence. If no directly relevant source surfaces, state the evidence gap instead of citing a weaker source.

Useful queries include:

- Core reading: "best books on [skill/transition]" — the anchor texts.
- Practical depth: videos/courses for hands-on skills.
- **Live events:** set `content_types` to `['live-events']` and surface upcoming Superstreams/workshops that fit — always include their dates. If none are scheduled, just note that and rely on on-demand content.
- Topic-specific queries for each competency the transition requires (e.g., for senior→staff: "technical strategy," "influence without authority," "writing engineering strategy docs").

Search the competencies in the requested transition; do not force familiar titles into an unrelated path. Add the placement rationale after the unchanged citation rather than editing the citation itself.

A path someone follows for months should reflect current best thinking, not a superseded one. When an anchor text has a newer edition, or an author has since published a follow-up covering the same ground, sequence in the newer one — unless the transition specifically calls for the historical or original text.

## Step 3: Draft the learning path

Default to a **phased path**. If the user asks for a competency map or another structure, use that instead.

---

### Learning Path — [From] → [To] ([Timeframe])

**How this path works:** one or two sentences on the arc — what the early phase builds toward the later one, and roughly the weekly commitment assumed.

**Phase 1 — [name] (weeks X–Y)**
- **Read/watch (in order):** each item with a one-line why-this-now. Cite the selected result following the source and citation rules above, then explain why it belongs here.
- **Practice:** a concrete exercise that applies the material (write a strategy doc, run a design review, ship X).
- **Success markers:** observable evidence that the phase landed — not "understands strategy" but "has written and socialized one technical strategy document."

**Phase 2 — … / Phase 3 — …**
- Same shape, building on the last.

**Live & cohort touchpoints** *(if applicable)*
- Upcoming live events with dates; suggested manager/mentor check-ins for a cohort.

---

If a **competency map** is requested instead: organize by target competency (e.g., technical strategy, influence, execution, writing), mapping cited content + a practice + a success marker to each.

## Step 4: Verify the learning path

Before responding:

1. Check that the sequence fits the transition, timeframe, audience, and available hours.
2. Confirm that every phase or competency includes content, practice, and an observable success marker.
3. Compare every citation with the MCP result. The linked title, author, edition, URL, and live-event date must match exactly; every O'Reilly URL must be on `learning.oreilly.com` and retain `orm_source=mcp`.
4. Remove any citation whose exact metadata cannot be verified. Never repair it by guessing or synthesizing a URL.
5. Remove duplicate or excessive resources that make the plan unrealistic.

If any check fails, revise and run these checks again. Do not respond until all of them pass.

## Principles

Prefer the newest applicable edition. Sequence deliberately and explain why each item comes when it does. Keep the workload realistic, and make every success marker observable and behavioral.
