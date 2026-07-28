# Technical Proposal Review

Reviews an RFC for gaps and generates the pushback questions you'll get.

Part of the [expert-intelligence-skills](https://github.com/oreillymedia/expert-intelligence-skills)
marketplace. Each skill installs as its own plugin, so you can take just this one.

## What you get

A read of what the proposal claims versus what it assumes, the gaps a practitioner would catch, and
a set of concrete pushback questions to expect in review. Aimed at a better proposal, not a defeated
author — where the design is sound it says so.

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
4. Install **Technical Proposal Review** from the list.

Anthropic's walkthrough has the current UI:
https://support.claude.com/en/articles/13837440-use-plugins-in-claude

</details>

<details>
<summary><b>Claude CLI</b></summary>

From inside a session:

```
/plugin marketplace add oreillymedia/expert-intelligence-skills
/plugin install review-technical-proposal@expert-intelligence-skills
```

</details>

<details>
<summary><b>Codex</b></summary>

For both the Codex CLI and Codex desktop, you must use the terminal to add the marketplace — run:

```
codex plugin marketplace add oreillymedia/expert-intelligence-skills
codex plugin add review-technical-proposal@expert-intelligence-skills
```

</details>

<details>
<summary><b>Manual: copy the file</b> — works anywhere</summary>

Download
[SKILL.md](https://github.com/oreillymedia/expert-intelligence-skills/blob/main/plugins/review-technical-proposal/skills/review-technical-proposal/SKILL.md)
with the **Download raw file** button, then:

- **Claude desktop, web, or Cowork:** open **Customize** → **Skills**, click **Add** → **Upload
  skill**, and drop in the `.md` file — it's accepted as-is, no zipping needed. One upload covers
  both Chat and Cowork.
- **Claude Code or Codex CLI:** save it, filename unchanged, as `review-technical-proposal/SKILL.md` inside
  `~/.claude/skills/` or `~/.codex/skills/`. This route is CLI-only — the desktop and web apps
  don't read those directories.

**Important:** When using this method you won't receive updates to this skill.

</details>

## Try it

> Review this RFC and find the gaps.
>
> What pushback should I expect on this design?
>
> Where is my proposal weakest?

You don't need to name the skill. It triggers on the shape of the request — see the `description`
field in `skills/review-technical-proposal/SKILL.md` for the full set of trigger conditions.
