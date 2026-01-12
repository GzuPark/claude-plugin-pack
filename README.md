# Claude Plugin Pack

A collection of plugins for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## About Claude Code Plugins

Claude Code plugins extend the functionality of Claude Code CLI. This repository provides ready-to-use plugins for productivity and development workflows.

## Installation

### From GitHub (Recommended)

1. Add the marketplace:

   ```bash
   /plugin marketplace add GzuPark/claude-plugin-pack
   ```

2. Install plugins:

   ```bash
   /plugin install plugin-name@claude-plugin-pack
   ```

### From CLI

```bash
claude plugin install plugin-name@claude-plugin-pack
```

### Local Development

```bash
claude --plugin-dir ./claude-plugin-pack
```

## Included Plugins

### creators

Skills for creating Claude Code extensions:

- **skill-creator** - Create Agent Skills with SKILL.md
- **slash-command-creator** - Create custom slash commands
- **hook-creator** - Create event hooks
- **subagent-creator** - Create custom subagents

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
