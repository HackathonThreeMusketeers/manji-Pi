#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pygame
import time
from pydub import AudioSegment

# const
url= 'http://webapi.aitalk.jp/webapi/v2/ttsget.php'

def load(text):
    body = {
        "username": "spajam2018",
        "password": "Lpnsen58",
        "speaker_name": "maki",
        "text": text
    }
    res = requests.post(url, params=body)
    if res.status_code == 200:
        with open('temp.ogg', 'wb') as fs:
            fs.write(res.content)

def speak(text):
    # initialization
    pygame.init()
    SONG_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(SONG_END)
    ogg = load(text)
    pygame.mixer.init()
    sound = AudioSegment.from_ogg("temp.ogg")
    pygame.mixer.music.load('temp.ogg')
    pygame.mixer.music.play()
    time.sleep(sound.duration_seconds)
    pygame.mixer.music.stop()
