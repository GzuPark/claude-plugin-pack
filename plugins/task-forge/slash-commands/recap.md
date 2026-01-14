---
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task, AskUserQuestion
description: Work recap with multi-agent analysis
argument-hint: "[commit message]"
---

# Work Recap Command

Analyze the session and organize documentation updates, automation suggestions, learning records, and follow-up tasks.

## Input

- `$1`: (Optional) Commit message. If provided, automatically commits after analysis.

## Execution Flow

### Step 1: Check Git Status

```bash
git status
git diff --stat
```

Check if there are any changes.

**Early Exit:** If there are no staged/unstaged changes and no untracked files, inform the user "No changes to analyze" and end the command.

### Step 2: Prepare Session Context

Identify **important turns** in the current session:

- Turns where AskUserQuestion was used (user decisions)
- Include the last 15 turns by default
- Include important turns regardless of their position

Prepare session summary:

- Tasks performed
- Files modified
- Key decisions made

### Step 3: Phase 1 - Parallel Analysis

Run 4 agents **in parallel**. Use the Task tool to execute them simultaneously:

```
Task 1: doc-updater agent
- Pass session context
- Collect CLAUDE.md, context.md update suggestions

Task 2: automation-scout agent
- Pass session context
- Detect automation opportunities from repetitive patterns

Task 3: learning-extractor agent
- Pass session context
- Extract TIL (Today I Learned) items

Task 4: followup-suggester agent
- Pass session context
- Organize incomplete tasks and next priorities
```

**Important**: The 4 agents are independent, so they MUST be run in parallel.

### Step 4: Phase 2 - Duplicate Validation

After collecting Phase 1 results, run the duplicate-checker agent:

```
Task: duplicate-checker agent
- Pass all suggestions from Phase 1
- Compare with current project's CLAUDE.md, context.md, .claude/
- Filter duplicate items
```

### Step 5: Results Integration and Display

Display results **grouped by action**:

```markdown
## Work Recap Analysis Complete

### To Commit
- N files changed
- Suggested commit message: "[generated message]"

### Documentation Updates
- CLAUDE.md: N items suggested
  - [Item 1 summary]
  - [Item 2 summary]
- context.md: N items suggested
  - [Item 1 summary]

### Automation Opportunities
- N automation suggestions
  - [Type] [Name]: [Description]

### Learning Records (TIL)
- N items
  - [Item 1]
  - [Item 2]

### Next Steps
- P0: [Urgent task]
- P1: [High priority]
- P2: [Medium priority]
```

### Step 6: Action Selection

Use AskUserQuestion to present **multi-select** options:

```
Which actions would you like to execute?

Options:
1. Create commit
2. Update documentation (CLAUDE.md, context.md)
3. Generate automation (skills/commands/agents)
4. Save TIL
5. Do nothing
```

Set `multiSelect: true` to allow multiple selections.

### Step 7: Execute Actions

Execute selected actions in **fixed order**:

1. **Documentation Update** (if selected)
   - Add suggested items to CLAUDE.md
   - Add suggested items to context.md

2. **Automation Generation** (if selected)
   - Use skill-creator, slash-command-creator, or subagent-creator as appropriate
   - Select based on the type classified by automation-scout
   - **Note:** Requires `creators` plugin for automation generation

3. **TIL Save** (if selected)
   - Create or append to `docs/til/YYYY-MM-DD.md` file
   - Save learning-extractor results

4. **Commit** (if selected)
   - Check if `/commit` command exists (`.claude/commands/commit.md`)
   - If exists: Run `/commit` with `$1` or generated message
   - If not exists: Stage all changes and commit directly with `$1` or generated message

## Error Handling

### Phase 1 Agent Failure

- Continue with results from successful agents only
- Omit failed agent's section from results
- Notify user which agent failed

### Phase 2 Failure

- Display Phase 1 results without validation
- Add "Possible duplicates" warning message

## Quick Mode

When `$1` (commit message) is provided:

- Run full analysis process
- Present action selection to user after analysis
- Use provided `$1` for commit message

---

Begin execution. Proceed step by step from Step 1.
