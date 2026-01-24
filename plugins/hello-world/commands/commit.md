---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(git branch:*), Bash(git log:*)
description: Create a git commit
argument-hint: [additional context]
---

# Git Commit

Create a well-structured git commit based on the current changes.

## Additional Context from User

$ARGUMENTS

## Context

Gather information about the current repository state:

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD 2>/dev/null || git diff`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10 2>/dev/null || echo "No commits yet"`

## Your Task

Based on the above changes, create a single git commit.

### Commit Message Guidelines

1. **Subject line**: Use imperative mood, max 50 characters
   (e.g., "Add user authentication", "Fix memory leak in parser")
2. **Body** (if needed): Explain the "why" rather than the "what",
   wrap at 72 characters
3. **Format**: Follow conventional commit style when appropriate
   (feat, fix, docs, refactor, test, chore)

### Execution

- Stage relevant files and create the commit using a single message.
- Use unordered lists (bullet points) in the commit body when
  describing multiple changes or points.
- Do NOT include "Generated with Claude Code", "Co-Authored-By", or
  any AI attribution in the commit message unless the user explicitly
  requests it.
- Do not use any other tools or do anything else.
