# Hook Examples

Complete, tested hook configurations for common use cases.

## Table of Contents

1. [Logging Hooks](#logging-hooks)
2. [Auto-Formatting Hooks](#auto-formatting-hooks)
3. [File Protection Hooks](#file-protection-hooks)
4. [Notification Hooks](#notification-hooks)
5. [Validation Hooks](#validation-hooks)
6. [Session Hooks](#session-hooks)
7. [Permission Hooks](#permission-hooks)
8. [User Prompt Hooks](#user-prompt-hooks)
9. [Compaction Hooks](#compaction-hooks)
10. [Multiple Hooks Example](#multiple-hooks-example)
11. [Troubleshooting](#troubleshooting)

---

## Logging Hooks

### Required Tools for Logging

`jq`

### Log All Bash Commands

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"\\(.tool_input.command) - \\(.tool_input.description // \"No description\")\"' >> ~/.claude/bash-command-log.txt"
          }
        ]
      }
    ]
  }
}
```

### Log All File Edits

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"[\\(now | strftime(\"%Y-%m-%d %H:%M:%S\"))] \\(.tool_name): \\(.tool_input.file_path)\"' >> ~/.claude/edit-log.txt"
          }
        ]
      }
    ]
  }
}
```

## Auto-Formatting Hooks

### Required Tools for Formatting

`jq`, and formatters (`prettier`, `black`, `gofmt`)

### Format TypeScript Files

#### Required for TypeScript

`prettier` (`npm install -g prettier`)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read file_path; if echo \"$file_path\" | grep -q '\\.tsx\\?$'; then npx prettier --write \"$file_path\" 2>/dev/null; fi; }"
          }
        ]
      }
    ]
  }
}
```

### Format Python Files with Black

#### Required for Python

`black` (`pip install black`)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read f; [[ \"$f\" == *.py ]] && black \"$f\" 2>/dev/null; }"
          }
        ]
      }
    ]
  }
}
```

### Format Go Files

#### Required for Go

`gofmt` (included with Go installation)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read f; [[ \"$f\" == *.go ]] && gofmt -w \"$f\"; }"
          }
        ]
      }
    ]
  }
}
```

## File Protection Hooks

### Required Tools for Protection

`jq` or `python3`

### Block Edits to Sensitive Files

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 -c \"import json, sys; data=json.load(sys.stdin); path=data.get('tool_input',{}).get('file_path',''); blocked=['.env', 'package-lock.json', '.git/', 'secrets']; sys.exit(2 if any(p in path for p in blocked) else 0)\""
          }
        ]
      }
    ]
  }
}
```

### Block Modifications to Production Directory

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write|Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input | .file_path // .command // \"\"' | grep -q '/prod/' && echo 'BLOCKED: Cannot modify production files' && exit 2 || exit 0"
          }
        ]
      }
    ]
  }
}
```

## Notification Hooks

### Required Tools for Notifications

`jq`, platform-specific tools (`osascript` for macOS, `notify-send` for Linux)

### macOS Desktop Notification

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.message' | xargs -I{} osascript -e 'display notification \"{}\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

### Linux Desktop Notification

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.message' | xargs -I{} notify-send 'Claude Code' '{}'"
          }
        ]
      }
    ]
  }
}
```

### Sound Notification (macOS)

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Glass.aiff"
          }
        ]
      }
    ]
  }
}
```

## Validation Hooks

### Required Tools for Validation

`jq`, optionally `eslint`

### Validate JSON Before Write

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -e '.tool_input | select(.file_path | endswith(\".json\")) | .content' | jq . > /dev/null 2>&1 || { echo 'Invalid JSON content'; exit 2; }"
          }
        ]
      }
    ]
  }
}
```

### Lint TypeScript Before Commit

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.command' | grep -q 'git commit' && npx eslint . --max-warnings 0 || exit 0"
          }
        ]
      }
    ]
  }
}
```

## Session Hooks

### Required Tools for Sessions

Shell (bash)

### Initialize Environment on Session Start

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "[ -f .claude-env ] && source .claude-env"
          }
        ]
      }
    ]
  }
}
```

### Cleanup on Session End

```json
{
  "hooks": {
    "SessionEnd": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "rm -f /tmp/claude-session-* 2>/dev/null; exit 0"
          }
        ]
      }
    ]
  }
}
```

## Permission Hooks

Hooks for the `PermissionRequest` event to auto-approve or deny tool permissions.

### Auto-Approve Read Tool

Automatically approve all Read tool permission requests:

```json
{
  "hooks": {
    "PermissionRequest": [
      {
        "matcher": "Read",
        "hooks": [
          {
            "type": "command",
            "command": "exit 0"
          }
        ]
      }
    ]
  }
}
```

### Deny Write to System Directories

Block write operations to system directories:

```json
{
  "hooks": {
    "PermissionRequest": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path // \"\"' | grep -qE '^/(etc|usr|sys|proc)' && echo 'BLOCKED: System directory' && exit 2 || exit 0"
          }
        ]
      }
    ]
  }
}
```

## User Prompt Hooks

Hooks for the `UserPromptSubmit` event to process user input before Claude sees it.

### Required Tools for Prompts

`jq`

### Log User Prompts

Log all user prompts to a file:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"[\\(now | strftime(\"%Y-%m-%d %H:%M:%S\"))] \\(.prompt)\"' >> ~/.claude/prompts.log"
          }
        ]
      }
    ]
  }
}
```

### Validate Prompt Length

Warn if prompt exceeds a certain length:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.prompt | length' | { read len; [ \"$len\" -gt 10000 ] && echo 'Warning: Very long prompt' >&2; exit 0; }"
          }
        ]
      }
    ]
  }
}
```

## Compaction Hooks

Hooks for the `PreCompact` event triggered before context compaction.

### Log Compaction Event

Log when context compaction occurs:

```json
{
  "hooks": {
    "PreCompact": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"[$(date '+%Y-%m-%d %H:%M:%S')] Context compaction triggered\" >> ~/.claude/compaction.log"
          }
        ]
      }
    ]
  }
}
```

### Backup Before Compaction

Save important context information before compaction:

```json
{
  "hooks": {
    "PreCompact": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.summary // \"No summary\"' >> ~/.claude/context-backup.txt"
          }
        ]
      }
    ]
  }
}
```

## Multiple Hooks Example

Combine multiple hooks in one configuration:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 -c \"import json,sys; p=json.load(sys.stdin).get('tool_input',{}).get('file_path',''); sys.exit(2 if '.env' in p else 0)\""
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read f; [[ \"$f\" == *.ts ]] && npx prettier --write \"$f\" 2>/dev/null; exit 0; }"
          }
        ]
      }
    ],
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Glass.aiff"
          }
        ]
      }
    ]
  }
}
```

---

## Troubleshooting

Common issues and solutions when working with hooks.

### Hook Not Triggering

#### Symptom

Hook command never executes.

#### Solutions

1. **Check matcher pattern**: Ensure the matcher matches the tool name exactly (case-sensitive)

   ```text
   "matcher": "Bash"  // Correct
   "matcher": "bash"  // Wrong - won't match
   ```

2. **Verify event type**: Make sure you're using the correct event for your use case
   - `PreToolUse`: Before tool execution
   - `PostToolUse`: After tool execution
   - `PermissionRequest`: When permission dialog appears

3. **Test command manually**: Run your hook command in terminal to verify it works

### Hook Blocks Everything

#### Symptom: Blocking Issue

All operations of a certain type are blocked.

#### Solutions for Blocking Issue

1. **Check exit code**: Exit code 2 blocks the operation. Ensure your script returns 0 for allowed operations

   ```bash
   # Always allow (exit 0)
   echo "logged" && exit 0

   # Conditional block
   [[ "$path" == *".env"* ]] && exit 2 || exit 0
   ```

2. **Use proper error handling**: Add `|| exit 0` to prevent unexpected blocks

   ```bash
   some_command 2>/dev/null || exit 0
   ```

### JSON Parsing Errors

#### Symptom: Parsing Issue

`jq` commands fail or produce unexpected output.

#### Solutions for Parsing Issue

1. **Escape quotes properly**: JSON in shell requires careful escaping

   ```json
   "command": "jq -r '.tool_input.file_path'"  // Correct
   "command": "jq -r ".tool_input.file_path""  // Wrong
   ```

2. **Handle missing fields**: Use `// ""` for default values

   ```bash
   jq -r '.tool_input.description // ""'
   ```

3. **Debug with logging**: Temporarily log the input to see what's received

   ```bash
   tee /tmp/hook-debug.json | jq -r '.tool_input.command'
   ```

### Platform-Specific Issues

#### macOS

- Use `osascript` for notifications
- Sound files in `/System/Library/Sounds/`

#### Linux

- Use `notify-send` for notifications (requires `libnotify`)
- Install with: `sudo apt install libnotify-bin`

#### Windows (WSL)

- Use `powershell.exe` for Windows notifications
- Path conversion may be needed for Windows tools
