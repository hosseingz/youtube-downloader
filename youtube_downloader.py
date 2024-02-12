from pytube import YouTube, Playlist
import os
os.system('clear')
def download(url):
    yt = YouTube(url)
    video = yt.streams.get_by_resolution('720p')
    video.download()



download_list = []



while True:
    s = input('Harchi link dari bas galsin ( exit (e) ): ')
    os.system('clear')

    if 'list' in s:
        print('list added\n')
        download_list += Playlist(s).video_urls

    elif 'youtu.be' in s or 'watch' in s:
        print('link added\n')
        download_list.append(s)

    elif s == 'e':
        break


if not os.path.exists('YouTube Downloads'):
    os.mkdir('YouTube Downloads')

os.chdir('YouTube Downloads')

for i, url in enumerate(download_list):

    print(f'Progress: {(i * 100) / len(download_list):.2f}%')

    download(url)

    os.system('clear')

