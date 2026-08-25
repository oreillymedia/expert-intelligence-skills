#!/usr/bin/env python3
"""Generate the plugin tree and marketplace manifest from the skill metadata below.

This is build-time tooling and deliberately lives in `build.local/`, which is gitignored —
`oreillymedia/expert-intelligence-skills` is public and ships only the generated artifacts.
It will move to a dedicated build repo; until then it runs by hand.

One plugin per skill. Each plugin carries two manifests: `.claude-plugin/plugin.json`
(what Claude Code reads) and `.codex-plugin/plugin.json` (what Codex prefers; Codex falls
back to the Claude manifest, but the Codex manifest is where presentation metadata lives
that Claude Code's validator would flag as unknown fields).

SKILL.md is copied verbatim from the source repo — this script never edits skill content.
test-cases.md stays in the source repo; it is not for public consumption. Re-running this
script is idempotent, and it removes any test-cases.md left over from earlier runs.

Usage:
    python3 build.local/build-plugins.py [--source PATH]
"""

from __future__ import annotations

import argparse
import json
import textwrap
from pathlib import Path

import yaml

BUILD_DIR = Path(__file__).resolve().parent
REPO_ROOT = BUILD_DIR.parent
TEMPLATE = BUILD_DIR / "plugin-readme.template.md"
DEFAULT_SOURCE = Path.home() / "Projects/oreilly/orm-skill-creator/oreilly-created-skills/release-skills"

MARKETPLACE_NAME = "expert-intelligence-skills"
VERSION = "0.1.0"
AUTHOR = {"name": "O'Reilly Media", "url": "https://www.oreilly.com"}
HOMEPAGE = "https://github.com/oreillymedia/expert-intelligence-skills"

# Order here is the order Codex renders plugins in, and the order of the README table.
# Grouped by the buyer-facing bucket rather than alphabetically.
SKILLS = [
    {
        "name": "create-decision-brief",
        "display_name": "Decision Brief",
        "bucket": "De-risk a decision",
        "category": "productivity",
        "one_liner": 'Turns a "should we?" into a memo-ready recommendation grounded in expert consensus.',
        "what_you_get": (
            "A half-page brief that leads with the recommendation, then lays out where experts agree, "
            "where they disagree, the failure modes teams at your scale hit, what has to be true first, "
            "and what evidence would flip the call. Scannable in under two minutes and forwardable to a "
            "board or a skeptical peer."
        ),
        "prompts": [
            "Should we adopt platform engineering org-wide?",
            "Is it worth migrating off our monolith?",
            "Build or buy our feature-flag system?",
        ],
    },
    {
        "name": "compare-implementation-approaches",
        "display_name": "Implementation Advisor",
        "bucket": "Defend a design",
        "category": "development",
        "one_liner": "Compares implementation approaches with cited trade-offs and a code example.",
        "what_you_get": (
            "A direct recommendation between the approaches you're weighing, with the trade-offs that "
            "actually apply at your constraints, and a concrete code example of the recommended path. "
            "Deliberately light on searching — it answers rather than producing a research report."
        ),
        "prompts": [
            "Compare Kafka vs SQS for our event pipeline.",
            "Which caching approach fits our read load?",
            "Postgres or DynamoDB for this service?",
        ],
    },
    {
        "name": "review-architecture-decision",
        "display_name": "Architecture Decision Review",
        "bucket": "Defend a design",
        "category": "development",
        "one_liner": "Evaluates a system design against expert trade-off analysis.",
        "what_you_get": (
            "A review of your design that names the trade-offs you've implicitly accepted, checks them "
            "against how practitioners describe the same decisions, and flags the ones that tend to bite "
            "later. Credits what's sound instead of manufacturing objections."
        ),
        "prompts": [
            "Review my event-driven design's trade-offs.",
            "Poke holes in this multi-tenant architecture.",
            "Is this sharding plan sound at our scale?",
        ],
    },
    {
        "name": "review-technical-proposal",
        "display_name": "Technical Proposal Review",
        "bucket": "Defend a design",
        "category": "development",
        "one_liner": "Reviews an RFC for gaps and generates the pushback questions you'll get.",
        "what_you_get": (
            "A read of what the proposal claims versus what it assumes, the gaps a practitioner would "
            "catch, and a set of concrete pushback questions to expect in review. Aimed at a better "
            "proposal, not a defeated author — where the design is sound it says so."
        ),
        "prompts": [
            "Review this RFC and find the gaps.",
            "What pushback should I expect on this design?",
            "Where is my proposal weakest?",
        ],
    },
    {
        "name": "evaluate-security-risk",
        "display_name": "Security Risk Review",
        "bucket": "Defend a design",
        "category": "security",
        "one_liner": "Produces a STRIDE threat model, flagging the risks teams commonly miss.",
        "what_you_get": (
            "A threat model over your system — STRIDE by default, or another framework if you name one — "
            "with each threat tied to published analysis rather than a generic checklist, and explicit "
            "attention to the categories teams routinely skip."
        ),
        "prompts": [
            "Threat model our new payments endpoint.",
            "What security risks are we missing here?",
            "STRIDE review of this auth flow.",
        ],
    },
    {
        "name": "forecast-project-delivery",
        "display_name": "Delivery Forecast",
        "bucket": "De-risk a decision",
        "category": "productivity",
        "one_liner": "Pressure-tests a plan into realistic timelines and delivery risks.",
        "what_you_get": (
            "A forecast that separates the scope evidence from the schedule-risk drivers, then lands on a "
            "range rather than a single date — with the specific risks that would push you to the far end "
            "and what published estimation research says about each."
        ),
        "prompts": [
            "Pressure-test this six-week delivery plan.",
            "Is our Q3 migration timeline realistic?",
            "What delivery risks is this plan missing?",
        ],
    },
    {
        "name": "plan-service-reliability",
        "display_name": "Reliability Plan",
        "bucket": "Ship with confidence",
        "category": "monitoring",
        "one_liner": "Drafts SLOs and an error-budget policy for a new or evolving service.",
        "what_you_get": (
            "Candidate SLIs and SLOs sized to what the service actually does and who depends on it, plus "
            "an error-budget policy that says what happens when the budget burns — grounded in how SRE "
            "practitioners describe setting these, not in round numbers."
        ),
        "prompts": [
            "Draft SLOs for our new checkout service.",
            "Set an error-budget policy for this API.",
            "What should we alert on for this service?",
        ],
    },
    {
        "name": "plan-production-ready-ai",
        "display_name": "Production Ready AI",
        "bucket": "Ship with confidence",
        "category": "deployment",
        "one_liner": "Recommends an ML deployment strategy calibrated to your team's maturity.",
        "what_you_get": (
            "A deployment plan matched to what your team can actually operate today — a team with no "
            "MLOps practice gets different advice than one with a platform — covering rollout shape, "
            "monitoring, and the failure modes that show up at that maturity level."
        ),
        "prompts": [
            "How should we deploy this model to prod?",
            "We're new to MLOps — where do we start?",
            "Plan a safe rollout for this ML feature.",
        ],
    },
    {
        "name": "assess-team-structure",
        "display_name": "Team Assessment",
        "bucket": "De-risk a decision",
        "category": "productivity",
        "one_liner": "Diagnoses team structure problems against expert org-design frameworks.",
        "what_you_get": (
            "A diagnosis of what's actually causing the friction — coupling, cognitive load, ownership "
            "gaps — read against published org-design frameworks, with the changes worth making and the "
            "ones that would just reshuffle the org chart."
        ),
        "prompts": [
            "Our team keeps blocking on other teams — why?",
            "Diagnose our platform team's structure.",
            "Should we split this 30-person team?",
        ],
    },
    {
        "name": "plan-domain-rampup",
        "display_name": "Ramp Plan",
        "bucket": "Grow the team",
        "category": "learning",
        "one_liner": "Builds a 30-60-90 day plan for stepping into an unfamiliar domain.",
        "what_you_get": (
            "A 30-60-90 plan with observable milestones, the reading and events that support each phase, "
            "and agendas for the conversations to have with the people who already own the domain. "
            "Sequenced so you're credible early rather than well-read late."
        ),
        "prompts": [
            "I'm taking over search — build a ramp plan.",
            "30-60-90 for a domain I don't know yet.",
            "How do I get credible in Kafka fast?",
        ],
    },
    {
        "name": "create-learning-plan",
        "display_name": "Learning Plan",
        "bucket": "Grow the team",
        "category": "learning",
        "one_liner": "Sequences expert content into a learning path for a career transition.",
        "what_you_get": (
            "A learning path across books, video, and live events that says why each item comes when it "
            "does — the sequencing is the value a reading list doesn't give you. Paced to the hours you "
            "actually have, with behavioral markers for whether it's working."
        ),
        "prompts": [
            "Plan my move from backend to ML.",
            "Learning path to staff engineer.",
            "Sequence reading for a platform role.",
        ],
    },
]

BUNDLE = {
    "name": "oreilly-expert-intelligence",
    "display_name": "O'Reilly Expert Intelligence",
    "category": "productivity",
    "one_liner": (
        "A cited expert research toolkit for engineering decisions, delivery, reliability, security, "
        "and team growth."
    ),
    "what_you_get": (
        "All Expert Intelligence skills in one install: decision briefs, delivery forecasts, "
        "architecture and proposal reviews, security assessments, reliability and AI plans, and "
        "learning and team-development guidance."
    ),
    "prompts": [
        "Help me decide whether to adopt platform engineering.",
        "Review this architecture and find the trade-offs.",
        "Build a 30-60-90 plan for my new domain.",
    ],
    "manual_install": (
        "The all-in-one plugin is available through the marketplaces above. To install a skill "
        "manually, use that individual skill's README."
    ),
    "description_path": "the individual `SKILL.md` files",
}

WEBSITE_URL = "https://learning.oreilly.com/expert-intelligence/"
MCP_SERVER_URL = "https://api.oreilly.com/api/expert/v1/mcp"


def mcp_config() -> dict:
    """Configure the remote MCP server; authentication uses its OAuth flow."""
    return {
        "mcpServers": {
            "oreilly-expert-intelligence": {
                "type": "http",
                "url": MCP_SERVER_URL,
            }
        }
    }


def claude_manifest(skill: dict) -> dict:
    return {
        "name": skill["name"],
        "version": VERSION,
        "description": skill["one_liner"],
        "author": AUTHOR,
        "homepage": HOMEPAGE,
        "repository": HOMEPAGE,
        "license": "Apache-2.0",
        "keywords": ["oreilly", "expert-intelligence", "citations", skill["category"]],
    }


def codex_manifest(skill: dict) -> dict:
    return {
        "name": skill["name"],
        "version": VERSION,
        "description": skill["one_liner"],
        "author": AUTHOR,
        "homepage": HOMEPAGE,
        "repository": HOMEPAGE,
        "license": "Apache-2.0",
        "keywords": ["oreilly", "expert-intelligence", "citations", skill["category"]],
        "skills": "./skills/",
        "interface": {
            "displayName": skill["display_name"],
            "shortDescription": skill["one_liner"],
            "longDescription": skill["what_you_get"],
            "developerName": "O'Reilly Media",
            "category": skill["category"],
            "websiteURL": WEBSITE_URL,
            "defaultPrompt": skill["prompts"][:3],
        },
    }


def marketplace_manifest() -> dict:
    return {
        "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
        "name": MARKETPLACE_NAME,
        "description": (
            "O'Reilly Expert Intelligence skills — ground engineering and leadership decisions in "
            "expert consensus from the O'Reilly learning platform, with citations."
        ),
        "owner": AUTHOR,
        "interface": {"displayName": "O'Reilly Expert Intelligence"},
        "plugins": [
            {
                "name": s["name"],
                # Claude Code requires the string form here and rejects {"source": "local", ...}.
                # Codex accepts the string form too, so one entry serves both harnesses.
                "source": f"./plugins/{s['name']}",
                "description": s["one_liner"],
                "displayName": s["display_name"],
                "version": VERSION,
                "author": AUTHOR,
                "category": s["category"],
                "keywords": ["oreilly", "expert-intelligence", "citations"],
                # No `policy` block: Codex defaults to AVAILABLE/ON_INSTALL and Claude Code's
                # validator warns on the field. The plugin's remote MCP server is configured in
                # `.mcp.json`, where its OAuth flow is handled by the client.
            }
            for s in [*SKILLS, BUNDLE]
        ],
    }


def render_plugin_readme(skill: dict, template: str) -> str:
    prompts = "\n>\n".join(f"> {p}" for p in skill["prompts"])
    description_path = skill.get("description_path", f"`skills/{skill['name']}/SKILL.md`")
    manual_install = skill.get(
        "manual_install",
        textwrap.dedent(
            """\
            Download
            [SKILL.md](https://github.com/oreillymedia/expert-intelligence-skills/blob/main/plugins/{{SKILL_NAME}}/skills/{{SKILL_NAME}}/SKILL.md)
            with the **Download raw file** button, then:

            - **Claude desktop, web, or Cowork:** open **Customize** → **Skills**, click **Add** → **Upload
              skill**, and drop in the `.md` file — it's accepted as-is, no zipping needed. One upload covers
              both Chat and Cowork.
            - **Claude Code or Codex CLI:** save it, filename unchanged, as `{{SKILL_NAME}}/SKILL.md` inside
              `~/.claude/skills/` or `~/.codex/skills/`. This route is CLI-only — the desktop and web apps
              don't read those directories.

            **Important:** When using this method you won't receive updates to this skill.
            """
        ),
    )
    return (
        template
        .replace("{{DISPLAY_NAME}}", skill["display_name"])
        .replace("{{SKILL_NAME}}", skill["name"])
        .replace("{{ONE_LINER}}", textwrap.fill(skill["one_liner"], width=100))
        .replace("{{WHAT_YOU_GET}}", textwrap.fill(skill["what_you_get"], width=100))
        .replace("{{MANUAL_INSTALL}}", manual_install.replace("{{SKILL_NAME}}", skill["name"]))
        .replace("{{DESCRIPTION_PATH}}", description_path)
        .replace("{{EXAMPLE_PROMPTS}}", prompts)
    )


def normalize_frontmatter(text: str, *, label: str) -> str:
    """Make SKILL.md frontmatter parse as YAML without altering the prose.

    Several source descriptions contain a bare `word: value` (e.g. "...before shipping: a
    threat model...") inside an unquoted scalar, which is a YAML syntax error. A skill whose
    frontmatter fails to parse loads with empty metadata, so it never auto-triggers.

    The descriptions also contain double quotes, so re-quoting would mean escaping. A folded
    block scalar (`>-`) sidesteps both problems and keeps the text byte-for-byte.
    """
    opener, frontmatter, body = text.split("---\n", 2)
    try:
        yaml.safe_load(frontmatter)
        return text
    except yaml.YAMLError:
        pass

    fixed_lines = []
    for line in frontmatter.split("\n"):
        prefix = "description: "
        if line.startswith(prefix) and not line[len(prefix):].lstrip().startswith((">", "|", '"', "'")):
            fixed_lines.append("description: >-")
            fixed_lines.append("  " + line[len(prefix):])
        else:
            fixed_lines.append(line)
    fixed = "\n".join(fixed_lines)

    yaml.safe_load(fixed)  # bubble up if the description was not the problem
    print(f"  fixed unparseable frontmatter in {label}")
    return opener + "---\n" + fixed + "---\n" + body


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE,
                        help="path to release-skills/ in oreillymedia/orm-skill-creator")
    args = parser.parse_args()

    if not args.source.is_dir():
        parser.error(f"source skill directory not found: {args.source}")

    template = TEMPLATE.read_text()

    for skill in SKILLS:
        name = skill["name"]
        src = args.source / name
        if not src.is_dir():
            parser.error(f"missing source skill: {src}")

        plugin_root = REPO_ROOT / "plugins" / name
        skill_dir = plugin_root / "skills" / name
        skill_dir.mkdir(parents=True, exist_ok=True)

        (skill_dir / "test-cases.md").unlink(missing_ok=True)
        skill_md = normalize_frontmatter((src / "SKILL.md").read_text(),
                                        label=f"{name}/SKILL.md")
        (skill_dir / "SKILL.md").write_text(skill_md)

        write_json(plugin_root / ".claude-plugin/plugin.json", claude_manifest(skill))
        write_json(plugin_root / ".codex-plugin/plugin.json", codex_manifest(skill))
        write_json(plugin_root / ".mcp.json", mcp_config())
        (plugin_root / "README.md").write_text(render_plugin_readme(skill, template))
        print(f"built plugins/{name}")

    bundle_root = REPO_ROOT / "plugins" / BUNDLE["name"]
    for skill in SKILLS:
        name = skill["name"]
        src = args.source / name
        skill_dir = bundle_root / "skills" / name
        skill_dir.mkdir(parents=True, exist_ok=True)
        skill_md = normalize_frontmatter((src / "SKILL.md").read_text(), label=f"{name}/SKILL.md")
        (skill_dir / "SKILL.md").write_text(skill_md)

    write_json(bundle_root / ".claude-plugin/plugin.json", claude_manifest(BUNDLE))
    write_json(bundle_root / ".codex-plugin/plugin.json", codex_manifest(BUNDLE))
    write_json(bundle_root / ".mcp.json", mcp_config())
    (bundle_root / "README.md").write_text(render_plugin_readme(BUNDLE, template))
    print(f"built plugins/{BUNDLE['name']}")

    write_json(REPO_ROOT / ".claude-plugin/marketplace.json", marketplace_manifest())
    print(f"built .claude-plugin/marketplace.json ({len(SKILLS) + 1} plugins)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
