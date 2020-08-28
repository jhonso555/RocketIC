import cv2
import numpy as np

cap = cv2.VideoCapture('Video_4.mp4')

if (cap.isOpened() == False):
    print("Error opening video file")

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        cv2.imshow('Frame', frame)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #Region // Color range 
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('Frame', frame)
        cv2.imshow('Mask', mask)
        cv2.imshow('res', res)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    else:
        break



cap.release()