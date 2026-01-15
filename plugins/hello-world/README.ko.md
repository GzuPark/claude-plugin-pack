# hello-world

Claude Code를 위한 필수 개발 워크플로우입니다.
Git 커밋 및 GitHub PR 생성과 자동 코드 리뷰 기능을
포함합니다.

## Command

```text
/commit
/commit [추가 컨텍스트]
```

Conventional Commit 형식으로 구조화된 Git 커밋을 생성합니다.

**기능:**

- Conventional Commit 형식 (feat, fix, docs 등)
- 관련 파일 자동 스테이징
- 최근 커밋에서 스타일 참조

---

```text
/interview path/to/plan.md
/interview "React로 할 일 앱 만들기"
```

프로젝트 계획에 대한 기술 인터뷰를 수행하여
사양 문서를 생성합니다.

**기능:**

- 복잡도에 따른 동적 질문 수 (3-10개)
- 인터뷰 중 진행률 추적
- 자동 사양 문서 생성
- 긴 인터뷰를 위한 중간 저장

---

```text
/pr
/pr main
/pr --draft
/pr main --draft
```

자동 코드 리뷰가 포함된 GitHub PR을 생성합니다.

**기능:**

- 사전 검사 (git 저장소, 브랜치, 커밋되지 않은 변경사항,
  gh CLI)
- 에러/경고 분류가 포함된 자동 코드 리뷰
- 일반적인 이슈에 대한 자동 수정 제안
- 스마트 PR 제목/설명 생성
- PR 생성 전 푸시 확인

---

```text
/simplify
/simplify src/utils.ts
```

Code 완성 후 단순화를 수행합니다.

**기능:**

- 중첩 조건문 평탄화 (3단계 이상) - early return 사용
- 반복 pattern 추출 (3회 이상) - utility 함수로 분리
- 변수/함수 naming 개선 - 명확한 식별자 사용
- Dead code 제거: 미사용 import, 주석 처리된 code
- Edit 전 항상 사용자 확인 요청

## Agent

### code-simplifier

`/simplify` command는 `code-simplifier` agent를 사용합니다.
이 agent는 proactively code 단순화 기회를 분석합니다.

**단순화 원칙:**

- 복잡도 감소: early return, guard clause
- Pattern 추출: 반복 logic에 DRY 원칙 적용
- Naming 개선: 명확하고 설명적인 식별자
- Dead code 제거: 미사용 import, 도달 불가능한 code

## Skill

### plan-interview

`/interview` command는 내부적으로 `plan-interview` skill을
사용합니다. 이 skill은 다음을 제공합니다:

- 4단계 workflow: 입력 이해, 복잡도 평가, 인터뷰, 사양 작성
- 인터뷰 영역: architecture, backend, frontend, AI/LLM,
  우려사항, 확장성
- 사양 template 생성
- 인터뷰 질문 및 사양 형식을 위한 참조 문서

### pr-workflow

`/pr` command는 내부적으로 `pr-workflow` skill을 사용합니다.
이 skill은 다음을 제공합니다:

- 사전 검사부터 PR 생성까지 9단계 workflow
- 가독성, error 처리, 중복, type 안전성에 대한 code review 규칙
- PR template 생성
- Error message 처리

## Workflow

```text
/commit → /pr → 리뷰 → 푸시 → PR 생성
```

1. **Commit**: `/commit`으로 변경사항을 staging하고 commit합니다
2. **PR**: `/pr`을 실행하여 PR workflow를 시작합니다
3. **Review**: 자동 code review가 issue를 검사합니다
4. **푸시**: 원격으로 푸시를 확인합니다
5. **완료**: 생성된 제목과 설명으로 PR이 생성됩니다

## Code Review 카테고리

PR workflow는 다음 항목을 검토합니다:

- **가독성**: Naming, 함수 길이, 중첩 깊이
- **Error 처리**: Async/Promise, null 안전성, catch block
- **중복**: 동일한 code block
- **Type 안전성**: TypeScript `any` 사용, 누락된 type
- **보안**: 설정 파일의 하드코딩된 secret

## 요구사항

> [!IMPORTANT]
>
> - Git 저장소
> - [GitHub CLI (gh)](https://cli.github.com) 설치 및 인증 완료

## 설치

```bash
/plugin install hello-world@claude-plugin-pack
```

## 라이선스

MIT
