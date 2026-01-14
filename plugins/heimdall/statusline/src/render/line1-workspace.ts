import type { RenderContext } from '../types.js';
import { blue, green, yellow, cyan, magenta, dim } from './colors.js';

/**
 * Line 1: 디렉토리, Git 상태, 버전, 시간
 *
 * 예시: ~/project (main) S:2 M:1 │ ↑1↓0 │ v2.1.5 │ SUB:3 │ 🕐 22:30
 */
export function renderLine1(ctx: RenderContext): string {
  const parts: string[] = [];

  // 프로젝트 디렉토리 (~ 축약)
  const shortDir = ctx.stdin.workspace.project_dir
    .replace(process.env.HOME || '', '~');
  parts.push(blue(shortDir));

  // Git 브랜치
  if (ctx.git.isGitRepo && ctx.git.branch) {
    parts.push(green(`(${ctx.git.branch})`));
  }

  // Staged/Modified
  const status = formatGitStatus(ctx.git.staged, ctx.git.modified);
  if (status) {
    parts.push(yellow(status));
  }

  // Sync 상태
  parts.push(dim('│'));
  parts.push(cyan(formatSyncStatus(ctx.git)));

  // 버전
  parts.push(dim('│'));
  parts.push(magenta(`v${ctx.stdin.version}`));

  // MCP 서버
  parts.push(dim('│'));
  const mcpServers = ctx.stdin.mcp_servers || [];
  const mcpConnected = mcpServers.filter(s => s.status === 'connected' || s.status === 'active').length;
  const mcpCount = mcpConnected > 0 ? String(mcpConnected) : '--';
  parts.push(`MCP:${mcpCount}`);

  // 시간
  parts.push(dim('│'));
  const time = new Date().toLocaleTimeString('ko-KR', {
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  });
  parts.push(`🕐 ${time}`);

  return parts.join(' ');
}

function formatGitStatus(staged: number, modified: number): string {
  const parts: string[] = [];
  if (staged > 0) parts.push(`S:${staged}`);
  if (modified > 0) parts.push(`M:${modified}`);
  return parts.join(' ');
}

function formatSyncStatus(git: RenderContext['git']): string {
  if (!git.isGitRepo || !git.hasUpstream) return '--';
  if (git.ahead === 0 && git.behind === 0) return '✔';
  return `↑${git.ahead}↓${git.behind}`;
}
