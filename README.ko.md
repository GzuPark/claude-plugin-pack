# Claude Plugin Pack

[Claude Code](https://docs.anthropic.com/en/docs/claude-code)를 위한 플러그인 모음입니다.

## Claude Code 플러그인 소개

Claude Code 플러그인은 Claude Code CLI의 기능을 확장합니다. 이 저장소는 생산성과 개발 워크플로우를 위한 플러그인을 제공합니다.

## 설치

마켓플레이스 추가:

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
| [creators](#creators) | Claude Code 확장 기능 생성을 위한 스킬 |
| [task-forge](#task-forge) | 업무 생산성 도구: 회의 분석, 영상 인사이트 |

### hello-world

일상적인 개발을 위한 필수 워크플로우:

- **/commit** - Conventional Commit 형식으로 Git 커밋 생성
- **/interview** - 프로젝트 계획에 대한 기술 인터뷰를 수행하여 사양 문서 생성
- **/pr** - 자동 코드 리뷰가 포함된 GitHub PR 생성

```bash
/plugin install hello-world@claude-plugin-pack
```

### creators

Claude Code 확장 기능 생성을 위한 스킬:

- **skill-creator** - SKILL.md로 에이전트 스킬 생성
- **slash-command-creator** - 커스텀 슬래시 명령어 생성
- **hook-creator** - 이벤트 훅 생성
- **subagent-creator** - 커스텀 서브에이전트 생성

```bash
/plugin install creators@claude-plugin-pack
```

### task-forge

비개발자를 위한 업무 생산성 도구:

- **meeting-insight** - 회의 기록에서 커뮤니케이션 패턴과 인사이트 분석
- **video-insight** - 비디오에서 자막, 요약, Q&A, 심화 조사 추출

```bash
/plugin install task-forge@claude-plugin-pack
```

## 구조

```text
claude-plugin-pack/
├── .claude-plugin/
│   ├── marketplace.json     # 마켓플레이스 설정
│   └── plugin.json          # 플러그인 매니페스트
├── plugins/                 # 개별 플러그인
├── CLAUDE.md
├── LICENSE
├── README.ko.md
└── README.md
```

## 직접 만들기

[Claude Code 플러그인 문서](https://docs.anthropic.com/en/docs/claude-code/plugins)에서 플러그인을 만드는 방법을 확인하세요.

## 라이선스

MIT
