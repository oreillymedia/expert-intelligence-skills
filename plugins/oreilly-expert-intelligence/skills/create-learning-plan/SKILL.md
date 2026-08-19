---
name: create-learning-plan
description: Turn a skill or career goal into a credible, sequenced learning path — ordering O'Reilly books, videos, courses, and live events into phases with practice exercises and observable "what good looks like" markers. Works for an L&D lead designing a path for a cohort or role, or an individual planning their own transition. Use this skill whenever someone wants a learning path, curriculum, reading order, study plan, skill-up roadmap, or "how do I get from X to Y" development plan — e.g. senior-to-staff, IC-to-manager, or ramping a team on a new technology. Trigger on prompts like "build a 6-month learning path for engineers moving toward staff level," "what should my team read to learn X and in what order," or "design a curriculum for Y" — including when they just describe the transition and the timeframe.
---

# Create Learning Plan

You're building a learning path someone will actually trust and follow — one that sequences real expert content in a sensible order, gives people something to *practice* (not just read), and defines what progress looks like at each stage. The credibility comes from citing the sources practitioners already respect; the usefulness comes from the sequencing and the success markers.

Two audiences, same engine. An **L&D lead** is designing for a cohort or role and needs a path that's defensible and measurable. An **individual** is planning their own transition and needs a realistic order and clear milestones. Detect which from the prompt and tune accordingly — a cohort path leans harder on success markers and manager check-ins; a self-directed path leans on realistic pacing.

## Step 1: Establish the goal and the shape

Get clear on:

- **The transition** — from what, to what (senior → staff, backend → ML, new-hire → productive on our stack).
- **The timeframe** — 3 months, 6 months, a quarter of onboarding.
- **The audience** — designing for others (cohort/role) or for themselves.
- **Any constraints** — hours/week available, existing knowledge to skip, in-house priorities.

If timeframe or audience is unclear, ask one quick question — both shape the pacing and emphasis.

## Step 2: Query the O'Reilly MCP — across content types

A good path mixes formats. Use `search_oreilly_content` with `content_types` and `ask_oreilly_experts`:

- Core reading: "best books on [skill/transition]" — the anchor texts.
- Practical depth: videos/courses for hands-on skills.
- **Live events:** set `content_types` to `['live-events']` and surface upcoming Superstreams/workshops that fit — always include their dates. If none are scheduled, just note that and rely on on-demand content.
- Topic-specific queries for each competency the transition requires (e.g., for senior→staff: "technical strategy," "influence without authority," "writing engineering strategy docs").

Pull `get_oreilly_citation` on strong hits (≥0.75) when you want to justify placement. Anchors that tend to serve well for senior→staff (a guide — cite what actually surfaces): *The Staff Engineer's Path* (Reilly), *The Effective Software Engineer* (Osmani), *The Software Engineer's Guidebook* (Orosz). Use the right sources for whatever transition is in play.

A path someone follows for months should reflect current best thinking, not a superseded one. When an anchor text has a newer edition, or an author has since published a follow-up covering the same ground, sequence in the newer one — unless the transition specifically calls for the historical or original text.

## Step 3: Write the path

Default to a **phased path**. If the user asks for a competency map or another structure, use that instead.

---

### Learning Path — [From] → [To] ([Timeframe])

**How this path works:** one or two sentences on the arc — what the early phase builds toward the later one, and roughly the weekly commitment assumed.

**Phase 1 — [name] (weeks X–Y)**
- **Read/watch (in order):** each item with a one-line why-this-now, cited. *[The Staff Engineer's Path](url) by Tanya Reilly — start here for the scope of the role.*
- **Practice:** a concrete exercise that applies the material (write a strategy doc, run a design review, ship X).
- **What good looks like:** observable markers that this phase landed — not "understands strategy" but "has written and socialized one technical strategy doc."

**Phase 2 — … / Phase 3 — …**
- Same shape, building on the last.

**Live & cohort touchpoints** *(if applicable)*
- Upcoming live events with dates; suggested manager/mentor check-ins for a cohort.

---

If a **competency map** is requested instead: organize by target competency (e.g., technical strategy, influence, execution, writing), mapping cited content + a practice + a success marker to each.

## Principles

Cite as markdown links with author; cite only what surfaced — never invent a title, author, link, or event date. When the platform carries multiple editions of a title, use the newest edition unless the user specifically needs an older one. Sequence deliberately: say *why* each item comes when it does, because the order is the value a reading list alone doesn't provide. Make success markers observable and behavioral so a leader can actually tell if someone's progressing. Be realistic about pace given the stated hours — an over-stuffed path that no one finishes isn't credible. Where live events are included, verify dates from the MCP and never invent a schedule.
