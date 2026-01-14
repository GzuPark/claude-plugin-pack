import type { RenderContext, TodoItem } from '../types.js';
import { yellow, green, dim, brightCyan } from './colors.js';

/**
 * Todo 진행률 + 리셋 타이머
 *
 * 예시: ▸ [Implementing feature] (2/5) │ RESET at 14:00 (3h 30m left)
 */
export function renderProgress(ctx: RenderContext): string {
  const todoPart = renderTodos(ctx.transcript.todos);
  const resetPart = renderReset(ctx.reset);

  const parts = [todoPart, resetPart].filter(Boolean);
  return parts.join(` ${dim('│')} `);
}

function renderTodos(todos: TodoItem[]): string | null {
  if (todos.length === 0) {
    return null;
  }

  const completed = todos.filter(t => t.status === 'completed').length;
  const inProgress = todos.find(t => t.status === 'in_progress');
  const total = todos.length;

  // 모두 완료
  if (completed === total) {
    return green(`✓ All todos complete (${completed}/${total})`);
  }

  // 진행 중인 작업 표시 (full text)
  if (inProgress) {
    return yellow(`▸ [${inProgress.content}]`) + dim(` (${completed}/${total})`);
  }

  return null;
}

function renderReset(reset: RenderContext['reset']): string {
  return brightCyan(
    `RESET at ${reset.nextResetLocalTime} (${reset.hoursLeft}h ${reset.minutesLeft}m left)`
  );
}
