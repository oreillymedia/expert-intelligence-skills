---
name: plan-service-reliability
description: Creates a user-centered service reliability and SLO operating plan using cited O'Reilly SRE sources. Use when the primary task is defining or revising SLIs, candidate SLO targets, error-budget policy, degraded or fallback behavior, adoption steps, or stakeholder agreement for a service—with or without historical data. Incidents, performance problems, and architectural constraints may inform the plan. Not intended for real-time incident response or standalone performance diagnosis; use compare-implementation-approaches to choose among bounded remediation options and review-architecture-decision for system-level architecture trade-offs.
---

# Reliability Plan

Produce a user-centered reliability plan with SLIs, provisional SLO targets, an error-budget policy, fallback behavior, rollout steps, and a path to stakeholder agreement. Treat no-history targets as starting points to recalibrate, not commitments.

## Source and citation rules

Use only sources returned by the O'Reilly MCP tools. Tool names below are unqualified because the server name is user-configured; when the runtime requires qualified names, prepend the configured server name (for example, `oreilly:ask_oreilly_experts`). Cite each selected result as `[title](url) by authors`, using `product_title` when the result provides it instead of `title`. Copy the title and URL exactly from that same result; do not alter, normalize, shorten, repair, or reconstruct the URL. Use a string-valued `authors` field unchanged; for a list, join the returned names in order with commas. When `get_oreilly_citation` returns a fully rendered `citation_format`, use it unchanged. Never invent or reconstruct metadata or quotations. Remove a citation that cannot be verified against the tool result. Present uncited conclusions as your own analysis or omit them.

## Step 1: Frame reliability in user terms

Get clear on:

- **The service and its role** — what it does, who depends on it, what "failure" means to a user (a slow checkout is different from a wrong balance).
- **Its criticality** — user-facing and revenue-critical, or internal and best-effort? This sets how tight the targets should be.
- **Where they are** — pre-launch (no data), or evolving an existing service (some data)?
- **Degraded behavior** — caches, fallbacks, fail-open/fail-closed choices, and the maximum duration or staleness users can safely tolerate.
- **Hard dependencies** — the systems whose availability or latency sets an architectural ceiling.
- **The requested deliverable** — use a full SLO framework draft by default (proposed SLIs, candidate targets, error-budget policy, rollout plan, negotiation guide). Use a lighter methodology-only response when the user asks for one.

Separate availability failures from correctness or freshness failures. A cache may make a short outage invisible while allowing dangerously stale behavior later; the SLIs and safeguards must reflect that difference. Ask one focused question only when a missing fact would materially change the targets or fallback policy. Otherwise state the assumption.

## Step 2: Research the reliability decisions

Research in this order:

1. Turn the SLIs, targets, error budgets, rollout, and negotiation or fallback decisions into targeted questions.
2. Use `ask_oreilly_experts` and/or `search_oreilly_content` as appropriate for the research need, following their tool descriptions.
3. Select only results that directly support a target, policy, fallback, or rollout choice.
4. Draft from the verified evidence. If no directly relevant source surfaces, state the evidence gap instead of citing a weaker source.

Research across the sub-problems:

- "choosing SLIs that reflect user experience"
- "setting SLO targets without historical data aspirational SLOs"
- "error budget policy — what happens when it's spent"
- "negotiating SLOs / getting buy-in from product and stakeholders"
- "handling the rollout period for a new service reliability"

Useful anchors may include *Implementing Service Level Objectives*, *Site Reliability Engineering*, *SLO Adoption and Usage in SRE*, and *The Site Reliability Workbook*; cite only what surfaces and applies. Search the service's actual reliability problems. Do not force a named title into the plan or omit a stronger result because it is unfamiliar.

SRE practice keeps maturing past the original SRE book's framing — later titles build on it with sharper guidance on adoption tactics, target-setting, and negotiation. When a newer source covers the same ground as an older one, prefer the newer; the core vocabulary (error budgets, SLIs/SLOs) is stable, but the practice of applying it has moved on.

## Step 3: Draft the reliability plan

If producing the full framework, use this structure. Mark every target as a **starting point to refine with data**, not a commitment.

---

### Reliability Plan — [Service]

**What reliability means here**
- One or two sentences: the user-visible failures this plan is protecting against.

**Proposed SLIs**
- Use two to four signals tied to user outcomes. Prefer threshold-based request SLIs over raw percentile reporting, and measure at the point that observes the real experience. When client and server views can diverge, name both and say which governs the SLO.

**Candidate SLO targets** *(starting points — refine with data)*
- For each SLI, give an initial target or range grounded in criticality, load-test evidence, dependent-service needs, and hard-dependency ceilings. Label every no-history target **provisional** with a dated recalibration point.
- When caching or graceful degradation masks short outages, consider a maximum-outage-duration objective alongside aggregate availability.
- Treat a zero-tolerance safety boundary, such as never serving data beyond a dangerous staleness limit, as an enforced invariant rather than an error-budget percentage. Define fallback behavior by workload class when the safe direction differs.

**Error-budget policy**
- State the budget, at least one fast-burn trigger, the action when it is burning too quickly, and the consequence when it is spent. Scope freezes to the service causing the burn rather than its consumers unless the evidence requires otherwise. Name who can approve exceptions.

**Rollout with no history**
- Instrument first, onboard in small tranches, test the fallback path, observe before enforcing provisional targets, and schedule a dated recalibration. Do not onboard every dependent service at once when staged learning is possible.

**Negotiating with product & customer teams**
- How to frame the conversation, what trade-off to make explicit (more reliability = less feature velocity), and how to reach a number everyone signs. Cite the buy-in guidance.

---

If producing methodology only, cover the same reasoning without fixing specific numbers.

## Step 4: Verify the reliability plan

Before responding:

1. Check that every SLI maps to a user-visible outcome and that correctness, freshness, and availability are not conflated.
2. Confirm that every no-history target is provisional, while true safety invariants are enforced separately and have explicit fallback behavior.
3. Confirm that the error-budget policy has fast-burn and exhausted-budget actions, and that rollout includes staged onboarding, fallback testing, and a dated review.
4. Compare every citation with the MCP result — title, author, edition, and URL must match exactly — and remove any citation you cannot verify rather than repairing it. Remove unsupported precision.

If any check fails, revise and run these checks again. Do not respond until all of them pass.

## Principles

Prefer the newest applicable treatment when sources cover the same practice. Keep the plan decision-sized: enough operational detail to act, without turning the default response into an SRE handbook. A technically elegant SLO that users, product, developers, and on-call owners did not agree to is not usable.
