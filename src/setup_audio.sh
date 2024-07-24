#!/bin/bash

sudo apt-get update
sudo apt-get install -y ffmpeg

DEFAULT_SINK=$(pactl get-default-sink)
echo "Default Sink: $DEFAULT_SINK"

pactl list sinks | grep "$DEFAULT_SINK"

MONITOR_NAME=$(pactl list sinks | grep "$(pactl get-default-sink).monitor" | cut -d : -f 2 | xargs)
echo "Monitor Name: $MONITOR_NAME"