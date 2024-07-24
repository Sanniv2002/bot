import subprocess
import threading


def stream_audio_to_websocket():
    websocket_url = "ws://localhost:8765"

    # FFmpeg command to capture audio from PulseAudio
    ffmpeg_command = [
        "ffmpeg",
        "-f", "pulse",
        "-i", "alsa_output.pci-0000_00_1f.3.analog-stereo.monitor",
        "-f", "wav",
        "-"
    ]

    # websocat command to send FFmpeg output to the WebSocket server
    websocat_command = [
        "websocat",
        "-u",
        websocket_url
    ]

    ffmpeg_process = subprocess.Popen(
        ffmpeg_command, stdout=subprocess.PIPE, text=True)
    websocat_process = subprocess.Popen(
        websocat_command, stdin=ffmpeg_process, stdout=subprocess.PIPE, text=True)
    output, error = websocat_process.communicate()

    print(output)


if __name__ == "__main__":
    stream_audio_to_websocket()
