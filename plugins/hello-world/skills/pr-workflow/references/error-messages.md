# Error Messages

Standard error messages for PR workflow.

## Pre-check Errors

| Condition | Message |
|-----------|---------|
| Not a git repo | Not a git repository. |
| Detached HEAD | Cannot determine current branch. You are in detached HEAD state. |
| Uncommitted changes | There are uncommitted changes. Run /commit first. |
| gh not installed | gh CLI is not installed. Install it from <https://cli.github.com> |
| gh not authenticated | GitHub authentication required. Run `gh auth login` first. |
| No base branch found | Cannot find default branch. Please specify base branch explicitly. |
| No diff | No difference from <base-branch>. Verify you have changes to push. |
| PR already exists | A PR already exists for this branch: [URL] |

## Review Errors

| Condition | Message |
|-----------|---------|
| Review failed | Code review found N errors. (M auto-fixable) |
| Auto-fix completed | Auto-fix complete: N files modified, M issues remain. |
| Auto-fix skipped | Fix the issues above manually, then re-run /pr. |

## Push Errors

| Condition | Message |
|-----------|---------|
| Push cancelled | PR creation cancelled. |
| Push failed | Push failed. Check permissions or network connection. |
| Behind remote | Local branch is behind remote. Run git pull first. |

## PR Creation Errors

| Condition | Message |
|-----------|---------|
| Auth expired | GitHub authentication expired. Run `gh auth refresh`. |
| Permission denied | No permission to create PR in this repository. |
| Network error | Network error occurred. Check connection and try again. |

## Success Messages

| Condition | Message |
|-----------|---------|
| PR created | PR created successfully! |
| Draft PR created | Draft PR created! |

## Success Output Template

### Regular PR

```
PR created successfully!

[PR Title]
[PR URL]

Next steps:
- Review the PR content on the page
- Assign reviewers if needed
- Check CI status
```

### Draft PR

```
Draft PR created!

[PR Title]
[PR URL]

This is a draft PR. Click "Ready for review" on GitHub when ready.
```
