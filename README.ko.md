# Claude Plugin Pack

[Claude Code](https://docs.anthropic.com/en/docs/claude-code)를 위한 플러그인 모음입니다.

## Claude Code 플러그인 소개

Claude Code 플러그인은 Claude Code CLI의 기능을 확장합니다. 이 저장소는 생산성과 개발 워크플로우를 위한 플러그인을 제공합니다.

## 설치

Marketplace 추가:

```bash
/plugin marketplace add GzuPark/claude-plugin-pack
```

## 업데이트

커스텀 플러그인은 자동 업데이트되지 않습니다. 다음 명령어로 최신 버전을 받을 수 있습니다:

```bash
/plugin marketplace update claude-plugin-pack
```

## 포함된 플러그인

| 플러그인 | 설명 |
|----------|------|
| [hello-world](#hello-world) | 필수 개발 워크플로우: Git 커밋 및 GitHub PR |
| [heimdall](#heimdall) | Tool/agent/todo tracking 및 session monitoring을 지원하는 확장 statusline |
| [creators](#creators) | Claude Code 확장 기능 생성을 위한 skill |
| [task-forge](#task-forge) | 업무 생산성 도구: 회의 분석, 영상 insight, work recap |

### hello-world

일상적인 개발을 위한 필수 워크플로우:

- **/commit** - Conventional Commit 형식으로 Git 커밋 생성
- **/interview** - 프로젝트 계획에 대한 기술 인터뷰를 수행하여 사양 문서 생성
- **/pr** - 자동 코드 리뷰가 포함된 GitHub PR 생성

```bash
/plugin install hello-world@claude-plugin-pack
```

### heimdall

Claude Code용 확장 statusline입니다 (북유럽 신화의 감시자 신 헤임달의 이름을 따왔습니다):

- **/heimdall:bifrost** - Bifrost 다리 열기 (자동 빌드 및 설정)
- **Dynamic statusline** - 활동에 따라 3-5줄 동적 표시
- **Tool tracking** - 색상 코드별 완료 개수 표시
- **Agent tracking** - 경과 시간과 함께 실행 중인 agent 표시
- **Todo 진행률** - 전체 task 설명 표시
- **Git 통합** - branch, staged/modified, sync 상태
- **MCP server** - 연결 상태 표시
- **Context 사용량** - 색상 코드 progress bar (green → yellow → red)
- **5시간 리셋 타이머** - 사용량 추적

```bash
/plugin install heimdall@claude-plugin-pack
/heimdall:bifrost
```

### creators

Claude Code 확장 기능 생성을 위한 skill:

- **skill-creator** - SKILL.md로 agent skill 생성
- **slash-command-creator** - custom slash command 생성
- **hook-creator** - event hook 생성
- **subagent-creator** - custom subagent 생성

```bash
/plugin install creators@claude-plugin-pack
```

### task-forge

업무 생산성 도구:

- **/recap** - Multi-agent work session 분석으로 문서화, 자동화, TIL, follow-up 제안
- **meeting-insight** - 회의 기록에서 communication pattern과 insight 분석
- **video-insight** - 비디오에서 자막, 요약, Q&A, 심화 조사 추출
- **image-insight** - 이미지 분석 및 AI 이미지 재현을 위한 JSON profile 생성

```bash
/plugin install task-forge@claude-plugin-pack
```

## Hooks

재사용 가능한 Claude Code hook 설정입니다. Claude Code에 hook 설정을 요청하면 자동으로 설정됩니다.

| Hook | 설명 |
|------|------|
| [markdown-lint](hooks/README.ko.md#1-markdown-lint) | `.md` 파일 편집 시 자동 lint |

자세한 내용은 [hooks/README.ko.md](hooks/README.ko.md)를 참고하세요.

## 구조

```text
claude-plugin-pack/
├── .claude-plugin/
│   ├── marketplace.json     # marketplace 설정
│   └── plugin.json          # plugin manifest
├── plugins/                 # 개별 플러그인
├── hooks/                   # 재사용 가능한 hook 설정
├── CLAUDE.md
├── LICENSE
├── README.ko.md
└── README.md
```

## 직접 만들기

[Claude Code 플러그인 문서](https://docs.anthropic.com/en/docs/claude-code/plugins)에서 플러그인을 만드는 방법을 확인하세요.

## 라이선스

MIT
