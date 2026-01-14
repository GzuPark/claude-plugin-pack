// ANSI 색상 코드
export const RESET = '\x1b[0m';
export const BOLD = '\x1b[1m';
export const DIM = '\x1b[2m';

// Standard colors (30-37)
export const RED = '\x1b[31m';
export const GREEN = '\x1b[32m';
export const YELLOW = '\x1b[33m';
export const BLUE = '\x1b[34m';
export const MAGENTA = '\x1b[35m';
export const CYAN = '\x1b[36m';

// Bright colors (90-97)
export const BRIGHT_CYAN = '\x1b[96m';

// 색상 래퍼 함수
export const red = (s: string): string => `${RED}${s}${RESET}`;
export const green = (s: string): string => `${GREEN}${s}${RESET}`;
export const yellow = (s: string): string => `${YELLOW}${s}${RESET}`;
export const blue = (s: string): string => `${BLUE}${s}${RESET}`;
export const magenta = (s: string): string => `${MAGENTA}${s}${RESET}`;
export const cyan = (s: string): string => `${CYAN}${s}${RESET}`;
export const brightCyan = (s: string): string => `${BRIGHT_CYAN}${s}${RESET}`;
export const dim = (s: string): string => `${DIM}${s}${RESET}`;

/**
 * Context 사용률에 따른 색상 반환
 * 80%에서 auto-compact 발생
 */
export function getContextColor(percent: number): string {
  if (percent >= 80) return RED;
  if (percent >= 60) return YELLOW;
  return GREEN;
}

/**
 * 색상 막대 생성
 */
export function coloredBar(percent: number, width = 10): string {
  const filled = Math.round((percent / 100) * width);
  const empty = width - filled;
  const color = getContextColor(percent);

  return `${color}${'█'.repeat(filled)}${'░'.repeat(empty)}${RESET}`;
}
