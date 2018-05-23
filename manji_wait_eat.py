# --*-- coding: utf-8 --*--
from socketIO_client_nexus import SocketIO, LoggingNamespace
import manji_camera4p3
import main
import speak_audio
import json

def on_message(*args):
    if len(args[0]) > 5: func();

def func():
    manji_camera4p3.Move_Servo();
    print "main take photo"
    y, x = json.loads(main.take_photo());
    print y
    if y >= 0.6:
        speak_audio.speak("美味しいにゃぁぁぁ")
    else:
        speak_audio.speak("急に困るにゃぁぁぁ")

socketIO = SocketIO('http://ec2-18-191-25-206.us-east-2.compute.amazonaws.com',3000,LoggingNamespace)
socketIO.on('message',on_message)
socketIO.wait()

