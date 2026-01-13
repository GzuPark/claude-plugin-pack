---
name: meeting-insight
description: Analyzes meeting transcripts to uncover behavioral patterns and communication insights. Identifies conflict avoidance, filler words, conversation dominance, and listening gaps. Use for professionals seeking to improve communication and leadership skills.
metadata:
  model: sonnet
  allowed-tools:
    - Read
    - Grep
    - Glob
---

# Meeting Insight

Transforms meeting transcripts into actionable insights about communication patterns.

## Triggers

- Analyze meeting transcripts for communication patterns
- Get feedback on leadership/facilitation style
- Identify conflict avoidance moments
- Track speaking habits and filler words
- Compare communication improvement over time

## Supported Formats

`.txt`, `.md`, `.vtt`, `.srt`, `.docx`

## Workflow

### 1. Discover Data

```
1. Scan folder for transcript files
2. Check for speaker labels and timestamps
3. Confirm date range of meetings
4. Identify user's name/identifier in transcripts
```

### 2. Clarify Analysis Goals

If not specified, ask what to analyze:

- Specific behaviors (conflict avoidance, interruptions, filler words)
- Communication effectiveness (clarity, directness, listening)
- Meeting facilitation skills
- Speaking patterns and ratios

### 3. Analyze Patterns

See [references/analysis-criteria.md](references/analysis-criteria.md) for detailed criteria.

Key analysis areas:

- **Conflict Avoidance**: Hedging language, indirect phrasing, topic-shifting
- **Speaking Ratios**: Talk time percentage, interruption count, question-to-statement ratio
- **Filler Words**: "um", "uh", "like", "you know", "actually" frequency
- **Active Listening**: References, paraphrasing, clarifying questions
- **Leadership**: Decision-making approach, inclusion practices

### 4. Output Format

For each pattern:

```markdown
### [Pattern Name]

**Finding**: [One-sentence summary]
**Frequency**: [X times across Y meetings]

**Examples**:
1. **[Meeting Name/Date]** - [Timestamp]

   **What Happened**:
   > [Actual quote from transcript]

   **Why This Matters**:
   [Impact or missed opportunity explanation]

   **Better Approach**:
   [Specific alternative phrasing]
```

### 5. Synthesize Insights

```markdown
# Meeting Insights Summary

**Analysis Period**: [Date range]
**Meetings Analyzed**: [X meetings]
**Total Duration**: [X hours]

## Key Patterns

### 1. [Primary Pattern]
- **Observed**: [What was found]
- **Impact**: [Why it matters]
- **Recommendation**: [How to improve]

## Communication Strengths
1. [Strength + example]

## Growth Opportunities
1. **[Area]**: [Specific advice]

## Statistics
- Average speaking time: [X%]
- Questions asked: [X per meeting]
- Filler words: [X per minute]
- Interruptions: [X per meeting]
```

### 6. Offer Follow-Up Options

- Track same metrics in future meetings
- Deep dive into specific meetings or patterns
- Compare to previous periods
- Create personal development plan

## Usage Examples

```
Analyze all meetings in this folder and tell me when I avoided conflict.
```

```
Look at my meetings from the past month and identify my communication patterns.
```

```
Compare my Q1 vs Q2 meetings to see if my listening skills improved.
```

## Limitations

- Depends on transcript quality (cannot analyze audio directly)
- Text-only analysis misses tone, expressions, non-verbal cues
- Cultural communication differences need consideration
- Requires clear speaker identification for accurate analysis

## References

- [Detailed Analysis Criteria](references/analysis-criteria.md)
