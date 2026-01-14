# Synthesis Checklist

Self-review checklist replacing multi-agent synthesis. Apply multiple perspectives to validate skill design before finalization.

## Purpose

Ensures comprehensive review by systematically applying different viewpoints:

- Design perspective: Is it well-architected?
- Audience perspective: Is it usable?
- Evolution perspective: Is it future-proof?

---

## Design Perspective

Evaluates architectural quality and technical soundness.

### Design Checklist

| # | Item | Check | Notes |
|---|------|-------|-------|
| D1 | **Single responsibility**: Does the skill do one thing well? | ☐ | |
| D2 | **Clear boundaries**: Are scope limits explicitly defined? | ☐ | |
| D3 | **Minimal dependencies**: Are external dependencies minimized? | ☐ | |
| D4 | **Error handling**: Are failure modes identified and handled? | ☐ | |

### Design Key Questions

- Could this skill be split into smaller, more focused skills?
- Are there implicit assumptions that should be explicit?
- What happens when things go wrong?
- Is the complexity justified by the value delivered?

### Design Red Flags

- Skill tries to do too many things
- Dependencies on specific versions or tools
- No consideration for error cases
- Over-engineered for the problem at hand

---

## Audience Perspective

Evaluates usability and user experience.

### Audience Checklist

| # | Item | Check | Notes |
|---|------|-------|-------|
| A1 | **Clear triggers**: Are invocation methods obvious? | ☐ | |
| A2 | **Intuitive workflow**: Does the process match user expectations? | ☐ | |
| A3 | **Helpful output**: Does output guide next steps? | ☐ | |
| A4 | **Appropriate complexity**: Does difficulty match target audience? | ☐ | |

### Audience Key Questions

- Would a new user understand how to invoke this skill?
- Does the output format match what users expect?
- Are error messages actionable?
- Is there unnecessary friction in the workflow?

### Audience Red Flags

- Triggers require memorization or documentation lookup
- Output requires interpretation or additional processing
- Error messages are technical rather than actionable
- Workflow assumes expert knowledge

---

## Evolution Perspective

Evaluates future-readiness and maintainability.

### Evolution Checklist

| # | Item | Check | Notes |
|---|------|-------|-------|
| E1 | **Extension points**: Are customization hooks documented? | ☐ | |
| E2 | **Version independence**: No hardcoded versions or paths? | ☐ | |
| E3 | **Design rationale**: Is the WHY documented? | ☐ | |
| E4 | **Anti-patterns**: Are pitfalls documented? | ☐ | |

### Evolution Key Questions

- What will break when dependencies change?
- How would someone extend this skill?
- Why were these design decisions made?
- What mistakes might future maintainers make?

### Evolution Red Flags

- Specific version numbers in instructions
- No documentation of design decisions
- Closed systems with no extension points
- Assumptions about current state of tools/APIs

---

## Synthesis Process

### Step 1: Initial Pass

Complete all checklists quickly (2-3 minutes per perspective):

```markdown
## Synthesis Pass 1

### Design
- D1: ✓ Single responsibility maintained
- D2: ✓ Boundaries defined in Scope section
- D3: ⚠ Depends on specific tool (noted for review)
- D4: ✓ Error handling documented

### Audience
- A1: ⚠ Only 2 triggers, could add more
- A2: ✓ Standard workflow pattern
- A3: ✓ Output includes next steps
- A4: ✓ Appropriate for target audience

### Evolution
- E1: ✗ No extension points section
- E2: ✓ No hardcoded versions
- E3: ✗ Missing WHY section
- E4: ✓ Anti-patterns documented
```

### Step 2: Address Issues

For each ⚠ (warning) and ✗ (fail):

1. Assess impact (Critical/Major/Minor)
2. Decide: Fix now vs Accept with rationale
3. Document decision

```markdown
## Issue Resolution

### E1: No extension points (Critical)
Decision: Fix now
Action: Add ## Extension Points section with 2+ items

### A1: Only 2 triggers (Minor)
Decision: Fix now
Action: Add 2 more natural language triggers

### E3: Missing WHY section (Major)
Decision: Fix now
Action: Add ## Design Rationale section
```

### Step 3: Final Verification

After fixes, re-check all items:

```markdown
## Final Verification

Design: 4/4 ✓
Audience: 4/4 ✓
Evolution: 4/4 ✓

Status: Ready for packaging
```

---

## Integration with Workflow

### When to Apply

- After Implementation phase, before Packaging
- When making significant modifications to existing skills
- During skill review or audit

### Minimum Requirements

Before proceeding to packaging:

- [ ] All 12 checklist items evaluated
- [ ] All Critical issues resolved
- [ ] All Major issues resolved or accepted with rationale
- [ ] Minor issues documented (fix optional)
- [ ] Final verification passed

---

## Quick Reference Card

```text
DESIGN (Is it well-built?)
☐ D1 Single responsibility
☐ D2 Clear boundaries
☐ D3 Minimal dependencies
☐ D4 Error handling

AUDIENCE (Is it usable?)
☐ A1 Clear triggers
☐ A2 Intuitive workflow
☐ A3 Helpful output
☐ A4 Appropriate complexity

EVOLUTION (Is it future-proof?)
☐ E1 Extension points
☐ E2 Version independence
☐ E3 Design rationale (WHY)
☐ E4 Anti-patterns documented
```

---

## Synthesis Report Template

```markdown
# Synthesis Report: [Skill Name]

## Summary
- Date: [date]
- Reviewer: [name/role]
- Status: [Pass/Needs Work]

## Checklist Results

### Design Perspective
| Item | Status | Notes |
|------|--------|-------|
| D1 Single responsibility | ✓/⚠/✗ | |
| D2 Clear boundaries | ✓/⚠/✗ | |
| D3 Minimal dependencies | ✓/⚠/✗ | |
| D4 Error handling | ✓/⚠/✗ | |

### Audience Perspective
| Item | Status | Notes |
|------|--------|-------|
| A1 Clear triggers | ✓/⚠/✗ | |
| A2 Intuitive workflow | ✓/⚠/✗ | |
| A3 Helpful output | ✓/⚠/✗ | |
| A4 Appropriate complexity | ✓/⚠/✗ | |

### Evolution Perspective
| Item | Status | Notes |
|------|--------|-------|
| E1 Extension points | ✓/⚠/✗ | |
| E2 Version independence | ✓/⚠/✗ | |
| E3 Design rationale | ✓/⚠/✗ | |
| E4 Anti-patterns | ✓/⚠/✗ | |

## Issues and Resolutions
| Issue | Severity | Resolution |
|-------|----------|------------|
| [issue] | Critical/Major/Minor | [action taken] |

## Final Status
- Total: X/12 passed
- Critical issues: X resolved
- Major issues: X resolved, X accepted
- Ready for packaging: Yes/No
```
