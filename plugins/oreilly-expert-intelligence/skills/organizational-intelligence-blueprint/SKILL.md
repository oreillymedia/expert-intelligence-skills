---
name: organizational-intelligence-blueprint
description: Creates an organizational intelligence blueprint — maps where a team's knowledge lives, connects those systems, generates a custom reasoning skill file, and grounds analysis in named expert frameworks from O'Reilly. Use when someone has read (or not read) O'Reilly CTO Andrew Odewahn's piece on building organizational intelligence and asks how to apply it to their organization; wants to turn team data and health metrics into actionable recommendations; wants to build an internal AI research assistant or analyst agent over their own systems; wants AI reports to stop producing generic advice nobody trusts; or asks to write or fix a CLAUDE.md or skill file for an internal analyst agent. Trigger on prompts like "how do I apply this to my organization," "get started with organizational intelligence," "our AI reports are too generic," or "connect our systems so AI can reason about them." Trigger even when the person describes the problem rather than naming the solution.
---

# Create an Organizational Intelligence Blueprint

Internal AI assistants usually fail the same way: connected to company systems, retrieving accurately, and producing reports organized around the *data* rather than the *decision*. The output is correct, easy to agree with, and impossible to act on — "the team appears overloaded, consider adding headcount."

The fix is four parts working together: an explicit information hierarchy, connections to the systems plus a reasoning skill, an expert grounding layer supplying named frameworks and thresholds, and a human review loop. This skill walks someone through building all four for their own organization.

## Deliverables

Produce all four. A narrative summary without these artifacts is a failed run.

| # | Artifact | Delivery |
|---|---|---|
| 1 | Information hierarchy table — layer, system, purpose, authority | inline |
| 2 | Framework routing table — question type, framework, threshold, citation | inline |
| 3 | Reasoning skill file — ready to paste into their agent | file |
| 3b | Sample run — the skill file applied to one of their real questions | file |
| 4 | Review loop design | inline |

## Opening turn

Keep the first reply to a few lines. The person may have just read the article and typed something like "I want to do this," or may never have heard of it and arrived with only a vague problem ("our AI reports are useless"). Do not open with the deliverables, the scoping rationale, a checklist, or an interview.

1. **Check the Expert MCP first, silently.** Use `ToolSearch` for `oreilly-expert-intelligence`. If the tools are missing, say so in one line after the one-sentence explanation and point to "When the Expert MCP isn't connected" in `references/phase-3-expert-layer.md`, so they can connect it now rather than discover the gap in Phase 3.
2. **One sentence on what this is and why it matters, written for someone who has never read the article.** Lead with the benefit in plain words, give the concrete contrast, make clear that what you build together is a skill (a reusable set of instructions) their AI will use, and link the source. Do not assume they know the term "organizational intelligence" or what MCP is. For example: "This helps you build a skill, a reusable set of instructions for your AI, so its advice is specific to your team rather than generic ('hire more people'), by pairing your own data with expert frameworks, as in Andrew Odewahn's [Building Organizational Intelligence](https://www.oreilly.com/radar/building-organizational-intelligence/)." Adapt it, keep it to one sentence, and add no further pitch.
3. **One question, no more.** Ask which team or function they want to start with. Save "what question do you most wish it could answer?" for the next turn; it is hard to answer cold.
   - **Exception:** if they say they already have an AI tool producing reports (even loosely, like "our AI reports are useless"), ask instead for what that tool is told to do (its instructions or prompt file) and one report that disappointed them. Use plain words, not "skill file." That replaces the team question; the team usually becomes clear from the report.

Then stop and let them answer. Everything below is for you to use as the conversation unfolds, not to recite.

## Scope the first session

Aim for **one team, three to five question types, and whatever evidence is reachable today**, including none. Do not lecture about this. Apply it by steering: if they say "the whole company," suggest starting with one team and finishing it before the second, because a working system for one team teaches what the wide version should look like.

## Two things to establish early

**Greenfield or repair?** If they already have an agent producing generic output, ask for the existing skill file and one bad output. Diagnose against the four parts — the missing pieces are usually the routing table and epistemic standards, not the connections. Skip to Phase 2.

**Mapping is required; connecting is not.** They do not have to connect every system to get value, and many will connect none in the first session. But they do have to map how decisions actually get made — which systems hold what, and which one wins when two disagree. Say this when they hesitate over connections, not up front; someone who thinks they need five live connections before starting will stop before starting.

## Phases

Work through these in order, conversationally. Confirm each phase's output before moving on — Phase 2 depends on Phase 1 being right, and Phase 3 depends on Phase 2.

Read the reference file when reaching each phase:

- **Phase 1 — Map the information hierarchy**: `references/phase-1-hierarchy.md`
- **Phase 2 — Connections and reasoning skill**: `references/phase-2-reasoning.md`
- **Phase 3 — Expert grounding layer**: `references/phase-3-expert-layer.md`
- **Phase 4 — Human review loop**: `references/phase-4-review-loop.md`

Fill in `assets/reasoning-skill-template.md` rather than composing a skill file from scratch. It carries the format choice (`CLAUDE.md` vs `SKILL.md`) and the authoring rules the generated file has to meet.

### Phase 1 — Map the information hierarchy

An organizational task, not a technical one. The map is not a tool inventory; it is a model of how decisions get made and which source is authoritative when two systems disagree.

Ask what tools they use, where the important context lives, and how decisions actually get made. Then establish precedence — what happens when the roadmap system and the ticket system disagree. That question is the one people skip and the one that reveals how the organization really works.

Default to an engineering team: roadmap, execution, implementation, service ownership, observability. If they are in another function, the same five-layer logic applies with different systems — see the reference file for sales, finance, and legal.

### Phase 2 — Connections and the reasoning skill

**Work out what can be connected.** Tool names, connector directories, and how connections are made differ by AI platform, so do not assume any particular tool. For each system from Phase 1, work with the person to find the best route to it from the AI they use:

1. See what is already available — look at the tools and connections in the current session, and ask what their AI platform offers.
2. Check whether the product has an official connector or MCP server, and how their platform installs one.
3. If not, look for a direct route: a REST API the agent can call, or an export it can read.
4. If none works, the system stays in the hierarchy and the skill file tells the agent what to ask a human for.

Help them connect what is easy during the session rather than leaving it as homework. Ask who owns access — a connection that needs an admin they don't have is not yet a connection. Record the result for each system (route, status, notes).

**The reasoning skill.** This is where retrieval becomes analysis. It defines the reasoning hierarchy, the output format (an analyst, not a coding agent), epistemic standards (show the work, name gaps, surface assumptions), and tone. "Be curious, not judgmental" measurably improves output quality here.

### Phase 3 — Expert grounding layer

The phase that changes the character of the output. **Make the tool calls** — a routing table written from memory defeats the purpose, because the value is the traceable citation, not the framework name.

You checked for `oreilly-expert-intelligence` in the opening turn. If it was missing and still is, follow the "When the Expert MCP isn't connected" section of `references/phase-3-expert-layer.md`. Do not silently substitute framework names from general knowledge — that produces exactly the ungrounded output this whole approach exists to fix.

1. Take the question types from Phase 1.
2. For each, call `oreilly-expert-intelligence:ask_oreilly_experts` to find the anchoring framework and the threshold it supplies.
3. Call `oreilly-expert-intelligence:get_oreilly_citation` on results scoring 0.75 or higher — two to five per question — for the citable source and link.
4. Run a second query per question type seeking a *competing* framework. This is the check against favoring whichever framework surfaced first.
5. Assemble the routing table and name the gaps where the literature is thin.

Pass `skill_used: "organizational-intelligence-blueprint"` on every call.

### Phase 4 — Human review loop

Organizational systems rarely hold the full context behind a decision — the meeting last Tuesday that hasn't been written up, the person quietly planning to leave. And an agent can identify trade-offs but cannot decide which ones matter.

The requirement is a loop where documents are versioned, discussion is captured next to the document, and the agent can read both. The implementation is a choice; offer options sized to the organization rather than prescribing one.

## Validate the skill file before delivering it

The skill file is the artifact that actually runs. Do not hand it over untested.

1. Pick the sharpest question type from Phase 1.
2. Answer it *as if* their agent had loaded the skill file — following its hierarchy, its routing table, its output format — using whatever evidence is at hand, including pasted or hypothetical data.
3. Read the result against the file's own standards. Does it lead with a finding or a data summary? Does it cite a framework and a threshold? Does it name gaps? Does it reach anything non-obvious?
4. Where it falls short, fix the *instruction*, not the output. A vague result usually traces to a missing rule.
5. Repeat once. Then deliver both the file and the sample run — the sample is what convinces their stakeholders the thing works.

## Output structure

Use this template, adapting sections to what the engagement surfaced:

```markdown
# Organizational Intelligence Blueprint: [org / team / function]

## What we're solving
[The questions they want answered, in their words. Two or three sentences.]

## 1. Information hierarchy
[Table: Layer | System | Purpose | Authority]
[Precedence: what wins when sources conflict, and why.]

## 2. Connections and reasoning layer
[Table: System | Access method | Status | Notes]
[Pointer to the skill file artifact.]

## 3. Expert grounding
[Table: Question type | Framework | Threshold | Competing view | Citation — built from the frameworks and citations retrieved during Phase 3 of this conversation, not from memory.]
[Gaps: question types with no strong grounding, stated plainly.]
[Live connection: the new reasoning skill file also connects to the O'Reilly Expert Intelligence MCP, so it keeps retrieving and citing frameworks for questions outside this table. The table is its starting point, not its ceiling. Say which tools the skill file calls (`ask_oreilly_experts`, `get_oreilly_citation`) and how the person connects the MCP in their own environment.]

## 4. Review loop
[The mechanism, sized to this org. How discussion becomes context.]

## Build sequence
[Ordered next steps, the first small enough to do this week.]

## What this won't do
[Honest limits. Two or three lines.]
```

## Working principles

**Interview before architecting.** Someone who lists their tools has not answered the Phase 1 question.

**Cite or don't claim.** Every framework in the routing table needs a retrieved citation with a link. A named gap beats a framework stretched to fit.

**Name what's missing.** Gaps in their data, in the literature, and context the system will never have. This is the habit the generated skill file teaches their agent, so model it.

**Be curious, not judgmental.** Organizations have reasons for the shapes they're in.

**Don't overclaim.** What comes out of a session is a design plus a working reasoning skill file. What does not come out is a fully connected system, and the expert layer is not a magic ingredient that turns a generic setup into consultant-quality analysis. Say so if the person expects otherwise — the whole point is producing analysis people trust.
