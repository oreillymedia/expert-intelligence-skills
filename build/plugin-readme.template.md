# {{DISPLAY_NAME}}

{{ONE_LINER}}

Part of the [expert-intelligence-skills](https://github.com/oreillymedia/expert-intelligence-skills)
marketplace. 

## What you get

{{WHAT_YOU_GET}}

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
4. Install **{{DISPLAY_NAME}}** from the list.

Anthropic's walkthrough has the current UI:
https://support.claude.com/en/articles/13837440-use-plugins-in-claude

</details>

<details>
<summary><b>Claude CLI</b></summary>

From inside a session:

```
/plugin marketplace add oreillymedia/expert-intelligence-skills
/plugin install {{SKILL_NAME}}@expert-intelligence-skills
```

</details>

<details>
<summary><b>Codex</b></summary>

For both the Codex CLI and Codex desktop, you must use the terminal to add the marketplace — run:

```
codex plugin marketplace add oreillymedia/expert-intelligence-skills
codex plugin add {{SKILL_NAME}}@expert-intelligence-skills
```

</details>

<details>
<summary><b>Manual: copy the file</b> — works anywhere</summary>

{{MANUAL_INSTALL}}

</details>

## Requirements

An **O'Reilly learning platform account** is required to search the library. When installed as a
plugin, the O'Reilly Expert Intelligence MCP server is included automatically. If you copy an
individual skill manually instead, connect the MCP server yourself; see the
[MCP guide](https://www.oreilly.com/online-learning/support/mcp-guide.html) for setup steps.

## Try it

{{EXAMPLE_PROMPTS}}

This skill triggers based on the shape of your context and prompt. See the
`description` field in {{DESCRIPTION_PATH}} for the full set of trigger conditions.
