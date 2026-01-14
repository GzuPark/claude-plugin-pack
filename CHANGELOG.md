# Changelog

## 26.1.12 (2026-01-14)

- Add hooks directory with reusable hook configurations
  - markdown-lint: Auto-lint `.md` files on edit (PostToolUse hook)
- Add `.markdownlintrc` (disable MD013, MD060)
- Fix markdown lint errors across all plugins
  - creators (v1.0.2): 9 files fixed
  - heimdall (v1.1.1): 3 files fixed
  - hello-world (v1.1.2): 7 files fixed
  - task-forge (v1.2.2): 18 files fixed

## 26.1.11 (2026-01-14)

- Fix task-forge plugin (v1.2.1)
  - Remove invalid `commands` and `agents` fields from plugin.json
  - Rename `agents/` to `subagents/` for proper auto-discovery
  - Rename `commands/` to `slash-commands/` for proper auto-discovery

## 26.1.10 (2026-01-14)

- Update heimdall plugin (v1.1.0)
  - bifrost: Add version check, auto-update settings.json path, and old version cleanup
  - Step-by-step conditional workflow for install/update/cleanup

## 26.1.9 (2026-01-14)

- Fix heimdall plugin (v1.0.2)
  - Fix delimiter display bug between tools and agents (`| │ |` → `│`)

## 26.1.8 (2026-01-14)

- Fix heimdall plugin (v1.0.1)
  - Remove invalid `commands` field from plugin.json (auto-discovery used instead)

## 26.1.7 (2026-01-14)

- Add heimdall plugin (v1.0.0)
  - Dynamic statusline (3-5 lines based on activity)
  - `/heimdall:bifrost` command for automatic build and configuration
  - Tool tracking with color-coded completion counts
  - Agent tracking with elapsed time display
  - Running activity on separate line with spinner
  - Todo progress with full task description
  - Git integration (branch, staged/modified, sync status)
  - MCP server connection status
  - Context usage with color-coded progress bar (80%+ red, 60%+ yellow)
  - 5-hour reset timer (UTC blocks: 04, 09, 14, 19, 00)
  - Project directory display (stable, not affected by cd)

## 26.1.6 (2026-01-14)

- Update task-forge plugin (v1.2.0)
  - image-insight: Analyze images and generate JSON profiles for AI image recreation
  - 10-category analysis (composition, color, lighting, subject, background, etc.)
  - Critical area analysis for hair, hands, facial expression, lighting details
  - Structured output with hex color codes and actionable generation prompts

## 26.1.5 (2026-01-14)

- Update task-forge plugin (v1.1.0)
  - /recap: Multi-agent work session analysis command
  - 5 new agents: doc-updater, automation-scout, learning-extractor, followup-suggester, duplicate-checker
  - Documentation updates, automation suggestions, TIL extraction, follow-up task prioritization

## 26.1.4 (2026-01-13)

- Add task-forge plugin (v1.0.0)
  - meeting-insight: Analyze meeting transcripts for communication patterns and insights
  - video-insight: Extract transcripts, summaries, Q&A highlights from YouTube/local media
  - 4 subagents: transcript-analyzer, digest-writer, qa-generator, deep-researcher
  - Supports macOS and Ubuntu (see prerequisites.md for installation)
  - Parallel execution for Q&A and Deep Research
  - Dynamic Q&A count (1-5 pairs based on content length)

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
