---
name: forecast-project-delivery
description: Pressure-test a plan before the team commits — turn a backlog, design doc, or scope description into a realistic duration range, the schedule risks that drive it, and the trade-offs, all grounded in expert delivery and estimation frameworks from O'Reilly. Use this skill whenever someone asks how long something will really take, wants a project estimate or timeline, is deciding whether to commit a team to scoping, or asks about delivery/schedule risk. Trigger on prompts like "estimate how long this will take," "given this backlog and design doc, what's a realistic duration and the biggest risks," "can we ship this by Q3," or "what are the schedule risks here" — even a rough scope description in a couple sentences is enough to start.
---

# Delivery Forecast

You're helping someone decide whether a plan is worth committing to — before they burn weeks scoping it or promise a date they can't hit. The output is a realistic duration *range*, the specific risks that widen that range, and an honest read on what it means for committing.

The trap in estimation is false precision. A single confident number is almost always wrong and usually optimistic. What a leader actually needs is the shape of the uncertainty — "likely 4–6 months, but 9+ if the data-migration piece is as bad as it looks" — because that's what lets them decide. As McConnell puts it, early estimates live inside a cone of uncertainty that only narrows as work is done; your job is to make that cone visible, not to pretend it away.

## Step 1: Gather the scope evidence

Work from whatever the user has:

- Backlog / ticket list / epics (count, size distribution, how well-defined)
- Design doc, RFC, or architecture sketch
- Team size, seniority, and how much is new vs. familiar territory
- Hard constraints — deadlines, dependencies, people splitting time across work
- Known unknowns the team has already flagged

If connected tools exist (Jira, Linear, GitHub), offer to pull the backlog directly. If scope is vague, ask one focused question — usually "What's the biggest piece of unknown work in here?" — since that's what dominates the estimate.

## Step 2: Find the schedule-risk drivers

Before searching, identify what will actually move the timeline. Classic drivers:

- **Requirements instability** — scope still shifting, unclear acceptance criteria.
- **Unknowns / research work** — pieces the team has never done (new infra, migration, integration).
- **Dependencies** — waiting on other teams, vendors, approvals.
- **Optimism / anchoring** — the plan assumes everything goes right; no buffer for the normal failure rate.
- **Thin definition** — vague tickets that will each expand once picked up.
- **Coordination overhead** — more people ≠ proportionally faster (Brooks's Law territory).

The riskiest items dominate the range, so weight them.

## Step 3: Query the O'Reilly MCP

Use `ask_oreilly_experts` and `search_oreilly_content` to ground both the estimation method and the risk read:

- "realistic software project estimation cone of uncertainty ranges"
- "biggest software schedule risks and how to manage them"
- "estimating software-intensive systems sizing methods"
- "identifying and managing project risk software"
- "why software estimates are optimistic and how to correct"

Pull `get_oreilly_citation` on strong hits (≥0.75). Anchors that tend to serve well (a guide — cite what surfaces): *Rapid Development: Taming Wild Software Schedules* (McConnell), *Estimating Software-Intensive Systems* (Stutzke), *Identifying and Managing Project Risk* (Kendrick), and *Waltzing with Bears* (DeMarco & Lister) on risk. Cite whatever actually ranks for the specific situation.

The core theory here (the cone of uncertainty, why estimates run optimistic, classic risk-driver categories) is durable — a decades-old classic can still be the right citation. But when a risk driver is tied to a specific technology or practice (e.g., risks of a particular migration, platform, or way of working), prefer the newest treatment of that specific, since ecosystem-specific failure modes shift faster than the underlying psychology of estimation.

## Step 4: Write the forecast

Keep it tight and decision-oriented. Structure:

---

### [Project] — Delivery Forecast

**Estimate**
- **Best case:** [X] — if the known unknowns resolve cleanly.
- **Most likely:** [Y] — the number to plan around.
- **Worst case:** [Z] — if the top risks materialize.
- **Confidence:** [Low/Medium/High], and why. Note where you are on the cone of uncertainty (thin tickets + unresolved design = wide cone).

**What drives the spread** (the risks, ranked)
- **[Risk]** — why it matters, roughly how much time it could add, and the early signal that it's happening. Cite the framework: *[Rapid Development](url) by Steve McConnell classifies this as…*.

**Trade-offs / levers**
- What could compress the range — cutting a specific piece of scope, resolving a design question first, removing a dependency. Be concrete.

**Bottom line**
- One or two plain sentences: what the range means for committing (e.g., "the likely case fits this half, but only if the data migration is de-risked first; as scoped, treat the worst case as realistic").

---

## Principles

Never give a bare single number — always a range, because the range *is* the information. Cite only sources that actually surfaced; never invent a title, author, or link. Use markdown links with author for citations. When the platform carries multiple editions of a title, use the newest edition unless the user specifically needs an older one.

Be honest when the input is too thin to estimate well: say what you'd need (clearer tickets, a spiked design) to narrow the cone, rather than producing a confident-looking guess. A leader can act on "I can't estimate this until X is defined" — that's a finding, not a failure.
