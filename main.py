import cv2
import numpy as np
from cvzone.SerialModule import SerialObject

# ================ DECLARETIONS ==================
error = 0
pre_error = 0
integral = 0
kp = 25
kd = 10
ki = 0.02

base_speed = 200
esp = SerialObject("COM3",digits=3) # creating object esp
cap = cv2.VideoCapture(1) # For camera input
# hsvVals = [0,0,0,179,255,99] # main
hsvVals = [0,0,0,179,255,45]
threshold = 0.2

# ==================== OPERATIONAL FUNCTIONS =======================
def thresholding(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([hsvVals[0],hsvVals[1],hsvVals[2]])
    upper = np.array([hsvVals[3],hsvVals[4],hsvVals[5]])
    mask = cv2.inRange(hsv,lower,upper)
    return mask

def getContours(imgThresh,img):
    try:
        Contours, hery = cv2.findContours(imgThresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        biggest = max(Contours,key=cv2.contourArea)
        x,y,w,h = cv2.boundingRect(biggest)
        cx = x + w//2
        cy = y + h//2
        cv2.drawContours(img,biggest,-1,(0,255,0),3)
        cv2.circle(img,(cx,cy),10,(0,0,255),cv2.FILLED)

        return cx
    except:
        print("First Try Error")

def get_sensor_data(image,sensor):
    imgs = np.hsplit(image,sensor) # slipting screen into 3 parts
    total_pixel =(image.shape[1]//sensor) * image.shape[0] # finding total pixels in each section
    send_out = []

    for x,img in enumerate(imgs):
        pixel = cv2.countNonZero(img) # counting
        if pixel > threshold*total_pixel:
            send_out.append(1)
        else:
            send_out.append(0)

        cv2.imshow(str(x), img)
    # print(send_out)
    return send_out

def sendCommnads(send_out):

    global error , pre_error , integral

    # ================ Assigning Error Value ==================
    if send_out[1] == 1 and send_out[2] == 0 and send_out[3] == 0:
        error = -2
    elif send_out[1] == 1 and send_out[2] == 1 and send_out[3] == 0:
        error = -1
    elif send_out[1] == 0 and send_out[2] == 1 and send_out[3] == 0:
        error = 0
    elif send_out[1] == 0 and send_out[2] == 1 and send_out[3] == 1:
        error = 1
    elif send_out[1] == 0 and send_out[2] == 0 and send_out[3] == 1:
        error = 2

    # PID controller
    proportional = kp * error           # proportional
    derivative = kd * (error-pre_error) # derivative
    integral += ki * error              # integral


    print("Kp =",proportional,"Kd =",derivative,"Ki =",integral)
    lm_value = base_speed - ( proportional + derivative +integral,2)
    rm_value = base_speed + ( proportional + derivative + integral)
    pre_error = error

    esp.sendData([lm_value,rm_value])
    # print(lm_value,rm_value)

# ===================== MAIN LOOP ===========================

while 1:
    _,img = cap.read()
    # img = cv2.flip(img,1)
    # img = cv2.resize(img,(560,420)) # for 7
    img = cv2.resize(img,(480,360)) # for 5 & 3

    imgThresh = thresholding(img)
    cx = getContours(imgThresh,img)
    send_out = get_sensor_data(imgThresh,5)

    sendCommnads(send_out)

    # cv2.imshow("Output", img)
    cv2.imshow("Track",imgThresh)
    if (cv2.waitKey(1) & 0xff) == ord("q"):
        break