# Phase 4 — The Human Review Loop

## Why it's nonnegotiable

Organizational systems rarely contain the full context behind a decision. The meeting that changed everything happened last Tuesday and hasn't been written up. A key person is quietly planning to leave. A strategic direction shifted in a conversation that was never documented. An agent can synthesize everything in the connected systems with real fidelity, but it can't know what isn't there, and organizational reality changes faster than documentation does.

More fundamentally: an agent can identify trade-offs, but it can't decide which trade-offs matter. That judgment requires human knowledge of context, priorities, and risk tolerance. The goal isn't removing humans from the loop — it's giving them better-structured input to reason from.

## The failure mode to design against

The default setup breaks in a specific way. The agent produces a document, someone shares it, people add comments — and when the agent updates the document, pasting in a new version wipes the existing comments. Documents proliferate without clear relationships between them. And the agent has no visibility into the comment threads, which is where the most important context and pushback live.

Diagnose whether they're already in this failure mode. Many are, and haven't named it.

## The three properties

The implementation is a choice; these are not.

1. **Documents are versioned** — revisions are traceable, and updating doesn't destroy history.
2. **Discussion lives next to the document** — captured durably, not in a thread that scrolls away.
3. **The agent can read both** — this is the property most setups miss, and the one that changes the character of the system.

That third property turns a report generator into a participant. Once the agent reads the document *and* the discussion around it, new questions become possible: what is the consensus based on the discussion so far, what questions remain unresolved, incorporate the reviewer comments and produce an updated version.

## The reference implementation

Documents as Markdown in a repository; a Pages site rendering them with inline commenting; discussion in the platform's Discussions feature. Every comment, question, and revision is versioned and traceable, and an agent with repo access reads both the document content and the entire conversation that developed around it.

This is what O'Reilly built internally — it works well for engineering orgs whose reviewers already live in a repo, and gets the three properties almost for free.

## Lighter-weight alternatives

Offer these when the repo pattern doesn't fit where their reviewers actually work:

- **Wiki or doc platform with API access** — fits mixed engineering and business reviewers. Verify the agent can read comment threads through the API before committing; many platforms expose comments to humans but not to API.
- **Issue tracker** — one issue per analysis, document in the body, discussion in the thread. Weakest version history, lowest activation energy, and shipping something beats designing something.
- **Manual with discipline** — dated versions in a folder, review notes appended, the human pastes discussion back as context. Depends on discipline, and discipline decays — but it proves the value of the loop before anyone builds infrastructure for it.

## What to specify

Who reviews (named roles, not "stakeholders"), what triggers a review, where discussion is captured and how the agent reaches it, how a revision is produced and what happens to prior comments, and what escalates to a human decision rather than another iteration.

## The argument worth making

The loop isn't a compliance checkbox on top of the AI output. It's where organizational knowledge accumulates. Each round of review adds context that existed in no system, and once that context is captured where the agent can read it, the next analysis starts from a better place than the last. That compounding is the reason to build the loop — and a more compelling argument to a skeptical leader than "humans should check AI work."
