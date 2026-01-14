---
name: hook-creator
description: >-
  Create and configure Claude Code hooks for customizing agent behavior.
  Use when the user wants to (1) create a new hook, (2) configure automatic
  formatting, logging, or notifications, (3) add file protection or custom
  permissions, (4) set up pre/post tool execution actions, (5) configure
  session initialization or cleanup (SessionStart/SessionEnd), (6) auto-
  approve or deny permission requests (PermissionRequest), or (7) asks
  about any of the 10 hook events.
---

# Hook Creator

Create Claude Code hooks that execute shell commands at specific lifecycle events.

## Hook Creation Workflow

1. **Identify the use case** - Determine what the hook should accomplish
2. **Select the appropriate event** - Choose from available hook events
   (see references/hook-events.md)
3. **Design the hook command** - Write shell command that processes JSON
   input from stdin
4. **Configure the matcher** - Set tool/event filter (use `*` for all,
   or specific tool names like `Bash`, `Edit|Write`)
5. **Choose storage location** - User settings (`~/.claude/settings.json`)
   or project (`.claude/settings.json`)
6. **Test the hook** - Verify behavior with a simple test case

## Hook Configuration Structure

```json
{
  "hooks": {
    "<EventName>": [
      {
        "matcher": "<ToolPattern>",
        "hooks": [
          {
            "type": "command",
            "command": "<shell-command>",
            "once": true
          }
        ]
      }
    ]
  }
}
```

### Hook Types

- `type: "command"` - Execute shell command (default)
- `type: "prompt"` - LLM-based evaluation. Supported for: Stop,
  SubagentStop, UserPromptSubmit, PreToolUse, PermissionRequest

### Hook Options

- `once` - Run only once per session (optional, default: false)

## Common Patterns

### Reading Input Data

Hooks receive JSON via stdin. Use `jq` to extract fields:

```bash
# Extract tool input field
jq -r '.tool_input.file_path'

# Extract with fallback
jq -r '.tool_input.description // "No description"'

# Conditional processing
jq -r 'if .tool_input.file_path
  then .tool_input.file_path else empty end'
```

### Exit Codes for PreToolUse

- `0` - Allow the tool to proceed
- `2` - Block the tool and provide feedback to Claude

### Matcher Patterns

- `*` - Match all tools
- `Bash` - Match only Bash tool
- `Edit|Write` - Match Edit or Write tools
- `Read` - Match Read tool

## Quick Examples

**Log all bash commands:**

```bash
jq -r '"\(.tool_input.command)"' >> ~/.claude/bash-log.txt
```

**Auto-format TypeScript after edit:**

```bash
jq -r '.tool_input.file_path' | {
  read f
  [[ "$f" == *.ts ]] && npx prettier --write "$f"
}
```

**Block edits to .env files:**

```bash
python3 -c "
import json, sys
p = json.load(sys.stdin).get('tool_input', {}).get('file_path', '')
sys.exit(2 if '.env' in p else 0)
"
```

## Prompt-Based Hooks

Use `type: "prompt"` for LLM-based evaluation. The prompt receives
context and returns a decision.

**Example - Stop hook with evaluation:**

<!-- markdownlint-disable MD013 -->

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review if all user requirements are met. Context: {{context}}. Respond with JSON: {\"decision\": \"approve\" or \"block\", \"reason\": \"explanation\"}"
          }
        ]
      }
    ]
  }
}
```

<!-- markdownlint-enable MD013 -->

Supported events: `Stop`, `SubagentStop`, `UserPromptSubmit`, `PreToolUse`,
`PermissionRequest`

## Hooks in Skills/Agents/Commands

Define hooks directly in frontmatter for scoped lifecycle hooks:

```yaml
---
name: secure-operations
description: Perform operations with security checks
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/security-check.sh"
          once: true
---
```

Supported events in frontmatter: `PreToolUse`, `PostToolUse`, `Stop`

Hooks defined in Skills/Agents/Commands are scoped to that execution context
and automatically cleaned up when finished.

## Resources

- **Hook Events Reference**: See [references/hook-events.md](references/hook-events.md)
  for detailed event documentation with input/output schemas

## Triggers

This skill activates when users want to:

- Create a new hook for Claude Code
- Configure automatic formatting, linting, or code quality tools
- Set up logging or notification systems for tool usage
- Add file protection or access control rules
- Configure pre/post tool execution actions
- Set up session initialization or cleanup (SessionStart/SessionEnd)
- Auto-approve or deny permission requests (PermissionRequest)
- Understand hook events, input schemas, or exit codes

## Anti-Patterns

Avoid these common mistakes when creating hooks:

- **Blocking without feedback**: Using exit code 2 in PreToolUse without
  providing stdout message leaves Claude confused about why the tool was
  blocked
- **Ignoring stdin**: Not reading JSON from stdin causes hooks to fail
  silently or behave unexpectedly
- **Heavy synchronous operations**: Running slow commands in PreToolUse
  blocks the entire workflow; prefer async logging or use PostToolUse
- **Hardcoded paths**: Using absolute paths like `/home/user/...` instead
  of `$HOME` or relative paths breaks portability
- **Missing error handling**: Not handling `jq` parse failures or missing
  fields causes cryptic errors
- **Over-matching**: Using `*` matcher when only specific tools need the
  hook wastes resources and may cause side effects

## Extension Points

1. **Custom event handlers**: Add new hook configurations in settings.json
   for any of the 10 hook events
2. **External integrations**: Extend hooks to call external services
   (Slack, Discord, webhooks) via curl or custom scripts
3. **Project-specific overrides**: Layer project `.claude/settings.json`
   hooks over user `~/.claude/settings.json` defaults
4. **Script libraries**: Create reusable shell scripts in project that
   hooks can call for complex logic

## Design Rationale

**Why JSON via stdin?** Passing structured data through stdin allows hooks
to access any tool input field without parsing command-line arguments.
This is more flexible and handles special characters safely.

**Why exit codes for control flow?** Exit codes are the Unix-standard way
to signal success/failure. Using 0/2 for PreToolUse allows simple shell
commands to control tool execution without complex IPC.

**Why separate PreToolUse and PostToolUse?** Pre-hooks can block operations
(validation, access control) while post-hooks handle side effects
(formatting, logging). Mixing these concerns would complicate hook logic.

**Why 10 distinct events?** Each event represents a unique lifecycle moment
with different input schemas and use cases. Fine-grained events allow
precise hook targeting without over-triggering.
