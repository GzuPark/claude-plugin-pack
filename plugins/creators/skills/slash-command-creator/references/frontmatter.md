# Slash Command Frontmatter Reference

## Required Fields

### `description`
Brief description of what the command does. Shown in `/help` output.

```yaml
description: Create a git commit with staged changes
```

## Optional Fields

### `allowed-tools`
Specifies which tools the command can use. Format: `ToolName(pattern:*)` or just `ToolName`.

```yaml
# Single tool
allowed-tools: Bash(git status:*)

# Multiple tools
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)

# Tool without pattern
allowed-tools: Read, Write, Edit
```

Common tool patterns:
- `Bash(command:*)` - Allow specific bash commands
- `Read` - File reading
- `Write` - File writing
- `Edit` - File editing
- `Grep` - Content search
- `Glob` - File pattern matching

### `argument-hint`
Shows expected arguments when auto-completing the command.

```yaml
# Single argument
argument-hint: [message]

# Multiple arguments
argument-hint: [pr-number] [priority] [assignee]

# Alternative syntax
argument-hint: add [tagId] | remove [tagId] | list
```

### `model`
Specific model to use for this command. See [Models overview](https://docs.claude.com/en/docs/about-claude/models/overview).

```yaml
model: claude-3-5-haiku-20241022
model: claude-sonnet-4-5-20250929
```

### `disable-model-invocation`

Prevents the `Skill` tool from calling this command programmatically.

```yaml
disable-model-invocation: true
```

### `hooks`

Define hooks that run during command execution. Supports `PreToolUse`, `PostToolUse`, and `Stop` events.

```yaml
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate.sh"
```

## Skill Tool Permission Patterns

Permission rules for Skill tool invocation:

```yaml
# Exact match - only /commit with no arguments
allowed-tools: Skill(/commit)

# Prefix match - /review-pr with any arguments
allowed-tools: Skill(/review-pr:*)
```

## Wildcard Patterns for Bash

Bash commands support wildcard patterns:

```yaml
# Match npm commands
allowed-tools: Bash(npm *)

# Match any install command
allowed-tools: Bash(* install)

# Match python with any file
allowed-tools: Bash(python:*)
```

## Complete Frontmatter Example

```yaml
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
argument-hint: [message]
description: Create a git commit with staged changes
model: claude-3-5-haiku-20241022
---
```
