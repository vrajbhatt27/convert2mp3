import ffmpeg
import os


def convert(inp, out):
    stream = ffmpeg.input(inp)
    x = ffmpeg.output(stream, out)
    ffmpeg.run(x)


inputFile = ""
for file in os.listdir():
    if '.webm' in file:
        inputFile = file
        break

convert(inputFile, 'audio.mp3')
