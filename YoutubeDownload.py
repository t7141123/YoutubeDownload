from pytube import YouTube
import sys

yt = YouTube(sys.argv[1])
yt.streams.first().download()

