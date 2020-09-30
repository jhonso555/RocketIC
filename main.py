import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

#region / defining values
cap = cv2.VideoCapture('./src/Video_4.mp4')
data = open('coords.txt', 'w')
data.write("F  |  X  |  Y\n")
frames = 1
frame_atual = 1
k = 10
cX, cY = [], []
tempoI = time.time()
#endregion



if (cap.isOpened() == False):
    print("Error opening video file")

while(frames <= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    ret, frame = cap.read()
    
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
        #region // Color range and image processing 
        lower_red = np.array([150, 150, 200])
        upper_red = np.array([180, 255, 255])


        mask = cv2.inRange(hsv, lower_red, upper_red)

        cv2.imshow('Frame', frame)
        cv2.imshow('Mask', mask)
        #endregion

        #region // object tracking and optimizing its position
        if frames % 4 == 0 and frames > 19:
            for i in range(352):
                for j in range(640):
                    valor = mask[i][j]
                    if valor > 0 and frame_atual == frames:
                        if len(cX) < 10 and len(cY) < 10:
                            cX.append(j)
                            cY.append(i)


                        elif len(cX) >= 10 and len(cY) >= 10:
                            if (j > cX[k-1]) and (i > cY[k-1]):
                                diffX = j-cX[k-1]
                                diffY = i-cY[k-1]

                                cX.append(cX[k-1] + (diffX/2))
                                cY.append(cY[k-1] + (diffY/2))
                                data.write("%d  |  %.1f  |  %.1f\n" % (frames, cX[k], cY[k]))
                                k += 1
                                frame_atual += 1

                            elif (cX[k-1] > j) and (cY[k-1] > i):
                                diffX = cX[k-1]-j
                                diffY = cY[k-1]-i

                                cX.append(j + (diffX/2))
                                cY.append(i + (diffY/2))
                                data.write("%d  |  %.1f  |  %.1f\n" % (frames, cX[k], cY[k]))
                                k += 1
                                frame_atual += 1
                        

            np.savetxt('./data/' + str(frames) + '.txt', mask, fmt='%d')
        #endregion
    
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    else:
        break

    frames += 1
    frame_atual = frames
 
tempoF = time.time()
delta = tempoF - tempoI
print(delta)
cY[0], cY[1] = 0, 0
plt.plot(cX, cY)
plt.show()
data.close()
cap.release()