# heimdall

Tool/agent/todo tracking, Git 상태, session monitoring을 지원하는 Claude Code용 확장 statusline입니다.

> 북유럽 신화에서 Bifrost 다리를 감시하는 신 헤임달의 이름을 따왔습니다.

## 기능

| 기능 | 설명 |
|------|------|
| Dynamic statusline | 활동에 따라 3-5줄 동적 표시 |
| Tool tracking | Tool 유형별 색상 코드 완료 개수 |
| Agent tracking | 경과 시간과 함께 실행 중인 agent 표시 |
| Running activity | Spinner animation과 함께 별도 라인 표시 |
| Todo 진행률 | 완료율과 함께 전체 task 설명 표시 |
| Git 통합 | Branch, staged/modified 개수, sync 상태 |
| MCP server | 연결 상태 표시 |
| Context 사용량 | 색상 코드 progress bar (green -> yellow -> red) |
| 5시간 리셋 타이머 | Local 시간으로 사용량 추적 |
| 비용 추적 | Session 비용 및 라인 변경 (+/-) |

## 출력 예시

### 실행 중인 작업이 있을 때 (5줄)

```text
~/project/private/my-app (main) S:2 M:3 │ ↑1↓0 │ v2.1.7 │ MCP:2 │ 🕐 16:30
🧠 Opus 4.5 │ $12.50 │ +500/-120 │ ████████░░ 65%
Edit×8 | Bash×5 | Read×4 | WebFetch×2 │ ✓ Explore×2
⠋ Read(/src/components/Button.tsx) | ● Explore (searching for API endpoints)
▸ [Implement user authentication module] (2/5) │ RESET at 18:00 (1h 30m left)
```

### 실행 중인 작업이 없을 때 (4줄)

```text
~/project/private/my-app (main) S:2 M:3 │ ✔ │ v2.1.7 │ MCP:-- │ 🕐 16:30
🧠 Opus 4.5 │ $12.50 │ +500/-120 │ ████████░░ 65%
Edit×8 | Bash×5 | Read×4 │ ✓ Explore×2
✓ All todos complete (5/5) │ RESET at 18:00 (1h 30m left)
```

### 최소 표시 (3줄)

```text
~/project/private/my-app (main) │ ✔ │ v2.1.7 │ MCP:-- │ 🕐 16:30
🧠 Opus 4.5 │ $0.00 │ +0/-0 │ ░░░░░░░░░░ 0%
RESET at 18:00 (1h 30m left)
```

## 라인 구성

| Line | 내용 |
|------|------|
| 1 | Project 디렉토리, Git branch, Staged/Modified, Sync 상태, 버전, MCP, 시간 |
| 2 | Model (emoji), 비용, 라인 변경, Context bar + % |
| 3 | 완료된 tool (색상 코드), 완료된 agent (있을 경우) |
| 4 | 실행 중인 tool (spinner), 실행 중인 agent (있을 경우) |
| 4/5 | Todo 진행률, 5시간 리셋 타이머 |

## 설치

```bash
/plugin install heimdall@claude-plugin-pack
```

설치 후 setup command를 실행합니다:

```bash
/heimdall:bifrost
```

자동으로 수행되는 작업:

1. TypeScript statusline 빌드
2. `~/.claude/settings.json` 설정
3. Claude Code 재시작하여 적용

## 수동 설정

수동 설정을 원하는 경우:

### 1. Statusline 빌드

```bash
cd ~/.claude/plugins/cache/claude-plugin-pack/heimdall/*/statusline
npm install && npm run build
```

### 2. Claude Code 설정

`~/.claude/settings.json`에 추가:

```json
{
  "statusLine": {
    "type": "command",
    "command": "node <PATH_TO_PLUGIN>/statusline/dist/index.js",
    "padding": 0
  }
}
```

## Command

### /heimdall:bifrost

Heimdall statusline을 자동으로 빌드하고 설정합니다.

## 요구 사항

- Node.js 18+
- npm

## 라이선스

MIT
