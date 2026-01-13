# task-forge

Workplace productivity tools: meeting analysis, video summaries, and document insights for Claude Code.

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

## Installation

```bash
/plugin install task-forge@claude-plugin-pack
```

## License

MIT
