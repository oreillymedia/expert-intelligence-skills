# Phase 1 — Map the Information Hierarchy

## Contents
- What the map is
- The interview
- The reference hierarchy (engineering)
- Other functions
- Output of this phase

## What the map is

Every organization has systems where important knowledge lives, and they form a natural hierarchy from strategic intent at the top to operational detail at the bottom. Making that hierarchy explicit is the map of how decisions get made, which sources carry the most authority, and how different kinds of questions should be approached.

This is an organizational task, not a technical one. Doing it well requires understanding how decisions actually get made — which is why an inventory of tools is not an answer. The tell: every system sits at the same level and nothing wins when two disagree.

## The interview

Ask conversationally, a few at a time.

**Scope**
- Which team or function are we designing for?
- Who will ask this system questions?

**The questions themselves** — this drives Phase 3, so spend time here
- What do you research by hand that takes days?
- What question does someone ask you every quarter that you answer from scratch?

If they stall, the themes teams actually bring to these systems are: architecture and infrastructure (should we make this change, what will it cost, what might break), operational effectiveness (where is our toil coming from, what should we automate or retire), team health and capacity (where is the team's time going, what's limiting execution), organization and strategy (how should we organize, prioritize, invest), and engineering measurement (how do we know if we're healthy and improving). None of these is about writing code.

**The systems** — one per layer, using their vocabulary
- Strategic intent, execution, implementation, ownership, operational reality

**Authority** — do not skip
- When [roadmap system] and [execution system] disagree about what a team is working on, which is right?
- Which of these is updated reliably, and which drifts?
- What important context exists only in someone's head or in Slack?

That last question defines the boundary the agent can never cross, and feeds Phase 4.

## The reference hierarchy (engineering)

Propose this shape by default and let them correct it.

| Layer | System | Purpose |
|---|---|---|
| Roadmap | Productboard | Strategic goals, initiatives, feature prioritization |
| Execution | Jira | Epics, stories, sprints, contributor tracking |
| Implementation | GitHub | Source code, PR history, event instrumentation |
| Service catalog | Cortex | Service ownership, dependencies, on-call, Slack channels |
| Observability | Datadog | System performance, errors, incidents |

Add an Authority column as you fill it in with them.

## Other functions

The same five-layer logic with different systems. A sales org might put Salesforce at the top, then a revenue intelligence platform, marketing automation, and market research. A legal team might start with contract management, then a regulatory tracker, internal policy docs, and a research database. Finance runs across a planning tool, an ERP, and external benchmarks.

The specific systems matter less than the act of mapping: which layer answers which kind of question, and which sources take precedence when they conflict.

## Output of this phase

A hierarchy table, a one-line precedence rule, and three to five recurring question types (more only if they are mapping a second function). Confirm all three before Phase 2 — the question types especially, since they become the rows of the Phase 3 routing table.
