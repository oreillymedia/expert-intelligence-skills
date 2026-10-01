---
name: review-architecture-decision
description: Reviews system-level or expensive-to-reverse design decisions using cited O'Reilly architecture sources, identifying sound choices, fragile assumptions, failure modes, future costs, and unresolved questions. Use when the primary task is evaluating architecture trade-offs involving messaging, consistency, schemas, partitioning, caching, data ownership, or synchronous-versus-asynchronous boundaries, including designs presented in an RFC, ADR, diagram, or executive brief. For organization-level adoption recommendations, use create-decision-brief; for document-wide evaluation of a proposal's claims, gaps, and approval readiness, use review-technical-proposal; for a bounded implementation choice, use compare-implementation-approaches.
---

# Architecture Decision Review

Review the important trade-offs in a system design. Produce a specific map of what is sound, what is fragile, what creates future cost, and which questions must be resolved before committing.

## Source and citation rules

Use only sources returned by the O'Reilly MCP tools. Tool names below are unqualified because the server name is user-configured; when the runtime requires qualified names, prepend the configured server name (for example, `oreilly:ask_oreilly_experts`). Cite each selected result as `[title](url) by authors`, using `product_title` when the result provides it instead of `title`. Copy the title and URL exactly from that same result; do not alter, normalize, shorten, repair, or reconstruct the URL. Use a string-valued `authors` field unchanged; for a list, join the returned names in order with commas. When `get_oreilly_citation` returns a fully rendered `citation_format`, use it unchanged. Never invent or reconstruct metadata or quotations. Remove a citation that cannot be verified against the tool result. Present uncited conclusions as your own analysis or omit them.

## Step 1: Map the important decisions

Extract the design and the decisions inside it from the document, diagram, or prose. Identify choices that affect correctness or are expensive to reverse. For distributed or event-driven designs, explicitly check:

- atomicity between the system of record and messages;
- idempotency for external side effects;
- partial failure and compensation across independent consumers;
- partition keys, ordering scope, retries, and rebalancing;
- schema evolution and whether internal events become external contracts;
- operational costs introduced by the proposed remedy.

Apply only the checks relevant to the design, but do not silently skip a named component or failure path.

Use the **sound / fragile / future cost map** below by default. Use a **trade-off table** or **risk-ranked findings list** only when the user requests it or that format clearly fits the prompt better.

## Step 2: Research the decisive trade-offs

Research in this order:

1. Turn each important design decision into a targeted question.
2. Use `ask_oreilly_experts` and/or `search_oreilly_content` as appropriate for the research need, following their tool descriptions.
3. Select only results that directly support a sound, fragile, or future cost finding or a question the author must resolve.
4. Draft from the verified evidence. If no directly relevant source surfaces, state the evidence gap instead of citing a weaker source.

Search each important decision explicitly:

- "[pattern] trade-offs — when it works and when it breaks" (e.g., "exactly-once semantics trade-offs in event-driven systems")
- "schema evolution / consumer rebalancing / ordering guarantees [technology]"
- "failure modes of [architecture choice] at scale"
- "alternatives to [choice] and how to decide between them"

Search the actual technologies and guarantees in the design. Useful anchors may include *Kafka for Architects*, *Designing Event-Driven Systems*, *Foundations of Scalable Systems*, and *System Design on AWS*; cite only what surfaces and applies. Do not force a named title into the review or omit a stronger result because it is unfamiliar.

Foundational distributed-systems reasoning (ordering, consistency, failure modes) doesn't go stale. But where the trade-off depends on what a specific platform currently supports — managed service capabilities, a streaming engine's current guarantees, a cloud provider's offerings — prefer the newest coverage, since a design review that cites an outdated capability set will misjudge the trade-off.

## Step 3: Draft the review

Lead with a one-line verdict on the overall shape, then the map.

---

### Architecture Review — [System / Decision]

**Overall:** one or two sentences — is this the right shape, with reservations, or is an important choice wrong?

**Sound** — decisions well-supported by the evidence.
- **[Decision]** — why it holds up, followed by a citation formatted according to the source and citation rules above and, when useful, a short exact quotation from a verified expanded passage.

**Fragile** — decisions that work only under assumptions the design doesn't guarantee.
- **[Decision]** — the hidden assumption, what breaks it, and the source. Be specific about the failure mode (e.g., "exactly-once here assumes idempotent consumers; your handler isn't — on rebalance you'll double-process").

**Future cost** — decisions that are fine now but will get expensive.
- **[Decision]** — what it costs later (migration pain, operational load, lock-in) and the framework that predicts it.

**Questions to resolve before committing**
- The 2–4 sharpest questions the author should answer next.

---

## Step 4: Verify the review

Before responding:

1. Check that every finding maps to a stated design choice, component, sequence, or explicitly labeled inference.
2. Reconstruct each failure sequence and remove impossible states or wording that assumes an event occurred before the design allows it.
3. Confirm coverage of atomicity, idempotency, compensation, ordering, schema contracts, and operational cost wherever applicable.
4. Confirm that quotations are exact and short. Compare every citation with the MCP result — title, author, edition, and URL must match exactly — and remove any citation you cannot verify rather than repairing it. Prefer the newest applicable edition.

If any check fails, revise and run these checks again. Do not respond until all of them pass.

## Principles

Prefer the newest applicable edition when the same work is available in multiple editions. Quote precisely and sparingly — a sharp two-line quote beats a paragraph. Be direct about fragility; a review that only praises isn't a review. Where the evidence is genuinely mixed, say so and give the author the decision rather than a false verdict.
