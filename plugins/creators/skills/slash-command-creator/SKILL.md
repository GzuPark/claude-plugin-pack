---
name: slash-command-creator
description: Guide for creating Claude Code slash commands. Use when the user wants to create a new slash command, update an existing slash command, or asks about slash command syntax, frontmatter options, or best practices.
---

# Slash Command Creator

Create custom slash commands for Claude Code to automate frequently-used prompts.

## Quick Start

Initialize a new command:

```bash
./run.sh scripts/init_command.py <command-name> [--scope project|personal]

# Namespaced command (creates frontend/build.md)
./run.sh scripts/init_command.py frontend/build --scope project
```

## Command Structure

Slash commands are Markdown files with optional YAML frontmatter:

```markdown
---
description: Brief description shown in /help
---

Your prompt instructions here.

$ARGUMENTS
```

### File Locations

| Scope    | Path                  | Shown as  |
|----------|---------------------- |-----------|
| Project  | `.claude/commands/`   | (project) |
| Personal | `~/.claude/commands/` | (user)    |

### Namespacing

Organize commands in subdirectories:

- `.claude/commands/frontend/component.md` → `/component` shows "(project:frontend)"
- `~/.claude/commands/backend/api.md` → `/api` shows "(user:backend)"

## Features

### Arguments

**All arguments** - `$ARGUMENTS`:

```markdown
Fix issue #$ARGUMENTS following our coding standards
# /fix-issue 123 → "Fix issue #123 following..."
```

**Positional** - `$1`, `$2`, etc.:

```markdown
Review PR #$1 with priority $2
# /review 456 high → "Review PR #456 with priority high"
```

### Bash Execution

Execute shell commands with `!` prefix (requires `allowed-tools` in frontmatter):

```markdown
---
allowed-tools: Bash(git status:*), Bash(git diff:*)
---

Current status: !`git status`
Changes: !`git diff HEAD`
```

**Tip (Boris Cherny)**: Inline Bash pre-computes context, reducing round-trips with Claude:

```markdown
# Current branch
!`git branch --show-current`

# Changed files
!`git diff --name-only`

# Based on above, create a PR with...
```

This pattern is especially powerful for `/commit-push-pr` style commands where context changes frequently.

### File References

Include file contents with `@` prefix:

```markdown
Review @src/utils/helpers.js for issues.
Compare @$1 with @$2.
```

## Frontmatter Options

| Field                     | Purpose                                | Required |
|---------------------------|----------------------------------------|----------|
| `description`             | Brief description for /help            | Yes      |
| `allowed-tools`           | Tools the command can use              | No       |
| `argument-hint`           | Expected arguments hint                | No       |
| `model`                   | Specific model to use                  | No       |
| `disable-model-invocation`| Prevent Skill tool invocation          | No       |
| `hooks`                   | Define hooks for command execution (PreToolUse, PostToolUse, Stop) | No |

See [references/frontmatter.md](references/frontmatter.md) for detailed reference.

### Hooks in Commands

Define hooks that run during command execution:

```yaml
---
description: Deploy to staging with validation
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-deploy.sh"
---
```

## Examples

See [references/examples.md](references/examples.md) for complete examples including:

- Simple review/explain commands
- Commands with positional arguments
- Git workflow commands with bash execution
- Namespaced commands for frontend/backend

## Creation Workflow

1. **Identify the use case**: What prompt do you repeat often?
2. **Choose scope**: Project (shared) or personal (private)?
3. **Initialize**: Run `./run.sh scripts/init_command.py <name>`
4. **Edit**: Update description and body
5. **Test**: Run the command in Claude Code

## Triggers

This skill activates when users want to:

- Create a new slash command for Claude Code
- Update or modify an existing slash command
- Learn about slash command syntax or frontmatter options
- Understand best practices for command design
- Organize commands with namespacing

## Extension Points

1. **init_command.py customization**: Modify the template generation script to match organizational standards or add custom frontmatter fields
2. **Frontmatter schema**: Add custom frontmatter fields for organization-specific metadata (e.g., `owner`, `category`, `version`)
3. **Command templates**: Create reusable command templates in `assets/` for common patterns (review, deploy, test workflows)

## Anti-Patterns

Avoid these common mistakes when creating slash commands:

- **Overly complex commands**: Commands should do one thing well; split complex workflows into multiple commands
- **Missing descriptions**: Always include a description for discoverability in /help
- **Hardcoded paths**: Use arguments ($1, $2) instead of hardcoding file paths
- **Excessive bash execution**: Prefer Claude's tools over shell commands when possible
- **No argument hints**: For commands expecting arguments, include `argument-hint` in frontmatter

## Design Rationale

**Why Markdown format?** Markdown is readable, versionable, and familiar to developers. YAML frontmatter provides structured metadata without sacrificing readability.

**Why separate project/personal scopes?** Project commands are shared with the team via version control. Personal commands are private and portable across projects.

**Why namespacing?** Subdirectories prevent naming conflicts and organize commands by domain (frontend, backend, devops), making large command libraries manageable.
