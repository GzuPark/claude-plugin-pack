# Claude Plugin Pack

[Claude Code](https://docs.anthropic.com/en/docs/claude-code)를 위한 플러그인 모음입니다.

## Claude Code 플러그인 소개

Claude Code 플러그인은 Claude Code CLI의 기능을 확장합니다. 이 저장소는 생산성과 개발 워크플로우를 위한 플러그인을 제공합니다.

## 설치

### GitHub에서 설치 (권장)

1. 마켓플레이스 추가:

   ```bash
   /plugin marketplace add GzuPark/claude-plugin-pack
   ```

2. 플러그인 설치:

   ```bash
   /plugin install plugin-name@claude-plugin-pack
   ```

### CLI에서 설치

```bash
claude plugin install plugin-name@claude-plugin-pack
```

### 로컬 개발

```bash
claude --plugin-dir ./claude-plugin-pack
```

## 포함된 플러그인

(준비 중)

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
