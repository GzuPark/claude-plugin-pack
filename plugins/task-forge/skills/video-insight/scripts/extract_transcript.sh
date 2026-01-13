#!/bin/bash
# YouTube 자막 추출
# Usage: ./extract_transcript.sh <youtube-url> [output_dir]
# Priority: Korean manual > English manual > Korean auto > English auto

URL="$1"
OUTPUT_DIR="${2:-.}"

if [ -z "$URL" ]; then
    echo "Usage: $0 <youtube-url> [output_dir]" >&2
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Extract subtitles with priority: manual > auto, ko > en
yt-dlp \
    --write-sub \
    --write-auto-sub \
    --sub-lang "ko,en" \
    --skip-download \
    --convert-subs json3 \
    -o "$OUTPUT_DIR/%(title)s.%(ext)s" \
    "$URL"
