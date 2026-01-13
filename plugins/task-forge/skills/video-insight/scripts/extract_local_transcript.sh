#!/bin/bash
# 로컬 비디오/오디오에서 transcript 추출 (whisper.cpp 사용)
# Usage: ./extract_local_transcript.sh <file_path> [output_dir]

set -e

# OS 감지
detect_os() {
    case "$(uname -s)" in
        Darwin*) echo "macos" ;;
        Linux*)  echo "linux" ;;
        *)       echo "unknown" ;;
    esac
}

OS=$(detect_os)

FILE_PATH="$1"
OUTPUT_DIR="${2:-/tmp/youtube-digest}"
MODEL_PATH="$HOME/.cache/whisper/ggml-large-v3-turbo-q8_0.bin"

if [ -z "$FILE_PATH" ]; then
    echo "Usage: $0 <file_path> [output_dir]" >&2
    exit 1
fi

if [ ! -f "$FILE_PATH" ]; then
    echo "ERROR: File not found: $FILE_PATH" >&2
    exit 1
fi

if [ ! -f "$MODEL_PATH" ]; then
    echo "ERROR: Whisper model not found. Run check_dependencies.sh first." >&2
    exit 1
fi

# 출력 디렉토리 생성
mkdir -p "$OUTPUT_DIR"

# 파일명에서 확장자 제거
BASENAME=$(basename "$FILE_PATH" | sed 's/\.[^.]*$//')

# whisper.cpp Metal 리소스 경로 설정 (macOS only)
if [ "$OS" = "macos" ]; then
    export GGML_METAL_PATH_RESOURCES="$(brew --prefix whisper-cpp)/share/whisper-cpp"
fi

echo "Transcribing: $FILE_PATH"
echo "Output directory: $OUTPUT_DIR"
echo "Using model: $MODEL_PATH"
echo ""

# ffmpeg로 WAV 변환 후 whisper-cpp로 transcribe
# -ar 16000: 16kHz 샘플링 (whisper 요구사항)
# -ac 1: 모노 채널
# -f wav: WAV 포맷
ffmpeg -i "$FILE_PATH" -ar 16000 -ac 1 -f wav - 2>/dev/null | \
whisper-cpp --model "$MODEL_PATH" \
    --language ko \
    --output-srt \
    --output-file "$OUTPUT_DIR/$BASENAME" \
    -

# 출력 파일 경로 반환
OUTPUT_FILE="$OUTPUT_DIR/$BASENAME.srt"
if [ -f "$OUTPUT_FILE" ]; then
    echo ""
    echo "Transcript saved to: $OUTPUT_FILE"
    echo "$OUTPUT_FILE"
else
    echo "ERROR: Failed to create transcript" >&2
    exit 1
fi
