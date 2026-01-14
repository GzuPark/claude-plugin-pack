/**
 * Claude Code statusline으로 전달되는 JSON 입력
 * @see https://code.claude.com/docs/en/statusline
 */
export interface StdinData {
  hook_event_name: 'Status';
  session_id: string;
  transcript_path: string;
  cwd: string;

  model: {
    id: string;
    display_name: string;
  };

  workspace: {
    current_dir: string;
    project_dir: string;
  };

  version: string;

  output_style: {
    name: string;
  };

  cost: {
    total_cost_usd: number;
    total_duration_ms: number;
    total_api_duration_ms: number;
    total_lines_added: number;
    total_lines_removed: number;
  };

  context_window: {
    total_input_tokens: number;
    total_output_tokens: number;
    context_window_size: number;
    /** v2.1.6+ */
    used_percentage?: number;
    /** v2.1.6+ */
    remaining_percentage?: number;
    current_usage: {
      input_tokens: number;
      output_tokens: number;
      cache_creation_input_tokens: number;
      cache_read_input_tokens: number;
    } | null;
  };

  mcp_servers?: McpServer[];
}

export interface McpServer {
  name: string;
  status: 'connected' | 'active' | 'disconnected' | 'error';
}

/**
 * Tool 실행 상태
 */
export interface ToolEntry {
  id: string;
  name: string;
  status: 'running' | 'completed' | 'error';
  target?: string;
  startTime?: number;
  endTime?: number;
}

/**
 * 서브에이전트 상태
 */
export interface AgentEntry {
  id: string;
  type: string;
  model?: string;
  description?: string;
  status: 'running' | 'completed';
  startTime?: number;
  endTime?: number;
}

/**
 * Todo 아이템
 */
export interface TodoItem {
  content: string;
  status: 'pending' | 'in_progress' | 'completed';
  activeForm?: string;
}

/**
 * 트랜스크립트에서 추출한 데이터
 */
export interface TranscriptData {
  tools: ToolEntry[];
  agents: AgentEntry[];
  todos: TodoItem[];
  sessionStart?: Date;
}

/**
 * Git 저장소 상태
 */
export interface GitStatus {
  isGitRepo: boolean;
  branch?: string;
  staged: number;
  modified: number;
  ahead: number;
  behind: number;
  hasUpstream: boolean;
  submoduleCount: number;
}

/**
 * 설정 파일 카운트
 */
export interface ConfigCounts {
  claudeMdCount: number;
  rulesCount: number;
  mcpCount: number;
  hooksCount: number;
}

/**
 * 5시간 블록 리셋 정보
 */
export interface ResetInfo {
  nextResetLocalTime: string;
  hoursLeft: number;
  minutesLeft: number;
}

/**
 * 렌더러에 전달되는 통합 컨텍스트
 */
export interface RenderContext {
  stdin: StdinData;
  transcript: TranscriptData;
  git: GitStatus;
  config: ConfigCounts;
  reset: ResetInfo;
  sessionDuration: string;
}
