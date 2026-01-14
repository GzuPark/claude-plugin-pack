import type { RenderContext, ToolEntry, AgentEntry } from '../types.js';
import { yellow, green, magenta, dim, cyan, blue } from './colors.js';

const SPINNER_FRAMES = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'];

// 도구별 색상
const TOOL_COLORS: Record<string, (s: string) => string> = {
  Read: cyan,
  Write: magenta,
  Edit: magenta,
  Bash: yellow,
  Glob: blue,
  Grep: blue,
  WebFetch: cyan,
  WebSearch: cyan,
  Task: magenta,
  TodoWrite: green,
  NotebookEdit: magenta,
  AskUserQuestion: yellow,
  Skill: magenta,
};

function getToolColor(name: string): (s: string) => string {
  return TOOL_COLORS[name] || green;
}

/**
 * Line 3: 완료된 Tools + Agents
 *
 * 예시: Edit×8 | Bash×5 | Read×4 │ ✓ Explore×2
 */
export function renderCompletedActivity(ctx: RenderContext): string | null {
  const completedTools = ctx.transcript.tools.filter(t => t.status === 'completed');
  const completedAgents = ctx.transcript.agents.filter(a => a.status === 'completed');

  if (completedTools.length === 0 && completedAgents.length === 0) {
    return null;
  }

  const sections: string[] = [];

  // 완료된 도구 (빈도순)
  const toolCounts = countByName(completedTools);
  const toolParts: string[] = [];
  Object.entries(toolCounts)
    .sort((a, b) => b[1] - a[1])
    .forEach(([name, count]) => {
      const color = getToolColor(name);
      const countStr = count > 1 ? `×${count}` : '';
      toolParts.push(color(`${name}${countStr}`));
    });
  if (toolParts.length > 0) {
    sections.push(toolParts.join(' | '));
  }

  // 완료된 에이전트 (타입별 그룹화)
  const agentCounts = countByType(completedAgents);
  const agentParts: string[] = [];
  Object.entries(agentCounts).forEach(([type, count]) => {
    const countStr = count > 1 ? `×${count}` : '';
    agentParts.push(green(`✓ ${type}${countStr}`));
  });
  if (agentParts.length > 0) {
    sections.push(agentParts.join(' | '));
  }

  return sections.join(` ${dim('│')} `);
}

/**
 * Line 4: 진행 중인 Tools + Agents (있을 경우만)
 *
 * 예시: ⠋ Read(src/index.ts) | ● Explore (searching for files)
 */
export function renderRunningActivity(ctx: RenderContext): string | null {
  const runningTools = ctx.transcript.tools.filter(t => t.status === 'running');
  const runningAgents = ctx.transcript.agents.filter(a => a.status === 'running');

  if (runningTools.length === 0 && runningAgents.length === 0) {
    return null;
  }

  const parts: string[] = [];
  const spinner = SPINNER_FRAMES[Math.floor(Date.now() / 100) % SPINNER_FRAMES.length];

  // 실행 중인 도구 (full text)
  runningTools.forEach(tool => {
    const color = getToolColor(tool.name);
    const target = tool.target ? `(${tool.target})` : '';
    parts.push(yellow(`${spinner} `) + color(`${tool.name}${target}`));
  });

  // 실행 중인 에이전트 (full text)
  runningAgents.forEach(agent => {
    const desc = agent.description ? ` (${agent.description})` : '';
    const elapsed = agent.startTime ? formatElapsed(Date.now() - agent.startTime) : '';
    parts.push(yellow(`● ${magenta(agent.type)}${desc}`) + (elapsed ? dim(` ${elapsed}`) : ''));
  });

  return parts.join(' | ');
}

function countByType(agents: AgentEntry[]): Record<string, number> {
  return agents.reduce((acc, agent) => {
    acc[agent.type] = (acc[agent.type] || 0) + 1;
    return acc;
  }, {} as Record<string, number>);
}

function countByName(tools: ToolEntry[]): Record<string, number> {
  return tools.reduce((acc, tool) => {
    acc[tool.name] = (acc[tool.name] || 0) + 1;
    return acc;
  }, {} as Record<string, number>);
}

function formatElapsed(ms: number): string {
  const secs = Math.floor(ms / 1000);
  if (secs < 60) return `${secs}s`;
  const mins = Math.floor(secs / 60);
  const remainSecs = secs % 60;
  return `${mins}:${String(remainSecs).padStart(2, '0')}`;
}
