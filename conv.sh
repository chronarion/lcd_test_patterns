#avconv -y -framerate 90 -qmax 1 -qscale 1 -i "cursor_pattern_%06d.png" video.webm -t 4

avconv -y -framerate 90 -i "cursor_pattern_%06d.png" -c:v h264 -crf 1 out.mov

rm out.zip
zip out.zip *.png
