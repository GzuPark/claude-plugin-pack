# Creators

Skills for creating Claude Code extensions.

## Installation

```bash
/plugin marketplace add GzuPark/claude-plugin-pack
/plugin install creators@claude-plugin-pack
```

## Skills

After installation, these skills are automatically triggered when you ask Claude to create extensions.

### skill-creator

**Triggers:** "create a skill", "make a new skill", "update this skill"

Creates Agent Skills with proper structure:

```text
skill-name/
├── SKILL.md       # Required - frontmatter + instructions
├── scripts/       # Optional - executable code
├── references/    # Optional - documentation
└── assets/        # Optional - templates, images
```

### slash-command-creator

**Triggers:** "create a slash command", "make a command for /deploy"

Creates custom commands in:

- Project: `.claude/commands/`
- Personal: `~/.claude/commands/`

Command format:

```markdown
---
description: Brief description
---

Prompt instructions with $ARGUMENTS or $1, $2
```

### hook-creator

**Triggers:** "create a hook", "auto-format on save", "block edits to .env"

Creates event hooks in `settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{ "type": "command", "command": "your-script.sh" }]
    }]
  }
}
```

**Events:** PreToolUse, PostToolUse, SessionStart, SessionEnd, PermissionRequest, Stop, etc.

### subagent-creator

**Triggers:** "create a subagent", "make a code reviewer agent"

Creates subagents in:

- Project: `.claude/agents/`
- User: `~/.claude/agents/`

Subagent format:

```markdown
---
name: code-reviewer
description: Reviews code. Use proactively after changes.
tools: Read, Grep, Glob, Bash
model: sonnet
---

System prompt here.
```

## License

MIT
