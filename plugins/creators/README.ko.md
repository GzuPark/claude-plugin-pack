# Creators

Claude Code 확장 기능 생성을 위한 skill 모음입니다.

## 설치

```bash
/plugin marketplace add GzuPark/claude-plugin-pack
/plugin install creators@claude-plugin-pack
```

## Skill

설치 후, 확장 기능 생성을 요청하면 해당 skill이 자동으로 trigger됩니다.

### skill-creator

**Trigger:** "skill을 만듭니다", "새 skill을 생성합니다", "이 skill을 수정합니다"

Agent skill을 다음 구조로 생성:

```text
skill-name/
├── SKILL.md       # 필수 - frontmatter + 지침
├── scripts/       # 선택 - 실행 코드
├── references/    # 선택 - 참조 문서
└── assets/        # 선택 - template, 이미지
```

### slash-command-creator

**Trigger:** "slash command를 만듭니다", "/deploy command를 생성합니다"

Custom command 생성 위치:

- 프로젝트: `.claude/commands/`
- 개인: `~/.claude/commands/`

Command 형식:

```markdown
---
description: 간단한 설명
---

$ARGUMENTS 또는 $1, $2를 사용한 prompt 지침
```

### hook-creator

**Trigger:** "hook을 만듭니다", "저장 시 자동 format을 설정합니다", ".env 수정을 차단합니다"

`settings.json`에 event hook 생성:

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

**Event:** PreToolUse, PostToolUse, SessionStart, SessionEnd, PermissionRequest, Stop 등

### subagent-creator

**Trigger:** "subagent를 만듭니다", "code reviewer agent를 생성합니다"

Subagent 생성 위치:

- 프로젝트: `.claude/agents/`
- 사용자: `~/.claude/agents/`

Subagent 형식:

```markdown
---
name: code-reviewer
description: 코드를 review합니다. 변경 후 자동으로 사용.
tools: Read, Grep, Glob, Bash
model: sonnet
---

System prompt 내용
```

## 라이선스

MIT
