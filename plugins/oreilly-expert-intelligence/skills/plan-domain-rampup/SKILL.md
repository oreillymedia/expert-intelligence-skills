---
name: plan-domain-rampup
description: Creates a staged, role-specific ramp plan into an unfamiliar technical domain using cited O'Reilly domain fundamentals and onboarding guidance. Use when the primary task is planning a manager's or individual contributor's early effectiveness—typically over the first 90 days—including learning priorities, stakeholder and team discovery, early contributions, success markers, and decisions to defer. The plan may include assessing an inherited team as part of the ramp; for a standalone team-health diagnosis, use assess-team-structure, and for a primarily content-focused learning curriculum, use create-learning-plan.
---

# Ramp Plan

Create a role-specific 30-60-90 day ramp plan with domain learning, early contributions, decisions to defer, observable success markers, and ready-to-use conversation agendas. Keep manager ramps focused on people, ownership, and judgment; keep individual-contributor ramps focused on technical fluency and useful delivery.

## Source and citation rules

Use only sources returned by the O'Reilly MCP tools. Tool names below are unqualified because the server name is user-configured; when the runtime requires qualified names, prepend the configured server name (for example, `oreilly:ask_oreilly_experts`). Cite each selected result as `[title](url) by authors`, using `product_title` when the result provides it instead of `title`. Copy the title and URL exactly from that same result; do not alter, normalize, shorten, repair, or reconstruct the URL. Use a string-valued `authors` field unchanged; for a list, join the returned names in order with commas. When `get_oreilly_citation` returns a fully rendered `citation_format`, use it unchanged. Never invent or reconstruct metadata or quotations. Remove a citation that cannot be verified against the tool result. Present uncited conclusions as your own analysis or omit them.

## Step 1: Frame the transition

Get clear on:

- **The target domain** — what they're ramping into (data engineering, ML platform, security, payments…).
- **Their starting point** — what they already know that transfers, and the specific gap ("strong backend, no data-infra experience").
- **Their role in it** — managing the domain, or doing the work? This reshapes the whole plan.
- **Context** — team size and maturity if managing; timeline pressure; any early decision already looming.

Ask one focused question only when the role or domain is unclear. Otherwise proceed and label assumptions.

## Step 2: Research domain and transition tracks

Research in this order:

1. Turn the target-domain fundamentals and transition craft into targeted questions.
2. Use `ask_oreilly_experts` and/or `search_oreilly_content` as appropriate for the research need, following their tool descriptions.
3. Select only results that directly support a learning priority, conversation, deliverable, or decision to defer.
4. Draft from the verified evidence. If no directly relevant source surfaces, state the evidence gap instead of citing a weaker source.

Ramp plans need both the **domain fundamentals** and the **transition craft**. Search both:

*Domain track:*
- "fundamentals of [domain] — core concepts a newcomer must understand"
- "[domain] common architecture / tooling / failure modes"
- "what every [domain] practitioner should know"

*Transition track:*
- "manager's first 90 days new team best practices" (if managing)
- "onboarding into a new technical domain effectively" (if an individual contributor)
- "early decisions new managers get wrong"

Search the user's actual domain and transition rather than forcing generic onboarding or familiar domain titles.

How much recency matters depends on the domain: a fast-moving one (ML infrastructure, AI tooling, security) needs the newest coverage you can find, since the fundamentals themselves are still shifting; a more settled one (relational databases, core distributed-systems theory) can lean on an older, well-established text without losing accuracy. Judge which case you're in before defaulting to "newer is better."

## Step 3: Draft the ramp plan

Structure it as three phases with a clear intent for each, then the agendas. Keep each item concrete — a plan someone can act on Monday.

---

### 30-60-90 Ramp Plan — [Role] into [Domain]

**The shape of this ramp:** one or two sentences on the strategy — e.g., "You're managing, not doing, so days 1–30 are about understanding what the team owns and who holds what, not learning to write Spark jobs."

**Days 1–30 — Learn & listen**
- **Learn:** the specific concepts or tools to become fluent in. Cite the selected result following the source and citation rules above and give a concrete scope, such as selected chapters or modules, only when the returned evidence supports it.
- **Conversations:** who to talk to and what to ask.
- **Avoid:** the early decisions/mistakes to *not* make yet, and why.

**Days 31–60 — Contribute & align**
- Learn / Conversations / Deliver (the first real contribution or decision) / Avoid.

**Days 61–90 — Own & set direction**
- Learn / Deliver / Decide (what should now be yours to call).

**Success markers**
- What "ramped" looks like at each phase — observable, not vibes.

### Conversation agendas

Provide ready-to-use agendas for the 2–4 highest-leverage early conversations — e.g., first team 1:1s, a "how does this system actually work" session with the tech lead, a stakeholder alignment. For each: who, when in the plan, and 3–5 specific questions or talking points.

---

## Step 4: Verify the ramp plan

Before responding:

1. Check that activities fit the role, starting point, domain, and 90-day horizon.
2. Confirm that each phase builds on the previous one and includes observable success markers.
3. Compare every citation with the MCP result — title, author, edition, and URL must match exactly — and remove any citation you cannot verify rather than repairing it.
4. Remove unrealistic learning goals or decisions that require expertise the user cannot build in the period.

If any check fails, revise and run these checks again. Do not respond until all of them pass.

## Principles

Prefer the newest applicable edition for fast-moving domains; for durable fundamentals, relevance may outrank recency. The goal is useful competence and sound judgment about what to defer, not mastery in 90 days. Keep manager and individual-contributor ramps materially different.
