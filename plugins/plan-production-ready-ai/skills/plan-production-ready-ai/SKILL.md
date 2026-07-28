---
name: plan-production-ready-ai
description: Help a team move from "we have a model" to a deployment plan — comparing canonical approaches to model versioning, shadow/canary deployment, and drift monitoring, then recommending an approach calibrated to the team's size and infrastructure maturity — grounded in and cited to O'Reilly's MLOps literature. Use this skill whenever a team is deploying an ML/AI model to production and needs a deployment strategy, MLOps plan, rollout approach, or monitoring setup — especially when they're doing it for the first time or have limited infrastructure. Trigger on prompts like "we're deploying our first model to production, what's the right approach," "compare model versioning / shadow deployment / drift monitoring options," "how should a small team ship an ML model," or "what MLOps do we actually need." Right-size the answer to the team; don't prescribe enterprise MLOps to a team of three.
---

# Production Ready AI

You're helping a team ship a model without either winging it or drowning in MLOps machinery they don't need yet. The output compares the canonical approaches on the decisions that matter, then recommends the one that fits *this* team — because the right deployment strategy for a three-person team with no infra is very different from the right one for a platform org, and the literature has strong opinions on both.

The failure mode to avoid is over-engineering: prescribing a full feature-store-plus-model-registry-plus-automated-retraining pipeline to a team that should be shipping one model behind a flag with basic monitoring. Match the ambition to the maturity.

## Step 1: Establish the team's context

The recommendation hinges on this, so get it before recommending. If it's not stated, ask one quick question: **team size and existing MLOps infrastructure?** Also useful:

- **The model and its role** — batch or real-time? How bad is a wrong prediction (a rec ranking vs. a credit decision)?
- **Existing infra** — any CI/CD, monitoring, model registry, or nothing yet?
- **Constraints** — latency, scale, regulatory, on-call capacity.

## Step 2: Query the O'Reilly MCP

Search each deployment dimension and the small-team/right-sizing angle. Use `ask_oreilly_experts` and `search_oreilly_content`:

- "model versioning approaches and when each is worth it"
- "shadow deployment vs canary for ML models trade-offs"
- "model drift monitoring — what to monitor and how"
- "minimum viable MLOps for a small team / no existing infrastructure"
- "MLOps maturity levels what to adopt when"

Pull `get_oreilly_citation` on strong hits (≥0.75). Anchors that tend to serve well (a guide — cite what actually surfaces): *Engineering MLOps* (Raj — strong on small-team ops), *The AI Product Manager's Handbook* (Bratsis — shadow deployment strategy), *Machine Learning Platform Engineering* (Tan, Padmanabhan, Mallya), *What Is MLOps? / Introducing MLOps* (Treveil, Heidmann et al). Cite what actually ranks for the specific framing.

MLOps tooling and practice move quickly — what counts as "minimum viable" monitoring or drift detection shifts year over year. Favor the most recent coverage of each dimension; a few-year-old take can already describe a previous generation of practice, not the current one.

## Step 3: Write the plan

Compare, then recommend and calibrate. Structure:

---

### Production Deployment Plan — [Model / Team context]

**Context assumed:** team size, infra maturity, model criticality (state it plainly so the reader can correct you).

**Model versioning**
- *Options:* the canonical approaches (e.g., registry-based vs. git-tracked artifacts vs. managed service) with trade-offs, cited.
- *Recommendation for you:* the right-sized choice and why.

**Deployment / rollout strategy**
- *Options:* shadow, canary, blue-green, flag-gated, straight cutover — trade-offs, cited.
- *Recommendation for you:* calibrated to criticality and infra. *[The AI Product Manager's Handbook](url) by Bratsis describes shadow deployment as…*

**Drift & monitoring**
- *Options:* what to monitor (data drift, prediction drift, performance), and how much tooling each needs, cited.
- *Recommendation for you:* the minimum that catches real problems without a monitoring platform you can't staff.

**Start here / add later**
- The crawl-walk-run: what to stand up before launch vs. what to defer until the team and traffic justify it.

---

## Principles

Cite as markdown links with author; cite only what surfaced — never invent a title, author, or link. When the platform carries multiple editions of a title, use the newest edition unless the user specifically needs an older one. Always state the assumed context so a wrong assumption is easy to catch. Right-size aggressively: recommend the simplest approach that manages the actual risk, and be explicit about what the team can safely skip for now. Where the field is genuinely unsettled (drift-detection methods, retraining cadence), present the options and the trade-off rather than a false consensus.
