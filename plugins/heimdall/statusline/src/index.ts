#!/usr/bin/env node

import { readStdin } from './stdin.js';
import { parseTranscript } from './transcript.js';
import { getGitStatus } from './git.js';
import { countConfigs } from './config-reader.js';
import { calculateResetTime } from './reset-timer.js';
import { render } from './render/index.js';
import type { RenderContext } from './types.js';

async function main(): Promise<void> {
  try {
    // 1. stdin 읽기
    const stdin = await readStdin();
    if (!stdin) {
      return;
    }

    // 2. 트랜스크립트 파싱
    const transcript = await parseTranscript(stdin.transcript_path);

    // 3. Git 상태 조회
    const git = getGitStatus(stdin.workspace.current_dir);

    // 4. 설정 파일 카운트
    const config = countConfigs(stdin.workspace.project_dir || stdin.workspace.current_dir);

    // 5. 리셋 타이머 계산
    const reset = calculateResetTime();

    // 6. 세션 지속 시간 계산
    const sessionDuration = formatSessionDuration(transcript.sessionStart);

    // 7. 렌더링 컨텍스트 구성
    const ctx: RenderContext = {
      stdin,
      transcript,
      git,
      config,
      reset,
      sessionDuration,
    };

    // 8. 출력
    render(ctx);

  } catch (error) {
    console.error('Statusline error:', error);
    process.exit(1);
  }
}

function formatSessionDuration(start?: Date): string {
  if (!start) return '';

  const ms = Date.now() - start.getTime();
  const hours = Math.floor(ms / (1000 * 60 * 60));
  const mins = Math.floor((ms % (1000 * 60 * 60)) / (1000 * 60));

  if (hours > 0) {
    return `${hours}h ${mins}m`;
  }
  return `${mins}m`;
}

main();
