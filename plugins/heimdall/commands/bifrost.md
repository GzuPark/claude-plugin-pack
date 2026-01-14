---
allowed-tools: Bash(npm install:*), Bash(npm run build:*), Bash(node:*), Bash(mkdir:*), Bash(cat:*), Bash(ls:*), Read, Write, Edit
description: Open the Bifrost - Build and activate Heimdall statusline
---

# Bifrost

Open the Bifrost bridge and summon Heimdall to watch over your Claude Code session.

## Workflow

### Step 1: Find Plugin Directory

Locate the installed Heimdall plugin:

```bash
ls -d ~/.claude/plugins/cache/claude-plugin-pack/heimdall/*/statusline 2>/dev/null | head -1
```

If not found, inform the user to install first:

```
/plugin install heimdall@claude-plugin-pack
```

### Step 2: Build TypeScript Project

Navigate to the statusline directory and build:

```bash
cd <PLUGIN_DIR>/statusline
npm install
npm run build
```

Verify `dist/index.js` exists after build.

### Step 3: Update Settings

Read `~/.claude/settings.json` and update the `statusLine` configuration:

```json
{
  "statusLine": {
    "type": "command",
    "command": "node <FULL_PATH>/dist/index.js",
    "padding": 0
  }
}
```

Use the Edit tool to update settings.json, preserving existing settings.

### Step 4: Confirm Success

Display success message:

```
The Bifrost is open! Heimdall now watches over your session.

Restart Claude Code to see the new statusline.

Output example:
~/project (main) S:2 M:1 │ ↑1↓0 │ v2.1.5 │ 🕐 22:30
🧠 Claude Opus 4.5 │ $0.05 │ +100/-20 │ ████████░░ 65%
⠋ Read(file.ts) │ ● Explore (searching)
▸ [Current task] (2/5) │ RESET at 14:00 (3h 30m left)
```

## Error Handling

- If npm install fails: Check Node.js version (requires 18+)
- If build fails: Check for TypeScript errors in src/
- If settings.json doesn't exist: Create it with statusLine config only
