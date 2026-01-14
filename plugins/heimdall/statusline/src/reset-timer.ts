import type { ResetInfo } from './types.js';

/**
 * Claude 5시간 블록 리셋 시간 계산
 * 블록은 UTC 기준 04:00, 09:00, 14:00, 19:00, 00:00에 리셋
 */
export function calculateResetTime(): ResetInfo {
  const now = new Date();

  const utcHour = now.getUTCHours();
  const utcMin = now.getUTCMinutes();

  // 리셋 시간: 04, 09, 14, 19, 00 (UTC)
  // 4시간 offset 적용하여 블록 내 위치 계산
  const adjustedHour = (utcHour + 24 - 4) % 24;
  const hoursIntoBlock = adjustedHour % 5;

  // 블록 내 경과 시간 (분 단위)
  const minsIntoBlock = hoursIntoBlock * 60 + utcMin;

  // 남은 시간 (분) - 5시간 블록
  const totalMinsLeft = 5 * 60 - minsIntoBlock;

  const hoursLeft = Math.floor(totalMinsLeft / 60);
  const minutesLeft = totalMinsLeft % 60;

  // 다음 리셋 UTC 시간 계산
  const nextResetUtc = (utcHour + hoursLeft + (minutesLeft > 0 ? 1 : 0)) % 24;

  // 로컬 시간으로 변환
  const tzOffsetMinutes = -now.getTimezoneOffset();
  const tzOffsetHours = tzOffsetMinutes / 60;

  let nextResetLocal = nextResetUtc + tzOffsetHours;
  if (nextResetLocal < 0) nextResetLocal += 24;
  if (nextResetLocal >= 24) nextResetLocal -= 24;

  return {
    nextResetLocalTime: `${String(Math.floor(nextResetLocal)).padStart(2, '0')}:00`,
    hoursLeft,
    minutesLeft,
  };
}
