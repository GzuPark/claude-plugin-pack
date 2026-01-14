# Hooks

Reusable Claude Code hook configurations for automatic workflows.

## How to Use

### For Claude Code / Agents

Read this file and set up the desired hook by:

1. Check prerequisites are installed
2. Ask user for settings location (personal or project)
3. Read the hook's JSON configuration
4. Merge into selected settings.json under the `hooks` key
5. Inform user to restart Claude Code

#### Settings Location

| Location | File                      | Scope                |
| -------- | ------------------------- | -------------------- |
| Personal | `~/.claude/settings.json` | All projects         |
| Project  | `.claude/settings.json`   | Current project only |

### For Users

Ask Claude Code:

> "Set up the markdown lint hook from hooks/README.md"

Or manually copy the JSON configuration to `~/.claude/settings.json`.

---

## Available Hooks

### 1. Markdown Lint

Automatically runs markdownlint after editing `.md` files to detect lint errors.

#### Prerequisites

**markdownlint-cli** (required):

```bash
npm install -g markdownlint-cli
```

**jq** (required for JSON parsing):

```bash
# Ubuntu/Debian
sudo apt install jq

# macOS
brew install jq
```

#### Configuration

Merge [markdown-lint.json](markdown-lint.json) into `~/.claude/settings.json` (personal) or `.claude/settings.json` (project) under the `hooks` key.

#### How It Works

| Field   | Value           | Description                             |
| ------- | --------------- | --------------------------------------- |
| Event   | `PostToolUse`   | Triggers after tool execution completes |
| Matcher | `Edit\|Write`   | Applies only to Edit or Write tools     |
| Type    | `command`       | Executes shell command                  |

Command breakdown:

```bash
jq -r '.tool_input.file_path // empty'  # Extract file_path from stdin JSON
| { read f;                              # Store in variable f
    [[ "$f" == *.md ]] &&                # Only if .md extension
    npx markdownlint "$f" 2>&1           # Run markdownlint
    || true;                             # Ignore error code (non-blocking)
  }
```

#### Verification

After setup:

1. Restart Claude Code
2. Edit any `.md` file
3. Lint results should appear in the response

#### Customization

**Disable specific rules** - Create `.markdownlintrc` in project root:

```json
{
  "MD013": false,
  "MD033": false
}
```

**Lint only specific directories** - Modify command:

```bash
jq -r '.tool_input.file_path // empty' | { read f; [[ "$f" == *.md ]] && [[ "$f" == /path/to/docs/* ]] && npx markdownlint "$f" 2>&1 || true; }
```

#### Troubleshooting

##### "markdownlint: command not found"

markdownlint-cli is not installed or not in PATH.

```bash
npm install -g markdownlint-cli
```

##### Hook not working

1. Restart Claude Code
2. Check settings.json JSON syntax
3. Verify jq installation: `which jq`

---

## Creating New Hooks

See [hook-creator skill](../plugins/creators/skills/hook-creator/SKILL.md) for guidance.
