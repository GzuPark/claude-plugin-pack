---
allowed-tools: Bash(npm install:*), Bash(npm run build:*), Bash(rm -rf:*), Bash(ls:*), Read, Write, Edit
description: Open the Bifrost - Install, update, or manage Heimdall statusline
---

# Bifrost

Open the Bifrost bridge and summon Heimdall to watch over your Claude Code session.

## Step 1: Find Plugin Versions

```bash
ls -d ~/.claude/plugins/cache/claude-plugin-pack/heimdall/*/ 2>/dev/null
```

**If no directories found:**
→ Inform user: "Heimdall not installed. Run `/plugin install heimdall@claude-plugin-pack` first."
→ END

**If directories found:**
→ Identify the latest version (highest semver)
→ Continue to Step 2

## Step 2: Check Current Settings

Read `~/.claude/settings.json` and extract current `statusLine.command` path.

**Case A: No statusLine configured**
→ Set `CURRENT_VERSION` = none
→ Continue to Step 3

**Case B: statusLine configured with heimdall path**
→ Extract version from path (e.g., `/heimdall/1.0.1/statusline/` → `1.0.1`)
→ Set `CURRENT_VERSION` = extracted version
→ Continue to Step 3

**Case C: statusLine configured with non-heimdall command**
→ Warn user: "Existing statusLine will be replaced"
→ Set `CURRENT_VERSION` = none
→ Continue to Step 3

## Step 3: Compare Versions

**If `CURRENT_VERSION` == `LATEST_VERSION`:**
→ Inform user: "Already up to date (v{VERSION})"
→ Continue to Step 6 (cleanup only)

**If `CURRENT_VERSION` != `LATEST_VERSION`:**
→ Continue to Step 4

## Step 4: Build Latest Version

```bash
cd ~/.claude/plugins/cache/claude-plugin-pack/heimdall/<LATEST_VERSION>/statusline
npm install
npm run build
```

**If build fails:**
→ Show error message
→ END

**If build succeeds:**
→ Verify `dist/index.js` exists
→ Continue to Step 5

## Step 5: Update Settings

Update `~/.claude/settings.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "node <HOME>/.claude/plugins/cache/claude-plugin-pack/heimdall/<LATEST_VERSION>/statusline/dist/index.js",
    "padding": 0
  }
}
```

Use Edit tool to preserve existing settings.

**If settings.json doesn't exist:**
→ Create new file with statusLine config only

→ Continue to Step 6

## Step 6: Clean Up Old Versions

List all version directories except `LATEST_VERSION`.

**If old versions exist:**

```bash
rm -rf ~/.claude/plugins/cache/claude-plugin-pack/heimdall/<OLD_VERSION>/
```

→ Record removed versions

**If no old versions:**
→ Skip cleanup

→ Continue to Step 7

## Step 7: Report

**Fresh install (Case A from Step 2):**

```
The Bifrost is open! Heimdall now watches over your session.

Installed: v<LATEST_VERSION>
Restart Claude Code to see the new statusline.
```

**Update (had previous version):**

```
Bifrost Status:
- Updated: v<OLD_VERSION> → v<LATEST_VERSION>
- Removed: <OLD_VERSIONS_LIST>
- Settings: Updated ✓

Restart Claude Code to activate.
```

**Already up to date:**

```
Bifrost Status:
- Current: v<LATEST_VERSION> (up to date)
- Removed: <OLD_VERSIONS_LIST or "none">
```
