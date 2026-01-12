# Creators

Claude Code 확장 기능 생성을 위한 스킬 모음입니다.

## 설치

```bash
/plugin marketplace add GzuPark/claude-plugin-pack
/plugin install creators@claude-plugin-pack
```

## 스킬

설치 후, 확장 기능 생성을 요청하면 해당 스킬이 자동으로 트리거됩니다.

### skill-creator

**트리거:** "스킬을 만듭니다", "새 스킬을 생성합니다", "이 스킬을 수정합니다"

에이전트 스킬을 다음 구조로 생성:

```text
skill-name/
├── SKILL.md       # 필수 - 프론트매터 + 지침
├── scripts/       # 선택 - 실행 코드
├── references/    # 선택 - 참조 문서
└── assets/        # 선택 - 템플릿, 이미지
```

### slash-command-creator

**트리거:** "슬래시 명령어를 만듭니다", "/deploy 명령어를 생성합니다"

커스텀 명령어 생성 위치:

- 프로젝트: `.claude/commands/`
- 개인: `~/.claude/commands/`

명령어 형식:

```markdown
---
description: 간단한 설명
---

$ARGUMENTS 또는 $1, $2를 사용한 프롬프트 지침
```

### hook-creator

**트리거:** "훅을 만듭니다", "저장 시 자동 포맷을 설정합니다", ".env 수정을 차단합니다"

`settings.json`에 이벤트 훅 생성:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{ "type": "command", "command": "your-script.sh" }]
    }]
  }
}
```

**이벤트:** PreToolUse, PostToolUse, SessionStart, SessionEnd, PermissionRequest, Stop 등

### subagent-creator

**트리거:** "서브에이전트를 만듭니다", "코드 리뷰어 에이전트를 생성합니다"

서브에이전트 생성 위치:

- 프로젝트: `.claude/agents/`
- 사용자: `~/.claude/agents/`

서브에이전트 형식:

```markdown
---
name: code-reviewer
description: 코드를 리뷰합니다. 변경 후 자동으로 사용.
tools: Read, Grep, Glob, Bash
model: sonnet
---

시스템 프롬프트 내용
```

## 라이선스

MIT
