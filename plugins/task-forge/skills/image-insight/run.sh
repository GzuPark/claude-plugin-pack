#!/bin/bash
# run.sh - Python script runner with uv priority and fallback
#
# Usage: ./run.sh scripts/example.py [args...]
#
# Execution priority:
# 1. uv run (if uv is available)
# 2. Fallback to python with shared venv (~/.claude/skills/.venv)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SHARED_VENV="$HOME/.claude/skills/.venv"
SCRIPT_PATH="$1"
shift || true

if [ -z "$SCRIPT_PATH" ]; then
    echo "Usage: ./run.sh <script.py> [args...]"
    exit 1
fi

# Resolve script path relative to skill directory
if [[ ! "$SCRIPT_PATH" = /* ]]; then
    SCRIPT_PATH="$SCRIPT_DIR/$SCRIPT_PATH"
fi

# Check if uv is available
if command -v uv &> /dev/null; then
    exec uv run "$SCRIPT_PATH" "$@"
fi

# Fallback: Parse inline metadata and use shared venv
echo "uv not found, using fallback with shared venv..."

# Parse dependencies from inline script metadata
# Supports: # /// script
#           # dependencies = ["pkg1", "pkg2>=1.0"]
#           # ///
parse_dependencies() {
    local script="$1"
    local in_metadata=0
    local deps=""

    while IFS= read -r line; do
        if [[ "$line" =~ ^#[[:space:]]*///[[:space:]]*script ]]; then
            in_metadata=1
            continue
        fi
        if [[ $in_metadata -eq 1 && "$line" =~ ^#[[:space:]]*/// ]]; then
            break
        fi
        if [[ $in_metadata -eq 1 && "$line" =~ ^#[[:space:]]*dependencies[[:space:]]*=[[:space:]]*\[(.*)] ]]; then
            deps="${BASH_REMATCH[1]}"
            # Clean up: remove quotes and spaces
            deps=$(echo "$deps" | sed 's/"//g' | sed "s/'//g" | sed 's/[[:space:]]//g')
            break
        fi
    done < "$script"

    echo "$deps"
}

# Check for complex metadata that requires uv
check_complex_metadata() {
    local script="$1"
    if grep -q "^\#[[:space:]]*\(requires-python\|optional-dependencies\|\[tool\.\)" "$script" 2>/dev/null; then
        echo "Warning: Complex PEP 723 metadata detected. Please install uv for full support:" >&2
        echo "  curl -LsSf https://astral.sh/uv/install.sh | sh" >&2
        echo "Continuing with basic dependency parsing..." >&2
    fi
}

# Create shared venv if it doesn't exist
ensure_venv() {
    if [ ! -d "$SHARED_VENV" ]; then
        echo "Creating shared venv at $SHARED_VENV..."
        python3 -m venv "$SHARED_VENV"
    fi
}

# Install dependencies to shared venv
install_deps() {
    local deps="$1"
    if [ -n "$deps" ]; then
        echo "Installing dependencies: $deps"
        IFS=',' read -ra DEP_ARRAY <<< "$deps"
        "$SHARED_VENV/bin/pip" install -q "${DEP_ARRAY[@]}"
    fi
}

# Main fallback logic
check_complex_metadata "$SCRIPT_PATH"
ensure_venv

DEPS=$(parse_dependencies "$SCRIPT_PATH")
install_deps "$DEPS"

exec "$SHARED_VENV/bin/python" "$SCRIPT_PATH" "$@"
