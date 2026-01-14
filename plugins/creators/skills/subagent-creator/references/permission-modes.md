# Permission Modes

Sub-agents can operate with different permission levels.
Choose the appropriate mode based on the sub-agent's purpose and required autonomy.

## Available Modes

| Mode | Description | Use Case |
| ---- | ----------- | -------- |
| `default` | Standard permission checking | General-purpose sub-agents |
| `acceptEdits` | Auto-accept file edits | Trusted code modification tasks |
| `bypassPermissions` | Skip all permission prompts | Fully trusted automation |
| `plan` | Planning mode (read-only) | Architecture and design tasks |
| `ignore` | Ignore permission system entirely | Edge cases, testing |

---

## Mode Details

### `default`

The standard permission mode. Users are prompted for approval before:

- Writing or editing files
- Running potentially dangerous bash commands
- Accessing sensitive resources

**When to use:**

- General-purpose sub-agents
- Tasks where user oversight is desired
- Sub-agents that may modify important files

```yaml
permissionMode: default
```

### `acceptEdits`

Automatically accepts file edit operations without prompting.

**When to use:**

- Trusted code formatters or linters
- Auto-fix tools
- Refactoring sub-agents with well-defined scope

**Caution:** Still prompts for bash commands and other non-edit operations.

```yaml
permissionMode: acceptEdits
```

### `bypassPermissions`

Skips all permission checks. The sub-agent operates with full autonomy.

**When to use:**

- Fully trusted automation pipelines
- CI/CD integration sub-agents
- Well-tested, scoped sub-agents

**Warning:** Use with caution.
Only for sub-agents with limited tool access and well-defined scope.

```yaml
permissionMode: bypassPermissions
tools: Read, Grep, Glob  # Limit tools when bypassing permissions
```

### `plan`

Restricts the sub-agent to planning and read-only operations.

**When to use:**

- Architecture design sub-agents
- Code analysis and review
- Investigation and exploration tasks

**Benefits:**

- Safe for exploration
- Cannot make unintended changes
- Ideal for generating plans before implementation

```yaml
permissionMode: plan
```

### `ignore`

Completely ignores the permission system.
The sub-agent behaves as if permissions don't exist.

**When to use:**

- Testing and development scenarios
- Edge cases where permission handling causes issues
- Controlled environments with no security concerns

**Warning:** This mode provides no safety guarantees.
Use only when you fully understand the implications.

```yaml
permissionMode: ignore
```

---

## Best Practices

### 1. Match Mode to Purpose

| Sub-agent Type | Recommended Mode |
| -------------- | ---------------- |
| Code reviewer | `plan` or `default` |
| Formatter/Linter | `acceptEdits` |
| Debugger | `default` |
| Security auditor | `plan` |
| CI automation | `bypassPermissions` + limited tools |

### 2. Combine with Tool Restrictions

When using permissive modes, always restrict tools:

```yaml
# Safe automation pattern
permissionMode: bypassPermissions
tools: Read, Grep, Glob, Bash
# Only read operations + bash for specific commands
```

### 3. Start Restrictive, Expand as Needed

Begin with `default` or `plan`, then expand permissions
only if the workflow requires it.

---

## Examples

### Read-Only Analyzer

```yaml
name: code-analyzer
description: Analyzes code patterns and metrics
tools: Read, Grep, Glob
permissionMode: plan
```

### Trusted Auto-Formatter

```yaml
name: auto-formatter
description: Formats code on save
tools: Read, Write, Edit
permissionMode: acceptEdits
```

### CI Pipeline Runner

```yaml
name: ci-runner
description: Runs CI checks and tests
tools: Read, Grep, Glob, Bash
permissionMode: bypassPermissions
```
