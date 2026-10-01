---
name: review-technical-proposal
description: Reviews a submitted or described technical proposal against cited O'Reilly practitioner sources, identifying strengths, unsupported claims, hidden assumptions, underestimated risks, material omissions, and specific questions needed before approval. Use when the primary task is evaluating the proposal's overall justification and readiness, whether it is presented as an RFC, technical specification, ADR, design proposal, migration plan, or informal description. Architecture trade-offs may be part of the review; for an organization-level adoption recommendation, use create-decision-brief, and for evaluation centered on the underlying system-design choices, use review-architecture-decision.
---

# Technical Proposal Review

Review a submitted technical proposal for strengths, unsupported claims, underestimated risks, and material unanswered questions. Evaluate the document in front of you rather than replacing it with a new design.

## Source and citation rules

Use only sources returned by the O'Reilly MCP tools. Tool names below are unqualified because the server name is user-configured; when the runtime requires qualified names, prepend the configured server name (for example, `oreilly:ask_oreilly_experts`). Cite each selected result as `[title](url) by authors`, using `product_title` when the result provides it instead of `title`. Copy the title and URL exactly from that same result; do not alter, normalize, shorten, repair, or reconstruct the URL. Use a string-valued `authors` field unchanged; for a list, join the returned names in order with commas. When `get_oreilly_citation` returns a fully rendered `citation_format`, use it unchanged. Never invent or reconstruct metadata or quotations. Remove a citation that cannot be verified against the tool result. Present uncited conclusions as your own analysis or omit them.

## Step 1: Map the proposal's claims and omissions

Extract from the document:

- **The decision/change proposed** and the motivation.
- **The claims** — what the author asserts will be true (benefits, effort, risks handled).
- **The assumptions** — often unstated: that the team has capacity, that the migration is reversible, that the new dependency is operable, that adoption will be smooth.
- **The gaps** — what a proposal like this usually needs to address but this one skips (rollback, operational cost, security, org readiness, the "day 2" story).

If no document is attached but the user describes a proposal, work from the description and say what you're inferring.

## Step 2: Research the practitioner evidence

Research in this order:

1. Turn the proposal's claims, assumptions, and adoption or operations gaps into targeted questions.
2. Use `ask_oreilly_experts` and/or `search_oreilly_content` as appropriate for the research need, following their tool descriptions.
3. Select only results that directly support a strength, gap, or pushback question.
4. Draft from the verified evidence. If no directly relevant source surfaces, state the evidence gap instead of citing a weaker source.

Search for what experienced teams have learned about *this kind* of proposal — especially the adoption realities and things that get underestimated:

- "[technology/change] adoption trade-offs — what teams underestimate"
- "when NOT to adopt [X] / [X] anti-patterns"
- "operational cost / day-2 realities of [X]"
- "[X] migration risks and how to de-risk"

Search the proposal's actual technology, adoption pattern, and claims; do not force a familiar title into the review.

What a proposal like this "usually gets wrong" shifts as an ecosystem matures — tooling improves, known rough edges get fixed, and new ones emerge. When sources on the same adoption pattern differ mainly in age, prefer the newer one so the pushback questions reflect the technology's current state, not problems it solved two years ago.

## Step 3: Draft the review

Use the structure below. Rank findings by decision impact and consolidate related symptoms under their shared cause. By default, cover the three to five gaps most likely to change approval, rollout safety, or ongoing ownership; do not inventory every plausible omission. The pushback questions are the payload, but each should earn its place by testing a material claim or closing a material gap.

---

### Review — [Proposal Title]

**What it handles well**
- Credit the proposal's strongest one or two choices briefly; cite where the approach matches expert guidance.

**What it underestimates**
- For each ranked gap, state the proposal claim or omission, the evidence, and the consequence for this team. Avoid repeating the same risk under staffing, rollout, and operations when one combined finding is clearer.

**Questions to push back on**
- Ask one or two specific, answerable questions per material gap. "What's the rollback path if the mesh control plane fails in prod?" is useful; "Have you considered reliability?" is not. Do not add a second checklist that merely restates every finding.

**Overall read**
- One or two sentences: is this ready, ready-with-revisions, or not-yet — and the single most important thing to resolve.

---

## Step 4: Verify the review

Before responding:

1. Check that each strength, gap, and question maps to the proposal or to an explicitly labeled inference.
2. Confirm that questions are specific, answerable, and tied to material risks.
3. Compare every citation with the MCP result — title, author, edition, and URL must match exactly — and remove any citation you cannot verify rather than repairing it.
4. Remove generic objections, duplicated findings, and criticism not supported by the proposal or cited evidence.
5. Check that the review evaluates the submitted proposal rather than expanding into a generic architecture review or writing a replacement proposal. Offer a counter-proposal only when it clarifies the minimum revision needed for approval.

If any check fails, revise and run these checks again. Do not respond until all of them pass.

## Principles

Prefer the newest applicable edition for changing technology and adoption practices. Credit real strengths, make criticism evidence-based, and keep pushback questions concrete and fair. If the proposal is sound, say so instead of manufacturing objections.
