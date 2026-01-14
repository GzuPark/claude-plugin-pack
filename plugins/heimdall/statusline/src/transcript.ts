import * as fs from 'fs';
import * as readline from 'readline';
import type { TranscriptData, ToolEntry, AgentEntry, TodoItem } from './types.js';

const MAX_TOOLS = 20;
const MAX_AGENTS = 10;

/**
 * 트랜스크립트 파일 파싱
 */
export async function parseTranscript(path: string): Promise<TranscriptData> {
  const result: TranscriptData = {
    tools: [],
    agents: [],
    todos: [],
  };

  if (!fs.existsSync(path)) {
    return result;
  }

  const toolMap = new Map<string, ToolEntry>();
  const agentMap = new Map<string, AgentEntry>();

  const stream = fs.createReadStream(path, { encoding: 'utf-8' });
  const rl = readline.createInterface({
    input: stream,
    crlfDelay: Infinity,
  });

  for await (const line of rl) {
    if (!line.trim()) continue;

    try {
      const entry = JSON.parse(line);
      processEntry(entry, toolMap, agentMap, result);

      if (!result.sessionStart && entry.timestamp) {
        result.sessionStart = new Date(entry.timestamp);
      }
    } catch {
      continue;
    }
  }

  result.tools = Array.from(toolMap.values()).slice(-MAX_TOOLS);
  result.agents = Array.from(agentMap.values()).slice(-MAX_AGENTS);

  return result;
}

function processEntry(
  entry: Record<string, unknown>,
  toolMap: Map<string, ToolEntry>,
  agentMap: Map<string, AgentEntry>,
  result: TranscriptData
): void {
  const message = entry.message as Record<string, unknown> | undefined;
  const content = message?.content;
  if (!Array.isArray(content)) return;

  for (const block of content) {
    if (block.type === 'tool_use') {
      processToolUse(block, toolMap, agentMap, result, entry.timestamp as string | undefined);
    } else if (block.type === 'tool_result') {
      processToolResult(block, toolMap, agentMap);
    }
  }
}

function processToolUse(
  block: Record<string, unknown>,
  toolMap: Map<string, ToolEntry>,
  agentMap: Map<string, AgentEntry>,
  result: TranscriptData,
  timestamp?: string
): void {
  const id = block.id as string;
  const name = block.name as string;
  const input = block.input as Record<string, unknown> | undefined;
  const startTime = timestamp ? new Date(timestamp).getTime() : undefined;

  if (name === 'Task') {
    agentMap.set(id, {
      id,
      type: (input?.subagent_type as string) || 'unknown',
      model: input?.model as string | undefined,
      description: input?.description as string | undefined,
      status: 'running',
      startTime,
    });
  } else if (name === 'TodoWrite') {
    const todos = input?.todos;
    if (todos && Array.isArray(todos)) {
      result.todos = todos as TodoItem[];
    }
  } else {
    toolMap.set(id, {
      id,
      name,
      status: 'running',
      target: extractTarget(name, input),
      startTime,
    });
  }
}

function processToolResult(
  block: Record<string, unknown>,
  toolMap: Map<string, ToolEntry>,
  agentMap: Map<string, AgentEntry>
): void {
  const toolUseId = block.tool_use_id as string;
  const isError = block.is_error as boolean;
  const endTime = Date.now();

  if (toolMap.has(toolUseId)) {
    const tool = toolMap.get(toolUseId)!;
    tool.status = isError ? 'error' : 'completed';
    tool.endTime = endTime;
  }

  if (agentMap.has(toolUseId)) {
    const agent = agentMap.get(toolUseId)!;
    agent.status = 'completed';
    agent.endTime = endTime;
  }
}

function extractTarget(name: string, input?: Record<string, unknown>): string | undefined {
  if (!input) return undefined;

  switch (name) {
    case 'Read':
    case 'Write':
    case 'Edit':
      return input.file_path as string | undefined;
    case 'Glob':
    case 'Grep':
      return input.pattern as string | undefined;
    case 'Bash': {
      const cmd = input.command as string | undefined;
      return cmd?.slice(0, 30);
    }
    default:
      return undefined;
  }
}
