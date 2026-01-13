# Deep Research Reference

Deep Research is conducted via web search after quiz completion when the user selects "Deep Research".

---

## Activation

Deep Research is activated when:

- User selects "Deep Research" option after quiz completion
- Or user explicitly requests in-depth research

---

## Workflow

### Step 1: Parallel Web Search (3-5 queries)

Generate search queries based on video content:

| Query Type | Pattern | Example |
|------------|---------|---------|
| Topic Deep Analysis | `"{topic}" in-depth analysis` | `"microservices" in-depth analysis` |
| Case Studies | `"{core concept}" case studies` | `"event-driven architecture" case studies` |
| Speaker/Channel Materials | `"{speaker/channel}" materials` | `"Martin Fowler" materials` |
| Technology Best Practices | `"{technology}" best practices` | `"Kubernetes" best practices` |
| Academic Materials | `"{topic}" research paper` | `"distributed systems" research paper` |

**Parallel Execution**: Execute 3-5 queries simultaneously with WebSearch tool

### Step 2: Collect Related Pages (3-5)

Select most relevant pages from search results:

- Official documentation
- Technical blogs
- Academic materials
- Reliable media

### Step 3: Document Integration

Add `## Deep Research` section to existing Video Insight document

---

## Output Structure

```markdown
## Deep Research

> Generated: {YYYY-MM-DD HH:MM}
> Queries: {list of search queries used}

### Additional Context
{Background information not covered in the video, extended concept explanations}

### Related Resources

| Source | Summary | URL |
|--------|---------|-----|
| {source name} | {1-2 sentence summary} | {URL} |
| ... | ... | ... |

### Advanced Insights
{In-depth analysis integrating video content + web research results}
- Broader context of concepts mentioned in video
- Latest trends or developments
- Different perspectives or critical viewpoints

### Next Steps
{Specific follow-up action suggestions}
- {action 1}: {description}
- {action 2}: {description}
- {action 3}: {description}
```

---

## Query Generation Tips

1. **Use specific terms**: Utilize exact terms mentioned in the video
2. **Include speaker name**: Search for other materials if speaker is well-known
3. **Prioritize recent information**: Include year for latest materials
4. **Diverse sources**: Balance official docs, blogs, and academic materials

---

## Quality Standards

1. **Source citation**: Include source URL for all information
2. **Brief summary**: Each resource summary is 1-2 sentences
3. **Actionable**: Next Steps must be specific and actionable
4. **No duplication**: Don't repeat content already covered in video
5. **Critical perspective**: Include diverse viewpoints (pros/cons)
