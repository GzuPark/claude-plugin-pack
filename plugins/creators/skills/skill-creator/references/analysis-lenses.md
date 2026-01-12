# 6-Lens Analysis Framework

Systematically applies 6 mental models to skill design. Each lens reveals different aspects of the problem space that single-perspective analysis might miss.

## Application Rules

- **Complex skills**: All 6 lenses mandatory
- **Simple skills**: Recommended (optional)

---

## Lens 1: First Principles

**Core Question**: What is fundamentally needed? What remains when conventions are removed?

**Application Method**:

1. Think outside existing skill patterns
2. "If skills didn't exist, how would we solve this problem?"
3. Identify the core value this skill provides
4. Build from fundamental requirements

**Key Questions**:

- What is the atomic unit of value this skill delivers?
- What assumptions are we unnecessarily carrying from existing skills?
- What does the minimum viable skill (MVS) look like?

**Example**:

```
Input: "I need a PDF processing skill"
Analysis: Is PDF the real goal? Or is "extracting information from documents" the goal?
Conclusion: Core value is "information extraction"; PDF is just one input format
```

**Output**: Core value proposition free from conventions

---

## Lens 2: Pre-Mortem

**Core Question**: Assuming this skill has failed, why did it fail?

**Application Method**:

1. Imagine complete failure 6 months from now
2. List all possible reasons for failure
3. Prioritize by likelihood × impact
4. Proactively mitigate top risks

**Pre-Mortem Template**:

```markdown
## Pre-Mortem Analysis

Date: 6 months from now
Outcome: Skill is unused and deprecated

### Failure Reasons:
1. [Reason 1] - Likelihood: High - Impact: Critical
2. [Reason 2] - Likelihood: Medium - Impact: Major
3. [Reason 3] - Likelihood: Low - Impact: Minor

### Added Mitigations:
- [Mitigation for Reason 1]
- [Mitigation for Reason 2]
```

**Failure Categories**:

| Category | Failure Examples |
|----------|------------------|
| Adoption | Too complex, unclear triggers, wrong audience |
| Execution | Timeouts, wrong output, missing edge cases |
| Integration | Conflicts with other skills, ecosystem disruption |
| Evolution | Quickly obsolete, non-extensible, tight coupling |

**Output**: Risk-aware design with built-in mitigations

---

## Lens 3: Constraint Analysis

**Core Question**: What are the real constraints? Which are self-imposed?

**Application Method**:

1. List all perceived constraints
2. Categorize: Hard (real) vs Soft (assumed)
3. Challenge soft constraints
4. Work creatively within hard constraints

**Constraint Categories**:

| Type | Examples | Fixed? |
|------|----------|--------|
| Platform | Claude's token limits | Hard |
| Convention | "Skills should be under 500 lines" | Soft |
| Technical | Must work with existing tools | Mostly Hard |
| Social | "Users expect X pattern" | Soft |

**Example**:

```
Constraint: "10MB file size limit"
Question: Is this a real constraint?
Analysis: Not an API limit, just an assumption from past experience
Conclusion: Needs verification, actual limit may differ
```

**Output**: Clear understanding of real constraints, creative solutions

---

## Lens 4: Pareto Analysis (80/20)

**Core Question**: Which 20% of features deliver 80% of the value?

**Application Method**:

1. List all potential features/capabilities
2. Estimate value contribution of each
3. Identify the vital few (20%)
4. Focus resources on high-value features

**Pareto Matrix**:

| Feature | Value Contribution | Effort | Include? |
|---------|-------------------|--------|----------|
| Core functionality | 60% | Medium | Yes - Essential |
| Edge case handling | 10% | High | Defer - Later |
| Nice-to-have UI | 5% | Low | Consider - Easy win |
| Advanced settings | 5% | High | No - Postpone |

**Key Questions**:

- What features will users use most frequently?
- Without which features would the skill be meaningless?
- What has the highest value-to-complexity ratio?

**Output**: Focused feature set, deferred backlog

---

## Lens 5: Root Cause Analysis (5 Whys)

**Core Question**: Why is this skill needed? (Ask 5 times)

**Application Method**:

1. Need statement: "We need a skill for X"
2. Ask "Why?" and answer
3. Ask "Why?" about the answer
4. Repeat until root cause emerges
5. Verify skill addresses root cause, not symptoms

**Example**:

```text
Need: "Users frequently misuse skills"
Why 1? → Triggers are unclear
Why 2? → Descriptions are too generic
Why 3? → No specific use cases provided
Why 4? → Written without user research
Why 5? → No user research step in skill creation process

Root Cause: Missing user understanding step
Solution: Make specific use case collection mandatory in Understanding phase
```

**Output**: Skill that addresses root cause, not symptoms

---

## Lens 6: Systems Thinking

**Core Question**: How do the parts interact? What are the feedback loops?

**Application Method**:

1. Map skill as a system (inputs, processes, outputs)
2. Identify relationships with other system components
3. Find feedback loops (positive/negative)
4. Locate leverage points for maximum impact

**System Diagram Elements**:

- **Inputs**: User goals, context, settings
- **Processes**: Each step of the skill
- **Outputs**: Artifacts, side effects, state changes
- **Connections**: Dependencies, triggers, compositions

**Key Questions**:

- What other skills does this skill interact with?
- What feedback loops exist (success breeds success, failure propagates)?
- Where are the leverage points with big impact?

**Example**:

```text
Skill: Commit message generator
System Relationships:
- Can integrate with pre-commit hooks
- Can auto-run in CI/CD pipeline
- Influences other developers' commit styles

Feedback Loops:
- Good commit messages → easier code review → more usage → quality improvement
- Wrong messages → trust loss → abandonment → lost improvement opportunity
```

**Output**: System integration map, leverage point identification

---

## Application Protocol

### Step 1: Quick Scan (All Lenses)

Apply each lens for 2-3 minutes to identify most relevant ones:

```markdown
| Lens | Relevance (H/M/L) | Key Insight |
|------|-------------------|-------------|
| First Principles | High | Need to remove X convention |
| Pre-Mortem | High | Clear failure mode: Y |
| Constraint Analysis | Medium | Fake constraint: V |
| Pareto | High | 2 features deliver 80% value |
| Root Cause | High | Address cause not symptom |
| Systems Thinking | Medium | Integration point: W |
```

### Step 2: Deep Analysis (High Relevance Lenses)

Invest 10-15 minutes on each High relevance lens:

1. Apply full protocol described above
2. Document insights in structured format
3. Integrate insights into design
4. Record conflicts with other lenses

### Step 3: Conflict Resolution

When lenses suggest conflicting approaches:

1. Clearly state each perspective
2. Identify underlying tension
3. Decide which lens should take priority for this decision
4. Document resolution and rationale

---

## Minimum Requirements Checklist

Before proceeding with skill creation:

- [ ] All 6 lenses scanned for relevance
- [ ] At least 3 lenses applied in depth
- [ ] At least 3 actionable insights documented
- [ ] All High relevance lenses fully applied
- [ ] Conflicts between lenses resolved
