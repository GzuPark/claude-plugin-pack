# Changelog

## 26.1.3 (2026-01-13)

- Update creators plugin (v1.0.1)
  - slash-command-creator: Fix bash execution example description
- Update hello-world plugin (v1.1.1)
  - /commit: Add missing allowed-tools (git diff, branch, log), add error handling for empty repos
  - /interview: Improve description
  - plan-interview: Add Triggers section

## 26.1.2 (2026-01-13)

- Update hello-world plugin (v1.1.0)
  - /interview: Conduct technical interviews about project plans (uses plan-interview skill)

## 26.1.1 (2026-01-13)

- Add hello-world plugin (v1.0.0)
  - /commit: Create well-structured git commits with conventional commit format
  - /pr: Create GitHub PR with automated code review (uses pr-workflow skill)

## 26.1.0 (2026-01-12)

- Add creators plugin (v1.0.0)
  - skill-creator: Create Agent Skills with SKILL.md
  - slash-command-creator: Create custom slash commands
  - hook-creator: Create event hooks for Claude Code
  - subagent-creator: Create custom subagents
- Add CLAUDE.md
  - Repository structure and plugin creation guide
  - Documentation rules (README.md / README.ko.md sync)
  - Korean language style guide
  - Versioning rules (CalVer for marketplace, SemVer for plugins)
  - Changelog format
