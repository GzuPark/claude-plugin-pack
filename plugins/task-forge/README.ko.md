# task-forge

Claude Code를 위한 업무 생산성 도구입니다. 회의 분석, 영상 요약, 작업 정리, 문서 insight 기능을 제공합니다.

## Command

### /recap

Multi-agent system으로 작업 session을 분석하고 실행 가능한 결과물을 정리합니다.

**기능:**

- 5개 agent가 병렬로 session context 분석
- 제안 전 중복 검증
- Interactive multi-select로 action 선택

**분석 결과:**

| 결과 | 설명 |
|------|------|
| 문서 | CLAUDE.md, context.md 수정 제안 |
| 자동화 | skill/command/agent 생성 기회 |
| TIL | 오늘 배운 것 |
| 다음 단계 | 미완료 작업과 우선순위 |

**사용법:**

```
/recap
```

```
/recap "feat: 사용자 인증 추가"
```

## Skill

### meeting-insight

회의 기록을 분석하여 행동 패턴과 communication insight를 도출합니다.

**Trigger:**

- 회의 기록의 communication pattern 분석
- Leadership/facilitation style feedback
- 갈등 회피 순간 식별
- 발화 습관 및 군말 추적
- 시간에 따른 커뮤니케이션 개선 비교

**지원 형식:** `.txt`, `.md`, `.vtt`, `.srt`, `.docx`

**사용 예시:**

```
이 폴더의 모든 회의를 분석하고 갈등을 회피한 순간을 알려 주세요.
```

```
지난 달 회의를 보고 communication pattern을 파악해 주세요.
```

```
Q1과 Q2 회의를 비교하여 경청 skill이 개선되었는지 확인해 주세요.
```

**주요 분석 영역:**

- **갈등 회피**: 회피 언어, 간접적 표현, 주제 전환
- **발언 비율**: 발언 시간 비율, 끼어들기 횟수, 질문 대 진술 비율
- **군말**: "음", "어", "그러니까", "있잖아", "뭐랄까" 빈도
- **적극적 경청**: 인용, 바꿔 말하기, 명확화 질문
- **리더십**: 의사결정 방식, 포용적 진행

### video-insight

YouTube 영상 및 로컬 미디어 파일에서 자막을 추출하고, 요약을 생성하며, 퀴즈를 만들고, 심화 조사를 수행합니다.

**Trigger:**

- "video insight", "summarize video", "유튜브 정리해줘", "영상 요약해줘"
- YouTube URL 또는 로컬 비디오/오디오 파일 경로

**지원 입력:**

| 유형 | 형식 |
|------|------|
| YouTube | `https://youtu.be/...`, `https://youtube.com/...` |
| 비디오 | `.mp4`, `.mov`, `.mkv`, `.avi`, `.webm` |
| 오디오 | `.mp3`, `.m4a`, `.wav`, `.flac`, `.aac` |
| 자막 | `.srt`, `.vtt` |

**기능:**

- Context 효율성을 위한 multi-agent architecture
- 선택적 Q&A 하이라이트 (내용 길이에 따라 1-5쌍)
- 웹 검색을 통한 심화 조사
- 한국어/영어 자막 지원

**필수 도구:**

| 기능 | 필요 도구 |
|------|-----------|
| YouTube | `yt-dlp` |
| 로컬 파일 | `whisper-cpp`, `ffmpeg` |

<details>
<summary><strong>macOS 설치</strong></summary>

```bash
# 모든 도구
brew install yt-dlp ffmpeg whisper-cpp
```

</details>

<details>
<summary><strong>Ubuntu 설치</strong></summary>

```bash
# yt-dlp
pipx install yt-dlp

# ffmpeg
sudo apt install ffmpeg

# whisper-cpp (소스에서 빌드)
git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp && make && sudo cp main /usr/local/bin/whisper-cpp
```

</details>

**사용 예시:**

```
이 유튜브 영상을 요약해 주세요: https://youtu.be/...
```

```
~/Downloads/lecture.mp4 파일을 정리해 주세요.
```

### image-insight

이미지를 분석하여 style 재현 및 AI 이미지 생성을 위한 종합적인 JSON profile을 생성합니다.

**Trigger:**

- `image-insight` - Primary trigger
- "analyze this image", "이미지 분석해 줘", "visual style 추출해 줘"

**기능:**

- 10개 category 종합 분석 (composition, color, lighting, subject, background 등)
- AI 이미지 재현을 위한 구조화된 JSON 출력 (Midjourney, DALL-E 등)
- 중요 영역 분석: hair, hands, 표정, lighting 세부사항
- Hex color code 및 실행 가능한 generation prompt

**분석 Category:**

| Category | 설명 |
|----------|------|
| metadata | 신뢰도, 이미지 유형, 목적 |
| composition | 구도, layout, focal point, hierarchy |
| color_profile | Hex code 포함 dominant color, palette, 온도 |
| lighting | 유형, 방향, shadow, highlight |
| technical_specs | 매체, style, texture, 피사계 심도 |
| artistic_elements | 장르, 영향, 분위기, atmosphere |
| subject_analysis | 표정, hair, hands, 자세 |
| background | 배경 설정, 표면, object catalog |
| generation_parameters | 재현 prompt, keyword |

**사용 예시:**

```
이 이미지를 분석하고 visual style을 추출해 주세요.
```

```
이 사진의 조명과 구도를 재현할 수 있는 JSON profile을 생성해 주세요.
```

## 설치

```bash
/plugin install task-forge@claude-plugin-pack
```

## 라이선스

MIT
