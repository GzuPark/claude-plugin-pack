# hello-world

Essential dev workflow: git commit and GitHub PR with automated code review for Claude Code.

## Commands

### /commit

Create well-structured git commits with conventional commit format.

```
/commit
/commit [additional context]
```

**Features:**

- Conventional commit format (feat, fix, docs, etc.)
- Automatic staging of relevant files
- Style reference from recent commits

### /pr

Create GitHub PR with automated code review.

```
/pr
/pr main
/pr --draft
/pr main --draft
```

**Features:**

- Pre-flight checks (git repo, branch, uncommitted changes, gh CLI)
- Automated code review with error/warning categorization
- Auto-fix suggestions for common issues
- Smart PR title/description generation
- Push confirmation before creating PR

## Skills

### pr-workflow

The `/pr` command uses the `pr-workflow` skill internally. This skill provides:

- 9-step workflow from pre-checks to PR creation
- Code review rules for readability, error handling, duplication, type safety
- PR template generation
- Error message handling

## Workflow

```
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

- Git repository
- [GitHub CLI (gh)](https://cli.github.com) installed and authenticated

## Installation

```bash
/plugin install hello-world@claude-plugin-pack
```

## License

MIT
