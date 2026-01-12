---
name: subagent-creator
description: Create specialized Claude Code sub-agents with custom system prompts and tool configurations. Use when users ask to create a new sub-agent, custom agent, specialized assistant, or want to configure task-specific AI workflows for Claude Code.
---

# Sub-agent Creator

Create specialized AI sub-agents for Claude Code that handle specific tasks with customized prompts and tool access.

## Sub-agent File Format

Sub-agents are Markdown files with YAML frontmatter stored in:

- **Project**: `.claude/agents/` (higher priority)
- **User**: `~/.claude/agents/` (lower priority)

### Structure

```markdown
---
name: subagent-name
description: When to use this subagent (include "use proactively" for auto-delegation)
tools: Tool1, Tool2, Tool3  # Optional - inherits all if omitted
model: sonnet               # Optional - sonnet/opus/haiku/inherit
permissionMode: default     # Optional - default/acceptEdits/bypassPermissions/plan
skills: skill1, skill2      # Optional - auto-load skills
---

System prompt goes here. Define role, responsibilities, and behavior.
```

### Configuration Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Lowercase with hyphens |
| `description` | Yes | Purpose and when to use (key for auto-delegation) |
| `tools` | No | Comma-separated tool list (omit to inherit all) |
| `model` | No | `sonnet`, `opus`, `haiku`, or `inherit` |
| `permissionMode` | No | `default`, `acceptEdits`, `bypassPermissions`, `plan`, `ignore` (see [permission-modes.md](references/permission-modes.md)) |
| `skills` | No | Skills to auto-load |
| `hooks` | No | Define hooks for subagent lifecycle (PreToolUse, PostToolUse, Stop) |

## Creation Workflow

1. **Gather requirements**: Ask about the sub-agent's purpose, when to use it, and required capabilities
2. **Choose scope**: Project (`.claude/agents/`) or user (`~/.claude/agents/`)
3. **Define configuration**: Name, description, tools, model
4. **Write system prompt**: Clear role, responsibilities, and output format
5. **Create file**: Write the `.md` file to the appropriate location

## Writing Effective Sub-agents

### Description Best Practices

The `description` field is critical for automatic delegation:

```yaml
# Good - specific triggers
description: Expert code reviewer. Use PROACTIVELY after writing or modifying code.

# Good - clear use cases
description: Debugging specialist for errors, test failures, and unexpected behavior.

# Bad - too vague
description: Helps with code
```

### System Prompt Guidelines

1. **Define role clearly**: "You are a [specific expert role]"
2. **List actions on invocation**: What to do first
3. **Specify responsibilities**: What the sub-agent handles
4. **Include guidelines**: Constraints and best practices
5. **Define output format**: How to structure responses

### Tool Selection

- **Read-only tasks**: `Read, Grep, Glob, Bash`
- **Code modification**: `Read, Write, Edit, Grep, Glob, Bash`
- **Full access**: Omit `tools` field

See [references/available-tools.md](references/available-tools.md) for complete tool list.

## Example Sub-agents

See [references/examples.md](references/examples.md) for complete examples:

- Code Reviewer
- Debugger
- Data Scientist
- Test Runner
- Documentation Writer
- Security Auditor

## Template

Copy from [assets/subagent-template.md](assets/subagent-template.md) to start a new sub-agent.

## Quick Start Example

Create a code reviewer sub-agent:

```bash
mkdir -p .claude/agents
```

Write to `.claude/agents/code-reviewer.md`:

```markdown
---
name: code-reviewer
description: Reviews code for quality and security. Use proactively after code changes.
tools: Read, Grep, Glob, Bash
model: inherit
---

You are a senior code reviewer.

When invoked:
1. Run git diff to see changes
2. Review modified files
3. Report issues by priority

Focus on:
- Code readability
- Security vulnerabilities
- Error handling
- Best practices
```

### Hooks in Subagents

Define hooks that run during subagent execution:

```yaml
---
name: code-reviewer
description: Review code with auto-linting
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/run-linter.sh"
---
```

Hooks are scoped to the subagent's execution and automatically cleaned up when finished.

## Triggers

This skill activates when users want to:

- Create a new sub-agent or custom agent for Claude Code
- Configure task-specific AI workflows with specialized prompts
- Set up automatic delegation for specific task types
- Customize tool access or permission modes for agents
- Build specialized assistants (code reviewer, debugger, etc.)

## Extension Points

1. **Template customization**: Modify `assets/subagent-template.md` to match organizational standards or add custom fields
2. **Permission mode additions**: Extend `references/permission-modes.md` with organization-specific permission configurations
3. **Example library**: Add new sub-agent examples to `references/examples.md` for common use cases
4. **Tool configurations**: Create preset tool combinations in references for different agent types

## Anti-Patterns

Avoid these common mistakes when creating sub-agents:

- **Overly broad descriptions**: Vague descriptions like "helps with code" prevent effective auto-delegation
- **Missing proactive trigger**: Forgetting "use proactively" in description when auto-delegation is desired
- **Excessive tool restrictions**: Over-restricting tools when the agent needs flexibility
- **Monolithic prompts**: Writing very long system prompts instead of keeping them focused and concise
- **Hardcoded paths**: Including absolute paths or environment-specific values in prompts
- **Ignoring permission modes**: Not considering `permissionMode` for agents that need elevated access

## Design Rationale

**Why YAML frontmatter?** Provides structured, parseable configuration while keeping the system prompt in readable Markdown. This matches Claude Code's skill format for consistency.

**Why description is critical?** The Task tool uses descriptions to determine which sub-agent to delegate to. A well-written description is the primary mechanism for automatic task routing.

**Why optional tools field?** Most sub-agents benefit from full tool access. Restricting tools is only needed for security-sensitive or read-only tasks. Defaulting to inheritance reduces configuration overhead.

**Why permission modes?** Different tasks require different trust levels. A code reviewer needs only read access, while an auto-fixer needs edit permissions. Permission modes enable safe automation without blanket approvals.
