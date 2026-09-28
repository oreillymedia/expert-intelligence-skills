---
name: plan-production-ready-ai
description: Plans a production deployment for an ML or AI model using cited O'Reilly MLOps sources, covering versioning, release strategy, monitoring, rollback, and staged capability growth. Use when a team needs a right-sized model deployment, rollout, drift-monitoring, or MLOps plan; not for choosing or training the model, comparing one implementation library, or making an organization-wide AI-platform adoption decision.
---

# Plan Production Ready AI

Produce a right-sized production deployment plan for an ML or AI model. Recommend the smallest auditable approach that manages the stated risk, and give deferred capabilities observable adoption triggers.

Match the plan’s ambition to the team’s maturity; avoid over-engineering.

This is a planning task. Do not create files, update project memory, or save the team's context unless the user explicitly asks you to.

## Source and citation rules

Use only sources returned by the O'Reilly MCP tools. Tool names below are unqualified because the server name is user-configured; when the runtime requires qualified names, prepend the configured server name (for example, `oreilly:ask_oreilly_experts`). Cite each selected result as `[title](url) by authors`, using `product_title` when the result provides it instead of `title`. Copy the title and URL exactly from that same result; do not alter, normalize, shorten, repair, or reconstruct the URL. Use a string-valued `authors` field unchanged; for a list, join the returned names in order with commas. When `get_oreilly_citation` returns a fully rendered `citation_format`, use it unchanged. Never invent or reconstruct metadata or quotations. Remove a citation that cannot be verified against the tool result. Present uncited conclusions as your own analysis or omit them.

## Step 1: Frame the deployment context

The recommendation hinges on context. Ask one focused question only when missing team size, infrastructure maturity, or model criticality could reverse the recommendation. Otherwise state assumptions. Establish:

- **The model and its role** — batch or real-time? How bad is a wrong prediction (a rec ranking vs. a credit decision)?
- **Existing infra** — any CI/CD, monitoring, model registry, or nothing yet?
- **Constraints** — latency, scale, regulatory, on-call capacity.

## Step 2: Research the deployment decisions

Research in this order:

1. Turn model versioning, rollout, monitoring, rollback, and right-sizing into targeted questions.
2. Use `ask_oreilly_experts` and/or `search_oreilly_content` as appropriate for the research need, following their tool descriptions.
3. Select only results that directly support a deployment recommendation or adoption trigger.
4. Draft from the verified evidence. If no directly relevant source surfaces, state the evidence gap instead of citing a weaker source.

Search each deployment dimension and the small-team/right-sizing angle:

- "model versioning approaches and when each is worth it"
- "shadow deployment vs canary for ML models trade-offs"
- "model drift monitoring — what to monitor and how"
- "minimum viable MLOps for a small team / no existing infrastructure"
- "MLOps maturity levels what to adopt when"

Search the model's actual deployment mode, risk, and team maturity; do not force an enterprise MLOps pattern or a familiar title into the plan.

MLOps tooling and practice move quickly — what counts as "minimum viable" monitoring or drift detection shifts year over year. Favor the most recent coverage of each dimension; a few-year-old take can already describe a previous generation of practice, not the current one.

## Step 3: Draft the deployment plan

Lead with the recommendation, then compare only the plausible alternatives needed to explain it. Do not give enterprise tooling equal space when the team's scale or maturity has already ruled it out. Structure:

---

### Production Deployment Plan — [Model / Team context]

**Context assumed:** team size, infra maturity, model criticality (state it plainly so the reader can correct you).

**Model versioning**
- *Recommendation for you:* the smallest auditable approach that supports reproducibility, per-decision traceability, and rollback.
- *Alternatives considered:* briefly name only the credible next-heavier option and the condition that would justify it.

**Deployment / rollout strategy**
- *Recommendation for you:* a staged path calibrated to criticality and existing infrastructure, with entry and exit criteria, rollback triggers, fallback behavior, and an owner.
- Mention rejected rollout modes only when the contrast explains a consequential choice.

**Drift & monitoring**
- *Recommendation for you:* the minimum set of data, prediction, operational, and delayed-outcome signals needed to catch the stated harm. For each alert, say what happens when it trips and who responds. Avoid a catalog of monitoring products.

**Start here / add later**
- The crawl-walk-run: what to stand up before launch vs. what to defer until the team and traffic justify it.

---

## Step 4: Verify the deployment plan

Before responding:

1. Check that recommendations match the model's criticality, team size, infrastructure maturity, and operational capacity.
2. Confirm that the plan distinguishes launch requirements from capabilities that can wait.
3. Confirm that rollout includes rollback criteria and monitoring includes a response, not just a metric.
4. Compare every citation with the MCP result — title, author, edition, and URL must match exactly — and remove any citation you cannot verify rather than repairing it.
5. Remove tooling or process that does not manage a stated risk.
6. Confirm that deferred capabilities have an observable adoption trigger rather than an arbitrary maturity milestone.

If any check fails, revise and run these checks again. Do not respond until all of them pass.

## Principles

Prefer current coverage because MLOps tooling changes quickly. State assumptions, recommend the simplest approach that manages the stated risk, and say what can safely wait. A registry, feature store, dedicated drift platform, or automated retraining pipeline must be justified by a current requirement; otherwise name the concrete trigger for adding it later. Where practice is unsettled, present the decision criteria rather than false consensus.
