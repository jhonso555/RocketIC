import cv2, time, shutil, os
import numpy as np
import matplotlib.pyplot as plt
 
def nothing(x):
    pass

# Open the video
cap = cv2.VideoCapture('./src/Video_4.mp4')

data = open('coords.txt', 'w')
data.write("F  |  X  |  Y\n")

if os.path.isdir('./data/') == False:
    os.mkdir('data')
else:
    shutil.rmtree('./data/')
    os.mkdir('data')

frames = 0
cap = cv2.VideoCapture('./src/Video_4.mp4')
frames, frame_atual, k = 1, 1, 10
posX, posY, deltaTempo = [], [], []
width, height  = int(cap.get(3)), int(cap.get(4))
tempoI = time.time()

# Create a window
cv2.namedWindow('image')
 
# create trackbars for color change
cv2.createTrackbar('lowH','image',150,179,nothing)
cv2.createTrackbar('highH','image',179,179,nothing)
 
cv2.createTrackbar('lowS','image',150,255,nothing)
cv2.createTrackbar('highS','image',255,255,nothing)
 
cv2.createTrackbar('lowV','image',200,255,nothing)
cv2.createTrackbar('highV','image',255,255,nothing)

# Check if video is opened
if (cap.isOpened() == False):
    print("Error opening video file")
 
while(frames <= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    ret, frame = cap.read()
    
    if ret == True:
        # get current positions of the trackbars
        ilowH = cv2.getTrackbarPos('lowH', 'image')
        ihighH = cv2.getTrackbarPos('highH', 'image')
        ilowS = cv2.getTrackbarPos('lowS', 'image')
        ihighS = cv2.getTrackbarPos('highS', 'image')
        ilowV = cv2.getTrackbarPos('lowV', 'image')
        ihighV = cv2.getTrackbarPos('highV', 'image')
        

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_hsv = np.array([ilowH, ilowS, ilowV])
        higher_hsv = np.array([ihighH, ihighS, ihighV])

        mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

        # // INSERT HERE OBJECT TRACKING
        if frames % 4 == 0 and frames > 19:
            for i in range(height):
                for j in range(width):  
                    pxValue = mask[i][j] 
                    if pxValue > 0 and frame_atual == frames:
                        if len(posX) < 10 and len(posY) < 10: 
                            posX.append(j)
                            posY.append(i)
                            delteatempoF = time.time()
                            deltaTempo.append(delteatempoF-tempoI)


                        elif len(posX) >= 10 and len(posY) >= 10: 
                            if (j > posX[k-1]) and (i > posY[k-1]):
                                                                
                                diffX = j-posX[k-1]
                                diffY = i-posY[k-1]
                                deltaTempoF = time.time()
                                posX.append(posX[k-1] + (diffX/2))
                                posY.append(posY[k-1] + (diffY/2))
                                deltaTempo.append(deltaTempoF-tempoI)

                                data.write("%d  |  %.1f  |  %.1f\n" % (frames, posX[k], posY[k])) 
                                k += 1
                                frame_atual += 1 

                            elif (posX[k-1] > j) and (posY[k-1] > i):
                                diffX = posX[k-1]-j
                                diffY = posY[k-1]-i
                                deltaTempoF = time.time()


                                posX.append(j + (diffX/2))
                                posY.append(i + (diffY/2))
                                deltaTempo.append(deltaTempoF-tempoI)

                                
                                data.write("%d  |  %.1f  |  %.1f\n" % (frames, posX[k], posY[k]))
                                k += 1
                                frame_atual += 1
                        
            np.savetxt('./data/' + str(frames) + '.txt', mask, fmt='%d')    
    else:
        break
    
    frames += 1
    frame_atual = frames

    # Apply the mask on the image to extract the original color
    frame = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('image', frame)
    cv2.imshow('mask', mask)
    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


tempoF = time.time()
delta = tempoF - tempoI
data.write('Tempo total de execucao: %.2f' % delta)
posY[0], posY[1] = 0, 0 

plt.plot(deltaTempo, posY)
plt.title('Posição em Y por tempo')
plt.show()
data.close()
cap.release()
cv2.destroyAllWindows()