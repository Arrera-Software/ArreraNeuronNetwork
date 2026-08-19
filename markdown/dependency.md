# System Dependencies

To run ArreraNeuronNetwork, you need to install some system-level dependencies depending on your operating system.

## Linux

### Debian / Ubuntu / Mint
```bash
sudo apt-get update
sudo apt-get install xclip xsel vlc python3-tk portaudio19-dev espeak ffmpeg
```

### Fedora
```bash
sudo dnf install xclip xsel vlc python3-tkinter portaudio-devel espeak-ng ffmpeg
```

### Arch Linux
```bash
sudo pacman -S xclip xsel vlc tk portaudio espeak-ng ffmpeg
```

## macOS

You may need [Homebrew](https://brew.sh/) to install some dependencies.

1.  **VLC Media Player**: Install it from the [official website](https://www.videolan.org/vlc/download-macosx.html) or via cask:
    ```bash
    brew install --cask vlc
    ```
2.  **PortAudio** (required for microphone access):
    ```bash
    brew install portaudio
    ```
3.  **FFmpeg** (recommended for media handling):
    ```bash
    brew install ffmpeg
    ```
4.  **Tkinter**: Usually included with Python, but if missing:
    ```bash
    brew install python-tk
    ```

## Windows

1.  **VLC Media Player**: Download and install from the [official website](https://www.videolan.org/vlc/download-windows.html).
    *Note: Ensure the bitness (32-bit or 64-bit) of VLC matches your Python installation.*
2.  **FFmpeg**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add it to your System PATH.
3.  **C++ Build Tools**: May be required for compiling some Python packages (like `llama-cpp-python` or `pyaudio` if wheels are missing). You can install the "Desktop development with C++" workload via Visual Studio Build Tools.

## Python Dependencies

After installing system dependencies, install the Python requirements:

```bash
pip install -r requirements.txt
```

*Note: `PyAudio` (required for microphone) is not always automatically installed or may fail if PortAudio is missing. If you encounter issues, try installing it manually after installing the system dependencies:*
```bash
pip install pyaudio
```
