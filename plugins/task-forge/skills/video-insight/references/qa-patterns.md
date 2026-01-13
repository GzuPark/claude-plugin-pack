# Q&A Patterns Reference

Video Insight Q&A generates 1-5 Q&A pairs based on content length to help viewers remember key information.

## Q&A Count Guidelines

| Content Length | Q&A Count | Criteria |
|----------------|-----------|----------|
| Very short | 1 | < 5 min video, minimal insights |
| Short | 2 | 5-15 min, few key points |
| Medium | 3 | 15-30 min, moderate content |
| Long | 4 | 30-60 min, substantial content |
| Very long | 5 | 60+ min, comprehensive content |

**Principle**: Quality over quantity. Each Q&A should cover a distinct, important point.

---

## Question Types

Select the most appropriate question types based on content:

| Type | Focus | When to Use |
|------|-------|-------------|
| Core Message | Main topic | Always include at least one |
| Key Facts | Specific data/numbers | When video contains important statistics |
| Definition | Basic concept | When new terms are introduced |
| Comparison | Concept differences | When video contrasts multiple ideas |
| Reasoning | Cause/Effect | When video explains why something works |
| Application | Practical use | When video provides actionable advice |

---

## Question Examples

**Core Message**

```markdown
**Q: What is the main message of this video?**

The speaker emphasizes that [core message]. This is demonstrated through [supporting point]. (around 2:30)
```

**Key Facts**

```markdown
**Q: What percentage improvement was achieved in the case study?**

The case study showed a 40% improvement in efficiency after implementing the new process. The speaker attributes this to [reason]. (around 12:15)
```

**Comparison**

```markdown
**Q: What is the key difference between approach A and approach B?**

Approach A focuses on [aspect], while approach B emphasizes [different aspect]. The speaker recommends A for [situation] and B for [other situation]. (around 8:45)
```

**Application**

```markdown
**Q: How can viewers apply this technique in their daily work?**

The speaker suggests starting with [first step], then [second step]. Key considerations include [important factor]. (around 18:20)
```

---

## Output Format

```markdown
## Q&A: Key Points to Remember

**Q: {question}**

{Detailed answer with context and timestamp reference}

**Q: {question}**

{Detailed answer with context and timestamp reference}
```

---

## Q&A Generation Guidelines

1. **Based on video content**: Q&A from actual mentioned content, not speculation
2. **Complete answers**: Provide enough context for standalone understanding
3. **Use timestamps**: Reference when the content appeared if possible
4. **Practical focus**: Emphasize actionable insights when available
5. **Clarity**: Both questions and answers should be unambiguous

---

## Answer Format

- **Length**: 2-4 sentences providing complete context
- **Timestamps**: Include approximate timestamps like "(around X:XX)"
- **Self-contained**: Answers should be understandable without watching the video

---

## Purpose

The Q&A section serves as a quick reference for viewers to:

- Review key points without re-watching the entire video
- Verify understanding of main concepts
- Find specific information with timestamp references
- Share knowledge highlights with others
