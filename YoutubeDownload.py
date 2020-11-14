from pytube import YouTube
from pytube import Playlist
import requests
from bs4 import BeautifulSoup
import sys
import re
import os

def onProgress(stream, chunk, remains):
    total = stream.filesize
    percent = (total-remains) / total * 100
    print('Downlading ... {:05.2f}%'.format(percent), end='\r')

playlist = Playlist('https://www.youtube.com/playlist?list=PLGs2AT8sZ-AxT6wbk3TPbIGQn7wc1zVbt')
print('Total %s videos in this playlist!' % len(playlist.video_urls))

pathdir = 'download'
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)

for video_url in playlist.video_urls:
    print("-----------------------------------")
    print("Now download " + video_url + " ...")
    YouTube(video_url, on_progress_callback=onProgress).streams.filter(subtype='mp4',resolution="720p")[0].download(pathdir)
    print("Download finished!")