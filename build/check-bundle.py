#!/usr/bin/env python3
"""Check that the generated all-in-one Expert Intelligence plugin is complete."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / "plugins" / "oreilly-expert-intelligence"
EXPECTED_SKILLS = {
    "assess-team-structure",
    "compare-implementation-approaches",
    "create-decision-brief",
    "create-learning-plan",
    "evaluate-security-risk",
    "forecast-project-delivery",
    "plan-domain-rampup",
    "plan-production-ready-ai",
    "plan-service-reliability",
    "review-architecture-decision",
    "review-technical-proposal",
}

assert BUNDLE.is_dir(), f"missing bundle directory: {BUNDLE}"
assert BUNDLE.joinpath(".claude-plugin", "plugin.json").is_file()
assert BUNDLE.joinpath(".codex-plugin", "plugin.json").is_file()
assert BUNDLE.joinpath("README.md").is_file()
assert "skills/oreilly-expert-intelligence/SKILL.md" not in BUNDLE.joinpath("README.md").read_text()
assert {
    path.parent.name
    for path in BUNDLE.glob("skills/*/SKILL.md")
} == EXPECTED_SKILLS

claude = json.loads(BUNDLE.joinpath(".claude-plugin", "plugin.json").read_text())
codex = json.loads(BUNDLE.joinpath(".codex-plugin", "plugin.json").read_text())
assert claude["name"] == "oreilly-expert-intelligence"
assert codex["interface"]["displayName"] == "O'Reilly Expert Intelligence"

marketplace = json.loads(ROOT.joinpath(".claude-plugin", "marketplace.json").read_text())
plugins = {plugin["name"]: plugin for plugin in marketplace["plugins"]}
assert len(plugins) == 12
assert plugins["oreilly-expert-intelligence"] == {
    "name": "oreilly-expert-intelligence",
    "source": "./plugins/oreilly-expert-intelligence",
    "description": "A cited expert research toolkit for engineering decisions, delivery, reliability, security, and team growth.",
    "displayName": "O'Reilly Expert Intelligence",
    "version": "0.1.0",
    "author": {"name": "O'Reilly Media", "url": "https://www.oreilly.com"},
    "category": "productivity",
    "keywords": ["oreilly", "expert-intelligence", "citations"],
}
