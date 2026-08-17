---
name: plan-service-reliability
description: Draft a practical reliability strategy for a new or evolving service — SLIs, SLO targets, an error-budget policy, how to handle the rollout period with no historical data, and how to negotiate all of it with product and customer teams — grounded in and cited to O'Reilly's SRE literature. Use this skill whenever someone is launching or maturing a service and needs SLOs, error budgets, a reliability plan, or help getting reliability targets agreed with stakeholders. Trigger on prompts like "draft an SLO framework for our new payments service," "how do we set error budgets with no historical data," "help me define reliability targets for X," or "how do I negotiate SLOs with product" — even a short description of the service is enough to start.
---

# Reliability Plan

You're helping a team define what "reliable enough" means for a service and get everyone to agree to it — before launch, when there's no data, and when product and customers all want different things. The output lands as "this is how mature reliability orgs do it," which is what shortens the stakeholder argument.

Two hard parts recur. First, the **no-history problem**: you can't measure your way to a target for a service that hasn't run, so the first SLOs are aspirational and explicitly provisional. Second, the **negotiation**: SLOs are a cross-team agreement, not a purely technical artifact, so the plan has to be defensible to product and customer-facing teams, not just to engineers.

## Step 1: Confirm scope and the service shape

Get clear on:

- **The service and its role** — what it does, who depends on it, what "failure" means to a user (a slow checkout is different from a wrong balance).
- **Its criticality** — user-facing and revenue-critical, or internal and best-effort? This sets how tight the targets should be.
- **Where they are** — pre-launch (no data), or evolving an existing service (some data)?
- **What they want from you** — confirm the deliverable, since this varies: a **full SLO framework draft** (proposed SLIs, candidate targets, error-budget policy, rollout plan, negotiation guide) or a lighter **methodology + approach**. If unclear, ask: "Want a full draft SLO framework you can take to stakeholders, or the method and I'll leave the specific numbers to you?"

## Step 2: Query the O'Reilly MCP

Use `ask_oreilly_experts` and `search_oreilly_content` across the sub-problems:

- "choosing SLIs that reflect user experience"
- "setting SLO targets without historical data aspirational SLOs"
- "error budget policy — what happens when it's spent"
- "negotiating SLOs / getting buy-in from product and stakeholders"
- "handling the rollout period for a new service reliability"

Pull `get_oreilly_citation` on strong hits (≥0.75). Anchors that tend to serve well (a guide — cite what actually surfaces): *Implementing Service Level Objectives* (Hidalgo — strong on "what to do without a history" and "getting buy-in"), *Site Reliability Engineering* (Google SRE book — error budgets), *SLO Adoption and Usage in SRE* (Forsgren), *The Site Reliability Workbook*.

SRE practice keeps maturing past the original SRE book's framing — later titles build on it with sharper guidance on adoption tactics, target-setting, and negotiation. When a newer source covers the same ground as an older one, prefer the newer; the core vocabulary (error budgets, SLIs/SLOs) is stable, but the practice of applying it has moved on.

## Step 3: Write the plan

If producing the full framework, use this structure. Mark every target as a **starting point to refine with data**, not a commitment.

---

### Reliability Plan — [Service]

**What reliability means here**
- One or two sentences: the user-visible failures this plan is protecting against.

**Proposed SLIs**
- The 2–4 signals worth measuring (availability, latency at p99, correctness, freshness…), each tied to a user experience. Cite the reasoning.

**Candidate SLO targets** *(starting points — refine with data)*
- For each SLI, an initial target or range grounded in expert guidance and the service's criticality (e.g., "99.9% availability as a starting target; tighten or relax after 4–6 weeks of real data"). Be explicit that these are negotiable, not promises. *[Implementing Service Level Objectives](url) by Alex Hidalgo recommends…*

**Error-budget policy**
- What the budget is, and what happens when it's burning too fast or spent (freeze features, shift to reliability work). The policy is the teeth — spell out the agreed consequence.

**Rollout with no history**
- How to start without data: begin aspirational, instrument first, set a review checkpoint to recalibrate, and don't over-commit early. Cite the approach.

**Negotiating with product & customer teams**
- How to frame the conversation, what trade-off to make explicit (more reliability = less feature velocity), and how to reach a number everyone signs. Cite the buy-in guidance.

---

If producing methodology only, cover the same reasoning without fixing specific numbers.

## Principles

Cite as markdown links with author; cite only what surfaced — never invent a title, author, or link. When the platform carries multiple editions of a title, use the newest edition unless the user specifically needs an older one. Always frame proposed targets as provisional starting points, because SLOs presented as firm before there's data create commitments the team can't honor and erode trust in the whole framework. Keep the negotiation angle front and center — a technically perfect SLO no stakeholder agreed to is useless.
