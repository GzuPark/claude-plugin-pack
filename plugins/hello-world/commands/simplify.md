---
allowed-tools: Read, Edit, Grep, Glob, AskUserQuestion, Bash(git diff:*)
argument-hint: [file-path]
description: Simplify code after completion
---

# Simplify

Invoke the code-simplifier agent to analyze and simplify code.

**Input:** $ARGUMENTS

Use the code-simplifier agent to:

1. Identify target files from argument or recent git diff
2. Analyze code for simplification opportunities
3. Propose changes with explanation (NEVER auto-edit)
4. Apply approved changes after user confirmation

## Simplification Principles

### 1. Reduce Complexity

- Flatten nested conditionals using early return / guard clauses
- Remove unnecessary abstractions

### 2. Extract Repeated Logic

- Extract patterns that repeat 3+ times
- Separate into utility functions

### 3. Improve Naming

- Use meaningful variable names
- Make function names clearly describe their action

### 4. Remove Dead Code

- Remove unused imports
- Delete commented-out code

## Guidelines

- ALWAYS ask for confirmation before making any edits
- Preserve meaningful abstractions
- Warn if changes might break tests
- Don't simplify performance-critical optimized code

Begin by identifying the target files and analyzing for simplification
opportunities.
