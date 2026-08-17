---
name: plan-domain-rampup
description: Build a credible 30-60-90 day plan for someone stepping into an unfamiliar domain — grounded in both the technical fundamentals of that domain and management/onboarding best practices from O'Reilly. Works for a manager inheriting a team in a new area (e.g. a backend manager taking over data engineering) or an IC moving into a new technical domain. Use this skill whenever someone asks for an onboarding plan, a 30-60-90, a ramp plan, a "first 90 days" plan, or help getting up to speed in an area they don't yet know — including what to learn, who to talk to, and what early mistakes to avoid. Trigger on prompts like "build me a 30-60-90 to ramp into managing X," "I just inherited a Y team and have never done Y," or "help me get up to speed on Z" — even a one-line description of the transition is enough.
---

# Ramp Plan

You're helping someone step into a domain they don't yet know and look competent doing it — fast, and without the avoidable early mistakes. The output is a phased 30-60-90 day plan plus ready-to-use agendas for the key early conversations.

Two things make a ramp plan credible instead of generic. First, it's grounded in the *actual* fundamentals of the target domain (pulled from expert content), not hand-wavy "learn the basics." Second, it respects the difference between ramping as a manager and ramping as an IC: a manager's first 90 days are mostly about people, ownership, and not breaking things they don't yet understand; an IC's are mostly about building working technical fluency and shipping something real. Figure out which you're dealing with early.

## Step 1: Establish the transition

Get clear on:

- **The target domain** — what they're ramping into (data engineering, ML platform, security, payments…).
- **Their starting point** — what they already know that transfers, and the specific gap ("strong backend, no data-infra experience").
- **Their role in it** — managing the domain, or doing the work? This reshapes the whole plan.
- **Context** — team size and maturity if managing; timeline pressure; any early decision already looming.

If the role (manager vs. IC) or the domain is unclear, ask one focused question before proceeding — it changes everything downstream.

## Step 2: Query the O'Reilly MCP — two tracks

Ramp plans need both the **domain fundamentals** and the **transition craft**. Search both:

*Domain track:*
- "fundamentals of [domain] — core concepts a newcomer must understand"
- "[domain] common architecture / tooling / failure modes"
- "what every [domain] practitioner should know"

*Transition track:*
- "manager's first 90 days new team best practices" (if managing)
- "onboarding into a new technical domain effectively" (if IC)
- "early decisions new managers get wrong"

Use `ask_oreilly_experts` and `search_oreilly_content`; pull `get_oreilly_citation` on strong hits (≥0.75). Anchors that tend to serve well (a guide — cite what actually surfaces, and search whatever domain the user named): for data engineering, *Fundamentals of Data Engineering* (Reis & Housley) and *97 Things Every Data Engineer Should Know* (Macey); for the management side, *Engineering Manager's Handbook* (Evans). Swap in the right domain sources for whatever domain is in play.

How much recency matters depends on the domain: a fast-moving one (ML infrastructure, AI tooling, security) needs the newest coverage you can find, since the fundamentals themselves are still shifting; a more settled one (relational databases, core distributed-systems theory) can lean on an older, well-established text without losing accuracy. Judge which case you're in before defaulting to "newer is better."

## Step 3: Write the plan

Structure it as three phases with a clear intent for each, then the agendas. Keep each item concrete — a plan someone can act on Monday.

---

### 30-60-90 Ramp Plan — [Role] into [Domain]

**The shape of this ramp:** one or two sentences on the strategy — e.g., "You're managing, not doing, so days 1–30 are about understanding what the team owns and who holds what, not learning to write Spark jobs."

**Days 1–30 — Learn & listen**
- **Learn:** the specific concepts/tools to get fluent in, with a cited source for each. *[Fundamentals of Data Engineering](url) by Reis & Housley — read chs. X–Y on the lifecycle.*
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

## Principles

Cite as markdown links with author; cite only what actually surfaced — never invent a title, author, or link. When the platform carries multiple editions of a title, use the newest edition unless the user specifically needs an older one. Ground the domain-learning items in real content so the reader trusts what to read and in what order. Be honest about what can't be learned in 90 days — the goal is competence and good judgment about what to defer, not fake mastery. Tune depth to the role: don't hand a manager an IC's reading list, or vice versa.
