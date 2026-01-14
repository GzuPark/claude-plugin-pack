import type { RenderContext } from '../types.js';
import { getContextPercent, getModelName, getModelEmoji } from '../stdin.js';
import { cyan, green, red, dim, coloredBar, getContextColor, RESET } from './colors.js';

/**
 * Line 2: 모델, 비용, 라인 변경, Context 사용률
 *
 * 예시: 🧠 Claude Opus 4.5 │ $0.05 │ +96/-38 │ [████░░░░░░] 40%
 */
export function renderLine2(ctx: RenderContext): string {
  const parts: string[] = [];

  // 모델 (이모지 + 이름)
  const modelName = getModelName(ctx.stdin);
  const emoji = getModelEmoji(modelName);
  parts.push(`${emoji} ${cyan(modelName)}`);

  // 비용
  parts.push(dim('│'));
  const cost = ctx.stdin.cost?.total_cost_usd ?? 0;
  parts.push(green(`$${cost.toFixed(2)}`));

  // 라인 변경
  parts.push(dim('│'));
  const added = ctx.stdin.cost?.total_lines_added ?? 0;
  const removed = ctx.stdin.cost?.total_lines_removed ?? 0;
  parts.push(`${green(`+${added}`)}${red(`/-${removed}`)}`);

  // Context Bar + 퍼센트
  parts.push(dim('│'));
  const percent = getContextPercent(ctx.stdin);
  const bar = coloredBar(percent);
  const color = getContextColor(percent);
  parts.push(`${bar} ${color}${percent}%${RESET}`);

  // 95% 이상이면 경고
  if (percent >= 95) {
    parts.push(red('⚠️'));
  }

  return parts.join(' ');
}
