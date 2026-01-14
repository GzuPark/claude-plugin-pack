---
name: image-insight
description: >
  Analyze images and generate comprehensive JSON profiles for style recreation.
  Use when users upload images for visual analysis, style extraction,
  AI image generation prompts, or need detailed breakdowns of composition,
  lighting, color, and subject elements.
---

# Image Insight

## Overview

Analyze uploaded images and return structured JSON profiles containing
composition, color, lighting, subject, and background analysis with
actionable recreation parameters for AI image generation.

## Triggers

- `image-insight` - Primary trigger for image analysis
- "analyze this image" - Natural language trigger
- "extract visual style" - Style extraction request
- "generate image profile" - Profile generation request
- "what's in this image" - Detailed breakdown request

## Workflow

### Step 1: Receive Image

Accept the uploaded image file. Verify it's a valid image format.

### Step 2: Multi-Category Analysis

Analyze across all schema categories:

1. **metadata** - Confidence, image type, purpose
2. **composition** - Rule, layout, focal points, hierarchy
3. **color_profile** - Dominant colors with hex, palette, temperature
4. **lighting** - Type, direction, shadows, highlights
5. **technical_specs** - Medium, style, texture, depth of field
6. **artistic_elements** - Genre, influences, mood, atmosphere
7. **typography** - Fonts, placement (if text present)
8. **subject_analysis** - Expression, hair, hands, positioning
9. **background** - Setting, surfaces, objects catalog
10. **generation_parameters** - Recreation prompts, keywords

### Step 3: Apply Critical Area Rules

For portraits, apply detailed analysis per
[references/critical-areas.md](references/critical-areas.md):

- Hair: exact length, cut style, natural imperfections
- Hands: each hand separately, finger positions, tension
- Background: wall material distinction
  (drywall vs concrete vs brick)
- Lighting: directionality, shadow characteristics

### Step 4: Generate JSON Output

Return structured JSON following [references/json-schema.md](references/json-schema.md).

**Output requirements:**

- Valid JSON only - no markdown, no commentary
- All sections populated with specific values
- Hex codes for colors
- Actionable generation prompts

## Quick Reference

### Color Profile

```json
{
  "color": "coral pink",
  "hex": "#FF7F7F",
  "percentage": "35%",
  "role": "primary subject"
}
```

### Lighting Assessment

- **Directional**: Strong shadows, sculpted appearance
- **Diffused**: Soft minimal shadows, even illumination
- Assess: type, direction, shadow edge quality, contrast ratio

### Subject Analysis Priorities

1. Facial expression: mouth, eyes, emotion, authenticity
2. Hair: length, cut, texture, natural imperfections
3. Hands: position, tension, naturalness
4. Body: posture, angle, weight distribution

## Resources

### references/

- [core-prompt.md](references/core-prompt.md) - Core analysis system prompt
- [json-schema.md](references/json-schema.md) - Complete JSON output schema
- [analysis-rules.md](references/analysis-rules.md) -
  Category-specific analysis rules
- [critical-areas.md](references/critical-areas.md) -
  Hair, hands, background, lighting details

### scripts/

- `validate_output.py` - Validate JSON structure and completeness

## Anti-Patterns

- **Vague descriptions**: Avoid "nice", "good", "beautiful" -
  use specific technical terms
- **Perfect hair**: Never describe hair as "perfect" -
  real hair has flyaways, frizz, variation
- **Generic backgrounds**: Don't say "wall" -
  specify material (painted drywall, concrete, brick)
- **Skipped hands**: Always document hand positions
  even if hidden or out of frame
- **Markdown in output**: Output pure JSON only -
  no code blocks, no explanatory text

## Extension Points

1. **Image Type Variants**: Create specialized schemas
   for landscapes, products, architecture
2. **Selective Analysis**: Add parameter to request specific categories only
3. **Batch Processing**: Extend for analyzing multiple images in sequence
4. **Confidence Thresholds**: Add configurable confidence scoring criteria

## Design Rationale

This skill encapsulates 15+ years of visual analysis expertise to:

1. Enable consistent, reproducible image analysis across different contexts
2. Generate actionable prompts for AI image recreation
   (Midjourney, DALL-E, etc.)
3. Provide structured data for downstream processing and automation
4. Standardize style extraction with emphasis on natural imperfections
   over idealized descriptions
5. Support multimodal analysis leveraging Claude's vision
   capability
