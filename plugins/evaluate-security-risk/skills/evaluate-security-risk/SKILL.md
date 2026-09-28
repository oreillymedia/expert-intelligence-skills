---
name: evaluate-security-risk
description: Creates a structured defensive threat model for a proposed, changing, or existing service using cited O'Reilly security sources. Use when the primary task is identifying assets, data flows, trust boundaries, threats, prioritized mitigations, or STRIDE coverage for authentication, tokens, APIs, uploads, data stores, integrations, or service designs. A technical proposal, compliance requirement, or past incident may provide context. For proposal-wide approval review, use review-technical-proposal; for broader system-design trade-offs, use review-architecture- decision. Not intended for step-by-step exploit development, standalone compliance-control audits, or real-time security-incident investigation and response.
---

# Security Risk Review

Produce a defensive threat model that maps trust boundaries, prioritizes material threats, and pairs each threat with a concrete mitigation. Explain attack mechanisms only to the depth needed to understand and reduce the risk; do not provide step-by-step exploitation instructions.

## Source and citation rules

Use only sources returned by the O'Reilly MCP tools. Tool names below are unqualified because the server name is user-configured; when the runtime requires qualified names, prepend the configured server name (for example, `oreilly:ask_oreilly_experts`). Cite each selected result as `[title](url) by authors`, using `product_title` when the result provides it instead of `title`. Copy the title and URL exactly from that same result; do not alter, normalize, shorten, repair, or reconstruct the URL. Use a string-valued `authors` field unchanged; for a list, join the returned names in order with commas. When `get_oreilly_citation` returns a fully rendered `citation_format`, use it unchanged. Never invent or reconstruct metadata or quotations. Remove a citation that cannot be verified against the tool result. Present uncited conclusions as your own analysis or omit them.

## Step 1: Map the system and select the framework

Extract the components, data flows, entry points, identities, sensitive assets, and trust boundaries. Trace every path that bypasses the main application, such as signed URLs or direct object-store access. Treat anything that parses or executes attacker-controlled input as its own boundary even when it runs inside a nominally trusted network. Do not collapse credential-to-identity mapping, storage access, data-layer authorization, and untrusted-file processing into one generic boundary.

Use the user's requested framework. Otherwise default to STRIDE without asking. If a diagram would materially clarify data flow and bypass paths, include a small one, but ensure its trust-zone labels preserve rather than hide hostile-input boundaries.

## Step 2: Research the framework and system-specific threats

Research in this order:

1. Turn the framework coverage and system-specific threats into targeted questions.
2. Use `ask_oreilly_experts` and/or `search_oreilly_content` as appropriate for the research need, following their tool descriptions.
3. Select only results that directly support a concrete threat, mitigation, or priority.
4. Draft from the verified evidence. If no directly relevant source surfaces, state the evidence gap instead of citing a weaker source.

Search both the framework method and the domain-specific threats — the specifics are where the misses hide:

- "[framework] threat modeling methodology and categories"
- "[domain] commonly missed / overlooked security threats" (e.g., "OIDC token replay refresh token rotation consent phishing")
- "[component] attack patterns and mitigations"
- "security risks teams underestimate in [system type]"

Search the actual protocols and components in the design. Framework anchors such as *Threat Modeling* or *Threat-Driven Software Development* are useful only when they surface; domain-specific sources should support the concrete threats. Do not force a named title into the threat model or omit a stronger result because it is unfamiliar.

Tip: query the framework broadly *and* the domain specifics separately. The framework anchor surfaces best on framework-first queries; the specific-threat sources surface on protocol queries. Run both so both are available to cite.

Treat recency asymmetrically here. The methodology itself (STRIDE, Shostack's framework) doesn't need to be current to be right — it's foundational and still holds. But attacker techniques, protocol weaknesses, and what's "commonly missed" move fast; for the domain-specific threats, prefer the newest coverage you can find, since a dated source may be silent on the current attack surface.

## Step 3: Draft the threat model

Lead with the highest-value part — the missed threats — then the full model.

---

### Threat Model — [Service] ([Framework])

**System & trust boundaries**
- Brief: components, the boundaries, and what's sensitive.

**Most-often-missed threats** *(the payload)*
- **[Threat]** — explain the mechanism, why teams miss it, the concrete impact, and the mitigation. Cite the source. Favor non-obvious boundary failures over generic advice.

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
- Rank two to four threats by likelihood, impact, and mitigation leverage. State why each outranks the remaining findings.

---

## Step 4: Verify the threat model

Before responding:

1. Check every component, data flow, sensitive asset, and trust boundary, including bypass paths and parsers of untrusted input.
2. Confirm that every framework category was considered, even if the final table combines or omits categories with no material finding.
3. Confirm that priorities reflect likelihood, impact, and mitigation leverage rather than framework order.
4. Compare every citation with the MCP result — title, author, edition, URL, and the mitigation it supports must match exactly — and remove any citation you cannot verify rather than repairing it.
5. Remove unnecessary exploit instructions.

If any check fails, revise and run these checks again. Do not respond until all of them pass.

## Principles

Prefer the newest applicable edition for current attack surfaces, while allowing foundational framework sources to be older. Keep the framing defensive: mechanisms and mitigations, not exploit recipes. A model that lists many equal-weight threats is as unhelpful as one that misses the important boundary failures.
