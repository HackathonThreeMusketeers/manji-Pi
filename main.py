# --*-- coding: utf-8 --*--

import numpy as np
import cv2
import picamera
import time
import requests
import json

np.set_printoptions(threshold='nan')

def take_photo():
    with picamera.PiCamera() as camera :
        camera.resolution = (160,128)
        camera.framerate = 24
        time.sleep(2)
        output = np.empty((128 * 160 * 3,), dtype=np.uint8)
        camera.capture(output, 'bgr')
        output = output.reshape((128,160,3))
        hsv_color = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_color, np.array([128,100,50]), np.array([200,250,180]))
        cv2.imwrite('img.png',output);
        cv2.imwrite('mask.png',mask);

        #print hsv_color[ hsv_color[:,:,1] > 50 ]
        img = cv2.resize(mask,(16,12));
        cv2.imwrite('res.png',output);
        # print np.where(img > 200), "::end::"
        y,x = np.where(img > 200)
        y = y[len(y)/2]
        x = x[len(x)/2]
        # cv2.imshow("cap", img);
        # while True :
        #   if cv2.waitKey(33) >= 0:
        #     break;
        # cv2.destroyAllWindows()
        print  json.dumps([y/12.,x/16.])



def send():
  image = open ('./img.png', 'rb')
  files = {'image':('img.png', image,'image/png')}
  data = {'temperature': 32}
  r = requests.post('http://ec2-18-191-25-206.us-east-2.compute.amazonaws.com:3000/entry',files=files,data=data)
  # print r.text



# def test1():
#     output = cv2.imread('./filename.jpg')
#     output = cv2.resize(output,(24,32))
#     #output = output.reshape((240,320,3))
#     hsv_color = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
#     mask = cv2.inRange(hsv_color, np.array([120,100,50]), np.array([200,250,180]))
#     # print hsv_color[ hsv_color[:,:,1] > 50 ]
#     res = cv2.bitwise_and(output,output,mask=mask);
#     cv2.imshow("cap", res);
#     while True :
#       if cv2.waitKey(33) >= 0:
#         break;
#     cv2.destroyAllWindows()


take_photo();
# send();
