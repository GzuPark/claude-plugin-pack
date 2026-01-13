#!/bin/bash
# Dependency check for video-insight skill
# Usage: ./check_dependencies.sh [--youtube|--local|--all]
# Exit codes: 0 = success, 1 = missing dependencies

set -e

MODE="${1:---all}"

# OS detection
detect_os() {
    case "$(uname -s)" in
        Darwin*) echo "macos" ;;
        Linux*)  echo "linux" ;;
        *)       echo "unknown" ;;
    esac
}

OS=$(detect_os)
MISSING=0

check_command() {
    local cmd="$1"
    local brew_pkg="$2"
    local apt_pkg="$3"
    local apt_note="$4"

    if ! command -v "$cmd" &> /dev/null; then
        echo "MISSING: $cmd"
        if [ "$OS" = "macos" ]; then
            echo "  Install: brew install $brew_pkg"
        elif [ "$OS" = "linux" ]; then
            if [ -n "$apt_note" ]; then
                echo "  Install: $apt_note"
            else
                echo "  Install: sudo apt install $apt_pkg"
            fi
        fi
        return 1
    fi
    echo "OK: $cmd"
    return 0
}

# YouTube dependencies
check_youtube() {
    echo "=== YouTube Dependencies ==="
    check_command "yt-dlp" "yt-dlp" "yt-dlp" "pipx install yt-dlp" || MISSING=1
}

# Local file dependencies
check_local() {
    echo "=== Local File Dependencies ==="
    check_command "ffmpeg" "ffmpeg" "ffmpeg" || MISSING=1
    check_command "ffprobe" "ffmpeg" "ffmpeg" || MISSING=1
    check_command "whisper-cpp" "whisper-cpp" "" "Build from source (see references/prerequisites.md)" || MISSING=1
}

# Check Whisper model
check_model() {
    MODEL_DIR="$HOME/.cache/whisper"
    MODEL_NAME="ggml-large-v3-turbo-q8_0.bin"
    MODEL_PATH="$MODEL_DIR/$MODEL_NAME"

    echo ""
    echo "=== Whisper Model ==="
    if [ ! -f "$MODEL_PATH" ]; then
        echo "MISSING: Whisper model"
        echo "  Download: curl -L -o ~/.cache/whisper/$MODEL_NAME \\"
        echo "    \"https://huggingface.co/ggerganov/whisper.cpp/resolve/main/$MODEL_NAME?download=true\""
        MISSING=1
    else
        echo "OK: Whisper model"
    fi
}

# Run checks based on mode
case "$MODE" in
    --youtube)
        check_youtube
        ;;
    --local)
        check_local
        check_model
        ;;
    --all|*)
        check_youtube
        echo ""
        check_local
        check_model
        ;;
esac

echo ""
if [ $MISSING -eq 1 ]; then
    echo "RESULT: Missing dependencies"
    echo ""
    echo "See references/prerequisites.md for detailed installation guide."
    exit 1
else
    echo "RESULT: All dependencies ready"
    exit 0
fi
