import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('./src/Video_4.mp4')

if (cap.isOpened() == False):
    print("Error opening video file")

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        cv2.imshow('Frame', frame)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # #Region // Color range 
        lower_red = np.array([150, 150, 200])
        upper_red = np.array([255, 255, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        # Region // Thresholding
        ret, thresh1 - cv2.threshold(cap, 127, 255, cv2.THRESH_BINARY)

        cv2.imshow('Frame', frame)
        cv2.imshow('Mask', mask)
        cv2.imshow('Res', res)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    else:
        break

cap.release()