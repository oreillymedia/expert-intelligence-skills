---
name: forecast-project-delivery
description: Forecasts a realistic delivery range from a backlog, design document, or scope description using cited O'Reilly estimation and risk frameworks. Use for project estimates, deadline feasibility, timeline commitments, or schedule-risk reviews; not for diagnosing general team health or recommending a technical architecture.
---

# Delivery Forecast

Produce a delivery range with explicit assumptions, ranked schedule drivers, and concrete ways to narrow or compress the range. Avoid a bare single-date estimate; show how uncertainty changes the commitment.

## Source and citation rules

Use only sources returned by the O'Reilly MCP tools. Tool names below are unqualified because the server name is user-configured; when the runtime requires qualified names, prepend the configured server name (for example, `oreilly:ask_oreilly_experts`). Cite each selected result as `[title](url) by authors`, using `product_title` when the result provides it instead of `title`. Copy the title and URL exactly from that same result; do not alter, normalize, shorten, repair, or reconstruct the URL. Use a string-valued `authors` field unchanged; for a list, join the returned names in order with commas. When `get_oreilly_citation` returns a fully rendered `citation_format`, use it unchanged. Never invent or reconstruct metadata or quotations. Remove a citation that cannot be verified against the tool result. Present uncited conclusions as your own analysis or omit them.

## Working checklist

Track this checklist while working; do not include it in the final deliverable.

- [ ] Separate known facts, assumptions, and unknowns.
- [ ] Normalize effort and capacity into consistent units.
- [ ] Calculate best, likely, and worst cases from the same assumptions.
- [ ] Add calendar dependencies and external queues.
- [ ] Cross-check the arithmetic against the stated deadline.
- [ ] Rank schedule drivers by impact.
- [ ] Tie each lever to a driver and quantify its likely effect.
- [ ] State what new evidence would narrow the range.

## Step 1: Frame the forecast from available evidence

Work from whatever the user has:

- Backlog / ticket list / epics (count, size distribution, how well-defined)
- Design doc, RFC, or architecture sketch
- Team size, seniority, and how much is new vs. familiar territory
- Hard constraints — deadlines, dependencies, people splitting time across work
- Known unknowns the team has already flagged

Use connected Jira, Linear, or GitHub tools when available and authorized. Ask one focused question only when the missing information prevents a meaningful range. Otherwise proceed with explicit assumptions and widen confidence accordingly.

## Step 2: Identify the schedule drivers

Before searching, identify what will actually move the timeline. Classic drivers:

- **Requirements instability** — scope still shifting, unclear acceptance criteria.
- **Unknowns / research work** — pieces the team has never done (new infra, migration, integration).
- **Dependencies** — waiting on other teams, vendors, approvals.
- **Optimism / anchoring** — the plan assumes everything goes right; no buffer for the normal failure rate.
- **Thin definition** — vague tickets that will each expand once picked up.
- **Coordination overhead** — more people ≠ proportionally faster (Brooks's Law territory).

The riskiest items dominate the range, so weight them.

## Step 3: Research the estimation method and schedule drivers

Research in this order:

1. Turn the estimation method and highest-ranked schedule drivers into targeted questions.
2. Use `ask_oreilly_experts` and/or `search_oreilly_content` as appropriate for the research need, following their tool descriptions.
3. Select only results that directly support a forecast range, schedule driver, or delivery lever.
4. Draft from the verified evidence. If no directly relevant source surfaces, state the evidence gap instead of citing a weaker source.

Use queries such as:

- "realistic software project estimation cone of uncertainty ranges"
- "biggest software schedule risks and how to manage them"
- "estimating software-intensive systems sizing methods"
- "identifying and managing project risk software"
- "why software estimates are optimistic and how to correct"

Durable estimation frameworks may be older; for technology-specific migration or delivery risks, prefer current coverage. Cite only what surfaces and fits the forecast.

The core theory here (the cone of uncertainty, why estimates run optimistic, classic schedule-driver categories) is durable — a decades-old classic can still be the right citation. But when a schedule driver is tied to a specific technology or practice (e.g., risks of a particular migration, platform, or way of working), prefer the newest treatment of that specific, since ecosystem-specific failure modes shift faster than the underlying psychology of estimation.

## Step 4: Draft the forecast

Keep it tight and decision-oriented. Structure:

---

### [Project] — Delivery Forecast

**Estimate**
- **Best case:** [X] — if the known unknowns resolve cleanly.
- **Most likely:** [Y] — the number to plan around.
- **Worst case:** [Z] — if the top risks materialize.
- **Confidence:** [Low/Medium/High], and why. Note where you are on the cone of uncertainty (thin tickets + unresolved design = wide cone).

**What drives the spread** (the risks, ranked)
- **[Schedule driver]** — why it matters, roughly how much time it could add, and the early signal that it is materializing. Cite the selected result following the source and citation rules above, then explain how the source applies.

**Trade-offs / levers**
- What could compress the range — cutting a specific piece of scope, resolving a design question first, removing a dependency. Be concrete.

**Bottom line**
- One or two plain sentences: what the range means for committing (e.g., "the likely case fits this half, but only if the data migration is de-risked first; as scoped, treat the worst case as realistic").

---

## Step 5: Verify the forecast

Before responding:

1. Confirm that the estimate is a range and that its assumptions and confidence match the available evidence.
2. Check that the ranked risks explain the spread and that each proposed lever addresses a named risk.
3. Compare every citation with the MCP result — title, author, edition, and URL must match exactly — and remove any citation you cannot verify rather than repairing it.
4. If the evidence is too thin for a useful range, replace false precision with the next evidence needed to narrow it.

If any check fails, revise and run these checks again. Do not respond until all of them pass.

## Principles

Never give a bare single number: the range and its assumptions are the information. Prefer the newest applicable edition when sources cover the same practice.

Be honest when the input is too thin to estimate well: say what you'd need (clearer tickets, a spiked design) to narrow the cone, rather than producing a confident-looking guess. A leader can act on "I can't estimate this until X is defined" — that's a finding, not a failure.
