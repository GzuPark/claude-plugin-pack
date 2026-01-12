# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a Claude Code plugin marketplace repository. It hosts a collection of plugins that users can install via `/plugin marketplace add GzuPark/claude-plugin-pack`.

## Architecture

- `.claude-plugin/plugin.json` - Plugin manifest with metadata
- `.claude-plugin/marketplace.json` - Marketplace configuration listing available plugins
- `plugins/` - Contains individual plugin directories

## Adding a New Plugin

1. Create a plugin directory under `plugins/`:

   ```text
   plugins/my-plugin/
   ├── .claude-plugin/
   │   └── plugin.json
   ├── commands/      # Optional slash commands
   ├── agents/        # Optional custom agents
   ├── skills/        # Optional agent skills
   ├── hooks/         # Optional event handlers
   └── README.md
   ```

2. Register the plugin in `.claude-plugin/marketplace.json`:

   ```json
   {
     "name": "my-plugin",
     "description": "Plugin description",
     "source": "./plugins/my-plugin",
     "category": "productivity"
   }
   ```

## Testing Plugins Locally

```bash
claude --plugin-dir ./plugins/my-plugin
```

## Documentation

- `README.md` - English version
- `README.ko.md` - Korean version

**Important:** When either README is modified, the other must be updated to keep content in sync.

## Reference

- [Claude Code Plugins Documentation](https://docs.anthropic.com/en/docs/claude-code/plugins)
- [Plugin Marketplaces Guide](https://code.claude.com/docs/en/plugin-marketplaces)
