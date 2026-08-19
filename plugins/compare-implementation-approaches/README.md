# Implementation Advisor

Compares implementation approaches with cited trade-offs and a code example.

Part of the [expert-intelligence-skills](https://github.com/oreillymedia/expert-intelligence-skills)
marketplace. 

## What you get

A direct recommendation between the approaches you're weighing, with the trade-offs that actually
apply at your constraints, and a concrete code example of the recommended path. Deliberately light
on searching — it answers rather than producing a research report.

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
4. Install **Implementation Advisor** from the list.

Anthropic's walkthrough has the current UI:
https://support.claude.com/en/articles/13837440-use-plugins-in-claude

</details>

<details>
<summary><b>Claude CLI</b></summary>

From inside a session:

```
/plugin marketplace add oreillymedia/expert-intelligence-skills
/plugin install compare-implementation-approaches@expert-intelligence-skills
```

</details>

<details>
<summary><b>Codex</b></summary>

For both the Codex CLI and Codex desktop, you must use the terminal to add the marketplace — run:

```
codex plugin marketplace add oreillymedia/expert-intelligence-skills
codex plugin add compare-implementation-approaches@expert-intelligence-skills
```

</details>

<details>
<summary><b>Manual: copy the file</b> — works anywhere</summary>

Download
[SKILL.md](https://github.com/oreillymedia/expert-intelligence-skills/blob/main/plugins/compare-implementation-approaches/skills/compare-implementation-approaches/SKILL.md)
with the **Download raw file** button, then:

- **Claude desktop, web, or Cowork:** open **Customize** → **Skills**, click **Add** → **Upload
  skill**, and drop in the `.md` file — it's accepted as-is, no zipping needed. One upload covers
  both Chat and Cowork.
- **Claude Code or Codex CLI:** save it, filename unchanged, as `compare-implementation-approaches/SKILL.md` inside
  `~/.claude/skills/` or `~/.codex/skills/`. This route is CLI-only — the desktop and web apps
  don't read those directories.

**Important:** When using this method you won't receive updates to this skill.


</details>

## Requirements

An **O'Reilly learning platform account** is required to search the library. When installed as a
plugin, the O'Reilly Expert Intelligence MCP server is included automatically. If you copy an
individual skill manually instead, connect the MCP server yourself; see the
[MCP guide](https://www.oreilly.com/online-learning/support/mcp-guide.html) for setup steps.

## Try it

> Compare Kafka vs SQS for our event pipeline.
>
> Which caching approach fits our read load?
>
> Postgres or DynamoDB for this service?

This skill triggers based on the shape of your context and prompt. See the
`description` field in `skills/compare-implementation-approaches/SKILL.md` for the full set of trigger conditions.
