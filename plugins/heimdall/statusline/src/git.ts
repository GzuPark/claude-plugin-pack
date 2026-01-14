import { execSync } from 'child_process';
import type { GitStatus } from './types.js';

/**
 * Git 상태 조회
 */
export function getGitStatus(cwd: string): GitStatus {
  const result: GitStatus = {
    isGitRepo: false,
    staged: 0,
    modified: 0,
    ahead: 0,
    behind: 0,
    hasUpstream: false,
    submoduleCount: 0,
  };

  try {
    execSync('git rev-parse --git-dir', { cwd, stdio: 'pipe' });
    result.isGitRepo = true;
  } catch {
    return result;
  }

  result.branch = execGitSafe(cwd, 'rev-parse --abbrev-ref HEAD');
  result.staged = countLines(execGitSafe(cwd, 'diff --cached --name-only'));
  result.modified = countLines(execGitSafe(cwd, 'diff --name-only'));

  const upstream = execGitSafe(cwd, 'rev-parse --abbrev-ref @{upstream}');
  if (upstream) {
    result.hasUpstream = true;
    const counts = execGitSafe(cwd, 'rev-list --left-right --count HEAD...@{upstream}');
    if (counts) {
      const [ahead, behind] = counts.split(/\s+/).map(Number);
      result.ahead = ahead || 0;
      result.behind = behind || 0;
    }
  }

  result.submoduleCount = countLines(execGitSafe(cwd, 'submodule status'));

  return result;
}

function execGitSafe(cwd: string, args: string): string {
  try {
    return execSync(`git --no-optional-locks ${args}`, {
      cwd,
      stdio: 'pipe',
      encoding: 'utf-8',
    }).trim();
  } catch {
    return '';
  }
}

function countLines(output: string): number {
  if (!output) return 0;
  return output.split('\n').filter(Boolean).length;
}
