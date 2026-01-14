import * as readline from 'readline';
import type { StdinData } from './types.js';

/**
 * stdin에서 JSON 읽기
 */
export async function readStdin(): Promise<StdinData | null> {
  if (process.stdin.isTTY) {
    return null;
  }

  return new Promise((resolve, reject) => {
    let data = '';

    const rl = readline.createInterface({
      input: process.stdin,
      crlfDelay: Infinity,
    });

    rl.on('line', (line) => {
      data += line;
    });

    rl.on('close', () => {
      try {
        resolve(JSON.parse(data) as StdinData);
      } catch (e) {
        reject(new Error(`Failed to parse stdin JSON: ${e}`));
      }
    });

    rl.on('error', reject);
  });
}

/**
 * Context 사용률 계산
 * v2.1.6+ 에서는 used_percentage 필드를 직접 제공
 */
export function getContextPercent(stdin: StdinData): number {
  // v2.1.6+ 에서 제공하는 used_percentage 우선 사용
  if (stdin.context_window.used_percentage !== undefined) {
    return Math.round(stdin.context_window.used_percentage);
  }

  // fallback: 직접 계산
  const usage = stdin.context_window.current_usage;
  const size = stdin.context_window.context_window_size;

  if (!usage || !size || size === 0) {
    return 0;
  }

  const currentTokens =
    usage.input_tokens +
    usage.output_tokens +
    usage.cache_creation_input_tokens +
    usage.cache_read_input_tokens;

  return Math.round((currentTokens * 100) / size);
}

/**
 * 모델명 추출
 */
export function getModelName(stdin: StdinData): string {
  return stdin.model?.display_name || stdin.model?.id || 'Unknown';
}

/**
 * 모델 이모지 반환
 */
export function getModelEmoji(modelName: string): string {
  if (modelName.includes('Opus')) return '🧠';
  if (modelName.includes('Sonnet')) return '🎵';
  if (modelName.includes('Haiku')) return '⚡';
  return '🤖';
}
