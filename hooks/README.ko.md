# Hooks

자동 workflow를 위한 재사용 가능한 Claude Code hook 설정입니다.

## 사용 방법

### Claude Code / Agent용

이 파일을 읽고 원하는 hook을 설정합니다:

1. Prerequisites 설치 확인
2. 사용자에게 설정 위치 확인 (personal 또는 project)
3. Hook의 JSON 설정 읽기
4. 선택한 settings.json의 `hooks` key에 병합
5. 사용자에게 Claude Code 재시작 안내

#### 설정 위치

| 위치     | 파일                      | 범위                |
| -------- | ------------------------- | ------------------- |
| Personal | `~/.claude/settings.json` | 모든 project에 적용 |
| Project  | `.claude/settings.json`   | 현재 project만 적용 |

### 사용자용

Claude Code에 요청:

> "hooks/README.ko.md에서 markdown lint hook을 설정해줘"

또는 JSON 설정을 `~/.claude/settings.json`에 직접 복사합니다.

---

## 사용 가능한 Hooks

### 1. Markdown Lint

`.md` 파일 편집 후 자동으로 markdownlint를 실행하여 lint error를 감지합니다.

#### Prerequisites

**markdownlint-cli** (필수):

```bash
npm install -g markdownlint-cli
```

**jq** (JSON parsing에 필수):

```bash
# Ubuntu/Debian
sudo apt install jq

# macOS
brew install jq
```

#### Configuration

[markdown-lint.json](markdown-lint.json) 내용을
`~/.claude/settings.json` (personal) 또는 `.claude/settings.json` (project)의
`hooks` key에 병합합니다.

#### 동작 방식

| Field   | Value           | 설명                            |
| ------- | --------------- | ------------------------------- |
| Event   | `PostToolUse`   | tool 실행 완료 후 trigger       |
| Matcher | `Edit\|Write`   | Edit 또는 Write tool에만 적용   |
| Type    | `command`       | shell command 실행              |

Command 상세:

```bash
jq -r '.tool_input.file_path // empty'  # stdin JSON에서 file_path 추출
| { read f;                              # 변수 f에 저장
    [[ "$f" == *.md ]] &&                # .md 확장자인 경우에만
    npx markdownlint "$f" 2>&1           # markdownlint 실행
    || true;                             # error code 무시 (non-blocking)
  }
```

#### 검증

설정 후:

1. Claude Code 재시작
2. `.md` 파일 편집
3. lint 결과가 응답에 표시되는지 확인

#### Customization

**특정 rule 비활성화** - project root에 `.markdownlintrc` 생성:

```json
{
  "MD013": false,
  "MD033": false
}
```

**특정 directory만 lint** - command 수정:

```bash
jq -r '.tool_input.file_path // empty' \
  | { read f; [[ "$f" == *.md ]] && [[ "$f" == /path/to/docs/* ]] \
      && npx markdownlint "$f" 2>&1 || true; }
```

#### Troubleshooting

##### "markdownlint: command not found"

markdownlint-cli가 설치되지 않았거나 PATH에 없습니다.

```bash
npm install -g markdownlint-cli
```

##### Hook이 동작하지 않음

1. Claude Code 재시작 필요
2. settings.json JSON 문법 확인
3. jq 설치 확인: `which jq`

---

## 새 Hook 만들기

[hook-creator skill](../plugins/creators/skills/hook-creator/SKILL.md)을 참고하세요.
