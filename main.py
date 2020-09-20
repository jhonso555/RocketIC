import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture('./src/Video_4.mp4')
frames = 1
frame_atual = 1
cX, cY = [], []

coordenadas = open("coords.txt", "w")


if (cap.isOpened() == False):
    print("Error opening video file")

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


        if frames % 4 == 0 and frames > 20:
            for i in range(352):
                for j in range(640):
                    valor = mask[i][j]
                    #i = y & j = x
                    if valor != 0 and frame_atual == frames and j > 200 and j < 270:
                        frase =  "frame (%d) foi detectado em: X%d e Y%d\n" % (frames, i, j)
                        print(j)
                        coordenadas.write(frase)
                        cY.append(i)
                        cX.append(j)
                        frame_atual += 1
    

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    else:
        break
    frames += 1
    frame_atual = frames
plt.plot(cY, cX)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Teste!!')
coordenadas.close()
plt.show()

    
cap.release()