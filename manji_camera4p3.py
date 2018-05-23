import subprocess
import json
from gpiozero import Servo
from time import sleep

def ManjiCamera4p3():

    p = subprocess.Popen("python main.py", shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout_data, stderr_data = p.communicate(timeout=100)
    str = stdout_data.decode("utf-8")
    print (str)
    return json.loads(str)

def Move_Servo():
    servo = Servo(26)
    servo.max()
    sleep(.5)
    servo.min()
    sleep(.25)
    servo.max()

    


#if __name__ == '__main__':
#Move_Servo();
#print(ManjiCamera4p3());
