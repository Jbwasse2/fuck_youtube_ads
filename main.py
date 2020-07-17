import pickle

import pudb

import youtube_dl
from credentials import ydl_opts


def get_youtube_videos(channel):
    ret = ydl.extract_info(video_example, download=False)
    entries = ret['entries']
    ids = []
    for entry in entries:
        ids.append(entry['id'])
    returns ids

creators = ['EconomicsExplained']
video_example = 'https://www.youtube.com/watch?v=PCicKydX5GE'
video_example = 'https://www.youtube.com/c/EconomicsExplained/videos'
#Get list of all videos done by youtuber
pu.db
with youtube_dl.YoutubeDL({}) as ydl:
#    ret = ydl.download([video_example])
