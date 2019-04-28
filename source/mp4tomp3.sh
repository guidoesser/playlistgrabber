#!/bin/bash
for f in *; 
do ffmpeg -i "$f" -c:a libmp3lame "./mp3/${f%.*}.mp3"; 
done
