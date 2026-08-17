# Expert Intelligence Skills

Agent skills that ground engineering and leadership work — decisions, reviews, plans, forecasts — in
expert consensus from the O'Reilly learning platform, with citations.

These aren't prompt wrappers. Each skill runs a deliberate research pass against O'Reilly's
Expert Intelligence MCP tools, then writes to a specific output shape: a half-page decision brief, a
STRIDE threat model, a 30-60-90 ramp plan. Every claim carries a link back to the book, video, or
event it came from, and each skill is instructed never to cite a source that didn't actually surface.

The repo is a **plugin marketplace**. Install the complete
[`oreilly-expert-intelligence`](plugins/oreilly-expert-intelligence) toolkit or a single skill, in
Claude or Codex.

## Skills

| Category | Skill | What it does |
|---|---|---|
| All skills | [`oreilly-expert-intelligence`](plugins/oreilly-expert-intelligence) | Installs all 11 Expert Intelligence skills in one plugin |
| De-risk a decision | [`create-decision-brief`](plugins/create-decision-brief) | Turns a "should we?" into a memo-ready recommendation grounded in expert consensus |
| De-risk a decision | [`forecast-project-delivery`](plugins/forecast-project-delivery) | Pressure-tests a plan into realistic timelines and delivery risks |
| De-risk a decision | [`assess-team-structure`](plugins/assess-team-structure) | Diagnoses team structure problems against expert org-design frameworks |
| Defend a design | [`compare-implementation-approaches`](plugins/compare-implementation-approaches) | Compares implementation approaches with cited trade-offs and a code example |
| Defend a design | [`review-architecture-decision`](plugins/review-architecture-decision) | Evaluates a system design against expert trade-off analysis |
| Defend a design | [`review-technical-proposal`](plugins/review-technical-proposal) | Reviews an RFC for gaps and generates the pushback questions you'll get |
| Defend a design | [`evaluate-security-risk`](plugins/evaluate-security-risk) | Produces a STRIDE threat model, flagging the risks teams commonly miss |
| Ship with confidence | [`plan-service-reliability`](plugins/plan-service-reliability) | Drafts SLOs and an error-budget policy for a new or evolving service |
| Ship with confidence | [`plan-production-ready-ai`](plugins/plan-production-ready-ai) | Recommends an ML deployment strategy calibrated to your team's maturity |
| Grow the team | [`plan-domain-rampup`](plugins/plan-domain-rampup) | Builds a 30-60-90 day plan for stepping into an unfamiliar domain |
| Grow the team | [`create-learning-plan`](plugins/create-learning-plan) | Sequences expert content into a learning path for a career transition |

## Requirements

The O'Reilly Expert Intelligence MCP server must be connected to your agent. The skills call
`ask_oreilly_experts`, `search_oreilly_content`, and `get_oreilly_citation`; without those tools a
skill still triggers but has nothing to ground its answer in. Access requires an O'Reilly learning
platform account.

The skills themselves ship no MCP servers, no hooks, and no executable code — each one is a
`SKILL.md` instruction file.

## Install

Click a skill in the table above — each skill's README covers what it produces, the prompts it
fires on, and step-by-step install instructions for Claude desktop, the Claude CLI, and Codex.

After installing, restart your session or app — skills are discovered at startup. Then just
describe your problem. Skills trigger on the shape of the request, so you don't need to name one.
