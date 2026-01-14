# Claude Plugin Pack

> [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 경험을 향상시키는 plugin 모음입니다.

## Quick Start

```bash
# Marketplace 추가
/plugin marketplace add GzuPark/claude-plugin-pack

# Plugin 설치
/plugin install hello-world@claude-plugin-pack
```

## Plugins

### hello-world

**일상적인 개발을 위한 필수 workflow**

| Command | 설명 |
| ------- | ---- |
| `/commit` | Conventional format으로 Git commit 생성 |
| `/interview` | Project spec 생성을 위한 기술 인터뷰 |
| `/pr` | 자동 code review가 포함된 GitHub PR 생성 |

```bash
/plugin install hello-world@claude-plugin-pack
```

---

### heimdall

**Claude Code용 확장 statusline** *(북유럽 신화의 감시자 신 헤임달)*

| Feature | 설명 |
| ------- | ---- |
| `/heimdall:bifrost` | One-command 설정 (자동 빌드 및 구성) |
| Dynamic display | 활동에 따라 3-5줄 동적 표시 |
| Tool tracking | 색상 코드별 완료 개수 |
| Agent tracking | 경과 시간과 함께 실행 중인 agent |
| Todo progress | 전체 task 설명 표시 |
| Git integration | Branch, staged/modified, sync 상태 |
| Context usage | 색상 코드 progress bar |

```bash
/plugin install heimdall@claude-plugin-pack
/heimdall:bifrost
```

---

### creators

**Claude Code 확장 기능 생성을 위한 skill**

| Skill | 설명 |
| ----- | ---- |
| skill-creator | SKILL.md로 Agent Skill 생성 |
| slash-command-creator | Custom slash command 생성 |
| hook-creator | Event hook 생성 |
| subagent-creator | Custom subagent 생성 |

```bash
/plugin install creators@claude-plugin-pack
```

---

### task-forge

**업무 생산성 도구**

| Feature | 설명 |
| ------- | ---- |
| `/recap` | Multi-agent work session 분석 |
| meeting-insight | 회의 기록에서 pattern 분석 |
| video-insight | 비디오에서 자막, 요약, Q&A 추출 |
| image-insight | AI 이미지 재현을 위한 JSON profile 생성 |

```bash
/plugin install task-forge@claude-plugin-pack
```

---

## Hooks

재사용 가능한 hook 설정입니다. Claude Code에 설정을 요청하면 자동으로 적용됩니다.

| Hook | 설명 |
| ---- | ---- |
| [markdown-lint](hooks/README.ko.md#1-markdown-lint) | `.md` 파일 편집 시 자동 lint |

자세한 내용은 [hooks/README.ko.md](hooks/README.ko.md)를 참고하세요.

## Update

Custom plugin은 자동 업데이트되지 않습니다. 최신 버전 받기:

```bash
/plugin marketplace update claude-plugin-pack
```

## Structure

```text
claude-plugin-pack/
├── .claude-plugin/          # Marketplace & plugin manifest
├── plugins/                 # 개별 plugin
├── hooks/                   # 재사용 가능한 hook 설정
└── README.md
```

## 직접 만들기

[Claude Code Plugins Documentation](https://docs.anthropic.com/en/docs/claude-code/plugins)을 참고하세요.

## License

MIT
