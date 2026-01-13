#!/bin/bash
# 로컬 비디오/오디오 파일에서 메타데이터 추출 (ffprobe 사용)
# Usage: ./extract_local_metadata.sh <file_path>
# Output: JSON format metadata

FILE_PATH="$1"

if [ -z "$FILE_PATH" ]; then
    echo '{"error": "Usage: $0 <file_path>"}' >&2
    exit 1
fi

if [ ! -f "$FILE_PATH" ]; then
    echo '{"error": "File not found"}' >&2
    exit 1
fi

# ffprobe로 메타데이터 추출
PROBE_OUTPUT=$(ffprobe -v quiet -print_format json -show_format -show_streams "$FILE_PATH" 2>/dev/null)

if [ -z "$PROBE_OUTPUT" ]; then
    echo '{"error": "Failed to probe file"}' >&2
    exit 1
fi

# 파일명에서 제목 추출
FILENAME=$(basename "$FILE_PATH")
TITLE="${FILENAME%.*}"

# jq로 필요한 정보만 추출하여 YouTube 메타데이터 형식으로 변환
echo "$PROBE_OUTPUT" | jq --arg title "$TITLE" --arg filepath "$FILE_PATH" '{
    id: ($filepath | split("/") | last | split(".") | first),
    title: $title,
    channel: "Local File",
    upload_date: (now | strftime("%Y%m%d")),
    duration: (.format.duration | tonumber | floor),
    duration_string: (
        (.format.duration | tonumber | floor) as $total |
        (($total / 3600) | floor) as $hours |
        ((($total % 3600) / 60) | floor) as $minutes |
        ($total % 60) as $seconds |
        if $hours > 0 then
            "\($hours):\($minutes | tostring | if length < 2 then "0" + . else . end):\($seconds | tostring | if length < 2 then "0" + . else . end)"
        else
            "\($minutes):\($seconds | tostring | if length < 2 then "0" + . else . end)"
        end
    ),
    description: "Local media file: \($filepath)",
    format: .format.format_long_name,
    filepath: $filepath,
    source: "local"
}'
