---
allowed-tools: Bash(git:*), Bash(gh:*), Read, Edit, AskUserQuestion
description: Create a GitHub PR with code review
argument-hint: [base-branch] [--draft]
---

# Create Pull Request

Create a GitHub Pull Request with automated change analysis and code review.

## Arguments

$ARGUMENTS

Parse the arguments:

- If `--draft` is present, create a draft PR
- If a branch name is provided (not starting with `--`), use it as the base branch
- If no base branch specified, auto-detect it

## Execution

Follow the pr-workflow skill to complete this task.

The workflow consists of 9 steps:

1. **Pre-checks**: Verify git repo, branch, uncommitted changes, gh CLI
2. **Detect Base Branch**: Auto-detect or use provided argument
3. **Verify Changes**: Ensure diff exists against base branch
4. **Check Existing PR**: Warn if PR already exists for this branch
5. **Gather Context**: Collect commits, diff, changed files
6. **Code Review**: Analyze code quality, offer auto-fix if issues found
7. **Push Confirmation**: Confirm before pushing to remote
8. **Generate PR**: Create title and description, run `gh pr create`
9. **Complete**: Output PR URL and next steps

Refer to the pr-workflow skill for detailed instructions on each step.
