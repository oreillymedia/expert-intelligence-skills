# Delivery Forecast

Pressure-tests a plan into realistic timelines and delivery risks.

Part of the [expert-intelligence-skills](https://github.com/oreillymedia/expert-intelligence-skills)
marketplace. Each skill installs as its own plugin, so you can take just this one.

## What you get

A forecast that separates the scope evidence from the schedule-risk drivers, then lands on a range
rather than a single date — with the specific risks that would push you to the far end and what
published estimation research says about each.

Output is grounded in what practitioners have actually published — every claim carries a citation
back to the O'Reilly learning platform, and the skill is instructed never to cite a title, author,
or link that didn't surface in its search.

## Before you install

You need two things:

- **An O'Reilly learning platform account.** The skill's answers come from O'Reilly's library;
  without an account there is nothing to search.
- **The O'Reilly Expert Intelligence MCP server connected to your agent.** This is the connector
  that lets Claude (or Codex) search O'Reilly content.

## Install

Expand the path that matches your setup. **Whichever you use, restart your session or app
afterward** so the new skill is picked up.

<details>
<summary><b>Claude desktop</b></summary>

1. Open **Customize**, then **Plugins**.
2. Click **+**, then **Add marketplace**, then **Add from a repository**.
3. Paste `oreillymedia/expert-intelligence-skills`.
4. Install **Delivery Forecast** from the list.

Anthropic's walkthrough has the current UI:
https://support.claude.com/en/articles/13837440-use-plugins-in-claude

</details>

<details>
<summary><b>Claude CLI</b></summary>

From inside a session:

```
/plugin marketplace add oreillymedia/expert-intelligence-skills
/plugin install forecast-project-delivery@expert-intelligence-skills
```

</details>

<details>
<summary><b>Codex</b></summary>

For both the Codex CLI and Codex desktop, you must use the terminal to add the marketplace — run:

```
codex plugin marketplace add oreillymedia/expert-intelligence-skills
codex plugin add forecast-project-delivery@expert-intelligence-skills
```

</details>

<details>
<summary><b>Manual: copy the file</b> — works anywhere</summary>

Download
[SKILL.md](https://github.com/oreillymedia/expert-intelligence-skills/blob/main/plugins/forecast-project-delivery/skills/forecast-project-delivery/SKILL.md)
with the **Download raw file** button, then:

- **Claude desktop, web, or Cowork:** open **Customize** → **Skills**, click **Add** → **Upload
  skill**, and drop in the `.md` file — it's accepted as-is, no zipping needed. One upload covers
  both Chat and Cowork.
- **Claude Code or Codex CLI:** save it, filename unchanged, as `forecast-project-delivery/SKILL.md` inside
  `~/.claude/skills/` or `~/.codex/skills/`. This route is CLI-only — the desktop and web apps
  don't read those directories.

**Important:** When using this method you won't receive updates to this skill.

</details>

## Try it

> Pressure-test this six-week delivery plan.
>
> Is our Q3 migration timeline realistic?
>
> What delivery risks is this plan missing?

You don't need to name the skill. It triggers on the shape of the request — see the `description`
field in `skills/forecast-project-delivery/SKILL.md` for the full set of trigger conditions.
