# hello-world

Essential dev workflow: git commit and GitHub PR with automated code review
for Claude Code.

## Commands

```text
/commit
/commit [additional context]
```

Create well-structured git commits with conventional commit format.

**Features:**

- Conventional commit format (feat, fix, docs, etc.)
- Automatic staging of relevant files
- Style reference from recent commits

---

```text
/interview path/to/plan.md
/interview "Build a todo app with React"
```

Conduct technical interviews about project plans
to generate specifications.

**Features:**

- Dynamic question count based on complexity (3-10 questions)
- Progress tracking during interview
- Automatic specification document generation
- Intermediate save for long interviews

---

```text
/pr
/pr main
/pr --draft
/pr main --draft
```

Create GitHub PR with automated code review.

**Features:**

- Pre-flight checks (git repo, branch, uncommitted changes, gh CLI)
- Automated code review with error/warning categorization
- Auto-fix suggestions for common issues
- Smart PR title/description generation
- Push confirmation before creating PR

---

```text
/simplify
/simplify src/utils.ts
```

Simplify code after completion.

**Features:**

- Flatten nested conditionals (3+ levels) using early return
- Extract repeated patterns (3+ occurrences) into utility functions
- Improve variable/function naming for clarity
- Remove dead code: unused imports, commented code
- Always asks for confirmation before making edits

## Agents

### code-simplifier

The `/simplify` command uses the `code-simplifier` agent.
This agent proactively analyzes code for simplification opportunities.

**Simplification Principles:**

- Complexity reduction: early return, guard clauses
- Pattern extraction: DRY principle for repeated logic
- Naming improvement: clear, descriptive identifiers
- Dead code removal: unused imports, unreachable code

## Skills

### plan-interview

The `/interview` command uses the `plan-interview` skill internally.
This skill provides:

- 4-step workflow: input understanding, complexity assessment,
  interview, specification
- Interview areas: Architecture, Backend, Frontend, AI/LLM,
  Concerns, Scalability
- Specification template generation
- References for interview questions and spec format

### pr-workflow

The `/pr` command uses the `pr-workflow` skill internally. This skill provides:

- 9-step workflow from pre-checks to PR creation
- Code review rules for readability, error handling, duplication, type safety
- PR template generation
- Error message handling

## Workflow

```text
/commit → /pr → Review → Push → PR Created
```

1. **Commit**: Stage and commit your changes with `/commit`
2. **PR**: Run `/pr` to start the PR workflow
3. **Review**: Automated code review checks for issues
4. **Push**: Confirm push to remote
5. **Done**: PR is created with generated title and description

## Code Review Categories

The PR workflow reviews code for:

- **Readability**: Naming, function length, nesting depth
- **Error Handling**: Async/Promise, null safety, catch blocks
- **Duplication**: Identical code blocks
- **Type Safety**: TypeScript `any` usage, missing types
- **Security**: Hardcoded secrets in config files

## Requirements

> [!IMPORTANT]
>
> - Git repository
> - [GitHub CLI (gh)](https://cli.github.com) installed and authenticated

## Installation

```bash
/plugin install hello-world@claude-plugin-pack
```

## License

MIT
