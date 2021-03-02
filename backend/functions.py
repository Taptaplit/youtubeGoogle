from __future__ import unicode_literals
import youtube_dl
import json
import speech_recognition as sr
import os, shutil
from backend.AudioSplit import SplitWavAudioMubin

r = sr.Recognizer()




ydl_opts = {
    'outtmpl': 'video',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}


def get_data():
    with open('videos.json', 'r') as f:
        file = json.load(f)
    return file



def download_data(link):
    info = []
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(str(link), download=False)
        video_title = info_dict.get('title', None)
        video_url = info_dict.get("url", None)
        print(info_dict.get("channel", None))
        info.append(video_title)
        info.append(link)
        ydl.download([str(link)])
    return info


def add_video(link):
    info = download_data(str(link))
    folder = 'audioio'
    file = 'video.wav'
    split_wav = SplitWavAudioMubin(folder, file)
    text = split_wav.multiple_split(min_per_split=1)
    
    data = get_data()
    data[str(info[0])] = {}
    data[str(info[0])]['text'] = text
    data[str(info[0])]['url'] = str(info[1])
    with open('videos.json', 'w') as f:
        json.dump(data, f, indent=4)
        
        
        
def check_data(input):
    vid_list = []
    total = 0
    data = get_data()
    for video in data:
        text = data[str(video)]['text']
        if input.lower() in text.lower():
            total += 1
            vid_list.append(data[str(video)]['url'])
            vid_list.append(video)
    return vid_list, total
    

