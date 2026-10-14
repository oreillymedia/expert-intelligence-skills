# Phase 2 — Connections and the Reasoning Skill

Two parts that must work together. A connection gives the agent access to the data; it does not tell the agent how to use it. Without explicit guidance the agent retrieves information and organizes it the way the underlying systems organize it, which produces a data dump, not an analysis. The skill file is what transforms retrieval into analysis.

## Part A — Connections

Mapping is required; connecting is not. Someone can leave with zero systems connected and still have a usable blueprint. But connect what's easy during the session — a connector clicked now beats a connector on a to-do list.

**Work out what can be connected.** The tools and directories for connecting an AI to company systems vary by platform and change over time, so don't assume specific tool names. For each system named in Phase 1, work through these with the person, one system at a time:

1. **What's already connected?** Look at the tools available in the current session, and ask what connections or integrations their AI platform shows.
2. **Is there an official connector?** Many products offer an MCP server or a platform-specific integration. Ask them to check their platform's connector or integration settings, or search for "[product] MCP server" or "[product] integration for [their AI platform]." Prefer one published by the vendor.
3. **Is there a direct route?** A REST API the agent can call (for a bash-capable agent, `curl` and `jq` often suffice), or a scheduled export the agent can read. Less clean than a connector, but it works.
4. **Neither?** The system stays in the hierarchy, and the skill file says what to ask the human to supply instead of what to query.

Help them do the connecting now where it is easy; a connection made in the session beats one on a to-do list. If you can't verify a route from where you are, say so and give them the steps to check, rather than asserting a connector exists.

**Record what you find.**

| System | Access method | Status | Notes |
|---|---|---|---|
| [name] | Connector / MCP server / REST API / export / manual | connected / available / none | auth, who owns access |

A route requiring an admin the person doesn't have is not a connection. Ask who owns access.

## Part B — The reasoning skill

Fill in `assets/reasoning-skill-template.md`. It is a codified version of how a skilled analyst would approach these questions — it encodes the organization's reasoning process and makes it repeatable. Four things define it.

**Reasoning hierarchy.** Which systems to consult for which types of questions, and how to weigh them. This is Phase 1's table turned into instructions, including the precedence rule. Add: report conflicts between systems rather than reconciling them silently. Silent reconciliation hides the most interesting finding.

**Output format.** State that this is not a coding agent — it produces reports and recommendations, not code. Specify the template, and organize output around the *decision*, not around the systems the data came from. A report with a section per source system is a data dump wearing a report's clothes.

**Epistemic standards.** Show your work, name gaps, surface assumptions for human verification. Add: reach for the non-obvious conclusion when the evidence supports it. The obvious recommendation is the one nobody needed an agent for.

**Tone.** "Be curious, not judgmental." Borrowed from Ted Lasso, and it meaningfully improves the quality of the output — analysis that reads as assessment produces defensiveness and shuts down the review conversation Phase 4 depends on.

## The repair case

When an existing skill file is producing generic output, the failure is usually visible in under a minute:

| Symptom | Cause |
|---|---|
| Reports read as data summaries organized by source | No output format instruction |
| Recommendations could apply to any company | No expert grounding layer — the most common |
| Confident conclusions that turn out wrong | No conflict-reporting or gap-naming rule |
| Nobody trusts it | No traceable citations, so reviewers can only accept or reject |
| Writes code instead of analysis | Missing "this is not a coding agent" |

Ask for the skill file and one output they were unhappy with. Showing them the specific missing instruction is more persuasive than a rewrite.
