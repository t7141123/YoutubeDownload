from pytube import YouTube
#from pytube import Playlist
import sys

plURL = input("Please type your play list: ")
yt = YouTube(sys.argv[1])
yt.streams.first().download()
#pl = Playlist(plURL)
#pl.download_all()

