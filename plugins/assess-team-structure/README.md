# Team Assessment

Diagnoses team structure problems against expert org-design frameworks.

Part of the [expert-intelligence-skills](https://github.com/oreillymedia/expert-intelligence-skills)
marketplace. 

## What you get

A diagnosis of what's actually causing the friction — coupling, cognitive load, ownership gaps —
read against published org-design frameworks, with the changes worth making and the ones that would
just reshuffle the org chart.

Output is grounded in what practitioners have actually published — every claim carries a citation
back to the O'Reilly learning platform, and the skill is instructed never to cite a title, author,
or link that didn't surface in its search.

## Before you install

You need two things:

- **An O'Reilly learning platform account.** The skill's answers come from O'Reilly's library;
  without an account there is nothing to search.
- **The O'Reilly Expert Intelligence MCP server connected to your agent.** This is the connector
  that lets Claude (or Codex) search O'Reilly content. See the
  [MCP guide](https://www.oreilly.com/online-learning/support/mcp-guide.html) for setup steps.

## Install

Expand the path that matches your setup. **Whichever you use, restart your session or app
afterward** so the new skill is picked up.

<details>
<summary><b>Claude desktop</b></summary>

1. Open **Customize**, then **Plugins**.
2. Click **+**, then **Add marketplace**, then **Add from a repository**.
3. Paste `oreillymedia/expert-intelligence-skills`.
4. Install **Team Assessment** from the list.

Anthropic's walkthrough has the current UI:
https://support.claude.com/en/articles/13837440-use-plugins-in-claude

</details>

<details>
<summary><b>Claude CLI</b></summary>

From inside a session:

```
/plugin marketplace add oreillymedia/expert-intelligence-skills
/plugin install assess-team-structure@expert-intelligence-skills
```

</details>

<details>
<summary><b>Codex</b></summary>

For both the Codex CLI and Codex desktop, you must use the terminal to add the marketplace — run:

```
codex plugin marketplace add oreillymedia/expert-intelligence-skills
codex plugin add assess-team-structure@expert-intelligence-skills
```

</details>

<details>
<summary><b>Manual: copy the file</b> — works anywhere</summary>

Download
[SKILL.md](https://github.com/oreillymedia/expert-intelligence-skills/blob/main/plugins/assess-team-structure/skills/assess-team-structure/SKILL.md)
with the **Download raw file** button, then:

- **Claude desktop, web, or Cowork:** open **Customize** → **Skills**, click **Add** → **Upload
  skill**, and drop in the `.md` file — it's accepted as-is, no zipping needed. One upload covers
  both Chat and Cowork.
- **Claude Code or Codex CLI:** save it, filename unchanged, as `assess-team-structure/SKILL.md` inside
  `~/.claude/skills/` or `~/.codex/skills/`. This route is CLI-only — the desktop and web apps
  don't read those directories.

**Important:** When using this method you won't receive updates to this skill.

</details>

## Try it

> Our team keeps blocking on other teams — why?
>
> Diagnose our platform team's structure.
>
> Should we split this 30-person team?

This skill triggers based on the shape of your context and prompt. See the
`description` field in `skills/assess-team-structure/SKILL.md` for the full set of
trigger conditions.
