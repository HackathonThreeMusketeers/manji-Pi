import fileinput
import os
import re
import subprocess
import sys
import tempfile
import textwrap
import traceback
import aiy.audio
from aiy._drivers._hat import get_aiy_device_name
import speech_recognition

RECORD_DURATION_SECONDS = 3

def check_mic_works():
    """Check the microphone records correctly."""
    temp_file, temp_path = tempfile.mkstemp(suffix='.wav')
    os.close(temp_file)

    try:
        input("When you're ready, press enter and say 'Testing, 1 2 3'...")
        print('Recording...')
        aiy.audio.record_to_wave(temp_path, RECORD_DURATION_SECONDS)
        print('Playing back recorded audio...')
        aiy.audio.play_wave(temp_path)
        
        r = speech_recognition.Recognizer()
        with speech_recognition.AudioFile(temp_path) as source:
                audio = r.record(source)
                result = r.recognize_google(audio, language='ja-JP')
                print(result)
    finally:
        try:
            os.unlink(temp_path)
        except FileNotFoundError:
            pass

    return 0

if __name__ == '__main__':
    check_mic_works()
