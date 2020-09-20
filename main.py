import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import PIL

#441 x, 618 y, 640 w, 352 h


cap = cv2.VideoCapture('./src/Video_4.mp4')
frames = 1
frame_list = []
cX, cY = [], []

coordenadas = open("coords.txt", "w")


if (cap.isOpened() == False):
    print("Error opening video file")

# while(cap.isOpened()):
while(frames <= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    ret, frame = cap.read()
    
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
        #Region // Color range 
        lower_red = np.array([150, 150, 200])
        upper_red = np.array([180, 255, 255])


        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('Frame', frame)
        cv2.imshow('Mask', mask)
        cv2.imshow('Res', res)

        for i in range(352):
            for j in range(640):
                valor = mask[i][j]
                #i = y & j = x
                if valor != 0:
                    cY.append(mask[i])
                    cX.append(mask[j])
    

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    else:
        break
    frames += 1

plt.plot(cX, cY)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Teste!!')
plt.show()

    
cap.release()