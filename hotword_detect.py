from snowboy import snowboydecoder
import sys
import signal
import speak_audio
import recognition
import control_led

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def speak():
    control_led.listening()
    text = recognition.check_mic_works()
    index = text.find("OK")
    if index != -1:
        speak_audio.speak("fuck you")
    else:
        speak_audio.speak("not found")
    control_led.stopping()
model = "model.pmdl"

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=speak,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
