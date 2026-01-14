import * as fs from 'fs';
import * as path from 'path';
import type { ConfigCounts } from './types.js';

/**
 * 설정 파일 카운트
 */
export function countConfigs(projectDir: string): ConfigCounts {
  const result: ConfigCounts = {
    claudeMdCount: 0,
    rulesCount: 0,
    mcpCount: 0,
    hooksCount: 0,
  };

  // CLAUDE.md 카운트
  if (fs.existsSync(path.join(projectDir, 'CLAUDE.md'))) {
    result.claudeMdCount++;
  }

  // .claude 디렉토리 확인
  const claudeDir = path.join(projectDir, '.claude');
  if (fs.existsSync(claudeDir)) {
    // rules 카운트
    const rulesDir = path.join(claudeDir, 'rules');
    if (fs.existsSync(rulesDir)) {
      try {
        const files = fs.readdirSync(rulesDir);
        result.rulesCount = files.filter(f => f.endsWith('.md')).length;
      } catch {
        // ignore
      }
    }

    // settings.json에서 MCP 및 hooks 카운트
    const settingsPath = path.join(claudeDir, 'settings.json');
    if (fs.existsSync(settingsPath)) {
      try {
        const settings = JSON.parse(fs.readFileSync(settingsPath, 'utf-8'));
        if (settings.mcpServers) {
          result.mcpCount = Object.keys(settings.mcpServers).length;
        }
        if (settings.hooks) {
          result.hooksCount = Object.keys(settings.hooks).length;
        }
      } catch {
        // ignore
      }
    }
  }

  // 홈 디렉토리 설정도 확인
  const homeClaudeDir = path.join(process.env.HOME || '', '.claude');
  if (homeClaudeDir !== claudeDir && fs.existsSync(homeClaudeDir)) {
    const homeSettingsPath = path.join(homeClaudeDir, 'settings.json');
    if (fs.existsSync(homeSettingsPath)) {
      try {
        const settings = JSON.parse(fs.readFileSync(homeSettingsPath, 'utf-8'));
        if (settings.mcpServers) {
          result.mcpCount += Object.keys(settings.mcpServers).length;
        }
        if (settings.hooks) {
          result.hooksCount += Object.keys(settings.hooks).length;
        }
      } catch {
        // ignore
      }
    }
  }

  return result;
}
