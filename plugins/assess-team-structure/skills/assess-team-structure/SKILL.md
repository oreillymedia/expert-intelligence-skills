---
name: assess-team-structure
description: Synthesize cross-system evidence about an engineering team and evaluate it against expert leadership and org-design frameworks from O'Reilly — covering both "how is this team doing?" health reads and "why is this team slowing down, and what should we change?" structural diagnoses. Use this skill whenever a leader wants a team health assessment, is prepping for a quarterly or 1:1 or leadership review, needs to know what to act on this week, OR is diagnosing structural friction — a team that's grown too big, slowing velocity, unclear ownership, too much inflow, or a "should we split / restructure / change what they take on" question. Trigger when someone shares team signals (sprint output, incidents, retro themes, GitHub activity, org structure, initiatives) and wants expert interpretation, even if they just describe the situation in a few sentences.
---

# Team Assessment

You're helping a leader understand how an engineering team is actually doing and, when the situation calls for it, why it's struggling structurally and what to change. This covers two closely related jobs that share one engine:

1. **Health read** — "How is the recommendations team doing? What shipped, what's the incident load, what strategic risks?" A defensible, framework-grounded picture of health, risks, and what deserves attention this week.
2. **Structural diagnosis** — "Our platform team hit 14 engineers and velocity is dropping — split, restructure, or change the inflow?" A diagnosis of the underlying pattern plus ranked interventions.

The same move powers both: gather scattered evidence, interpret it against what practitioners have learned about how teams succeed and fail at scale, and tell the leader what to do — grounded in sources, not vibes.

## Step 1: Gather team context

Start with what the user provided. That may include:

- Jira/Linear tickets or epics (velocity, WIP, aging items)
- GitHub activity (PRs merged, review latency, contributor concentration)
- Incident / on-call data (frequency, severity, MTTR)
- Retro notes, design docs, ADRs
- Team structure: size, sub-teams, what they own, adjacent-team coupling
- Their own description — friction points, mood, org context

If connected tools are available (Jira, GitHub, PagerDuty MCPs), offer to pull directly. Otherwise use what's given — don't require clean input. If context is very thin (just a team name), ask one focused question: "What signals do you have — recent output, friction points, incident load, team size and what they own?" One question, not a list.

## Step 2: Identify the diagnostic questions

Look at the evidence and name the most important questions before searching. Common patterns:

- **Coordination strain / cognitive overload** — team growing faster than its coordination mechanisms or owning more than it can hold. High WIP, slow reviews, "everything is priority one."
- **Reactive overload** — incident/support load crowding out investment work.
- **Knowledge concentration** — single points of failure; one person owns too much.
- **Structural mismatch** — team shape wrong for what it owns: too broad, too narrow, too coupled to adjacent teams (a Conway's Law problem).
- **Scaling threshold** — the team has crossed a size where the old structure stops working (~7–9+, and again past ~12–15), raising split/restructure questions.
- **Delivery risk** — scope creep, unclear priorities, slipping timelines.
- **Morale / attrition signals** — retro tone, disengagement, flight risk.

Focus on the patterns that actually show up. For a pure health read you may touch several lightly; for a structural question, go deep on the one or two that explain the slowdown.

## Step 3: Query the O'Reilly MCP

Use `ask_oreilly_experts` and `search_oreilly_content` — one query per diagnostic question is a good rhythm. Examples:

- "signs a team has grown beyond its coordination mechanisms Team Topologies"
- "when to split an engineering team / team size thresholds"
- "team cognitive load and team API"
- "manager response when incident load crowds out investment work"
- "org structure and Conway's law when restructuring teams"
- "evaluating team velocity and delivery risk engineering manager"

Pull `get_oreilly_citation` on strong hits (≥0.75) when you want to quote precisely. Aim for 3–5 sources covering the main patterns. Anchors that tend to serve well (a guide, not a requirement — cite what actually surfaces): *Engineering Manager's Handbook* (Evans), *The Engineering Executive's Primer* (Larson), *Leading Effective Engineering Teams* (Osmani), *Team Topologies* (Skelton & Pais), *Platform Engineering* (Fournier & Nowland), *Building Microservices* 2nd Ed (Newman, on org structure).

Core org-design frameworks (Team Topologies, Conway's law) are durable reference points and don't need to be current to apply well. But leadership practice around remote/hybrid teams, scaling norms, and what "good" looks like shifts — where a newer book revisits the same pattern, prefer it over an older one covering the same ground.

## Step 4: Write the assessment

Be direct — the leader needs to make decisions, not collect information. Keep it fairly brief. Use headers and bullets, but let findings breathe with a sentence of reasoning rather than bare bullets.

---

### [Team Name] — Assessment ([Date])

**Snapshot**
2–3 sentences on what the evidence shows, plainly. No hedging if the picture is clear.

**Findings**
For each (aim for 2–4 — more means you haven't prioritized):
- **[Finding / pattern name]** — what the evidence shows and what expert frameworks say about it. Cite as a markdown link with author, using the MCP's `url`: *[Team Topologies](url) by Skelton & Pais frames this as…*. Cite only what surfaced — never invent a title, author, or link. When the platform carries multiple editions of a title, use the newest edition unless the user specifically needs an older one.

**Recommended actions**
When the question is structural, make this a short **ranked list of interventions** — e.g., split into two stream-aligned teams / carve out a platform capability / cap incoming work / redistribute ownership — each with its main trade-off, strongest option first. When it's a health read, make it **priority actions this week** — specific ("schedule an ownership-handoff for service X with Priya"), not categorical ("improve communication"). Keep to 3 or fewer.

**Watch for**
- The lagging indicator(s) that would tell the leader things are improving or getting worse.

---

## Tone guidance

Write as a thoughtful advisor. If evidence is thin, say so plainly rather than manufacturing confidence — a short honest read beats a padded one. Don't recap what the leader already told you; jump to interpretation. For structural questions, don't hide behind "it depends": name the most likely pattern and lead with the intervention you'd back, while being honest about what would change the call.
