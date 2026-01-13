---
name: plan-interview
description: Conduct technical interviews about project plans to uncover hidden assumptions and identify potential issues before implementation. Use when the user wants to be interviewed about a plan, spec, or project idea.
model: sonnet
user-invocable: false
allowed-tools:
  - Read
  - Glob
  - AskUserQuestion
  - Write
  - WebSearch
  - WebFetch
---

# Plan Interview

Conduct in-depth technical interviews about project plans to deeply understand implementation details, uncover hidden assumptions, and identify potential issues before implementation begins.

**Language:** Match the user's input language. Use explicitly requested language if specified.

## Workflow

### Step 1: Understand Input

Input: `$ARGUMENTS`

- **File path** (contains `/` or ends with `.md`, `.txt`) → Read the file, use Glob for related files
- **Text description** → Use directly as project concept

### Step 2: Assess Complexity

| Complexity | Indicators | Questions |
|------------|------------|-----------|
| Simple | Single feature, clear scope | 3-4 |
| Medium | Multiple features, some integrations | 5-7 |
| Complex | System-wide, many integrations | 8-10 |

### Step 3: Conduct Interview

Use AskUserQuestion tool. Ask ONE question at a time.

For question areas, see [references/interview-areas.md](references/interview-areas.md).

**Progress Tracking:** Display after each question:

```
[Progress: 2/6 | Covered: Architecture, API | Remaining: Security, Testing]
```

**Guidelines:**

- Ask meaningful follow-up questions
- Dig deeper on vague answers
- Challenge assumptions respectfully
- Skip non-applicable areas

**Intermediate Save:** Every 3-4 questions, save to `.interview-progress-<timestamp>.md`:

- Questions asked and responses
- Areas covered and remaining

**Completion:** Interview ends when:

1. All relevant areas covered, OR
2. Maximum questions (10) reached, OR
3. User requests to end

Before ending: "I've covered [areas]. Anything else before writing the specification?"

### Step 4: Write Specification

Use template from [references/spec-template.md](references/spec-template.md).

**Output location:**

- File input → Same directory with `-spec` suffix
- Text input → Ask user, default `./specs/<project-name>-spec.md`

**Cleanup:** Delete `.interview-progress-*.md` after successful spec generation.

## Anti-Patterns

- **Asking obvious questions**: Don't ask what's already in the plan
- **Rushing through areas**: Ensure clarity before moving on
- **Ignoring context**: Adapt questions to project type
- **Skipping confirmation**: Always confirm before ending

## Extension Points

1. **Custom interview areas**: Add domain-specific areas in references/interview-areas.md
2. **Template customization**: Modify spec template for organization standards

## Design Rationale

**Why dynamic question count?** Fixed counts don't fit all projects. Simple features need fewer questions; complex systems need thorough exploration.

**Why intermediate saves?** Long interviews risk context loss. Periodic saves preserve progress and enable session recovery.

**Why separate references?** Keeps SKILL.md lean. Question lists and templates are loaded only when needed.
