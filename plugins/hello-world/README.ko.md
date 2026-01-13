# hello-world

Claude Code를 위한 필수 개발 워크플로우입니다. Git 커밋 및 GitHub PR 생성과 자동 코드 리뷰 기능을 포함합니다.

## 커맨드

### /commit

Conventional Commit 형식으로 구조화된 Git 커밋을 생성합니다.

```
/commit
/commit [추가 컨텍스트]
```

**기능:**

- Conventional Commit 형식 (feat, fix, docs 등)
- 관련 파일 자동 스테이징
- 최근 커밋에서 스타일 참조

### /pr

자동 코드 리뷰가 포함된 GitHub PR을 생성합니다.

```
/pr
/pr main
/pr --draft
/pr main --draft
```

**기능:**

- 사전 검사 (git 저장소, 브랜치, 커밋되지 않은 변경사항, gh CLI)
- 에러/경고 분류가 포함된 자동 코드 리뷰
- 일반적인 이슈에 대한 자동 수정 제안
- 스마트 PR 제목/설명 생성
- PR 생성 전 푸시 확인

## 스킬

### pr-workflow

`/pr` 커맨드는 내부적으로 `pr-workflow` 스킬을 사용합니다. 이 스킬은 다음을 제공합니다:

- 사전 검사부터 PR 생성까지 9단계 워크플로우
- 가독성, 에러 처리, 중복, 타입 안전성에 대한 코드 리뷰 규칙
- PR 템플릿 생성
- 에러 메시지 처리

## 워크플로우

```
/commit → /pr → 리뷰 → 푸시 → PR 생성
```

1. **커밋**: `/commit`으로 변경사항을 스테이징하고 커밋합니다
2. **PR**: `/pr`을 실행하여 PR 워크플로우를 시작합니다
3. **리뷰**: 자동 코드 리뷰가 이슈를 검사합니다
4. **푸시**: 원격으로 푸시를 확인합니다
5. **완료**: 생성된 제목과 설명으로 PR이 생성됩니다

## 코드 리뷰 카테고리

PR 워크플로우는 다음 항목을 검토합니다:

- **가독성**: 네이밍, 함수 길이, 중첩 깊이
- **에러 처리**: Async/Promise, null 안전성, catch 블록
- **중복**: 동일한 코드 블록
- **타입 안전성**: TypeScript `any` 사용, 누락된 타입
- **보안**: 설정 파일의 하드코딩된 시크릿

## 요구사항

- Git 저장소
- [GitHub CLI (gh)](https://cli.github.com) 설치 및 인증 완료

## 설치

```bash
/plugin install hello-world@claude-plugin-pack
```

## 라이선스

MIT
