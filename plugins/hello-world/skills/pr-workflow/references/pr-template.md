# PR Template

PR generation rules for Step 8.

## Title Generation

### Change Type Detection

#### Priority 1: Branch name prefix

| Branch Pattern                 | Type     |
| ------------------------------ | -------- |
| `feature/*`, `feat/*`          | feat     |
| `fix/*`, `bugfix/*`, `hotfix/*`| fix      |
| `refactor/*`                   | refactor |
| `docs/*`, `documentation/*`    | docs     |
| `test/*`, `tests/*`            | test     |
| `chore/*`                      | chore    |
| `style/*`                      | style    |
| `perf/*`, `performance/*`      | perf     |

Extract: `git branch --show-current | sed -E 's|^([^/]+)/.*|\1|'`

#### Priority 2: Most recent commit message

Check for conventional commit prefix: `feat:`, `fix:`, `docs:`, etc.

```bash
git log <base-branch>..HEAD --format=%s | head -1
```

#### Priority 3: Changed file patterns

| File Pattern                  | Type  |
| ----------------------------- | ----- |
| Only `*.md` files             | docs  |
| Only `*test*`, `*spec*` files | test  |
| Only config files             | chore |

**Default**: `feat` if no pattern matches.

### Title Format

1. Get branch name without prefix: `git branch --show-current | sed -E 's|^[^/]+/||'`
2. Convert to readable: Replace `-` and `_` with spaces, capitalize first letter
3. **Length limit**: 50 characters

**Final format**: `[type]: [description]`

Examples:

- `feat: Add user authentication`
- `fix: Resolve memory leak in parser`
- `docs: Update API documentation`

## Description Template

```markdown
## Summary

- [3-5 bullet points summarizing changes]

## Changes

| File | Type | Description |
|------|------|-------------|
| path/to/file.ts | Added/Modified/Deleted | Brief description |

## Impact

[Describe how this change affects the system/users]

## Review Notes

- [Points reviewers should focus on]

## References

- Closes #123
- Related to #456
```

### Section Details

#### Summary Section

- Analyze commit messages: `git log <base>..HEAD --format=%s`
- Group related changes
- Focus on "what" and "why"

#### Changes Table Section

Build from: `git diff <base-branch>...HEAD --stat --name-status`

Type mapping:

- `A` -> Added
- `M` -> Modified
- `D` -> Deleted
- `R` -> Renamed

#### Impact Section

Analyze scope and describe:

- New API endpoints
- Breaking changes
- Database requirements
- Configuration changes

#### Review Notes Section

Based on:

- Code review warnings
- Complexity assessment
- Security considerations

Default: "Check overall code quality and logic."

#### References Section (Optional)

Extract issue references:

```bash
git log <base>..HEAD --format=%B | grep -oE '#[0-9]+'
```

Omit section if no references found.

## gh Command

```bash
gh pr create \
  --title "<generated-title>" \
  --body "<generated-body>" \
  --base <base-branch> \
  [--draft]
```

Add `--draft` flag if specified in arguments.
