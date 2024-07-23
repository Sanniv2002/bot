import subprocess
import threading
import time

def start_ffmpeg():
    # Command to start FFmpeg to capture audio
    command = [
        'ffmpeg',
        '-f', 'pulse',
        '-i', 'default',
        'output.wav'
    ]
    subprocess.run(command)


if __name__ == "__main__":
    start_ffmpeg()