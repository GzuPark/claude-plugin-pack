# heimdall

Enhanced statusline for Claude Code with tool/agent/todo tracking, Git status, and session monitoring.

> Named after Heimdall, the Norse god who watches over the Bifrost bridge.

## Features

| Feature | Description |
|---------|-------------|
| Dynamic statusline | 3-5 lines based on activity |
| Tool tracking | Color-coded completion counts by tool type |
| Agent tracking | Running agents with elapsed time display |
| Running activity | Separate line with spinner animation |
| Todo progress | Full task description with completion rate |
| Git integration | Branch, staged/modified counts, sync status |
| MCP server | Connection status display |
| Context usage | Color-coded progress bar (green -> yellow -> red) |
| 5-hour reset timer | Usage tracking with local time display |
| Cost tracking | Session cost and line changes (+/-) |

## Output Example

### With Running Activity (5 lines)

```text
~/project/private/my-app (main) S:2 M:3 │ ↑1↓0 │ v2.1.7 │ MCP:2 │ 🕐 16:30
🧠 Opus 4.5 │ $12.50 │ +500/-120 │ ████████░░ 65%
Edit×8 | Bash×5 | Read×4 | WebFetch×2 │ ✓ Explore×2
⠋ Read(/src/components/Button.tsx) | ● Explore (searching for API endpoints)
▸ [Implement user authentication module] (2/5) │ RESET at 18:00 (1h 30m left)
```

### Without Running Activity (4 lines)

```text
~/project/private/my-app (main) S:2 M:3 │ ✔ │ v2.1.7 │ MCP:-- │ 🕐 16:30
🧠 Opus 4.5 │ $12.50 │ +500/-120 │ ████████░░ 65%
Edit×8 | Bash×5 | Read×4 │ ✓ Explore×2
✓ All todos complete (5/5) │ RESET at 18:00 (1h 30m left)
```

### Minimal Output (3 lines)

```text
~/project/private/my-app (main) │ ✔ │ v2.1.7 │ MCP:-- │ 🕐 16:30
🧠 Opus 4.5 │ $0.00 │ +0/-0 │ ░░░░░░░░░░ 0%
RESET at 18:00 (1h 30m left)
```

## Line Details

| Line | Content |
|------|---------|
| 1 | Project directory, Git branch, Staged/Modified, Sync status, Version, MCP, Time |
| 2 | Model (emoji), Cost, Lines changed, Context bar + % |
| 3 | Completed tools (color-coded), Completed agents (if any) |
| 4 | Running tools with spinner, Running agents (if any) |
| 4/5 | Todo progress, 5-hour reset timer |

## Installation

```bash
/plugin install heimdall@claude-plugin-pack
```

After installation, run the setup command:

```bash
/heimdall:bifrost
```

This will automatically:

1. Build the TypeScript statusline
2. Configure `~/.claude/settings.json`
3. Restart Claude Code to apply changes

## Manual Setup

If you prefer manual configuration:

### 1. Build the statusline

```bash
cd ~/.claude/plugins/cache/claude-plugin-pack/heimdall/*/statusline
npm install && npm run build
```

### 2. Configure Claude Code

Add to `~/.claude/settings.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "node <PATH_TO_PLUGIN>/statusline/dist/index.js",
    "padding": 0
  }
}
```

## Commands

### /heimdall:bifrost

Automatically builds and configures the Heimdall statusline.

## Requirements

- Node.js 18+
- npm

## License

MIT
