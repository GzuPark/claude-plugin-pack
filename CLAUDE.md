# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code)
when working with code in this repository.

## Repository Purpose

This is a Claude Code plugin marketplace repository.
It hosts a collection of plugins that users can install via
`/plugin marketplace add GzuPark/claude-plugin-pack`.

## Architecture

- `.claude-plugin/plugin.json` - Plugin manifest with metadata
- `.claude-plugin/marketplace.json` - Marketplace configuration
  listing available plugins
- `plugins/` - Contains individual plugin directories

## Development

### Adding a New Plugin

1. Create plugin directory: `plugins/my-plugin/.claude-plugin/plugin.json`
2. Register in `.claude-plugin/marketplace.json`
3. Test locally: `claude --plugin-dir ./plugins/my-plugin`

See `README.md` for detailed plugin structure.

### Creating Claude Code Extensions

When creating Claude Code extensions, use the appropriate creator skill:

| Extension Type  | Creator Skill            |
| --------------- | ------------------------ |
| Skill           | `skill-creator`          |
| Hook            | `hook-creator`           |
| Agent           | `subagent-creator`       |
| Slash Command   | `slash-command-creator`  |

**If creator skills are not available:**
Recommend installing the `creators` plugin first,
then proceed with an agent to create the desired functionality.

## Rules

### Documentation

- `README.md` - English version
- `README.ko.md` - Korean version

**Important:** When either README is modified,
the other must be updated to keep content in sync.

### GitHub Alerts

Use [GitHub Alerts](https://github.com/orgs/community/discussions/16925)
sparingly for important information:

| Type           | Usage                            |
| -------------- | -------------------------------- |
| `[!IMPORTANT]` | Prerequisites, required setup    |
| `[!WARNING]`   | Manual steps, build warnings     |
| `[!NOTE]`      | Additional info, verification    |
| `[!TIP]`       | Optional improvements            |

**Do NOT overuse.** Apply only where truly needed.

**MD032 Note:** Add blank line before lists in alerts:

```markdown
> [!IMPORTANT]
>
> - Item 1
> - Item 2
```

### Korean Language Style

SHOULD use formal polite speech ("~합니다" form),
NOT casual speech ("~해줘" form).

- Good: "스킬을 만듭니다", "수정합니다"
- Bad: "스킬 만들어줘", "수정해줘"

### Technical Terms in Korean Documentation

Keep technical terms in English rather than transliterating to Korean.
This improves readability for developers.

**Example:**

- Good: "Multi-agent system으로 session context를 분석합니다"
- Bad: "멀티 에이전트 시스템으로 세션 컨텍스트를 분석합니다"

### Versioning

**Marketplace (CalVer):** `YY.M.patch` (e.g., 26.1.0)

- New plugin added → patch ↑
- Plugin version changed → patch ↑
- Hook added/removed/modified → patch ↑
- Plugin removed / structure change → minor ↑
- New year/month → YY.M reset

**Plugin (SemVer):** `major.minor.patch` (e.g., 1.0.0)

- Breaking change → major ↑
- New feature → minor ↑
- Bug fix → patch ↑

**Version Sync (CRITICAL):** Keep versions in sync between:

- `.claude-plugin/marketplace.json`
- `.claude-plugin/plugin.json`

Both files must have the same version number.

**IMPORTANT:** When updating `marketplace.json` version,
ALWAYS update `plugin.json` version as well.
Never leave these files out of sync.

**Heimdall Version Sync:** Keep versions in sync between:

- `plugins/heimdall/.claude-plugin/plugin.json`
- `plugins/heimdall/statusline/package.json`

Both files must have the same version number.

### Changelog

All changes are recorded in `CHANGELOG.md`.

**Important:** Update CHANGELOG.md only when marketplace version changes.
Do NOT update for documentation-only changes without version bump.

```markdown
## YY.M.patch (YYYY-MM-DD)

- Add plugin-name plugin (vX.X.X)
  - feature: Description
- Update plugin-name plugin (vX.X.X)
- Remove plugin-name plugin
```

**Important:** Update `CHANGELOG.md` when releasing a new version.

## Reference

- [Create plugins][plugins-md]:
  Create custom plugins to extend Claude Code with slash commands,
  agents, hooks, Skills, and MCP servers.
- [Plugins reference][plugins-reference-md]:
  Complete technical reference for Claude Code plugin system,
  including schemas, CLI commands, and component specifications.
- [Plugin Marketplaces Guide][plugin-marketplaces]

[plugins-md]: https://code.claude.com/docs/en/plugins.md
[plugins-reference-md]: https://code.claude.com/docs/en/plugins-reference.md
[plugin-marketplaces]: https://code.claude.com/docs/en/plugin-marketplaces
