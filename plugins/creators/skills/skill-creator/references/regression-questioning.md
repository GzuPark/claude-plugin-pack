# Regression Questioning Protocol

Core methodology for skill analysis. Apply questions iteratively until no new insights emerge.

## Termination Conditions

- **3 consecutive rounds** with no new insights, OR
- **Maximum 7 rounds** reached

---

## 7 Question Categories

### Category 1: Scope and Boundaries

Clarifies the skill's scope and limits.

| Question | Purpose |
|----------|---------|
| What should this skill **do**? | Define core functionality |
| What should this skill **NOT do**? | Limit scope |
| What are the edge cases? | Identify edge cases |
| Where does it overlap with other skills? | Prevent duplication |
| What does the minimum version look like? | Define MVP |

**Application Example**:

```text
Skill Request: "Git commit message writing helper"

Should do: Generate commit messages
Should NOT do: Branch management, PR creation
Edge cases: Empty commits, large diffs
Overlap: Role division with commit slash command
MVP: Simple commit message generation
```

---

### Category 2: Users and Context

Identifies target users and usage environment.

| Question | Purpose |
|----------|---------|
| Who is the primary user? | Define audience |
| In what situations will it be used? | Understand context |
| What is the user's skill level? | Adjust difficulty |
| What is the usage frequency? | Optimization direction |
| What output does the user expect? | Determine output format |

**Expert Simulation**:

| Expert Type | Key Question |
|-------------|--------------|
| Domain Expert | "What would a domain expert add?" |
| UX Expert | "Is this intuitive for the target user?" |
| System Designer | "How does this integrate with existing systems?" |

---

### Category 3: Technical Constraints

Identifies technical limitations and requirements.

| Question | Purpose |
|----------|---------|
| Required tools/libraries? | Identify dependencies |
| Performance requirements? | Optimization targets |
| Compatibility requirements? | Environment constraints |
| Security considerations? | Vulnerability prevention |
| Input size limits? | Set boundaries |

---

### Category 4: Quality Attributes

Defines quality criteria.

| Question | Purpose |
|----------|---------|
| Accuracy requirements? | Quality criteria |
| Response time requirements? | Performance criteria |
| Error tolerance? | Failure response |
| Consistency requirements? | Predictability |
| Verification method? | Test strategy |

---

### Category 5: Integration Requirements

Identifies integration with other systems.

| Question | Purpose |
|----------|---------|
| Integration with other skills? | Composition potential |
| External system integration? | API connections |
| Data format requirements? | Input/output formats |
| Hook integration? | Automation integration |
| Position in workflow? | Execution order |

---

### Category 6: Evolution Requirements

Prepares for future changes.

| Question | Purpose |
|----------|---------|
| Future expansion plans? | Design extension points |
| Expected changes? | Ensure flexibility |
| Version upgrade strategy? | Backward compatibility |
| Will it be valid in 2 years? | Assess longevity |
| Deprecation conditions? | Exit strategy |

**Time Projection Analysis**:

| Timeframe | Question | Focus |
|-----------|----------|-------|
| Now | Does it solve the immediate problem? | Current utility |
| 1 week | Can the first user succeed? | Initial experience |
| 1 month | What feedback is expected? | Early adoption |
| 6 months | How will usage patterns change? | Maturation |
| 1 year | What ecosystem changes? | External pressure |
| 2 years | Is the core approach still valid? | Fundamental soundness |

---

### Category 7: Risks and Mitigation

Identifies and addresses potential risks.

| Question | Target Failure Mode |
|----------|---------------------|
| What causes complete failure? | Critical failure |
| What produces wrong results? | Silent failure |
| What makes users give up? | Adoption failure |
| What causes obsolescence? | Evolution failure |
| What makes maintenance impossible? | Technical debt |

**For each identified failure mode**:

1. Assess likelihood (High/Medium/Low)
2. Assess impact (Critical/Major/Minor)
3. Design mitigation or prevention
4. Document in anti-patterns section

---

## Round Structure

Each questioning round follows this structure:

```text
Round N:

1. Apply 2-3 questions from different categories
2. Document all discovered insights
3. Integrate insights into design
4. Evaluate: New insights > 0?
   - Yes → Proceed to Round N+1
   - No → Check termination condition
```

### Round Execution Example

```markdown
## Round 3 Analysis

### Applied Questions:
1. Users: "What is the target user's skill level?"
2. Quality: "What are the response time requirements?"
3. Evolution: "What will usage patterns look like in 6 months?"

### Discovered Insights:
1. Users: Must be easy for beginner developers
2. Quality: Need response within 3 seconds even for complex diffs
3. Evolution: May need team-specific commit style support

### Design Updates:
- Added 2 natural language triggers
- Added timeout handling for long diffs
- Documented custom style settings as extension point

### Conclusion: 3 new insights → Continue to Round 4
```

---

## Round 5: No New Insights

```markdown
### Applied Questions:
1. Scope: "Missing edge cases?"
2. Integration: "Additional systems needing integration?"

### Discovered Insights:
(none)

### Conclusion: 1 empty round
```

## Rounds 6-7: Consecutive Empty Rounds

If Rounds 6 and 7 also yield no new insights → **Analysis complete**.

---

## Question Bank by Skill Type

### Executor Skills

- What inputs cause unexpected behavior?
- What outputs need verification before returning?
- What side effects need documentation?

### Analyzer Skills

- What analysis results could be misleading?
- What context is required for accurate analysis?
- Should output include confidence levels?

### Generator Skills

- What templates or patterns to use?
- What customization points are needed?
- How to verify output quality?

---

## Question Anti-Patterns

| Anti-Pattern | Problem | Instead |
|--------------|---------|---------|
| Surface-level questions | Miss deep issues | Apply 5 Whys technique |
| Single perspective | Blind spots | Rotate expert types |
| Early termination | Incomplete analysis | Require 3 empty rounds |
| Confirmation bias | Only validate existing ideas | Apply Devil's Advocate |
| Question fatigue | Skip important questions | Use structured checklist |

---

## Minimum Requirements Checklist

Before completing regression questioning:

- [ ] At least 1 question applied from all 7 categories
- [ ] At least 3 rounds completed
- [ ] At least 3 actionable insights discovered
- [ ] 3 consecutive empty rounds or 7 rounds reached
- [ ] Mitigations documented for major risks
