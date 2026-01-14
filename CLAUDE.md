# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a Claude Code plugin marketplace repository. It hosts a collection of plugins that users can install via `/plugin marketplace add GzuPark/claude-plugin-pack`.

## Architecture

- `.claude-plugin/plugin.json` - Plugin manifest with metadata
- `.claude-plugin/marketplace.json` - Marketplace configuration listing available plugins
- `plugins/` - Contains individual plugin directories

## Development

### Adding a New Plugin

1. Create plugin directory: `plugins/my-plugin/.claude-plugin/plugin.json`
2. Register in `.claude-plugin/marketplace.json`
3. Test locally: `claude --plugin-dir ./plugins/my-plugin`

See `README.md` for detailed plugin structure.

## Rules

### Documentation

- `README.md` - English version
- `README.ko.md` - Korean version

**Important:** When either README is modified, the other must be updated to keep content in sync.

### Korean Language Style

SHOULD use formal polite speech ("~합니다" form), NOT casual speech ("~해줘" form).

- Good: "스킬을 만듭니다", "수정합니다"
- Bad: "스킬 만들어줘", "수정해줘"

### Technical Terms in Korean Documentation

Keep technical terms in English rather than transliterating to Korean. This improves readability for developers.

**Example:**

- Good: "Multi-agent system으로 session context를 분석합니다"
- Bad: "멀티 에이전트 시스템으로 세션 컨텍스트를 분석합니다"

### Versioning

**Marketplace (CalVer):** `YY.M.patch` (e.g., 26.1.0)

- New plugin added → patch ↑
- Plugin removed / structure change → minor ↑
- New year/month → YY.M reset

**Plugin (SemVer):** `major.minor.patch` (e.g., 1.0.0)

- Breaking change → major ↑
- New feature → minor ↑
- Bug fix → patch ↑

**Version Sync:** Keep versions in sync between:

- `.claude-plugin/marketplace.json`
- `.claude-plugin/plugin.json`

Both files must have the same version number.

**Heimdall Version Sync:** Keep versions in sync between:

- `plugins/heimdall/.claude-plugin/plugin.json`
- `plugins/heimdall/statusline/package.json`

Both files must have the same version number.

### Changelog

All changes are recorded in `CHANGELOG.md`.

```markdown
## YY.M.patch (YYYY-MM-DD)

- Add plugin-name plugin (vX.X.X)
  - feature: Description
- Update plugin-name plugin (vX.X.X)
- Remove plugin-name plugin
```

**Important:** Update `CHANGELOG.md` when releasing a new version.

## Reference

- [Claude Code Plugins Documentation](https://docs.anthropic.com/en/docs/claude-code/plugins)
- [Plugin Marketplaces Guide](https://code.claude.com/docs/en/plugin-marketplaces)
