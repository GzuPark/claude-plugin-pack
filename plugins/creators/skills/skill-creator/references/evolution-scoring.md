# Evolution Scoring Framework

Evaluates a skill's future-readiness. Answers the question: "What will
happen to this skill over time?"

## Overview

Skills with low scores:

- Become maintenance burdens
- Cause confusion as they become obsolete
- Become obstacles to ecosystem evolution
- Become technical debt for future users

**Recommended Score**: 7 or higher (out of 10)

> **Note**: Scores below 7 show warnings and improvement suggestions,
> not block packaging.

---

## Timelessness Score Rubric

### Score 1-2: Ephemeral

**Characteristics**:

- Tightly coupled to specific API versions
- Hardcoded tool versions or paths
- Addresses temporary trends
- No consideration for change

**Example**:

```markdown
# Skill: Formatter for GPT-3.5-Turbo
Formats prompts for gpt-3.5-turbo-0301 API...
```

**Lifespan**: Weeks to months

**Assessment**: Reject. Fundamentally flawed approach.

---

### Score 3-4: Short-Lived

**Characteristics**:

- Depends on specific tools likely to change
- Solves problem in moment-specific way
- Some structure but no extensibility consideration
- May reference volatile external resources

**Example**:

```markdown
# Skill: React Class Component Generator
Generates class components following React 17 patterns...
```

**Lifespan**: 6 months to 1 year

**Assessment**: Reject. Needs fundamental redesign with evolution in mind.

---

### Score 5-6: Moderate

**Characteristics**:

- Sound core approach
- Some hardcoded elements that may change
- No explicit extension points
- Limited time projection

**Example**:

```markdown
# Skill: API Documentation Generator
Generates OpenAPI 3.0 specifications...
(No consideration for OpenAPI 4.0 or alternatives)
```

**Lifespan**: 1-2 years

**Assessment**: Needs modification. Add extension points, document
evolution path.

---

### Score 7-8: Solid Design

**Characteristics**:

- Principle-based, not implementation-specific
- Clear extension points documented
- Dependencies appropriately abstracted
- Time projection completed
- Designed for graceful degradation

**Example**:

```markdown
# Skill: API Documentation Generator
Generates API documentation following industry standards.
Supports OpenAPI 3.x with extension points for future specs.
Pattern-based approach adaptable to new documentation formats.
```

**Lifespan**: 2-4 years

**Assessment**: Approved. Good balance of current utility and future
resilience.

---

### Score 9-10: Timeless

**Characteristics**:

- Solves fundamental, unchanging problems
- Completely principle-based
- Highly composable with other skills
- Designed for evolution from the start
- Can serve as template for other skills

**Example**:

```markdown
# Skill: Systematic Problem Decomposition
Breaks complex problems into verifiable atomic steps.
Pattern: Define → Decompose → Verify → Iterate
(This process is technology-agnostic and timeless)
```

**Lifespan**: 5+ years

**Assessment**: Exemplary. Consider as template for other skills.

---

## Score Calculation Method

### Verification Items (4)

Each item earns 2 points, plus base 2 points:

| Item | Points | How to Check |
| ---- | ------ | ------------ |
| 2+ extension points | +2 | 2+ items in `## Extension Points` section |
| No hardcoded versions | +2 | No specific version strings |
| WHY documented | +2 | `## Design Rationale` or `## WHY` section exists |
| Anti-patterns section | +2 | `## Anti-Patterns` section exists |
| **Base score** | +2 | - |
| **Maximum score** | 10 | - |

### Score Calculation Example

```text
Extension points: 3 → +2 points
Hardcoded versions: None → +2 points
WHY documented: Yes → +2 points
Anti-patterns section: No → +0 points
Base score: +2 points

Total: 2 + 2 + 2 + 0 + 2 = 8 points ✓
```

---

## Common Evolution Anti-Patterns

### Anti-Pattern 1: Version Pinning

**Wrong**:

```markdown
Use claude-3-5-sonnet-20241022 for analysis...
```

**Correct**:

```markdown
Use configured model (default: claude-opus-4-5-20251101, configurable)...
```

---

### Anti-Pattern 2: Tool-Specific Design

**Wrong**:

```markdown
# ESLint Configuration Generator
Generates .eslintrc.json for ESLint 8...
```

**Correct**:

```markdown
# Linting Configuration Generator
Generates linting configuration for JavaScript/TypeScript.
Default: ESLint (configurable via lint_tool parameter).
Provides extension points for future linting tools.
```

---

### Anti-Pattern 3: Missing Extension Points

**Wrong**:

```markdown
## Supported Patterns
- Single-Phase
- Multi-Phase
- Orchestrator
(closed list)
```

**Correct**:

```markdown
## Supported Patterns
Built-in patterns: Single-Phase, Multi-Phase, Orchestrator
Custom patterns: Add to `patterns/` directory following template
```

---

### Anti-Pattern 4: Implicit Dependencies

**Wrong**:

```markdown
Run `npm run build` for validation...
```

**Correct**:

```markdown
Run validation command (default: `npm run build`,
configurable via BUILD_COMMAND or skill settings)
```

---

### Anti-Pattern 5: Point-in-Time Assumptions

**Wrong**:

```markdown
Since Claude currently supports 200K context...
```

**Correct**:

```markdown
Utilize available context window
(designed to scale with future context increases)
```

---

## Anti-Obsolescence Pattern Checklist

| Pattern | Applied? | Evidence |
| ------- | -------- | -------- |
| Principles over implementation | ☐ | General approach, not specific tools |
| WHY documented | ☐ | Rationale included for all decisions |
| Loose coupling | ☐ | Dependencies abstracted |
| Graceful degradation | ☐ | Fallbacks for breaking changes |
| Version independent | ☐ | No hardcoded versions |
| Ecosystem aware | ☐ | Related skills considered |

---

## Time Projection Analysis

Evaluate at each timepoint:

```markdown
## Time Projection

### 6 Months
- **Usage patterns**: How will typical usage differ?
- **Ecosystem changes**: What might change in the environment?
- **Risk assessment**: What could break?

### 1 Year
- **Usage patterns**: ...
- **Ecosystem changes**: ...
- **Risk assessment**: ...

### 2 Years
- **Core problem relevance**: Is the problem still relevant?
- **Approach validity**: Is the solution approach still valid?
```

---

## Evolution Score Template

```markdown
## [Skill Name] Evolution Analysis

### Basic Score Assessment
| Item | Score | Evidence |
| ---- | ----- | -------- |
| Extension points (2+) | 0 or 2 | [evidence] |
| No hardcoded versions | 0 or 2 | [evidence] |
| WHY documented | 0 or 2 | [evidence] |
| Anti-patterns section | 0 or 2 | [evidence] |
| Base score | 2 | - |
| **Total** | **X/10** | |

### Assessment Result
- 7+: ✓ Meets recommended criteria
- Below 7: ⚠ Improvements recommended

### If improvements needed:
1. [Specific improvement]
2. [Specific improvement]
```

---

## Packaging Behavior

When running `package_skill.py`:

1. Evolution score calculated automatically
2. Warning message displayed if below 7
3. Improvement suggestions provided
4. User prompted to continue or stop
5. Proceeds or stops based on user choice

```text
⚠ Evolution Score: 5/10 (recommended: 7+)

Improvement Suggestions:
- Add extension points section (at least 2)
- Add design rationale (WHY) section

Continue anyway? [y/N]
```
