import type { RenderContext } from '../types.js';
import { renderLine1 } from './line1-workspace.js';
import { renderLine2 } from './line2-session.js';
import { renderCompletedActivity, renderRunningActivity, renderMcpRunningActivity } from './line3-activity.js';
import { renderProgress } from './line4-progress.js';
import { RESET } from './colors.js';

/**
 * 동적 statusline 렌더링
 *
 * Line 1: Workspace (항상)
 * Line 2: Session (항상)
 * Line 3: 완료된 Tools + Agents (있을 때만)
 * Line 4: 진행 중인 Tools + Agents (있을 때만)
 * Line 4/5: Todo + Reset (항상)
 */
export function render(ctx: RenderContext): void {
  const lines: string[] = [];

  // Line 1: Workspace (항상 표시)
  lines.push(renderLine1(ctx));

  // Line 2: Session (항상 표시)
  lines.push(renderLine2(ctx));

  // Line 3: 완료된 activity (있을 때만)
  const completedActivity = renderCompletedActivity(ctx);
  if (completedActivity) {
    lines.push(completedActivity);
  }

  // Line 4: 진행 중인 activity (있을 때만)
  const runningActivity = renderRunningActivity(ctx);
  if (runningActivity) {
    lines.push(runningActivity);
  }

  // MCP Tools Line: 실행 중인 MCP tools (있을 때만)
  const mcpRunning = renderMcpRunningActivity(ctx);
  if (mcpRunning) {
    lines.push(mcpRunning);
  }

  // Line 4/5: Progress + Reset (항상 표시)
  lines.push(renderProgress(ctx));

  // 출력 (공백을 Non-Breaking Space로 변환하여 터미널 호환성 확보)
  lines.forEach(line => {
    const formatted = line.replace(/ /g, '\u00A0') + RESET;
    console.log(formatted);
  });
}
