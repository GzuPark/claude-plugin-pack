---
name: pr-workflow
description: >-
  GitHub PR creation workflow with automated code review.
  Use when user wants to create a PR, requests `/pr`,
  or needs to push changes to GitHub with quality checks.
---

# PR Workflow

Create GitHub Pull Requests with automated change analysis and code review.

## Triggers

- User runs `/pr` or `/pr [base-branch]`
- User asks to create a PR or pull request
- User wants to push changes and create a PR
- User requests code review before PR creation

## Workflow Overview

```text
Step 1: Pre-checks -> Step 2: Detect Base Branch -> Step 3: Verify Changes
    -> Step 4: Check Existing PR -> Step 5: Gather Context
    -> Step 6: Code Review -> Step 7: Push Confirmation
    -> Step 8: Generate PR -> Step 9: Complete
```

## Step 1: Pre-checks

Stop immediately if any check fails.

### 1.1 Verify Git Repository

```bash
git rev-parse --is-inside-work-tree
```

Fail: "Not a git repository."

### 1.2 Check Current Branch

```bash
git branch --show-current
```

Fail (empty): "Cannot determine current branch. You are in detached HEAD state."

### 1.3 Check Uncommitted Changes

```bash
git status --porcelain
```

Fail (any output): "There are uncommitted changes. Run /commit first."

### 1.4 Verify gh CLI

```bash
gh --version
```

Fail: "gh CLI is not installed. Install it from `https://cli.github.com`"

### 1.5 Verify gh Authentication

```bash
gh auth status
```

Fail: "GitHub authentication required. Run `gh auth login` first."

## Step 2: Detect Base Branch

If no base branch provided:

1. Try: `git remote show origin | grep 'HEAD branch' | cut -d: -f2 | tr -d ' '`
2. Fallback to `main` if exists
3. Fallback to `master` if exists
4. Fail: "Cannot find default branch. Please specify base branch explicitly."

## Step 3: Verify Changes Exist

```bash
git diff <base-branch>...HEAD --stat
```

Fail (no output): "No difference from base-branch."

## Step 4: Check Existing PR

```bash
gh pr list --head $(git branch --show-current) --json url --jq '.[0].url'
```

If URL returned: "A PR already exists for this branch: [URL]"

## Step 5: Gather Context

Collect information for review and PR generation:

```bash
# Commit history
git log <base-branch>..HEAD --oneline

# Changed files summary
git diff <base-branch>...HEAD --stat

# Full diff for review
git diff <base-branch>...HEAD
```

## Step 6: Code Review

Analyze changes for code quality issues.
See [references/code-review-rules.md](references/code-review-rules.md)
for detailed rules.

### 6.1 Change Analysis

```bash
git diff <base-branch>...HEAD --numstat
```

Categorize files and assess impact level (Low/Medium/High).

### 6.2-6.6 Review Categories

Check each code file for:

1. **Readability**: Naming, function length, nesting depth
2. **Error Handling**: Async/Promise, null safety, catch blocks
3. **Duplication**: Identical code blocks
4. **Type Safety** (TypeScript): `any` usage, assertions, missing types
5. **Config Files**: Secrets, localhost URLs

### 6.7 Review Output Format

```text
## Code Review Results

**Status**: PASS | FAIL
**Impact**: Low | Medium | High

### Summary
- Errors: N
- Warnings: M
- Auto-fixable: K

### Issues

#### Errors (blocking)
| File | Line | Category | Issue | Auto-fix |
|------|------|----------|-------|----------|

#### Warnings (informational)
| File | Line | Category | Issue |
|------|------|----------|-------|
```

### 6.8 Review Decision

- **PASS** (errors = 0): Continue to Step 7
- **FAIL** (errors > 0): Show errors, offer auto-fix if available

### 6.9 Auto-Fix

If user accepts auto-fix:

1. Apply fixes (prettier, eslint, Edit tool)
2. Stage modified files: `git add <files>`
3. Output summary
4. Stop (user must commit and re-run /pr)

## Step 7: Push Confirmation

### 7.1 Check Remote Status

```bash
git status -sb
```

| Status         | Action          |
| -------------- | --------------- |
| No remote info | Push with `-u`  |
| `[ahead N]`    | Push            |
| Up to date     | Skip push       |
| `[behind N]`   | Warn and stop   |

### 7.2 Push Scenarios

**No upstream**: Ask "Current branch has no upstream. Push and create PR?"

**Ahead of remote**: Ask "N new local commits. Push and create PR?"

**Behind remote**: "Local branch is behind remote. Run git pull first." Stop.

### 7.3 Execute Push

```bash
git push -u origin $(git branch --show-current)
```

## Step 8: Generate PR

See [references/pr-template.md](references/pr-template.md)
for detailed generation rules.

### 8.1 Generate Title

1. Detect type from branch name prefix (feat/, fix/, etc.)
2. Fallback to commit message prefix
3. Fallback to file patterns
4. Default: `feat`

Format: `[type]: [description]` (max 50 chars)

### 8.2 Generate Description

Build PR body with sections:

- **Summary**: 3-5 bullet points from commit messages
- **Changes**: Table of changed files
- **Impact**: System/user impact description
- **Review Notes**: Points for reviewers
- **References**: Issue links (optional)

### 8.3 Create PR

```bash
gh pr create \
  --title "<title>" \
  --body "<body>" \
  --base <base-branch> \
  [--draft]
```

## Step 9: Complete

Output success message with PR URL and next steps.

See [references/error-messages.md](references/error-messages.md)
for all message templates.

## Anti-Patterns

- **Skipping pre-checks**: Always run all pre-checks before proceeding
- **Auto-pushing without consent**: Always confirm before pushing
- **Blocking on warnings**: Only errors should block PR creation
- **Ignoring existing PRs**: Check for existing PR before creating new one
- **Hardcoded branch names**: Auto-detect or accept as argument

## Extension Points

1. **Review rules customization**: Modify `references/code-review-rules.md`
   to add project-specific rules
2. **PR template customization**: Edit `references/pr-template.md`
   for team-specific formats
3. **Additional pre-checks**: Add project-specific validation in Step 1
4. **Custom auto-fix rules**: Extend Step 6.9 with project-specific fixers

## Design Rationale

**Why inline review instead of separate agents?** MVP simplicity.
The workflow is straightforward enough that a single pass
can handle analysis and review.
Agents can be added in Phase 2 if more specialized review is needed.

**Why auto-fix with user confirmation?**
Balance between convenience and safety.
Auto-fix handles common issues
but requires user to review changes before committing.

**Why stop after auto-fix?** User should verify changes and commit manually.
This ensures awareness of modifications and prevents accidental commits.

**Why progressive push confirmation?**
Different scenarios require different handling.
No upstream needs `-u` flag, ahead needs simple push, behind needs pull first.
