# O'Reilly Expert Intelligence

A cited expert research toolkit for engineering decisions, delivery, reliability, security, and team
growth.

Part of the [expert-intelligence-skills](https://github.com/oreillymedia/expert-intelligence-skills)
marketplace. 

## What you get

All 11 Expert Intelligence skills in one install: decision briefs, delivery forecasts, architecture
and proposal reviews, security assessments, reliability and AI plans, and learning and team-
development guidance.

Output is grounded in what practitioners have actually published — every claim carries a citation
back to the O'Reilly learning platform, and the skill is instructed never to cite a title, author,
or link that didn't surface in its search.

## Install

Expand the path that matches your setup. **Whichever you use, restart your session or app
afterward** so the new skill is picked up.

<details>
<summary><b>Claude desktop</b></summary>

1. Open **Customize**, then **Plugins**.
2. Click **+**, then **Add marketplace**, then **Add from a repository**.
3. Paste `oreillymedia/expert-intelligence-skills`.
4. Install **O'Reilly Expert Intelligence** from the list.

Anthropic's walkthrough has the current UI:
https://support.claude.com/en/articles/13837440-use-plugins-in-claude

</details>

<details>
<summary><b>Claude CLI</b></summary>

From inside a session:

```
/plugin marketplace add oreillymedia/expert-intelligence-skills
/plugin install oreilly-expert-intelligence@expert-intelligence-skills
```

</details>

<details>
<summary><b>Codex</b></summary>

For both the Codex CLI and Codex desktop, you must use the terminal to add the marketplace — run:

```
codex plugin marketplace add oreillymedia/expert-intelligence-skills
codex plugin add oreilly-expert-intelligence@expert-intelligence-skills
```

</details>

<details>
<summary><b>Manual: copy the file</b> — works anywhere</summary>

The all-in-one plugin is available through the marketplaces above. To install a skill manually, use that individual skill's README.

</details>

## Requirements

An **O'Reilly learning platform account** is required to search the library. When installed as a
plugin, the O'Reilly Expert Intelligence MCP server is included automatically. If you copy an
individual skill manually instead, connect the MCP server yourself; see the
[MCP guide](https://www.oreilly.com/online-learning/support/mcp-guide.html) for setup steps.

## Try it

> Help me decide whether to adopt platform engineering.
>
> Review this architecture and find the trade-offs.
>
> Build a 30-60-90 plan for my new domain.

This skill triggers based on the shape of your context and prompt. See the
`description` field in the individual `SKILL.md` files for the full set of trigger conditions.
