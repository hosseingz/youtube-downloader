from pytube import YouTube, Playlist
import os
os.system('clear')


def resolution(url):
    yt = YouTube(url)
    video = yt.streams.filter(file_extension='.mp4')
    for i in video:
        print(i)


def download(url:str, res:str):
    yt = YouTube(url)
    video = yt.streams.get_by_resolution(res)
    video.download()


s = input('linki at galsin: ')

resolution(s)