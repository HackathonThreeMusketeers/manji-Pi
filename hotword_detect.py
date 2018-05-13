from snowboy import snowboydecoder
import sys
import signal
import speak_audio
import recognition
import control_led
import manji_camera4p3

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
    index = text.find("ご飯")
    if index != -1:
        speak_audio.speak("わかったにゃぁぁ")
        manji_camera4p3.Move_Servo()

        y, x = manji_camera4p3.ManjiCamera4p3()
        
        if y >= 0.6:
            speak_audio.speak("美味しいにゃぁぁぁ")
        else:
            speak_audio.speak("やっぱ，いらないにゃぁぁ")

    else:
        speak_audio.speak("何を言ってるかわからないにゃぁぁ")
    control_led.stopping()

if __name__ == '__main__':
   
    model = "model.pmdl"

    # capture SIGINT signal, e.g., Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    print('Listening... Press Ctrl+C to exit')
    control_led.ready()
    # main loop
    detector.start(detected_callback=speak,
                interrupt_check=interrupt_callback,
                sleep_time=0.03)

    detector.terminate()
