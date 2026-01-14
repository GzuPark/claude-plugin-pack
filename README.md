# Claude Plugin Pack

A collection of plugins for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## About Claude Code Plugins

Claude Code plugins extend the functionality of Claude Code CLI. This repository provides ready-to-use plugins for productivity and development workflows.

## Installation

Add the marketplace:

```bash
/plugin marketplace add GzuPark/claude-plugin-pack
```

## Update

Custom plugins do not auto-update. Run the following command to get the latest version:

```bash
/plugin marketplace update claude-plugin-pack
```

## Included Plugins

| Plugin | Description |
|--------|-------------|
| [hello-world](#hello-world) | Essential dev workflow: git commit and GitHub PR |
| [heimdall](#heimdall) | Enhanced statusline with tool/agent/todo tracking and session monitoring |
| [creators](#creators) | Skills for creating Claude Code extensions |
| [task-forge](#task-forge) | Workplace productivity tools: meeting analysis, video insights, work recap |

### hello-world

Essential dev workflow for daily development:

- **/commit** - Create well-structured git commits with conventional commit format
- **/interview** - Conduct technical interviews about project plans to generate specifications
- **/pr** - Create GitHub PR with automated code review

```bash
/plugin install hello-world@claude-plugin-pack
```

### heimdall

Enhanced statusline for Claude Code (named after the Norse watchman god):

- **/heimdall:bifrost** - Open the Bifrost bridge (automatic build and configuration)
- **Dynamic statusline** - 3-5 lines based on activity
- **Tool tracking** - Color-coded completion counts
- **Agent tracking** - Running agents with elapsed time
- **Todo progress** - Full task description display
- **Git integration** - Branch, staged/modified, sync status
- **MCP server** - Connection status display
- **Context usage** - Color-coded progress bar (green → yellow → red)
- **5-hour reset timer** - Usage tracking

```bash
/plugin install heimdall@claude-plugin-pack
/heimdall:bifrost
```

### creators

Skills for creating Claude Code extensions:

- **skill-creator** - Create Agent Skills with SKILL.md
- **slash-command-creator** - Create custom slash commands
- **hook-creator** - Create event hooks
- **subagent-creator** - Create custom subagents

```bash
/plugin install creators@claude-plugin-pack
```

### task-forge

Workplace productivity tools:

- **/recap** - Multi-agent work session analysis with documentation, automation, TIL, and follow-up suggestions
- **meeting-insight** - Analyze meeting transcripts for communication patterns and insights
- **video-insight** - Extract transcripts, summaries, Q&A, and deep research from videos
- **image-insight** - Analyze images and generate JSON profiles for AI image recreation

```bash
/plugin install task-forge@claude-plugin-pack
```

## Structure

```text
claude-plugin-pack/
├── .claude-plugin/
│   ├── marketplace.json     # Marketplace config
│   └── plugin.json          # Plugin manifest
├── plugins/                 # Individual plugins
├── CLAUDE.md
├── LICENSE
├── README.ko.md
└── README.md
```

## Creating Your Own

See the [Claude Code Plugins Documentation](https://docs.anthropic.com/en/docs/claude-code/plugins) for guides on creating plugins.

## License

MIT
