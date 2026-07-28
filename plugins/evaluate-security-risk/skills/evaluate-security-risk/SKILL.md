---
name: evaluate-security-risk
description: >-
  Produce a structured threat model for a new or changing service — organized by a recognized framework (STRIDE by default), highlighting the threats teams most often miss before launch, with an expert-cited source and mitigation for each — grounded in O'Reilly's application-security and threat-modeling literature. Use this skill whenever someone is designing or reviewing a service and wants a threat model, security risk review, STRIDE analysis, or help finding the security gaps before shipping: auth/SSO/OIDC flows, token handling, APIs, data stores, new integrations. Trigger on prompts like "walk me through a STRIDE threat model for our new SSO service," "threat-model this design," "what security risks are we missing," or "review this for security before launch." This is defensive security work — identifying and mitigating risks, not exploiting them.
---

# Security Risk Review

You're helping a team find the security holes in a design before an attacker does — and specifically the ones teams *routinely* miss, because those are where real breaches come from. The output reads as professional security work: a structured threat model, framework-organized, with each threat tied to a cited source and a concrete mitigation.

This is defensive: the goal is to surface and close risks. Describe threats at the level needed to understand and mitigate them — the mechanism and the fix — not step-by-step exploitation instructions.

## Step 1: Understand the system and confirm the framework

Extract the design: the components, trust boundaries, data flows, entry points, and what's sensitive (credentials, tokens, PII, money). A threat model is only as good as the boundaries you draw, so get those right first — where does untrusted input cross into trusted territory?

Then ask the user one quick question: **do they have a preferred framework** (STRIDE, PASTA, LINDDUN, attack trees)? If yes, use theirs. If not, default to STRIDE and let the expert content that surfaces shape the specifics. Keep the emphasis on commonly-missed threats regardless of framework.

## Step 2: Query the O'Reilly MCP

Search both the framework method and the domain-specific threats — the specifics are where the misses hide. Use `ask_oreilly_experts` and `search_oreilly_content`:

- "[framework] threat modeling methodology and categories"
- "[domain] commonly missed / overlooked security threats" (e.g., "OIDC token replay refresh token rotation consent phishing")
- "[component] attack patterns and mitigations"
- "security risks teams underestimate in [system type]"

Pull `get_oreilly_citation` on strong hits (≥0.75). Anchors that tend to serve well (a guide — cite what actually surfaces): *Threat Modeling* (Shostack — canonical STRIDE anchor), *Software Security for Developers* (Saikali & Spilca — protocol/token specifics), *Advanced Cyber Threat Intelligence and Hunting* (Sorensen & Tiepolo — attack flows like consent phishing), *Threat-Driven Software Development* (Howard, Holmes, Hernan). Search the actual protocols/components in play.

Tip: query the framework broadly *and* the domain specifics separately. The framework anchor (e.g., Shostack) surfaces best on framework-first queries; the specific-threat sources surface on protocol queries. Run both so both are available to cite.

Treat recency asymmetrically here. The methodology itself (STRIDE, Shostack's framework) doesn't need to be current to be right — it's foundational and still holds. But attacker techniques, protocol weaknesses, and what's "commonly missed" move fast; for the domain-specific threats, prefer the newest coverage you can find, since a dated source may be silent on the current attack surface.

## Step 3: Write the threat model

Lead with the highest-value part — the missed threats — then the full model.

---

### Threat Model — [Service] ([Framework])

**System & trust boundaries**
- Brief: components, the boundaries, and what's sensitive.

**Most-often-missed threats** *(the payload)*
- **[Threat]** — what it is, why teams miss it, the impact, and the mitigation. Cite the source. *[Software Security for Developers](url) by Saikali & Spilca covers refresh-token rotation…*

**Full threat model**

| Category | Threat | Affected component | Likelihood / Impact | Mitigation | Source |
|---|---|---|---|---|---|
| Spoofing | … | … | … | … | [link] |
| Tampering | … | … | … | … | [link] |
| Repudiation | … | … | … | … | [link] |
| Information disclosure | … | … | … | … | [link] |
| Denial of service | … | … | … | … | [link] |
| Elevation of privilege | … | … | … | … | [link] |

*(Adapt category rows to the chosen framework.)*

**Priorities before launch**
- The 2–4 threats to fix first, and why.

---

## Principles

Cite only sources that surfaced, as markdown links with author — one per threat where possible; never invent a title, author, or link. When the platform carries multiple editions of a title, use the newest edition unless the user specifically needs an older one. Keep the framing defensive: mechanisms and mitigations, not exploit recipes. Make the "commonly missed" section genuinely non-obvious — token replay, refresh-token rotation, consent-screen phishing, missing rate limits on auth endpoints — not generic "use HTTPS." Prioritize honestly; a model that flags 40 equal-weight threats is as useless as one that misses the real ones.
