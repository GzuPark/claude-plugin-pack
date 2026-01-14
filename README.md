# Claude Plugin Pack

> A curated collection of plugins to supercharge your
> [Claude Code](https://docs.anthropic.com/en/docs/claude-code) experience.

## Quick Start

```bash
# Add marketplace
/plugin marketplace add GzuPark/claude-plugin-pack
```

## Plugins

### hello-world

> Essential dev workflow for daily development

| Command | Description |
| ------- | ----------- |
| `/commit` | Create well-structured git commits with conventional format |
| `/interview` | Conduct technical interviews to generate project specs |
| `/pr` | Create GitHub PR with automated code review |

```bash
/plugin install hello-world@claude-plugin-pack
```

---

### heimdall

> Enhanced statusline for Claude Code *(named after the Norse watchman god)*

| Feature | Description |
| ------- | ----------- |
| `/heimdall:bifrost` | One-command setup (automatic build and configuration) |
| Dynamic display | 3-5 lines based on activity |
| Tool tracking | Color-coded completion counts |
| Agent tracking | Running agents with elapsed time |
| Todo progress | Full task description display |
| Git integration | Branch, staged/modified, sync status |
| Context usage | Color-coded progress bar |

```bash
/plugin install heimdall@claude-plugin-pack
```

```bash
/heimdall:bifrost
```

---

### creators

> Skills for creating Claude Code extensions

| Skill | Description |
| ----- | ----------- |
| skill-creator | Create Agent Skills with SKILL.md |
| slash-command-creator | Create custom slash commands |
| hook-creator | Create event hooks |
| subagent-creator | Create custom subagents |

```bash
/plugin install creators@claude-plugin-pack
```

---

### task-forge

> Workplace productivity tools

| Feature | Description |
| ------- | ----------- |
| `/recap` | Multi-agent work session analysis |
| meeting-insight | Analyze meeting transcripts for patterns |
| video-insight | Extract transcripts, summaries, Q&A from videos |
| image-insight | Generate JSON profiles for AI image recreation |

```bash
/plugin install task-forge@claude-plugin-pack
```

---

## Hooks

Reusable hook configurations.
Ask Claude Code to set them up automatically.

| Hook | Description |
| ---- | ----------- |
| [markdown-lint](hooks/README.md#1-markdown-lint) | Auto-lint `.md` files on edit |

See [hooks/README.md](hooks/README.md) for details.

## Update

Custom plugins do not auto-update. Get the latest version:

```bash
/plugin marketplace update claude-plugin-pack
```

## Structure

```text
claude-plugin-pack/
├── .claude-plugin/          # Marketplace & plugin manifests
├── plugins/                 # Individual plugins
├── hooks/                   # Reusable hook configurations
└── README.md
```

## Create Your Own

See [Claude Code Plugins Documentation][plugins-docs].

[plugins-docs]: https://docs.anthropic.com/en/docs/claude-code/plugins

## License

MIT
