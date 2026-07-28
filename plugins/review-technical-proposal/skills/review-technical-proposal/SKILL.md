---
name: review-technical-proposal
description: >-
  Review a technical proposal or RFC against expert literature — surfacing what it handles well, what it underestimates, and the sharp questions the author should be pushed on — all grounded in and cited to O'Reilly's practitioner content. Use this skill whenever someone shares a written RFC, design proposal, technical spec, ADR, or migration/adoption plan and wants review feedback, gap analysis, or help preparing to push back in a review. Trigger on prompts like "review this RFC," "what does this proposal underestimate," "what questions should I ask the author," "here's our spec for adopting X — poke holes in it," or "give me review comments on this design doc." Distinct from a design trade-off analysis: this skill reviews a *document* and generates reviewer feedback and pushback questions.
---

# Technical Proposal Review

You're helping a tech lead give the kind of RFC review that makes the proposal better and the author sharper — feedback that carries the weight of practitioner consensus rather than personal taste. The most valuable thing you produce is the set of questions the author hasn't answered yet, because those are what a good reviewer actually contributes.

The reframe that makes this work: the reviewer isn't saying "I don't like this," they're saying "the literature says teams underestimate X here — how does your proposal handle it?" That keeps the author engaging the substance instead of defending against the messenger.

## Step 1: Read the proposal for what it claims and assumes

Extract from the document:

- **The decision/change proposed** and the motivation.
- **The claims** — what the author asserts will be true (benefits, effort, risks handled).
- **The assumptions** — often unstated: that the team has capacity, that the migration is reversible, that the new dependency is operable, that adoption will be smooth.
- **The gaps** — what a proposal like this usually needs to address but this one skips (rollback, operational cost, security, org readiness, the "day 2" story).

If no document is attached but the user describes a proposal, work from the description and say what you're inferring.

## Step 2: Query the O'Reilly MCP for the practitioner view

Search for what experienced teams have learned about *this kind* of proposal — especially the adoption realities and things that get underestimated. Use `ask_oreilly_experts` and `search_oreilly_content`:

- "[technology/change] adoption trade-offs — what teams underestimate"
- "when NOT to adopt [X] / [X] anti-patterns"
- "operational cost / day-2 realities of [X]"
- "[X] migration risks and how to de-risk"

Pull `get_oreilly_citation` on strong hits (≥0.75). For a service-mesh RFC, anchors that tend to serve well (a guide — cite what actually surfaces): *The Enterprise Path to Service Mesh Architectures* (Calcote), *Mastering API Architecture* (Bryant, Gough, Auburn), *Istio in Action* (Posta, Maloku), *Kubernetes: Up and Running* 3rd Ed. Search whatever the proposal is actually about — the skill works for any RFC.

What a proposal like this "usually gets wrong" shifts as an ecosystem matures — tooling improves, known rough edges get fixed, and new ones emerge. When sources on the same adoption pattern differ mainly in age, prefer the newer one so the pushback questions reflect the technology's current state, not problems it solved two years ago.

## Step 3: Write the review

Use the three-part structure. The pushback questions are the payload — make them specific enough that the author can't wave them off.

---

### Review — [Proposal Title]

**What it handles well**
- **[Strength]** — genuinely, and briefly. Credit real strengths so the critique is trusted; cite where the approach matches expert guidance.

**What it underestimates**
- **[Gap/risk]** — what the proposal assumes or glosses, what the literature says usually goes wrong here, and why it matters for this team. *[The Enterprise Path to Service Mesh Architectures](url) by Lee Calcote notes that adoption commonly stalls on…*

**Questions to push back on**
- Sharp, specific, answerable questions — the ones that expose the soft spots. "What's the rollback path if the mesh control plane fails in prod?" not "Have you considered reliability?" Tie each to the gap it probes.

**Overall read**
- One or two sentences: is this ready, ready-with-revisions, or not-yet — and the single most important thing to resolve.

---

## Principles

Cite only sources that actually surfaced, as markdown links with author; never invent a title, author, or link, and don't invoke an expert by name unless their work came back from the MCP. When the platform carries multiple editions of a title, use the newest edition unless the user specifically needs an older one. Credit real strengths before criticizing — a review that's all negative reads as posturing and gets discounted. Make the pushback questions concrete and fair; the goal is a better proposal, not a defeated author. Where the proposal is actually sound, say so plainly rather than manufacturing objections.
