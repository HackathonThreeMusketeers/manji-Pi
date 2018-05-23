import pyaudio
import time
import wave
import speech_recognition

WAVE_OUTPUT_FILENAME = "output.wav"

def record_voice():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 3
    result = ""

    input_device_index = 0
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return

def speech_to_text():
    r = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(WAVE_OUTPUT_FILENAME) as source:
        audio = r.record(source)
        result = r.recognize_google(audio, language='ja-JP')
    return result

def get_speech_text():
    record_voice()
    text = speech_to_text()
    return text
