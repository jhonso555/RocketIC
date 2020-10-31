import os, time, shutil, cv2, tkinter, fileinput, colouring, pickle, colorsys
import numpy as np
import matplotlib.pyplot as plt

#region / defining values
#\
print("Cleaning '/data'...")
shutil.rmtree('./data/')
os.mkdir('data')
cap = cv2.VideoCapture('./src/Video_4.mp4')
data = open('coords.txt', 'w')
data.write("F  |  X  |  Y\n")
frames, frame_atual, k, i = 1, 1, 10, 0
cX, cY, deltaTempo = [], [], []
width, height  = int(cap.get(3)), int(cap.get(4))
file_lower = open('list_lower.pkl', 'rb')
file_upper = open('list_upper.pkl', 'rb')
colorRange_lower = pickle.load(file_lower)
colorRange_upper = pickle.load(file_upper)


# cor_atualizada = colorsys.rgb_to_hsv(colorRange_lower[0], colorRange_lower[1], colorRange_lower[2])
# print(cor_atualizada)
# time.sleep(10)


tempoI = time.time()

class Colors():
    rl = colorRange_lower[0]
    gl = colorRange_lower[1]
    bl = colorRange_lower[2]

    ru = colorRange_upper[0]
    gu = colorRange_upper[1]
    bu = colorRange_upper[2]
#endregion


if (cap.isOpened() == False):
    print("Error opening video file")

while(frames <= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))): 
    ret, frame = cap.read()
    
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
        #region // Color range and image processing 
        lower = np.array([Colors.rl, Colors.gl, Colors.bl])
        upper = np.array([Colors.ru, Colors.gu, Colors.bu])



        mask = cv2.inRange(hsv, lower, upper) 
        # res = cv2.bitwise_and(frame,frame, mask= mask)
        cv2.imshow('Frame', frame)
        cv2.imshow('Mask', mask)
        # cv2.imshow('Res', res)
        #endregion

        #region // object tracking and optimizing its position
        if frames % 4 == 0 and frames > 19:
            for i in range(height):
                for j in range(width):  
                    valor = mask[i][j] 
                    if valor > 0 and frame_atual == frames:
                        if len(cX) < 10 and len(cY) < 10: 
                            cX.append(j)
                            cY.append(i)
                            delteatempoF = time.time()
                            deltaTempo.append(delteatempoF-tempoI)


                        elif len(cX) >= 10 and len(cY) >= 10: 
                            if (j > cX[k-1]) and (i > cY[k-1]):
                                                                
                                diffX = j-cX[k-1]
                                diffY = i-cY[k-1]
                                deltaTempoF = time.time()
                                cX.append(cX[k-1] + (diffX/2))
                                cY.append(cY[k-1] + (diffY/2))
                                deltaTempo.append(deltaTempoF-tempoI)

                                data.write("%d  |  %.1f  |  %.1f\n" % (frames, cX[k], cY[k])) 
                                k += 1
                                frame_atual += 1 

                            elif (cX[k-1] > j) and (cY[k-1] > i):
                                diffX = cX[k-1]-j
                                diffY = cY[k-1]-i
                                deltaTempoF = time.time()


                                cX.append(j + (diffX/2))
                                cY.append(i + (diffY/2))
                                deltaTempo.append(deltaTempoF-tempoI)

                                
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

plt.plot(deltaTempo, cY)
plt.title('Posição em Y por tempo')
plt.show()
data.close()
cap.release()