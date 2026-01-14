# Hook Events Reference

## Event Overview

| Event             | Trigger           | Block     | Prompt | Use           |
|-------------------|-------------------|-----------|--------|---------------|
| PreToolUse        | Before tool exec  | Yes (2)   | Yes    | Validation    |
| PostToolUse       | After tool done   | No        | No     | Formatting    |
| PermissionRequest | Permission dialog | Yes       | Yes    | Auto-allow    |
| UserPromptSubmit  | User submits      | No        | Yes    | Pre-process   |
| Notification      | Claude notifies   | No        | No     | Custom alerts |
| Stop              | Claude finishes   | Yes       | Yes    | Post-process  |
| SubagentStop      | Subagent done     | Yes       | Yes    | Cleanup       |
| PreCompact        | Before compact    | No        | No     | Pre-compact   |
| SessionStart      | Session starts    | No        | No     | Init          |
| SessionEnd        | Session ends      | No        | No     | Cleanup       |

## PreToolUse

Runs before tool calls. Can block execution.

### Input Schema

```json
{
  "tool_name": "Bash",
  "tool_input": {
    "command": "ls -la",
    "description": "List files"
  }
}
```

### Exit Codes

- `0` - Allow tool to proceed
- `2` - Block tool, stdout sent as feedback to Claude

### Common tool_input Fields by Tool

- `Bash`: `command`, `description`
- `Edit`: `file_path`, `old_string`, `new_string`
- `Write`: `file_path`, `content`
- `Read`: `file_path`
- `Glob`: `pattern`, `path`
- `Grep`: `pattern`, `path`

## PostToolUse

Runs after tool calls complete.

### Input Schema for PostToolUse

```json
{
  "tool_name": "Edit",
  "tool_input": {
    "file_path": "/path/to/file.ts"
  },
  "tool_response": "File edited successfully"
}
```

### Use Cases for PostToolUse

- Auto-formatting edited files
- Logging tool results
- Triggering dependent actions

## PermissionRequest

Runs when permission dialog is shown.

### Input Schema for PermissionRequest

```json
{
  "tool_name": "Bash",
  "tool_input": {
    "command": "npm install"
  },
  "permission_type": "execute"
}
```

### Exit Codes for PermissionRequest

- `0` - Let user decide
- `1` - Auto-deny
- `2` - Auto-approve

## Notification

Runs when Claude sends notifications.

### Input Schema for Notification

```json
{
  "message": "Waiting for your input",
  "type": "input_required"
}
```

### Use Cases for Notification

- Custom desktop notifications
- Slack/Discord alerts
- Sound notifications

## UserPromptSubmit

Runs when user submits a prompt, before Claude processes it.

### Input Schema for UserPromptSubmit

```json
{
  "prompt": "Help me fix this bug",
  "session_id": "abc123"
}
```

### Use Cases for UserPromptSubmit

- Prompt logging
- Pre-processing
- Context injection

## Stop

Runs when Claude finishes responding.

### Input Schema for Stop

```json
{
  "stop_reason": "end_turn",
  "session_id": "abc123"
}
```

### Use Cases for Stop

- Session logging
- Cleanup tasks
- Metrics collection

## SubagentStop

Runs when subagent (Task tool) tasks complete.

### Input Schema for SubagentStop

```json
{
  "subagent_type": "Explore",
  "result": "Found 5 matching files"
}
```

## PreCompact

Runs before Claude compacts conversation context.

### Input Schema for PreCompact

```json
{
  "reason": "context_limit",
  "current_tokens": 50000
}
```

## SessionStart

Runs when Claude Code starts or resumes a session.

### Input Schema for SessionStart

```json
{
  "session_id": "abc123",
  "is_resume": false,
  "project_dir": "/path/to/project",
  "agent_type": "main"
}
```

### agent_type Values

`main`, `subagent`, `skill`

### Use Cases for SessionStart

- Environment setup
- Loading project config
- Starting background services

## SessionEnd

Runs when Claude Code session ends.

### Input Schema for SessionEnd

```json
{
  "session_id": "abc123",
  "end_reason": "user_exit"
}
```

### Use Cases for SessionEnd

- Cleanup resources
- Save session state
- Stop background services
