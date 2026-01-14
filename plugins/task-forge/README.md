# task-forge

Workplace productivity tools: meeting analysis, video summaries, work recap, and document insights for Claude Code.

## Commands

### /recap

Analyzes your work session with multi-agent system and organizes actionable outputs.

**Features:**

- 5 parallel agents analyze session context
- Duplicate validation before suggestions
- Interactive multi-select for actions

**Analysis Outputs:**

| Output | Description |
|--------|-------------|
| Documentation | CLAUDE.md, context.md update suggestions |
| Automation | Skill/command/agent creation opportunities |
| TIL | Today I Learned items |
| Next Steps | Incomplete tasks with priority |

**Usage:**

```
/recap
```

```
/recap "feat: add user authentication"
```

## Skills

### meeting-insight

Analyzes meeting transcripts to uncover behavioral patterns and communication insights.

**Triggers:**

- Analyze meeting transcripts for communication patterns
- Get feedback on leadership/facilitation style
- Identify conflict avoidance moments
- Track speaking habits and filler words
- Compare communication improvement over time

**Supported Formats:** `.txt`, `.md`, `.vtt`, `.srt`, `.docx`

**Usage Examples:**

```
Analyze all meetings in this folder and tell me when I avoided conflict.
```

```
Look at my meetings from the past month and identify my communication patterns.
```

```
Compare my Q1 vs Q2 meetings to see if my listening skills improved.
```

**Key Analysis Areas:**

- **Conflict Avoidance**: Hedging language, indirect phrasing, topic-shifting
- **Speaking Ratios**: Talk time percentage, interruption count, question-to-statement ratio
- **Filler Words**: "um", "uh", "like", "you know", "actually" frequency
- **Active Listening**: References, paraphrasing, clarifying questions
- **Leadership**: Decision-making approach, inclusion practices

### video-insight

Extract transcripts, generate summaries, create quizzes, and perform deep research from YouTube videos and local media files.

**Triggers:**

- "video insight", "summarize video", "유튜브 정리해줘", "영상 요약해줘"
- YouTube URL or local video/audio file path

**Supported Input:**

| Type | Formats |
|------|---------|
| YouTube | `https://youtu.be/...`, `https://youtube.com/...` |
| Video | `.mp4`, `.mov`, `.mkv`, `.avi`, `.webm` |
| Audio | `.mp3`, `.m4a`, `.wav`, `.flac`, `.aac` |
| Subtitle | `.srt`, `.vtt` |

**Features:**

- Multi-agent architecture for context efficiency
- Optional Q&A highlights (1-5 pairs based on content length)
- Deep research with web search integration
- Korean/English transcript support

**Prerequisites:**

| Feature | Required Tools |
|---------|----------------|
| YouTube | `yt-dlp` |
| Local files | `whisper-cpp`, `ffmpeg` |

<details>
<summary><strong>macOS Installation</strong></summary>

```bash
# All tools
brew install yt-dlp ffmpeg whisper-cpp
```

</details>

<details>
<summary><strong>Ubuntu Installation</strong></summary>

```bash
# yt-dlp
pipx install yt-dlp

# ffmpeg
sudo apt install ffmpeg

# whisper-cpp (build from source)
git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp && make && sudo cp main /usr/local/bin/whisper-cpp
```

</details>

**Usage Examples:**

```
Summarize this YouTube video: https://youtu.be/...
```

```
~/Downloads/lecture.mp4 파일을 정리해 주세요.
```

### image-insight

Analyze images and generate comprehensive JSON profiles for style recreation and AI image generation.

**Triggers:**

- `image-insight` - Primary trigger
- "analyze this image", "extract visual style", "generate image profile"

**Features:**

- 10-category comprehensive analysis (composition, color, lighting, subject, background, etc.)
- Structured JSON output for AI image recreation (Midjourney, DALL-E, etc.)
- Critical area analysis: hair, hands, facial expression, lighting details
- Hex color codes and actionable generation prompts

**Analysis Categories:**

| Category | Description |
|----------|-------------|
| metadata | Confidence, image type, purpose |
| composition | Rule, layout, focal points, hierarchy |
| color_profile | Dominant colors with hex, palette, temperature |
| lighting | Type, direction, shadows, highlights |
| technical_specs | Medium, style, texture, depth of field |
| artistic_elements | Genre, influences, mood, atmosphere |
| subject_analysis | Expression, hair, hands, positioning |
| background | Setting, surfaces, objects catalog |
| generation_parameters | Recreation prompts, keywords |

**Usage Examples:**

```
Analyze this image and extract the visual style.
```

```
Generate a JSON profile for recreating this photo's lighting and composition.
```

## Installation

```bash
/plugin install task-forge@claude-plugin-pack
```

## License

MIT
