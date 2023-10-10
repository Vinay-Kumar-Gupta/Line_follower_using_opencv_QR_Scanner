import cv2
import numpy as np
from pyzbar.pyzbar import decode
from TTS import *
from threading import Thread

cap = cv2.VideoCapture(0)
pre_data = ""
speak_config(125,0)
mydata = ""
flag = 1

while 1:
    _,frame = cap.read()
    frame = cv2.flip(frame,1)
    code = decode(frame)
    if code != []:
        for qr in code:
            mydata = qr.data.decode("utf-8")

            if mydata != pre_data and flag == 1:
                print(mydata)
                speak(mydata)
                    # t1 = Thread(target=speak, daemon=True, args=[mydata])
                    # t1.start()
                flag = 0
                pre_data = mydata
            pts = np.array([qr.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(frame,[pts],True,(255,0,255),2)
            cv2.putText(frame,mydata,(0,30),cv2.FONT_HERSHEY_SIMPLEX,0.,(0,0,255),2)
    else:
        flag = 1
    cv2.imshow("Output",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
