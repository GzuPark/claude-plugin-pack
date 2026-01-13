# Prerequisites Installation Guide

This guide covers installation of required tools for video-insight skill.

## Required Tools by Feature

| Feature | Required Tools |
|---------|----------------|
| YouTube URL processing | `yt-dlp` |
| Local media processing | `whisper-cpp`, `ffmpeg` |

---

## macOS Installation

### Homebrew (Package Manager)

If Homebrew is not installed:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### yt-dlp (YouTube)

```bash
brew install yt-dlp
```

Verify installation:

```bash
yt-dlp --version
```

### ffmpeg (Audio/Video Processing)

```bash
brew install ffmpeg
```

Verify installation:

```bash
ffmpeg -version
ffprobe -version
```

### whisper-cpp (Speech-to-Text)

```bash
brew install whisper-cpp
```

Verify installation:

```bash
whisper-cpp --help
```

### Whisper Model Download

The model (~1.5GB) is downloaded automatically on first use. To download manually:

```bash
mkdir -p ~/.cache/whisper
curl -L -o ~/.cache/whisper/ggml-large-v3-turbo-q8_0.bin \
  "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo-q8_0.bin?download=true"
```

### Quick Install (All Tools)

```bash
brew install yt-dlp ffmpeg whisper-cpp
```

---

## Ubuntu Installation

### yt-dlp (YouTube)

**Option 1: pipx (Recommended)**

```bash
sudo apt install pipx
pipx install yt-dlp
```

**Option 2: pip**

```bash
pip install yt-dlp
```

**Option 3: Binary**

```bash
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```

Verify installation:

```bash
yt-dlp --version
```

### ffmpeg (Audio/Video Processing)

```bash
sudo apt update
sudo apt install ffmpeg
```

Verify installation:

```bash
ffmpeg -version
ffprobe -version
```

### whisper-cpp (Speech-to-Text)

whisper-cpp must be built from source on Ubuntu:

```bash
# Install build dependencies
sudo apt install build-essential git

# Clone and build
git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp
make

# Install to system path
sudo cp main /usr/local/bin/whisper-cpp
```

Verify installation:

```bash
whisper-cpp --help
```

### Whisper Model Download

```bash
mkdir -p ~/.cache/whisper
curl -L -o ~/.cache/whisper/ggml-large-v3-turbo-q8_0.bin \
  "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo-q8_0.bin?download=true"
```

### Quick Install (All Tools)

```bash
# ffmpeg
sudo apt update && sudo apt install -y ffmpeg

# yt-dlp
sudo apt install -y pipx && pipx install yt-dlp

# whisper-cpp (build from source)
sudo apt install -y build-essential git
git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp && make && sudo cp main /usr/local/bin/whisper-cpp
```

---

## Verification

Run the dependency check script:

```bash
./scripts/check_dependencies.sh
```

Expected output when all tools are installed:

```
OK: yt-dlp found
OK: whisper-cpp found
OK: ffmpeg found
OK: ffprobe found
OK: Whisper model found at ~/.cache/whisper/ggml-large-v3-turbo-q8_0.bin

All dependencies are ready!
```

---

## Troubleshooting

### yt-dlp: "command not found"

- macOS: `brew install yt-dlp`
- Ubuntu: `pipx install yt-dlp` or add `~/.local/bin` to PATH

### whisper-cpp: "command not found"

- macOS: `brew install whisper-cpp`
- Ubuntu: Build from source (see above)

### ffmpeg/ffprobe: "command not found"

- macOS: `brew install ffmpeg`
- Ubuntu: `sudo apt install ffmpeg`

### Whisper model download fails

Try manual download:

```bash
wget -O ~/.cache/whisper/ggml-large-v3-turbo-q8_0.bin \
  "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo-q8_0.bin"
```

### Permission denied

Ensure scripts are executable:

```bash
chmod +x scripts/*.sh
```
