import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture('./src/Video_4.mp4')
frames = 1
frame_atual = 1
k = 0
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


        if frames % 4 == 0 and frames > 19:
            for i in range(352):
                for j in range(640):
                    valor = mask[i][j]
                    #i = y & j = x
                    if valor != 0 and frame_atual == frames and j > 200 and j < 270:
                        frase =  "frame (%d) foi detectado em: X%d e Y%d\n" % (frames, i, j)
                        
                        #calcular a diferença entre o ponto atual e o ponto anterior para fazer 
                        # append num valor médio. para diminuir a disparidade no gráfico.
                        if len(cX) > 1 and len(cY > 1):
                            print("X", j, cX[k-1])
                            print("Y", i, cY[k-1])
                            if j < cX[k-1]:
                                if j-cX[k-1] <= 10 and j-cX[k-1] > 0 :
                                    cX.append(j-cX[k-1])
                                    print(j-cX[k-1] + "Carai!!")
                                else:
                                    continue
                            
                            elif cX[k-1] > j:
                                if cX[k-1]-j <= 10 and cX[k-1] > 0:
                                    cx.append(cX[k-1])
                                    print("Deu certo")
                                else:
                                    continue
                                
                        elif len(cY) > 1:
                            print("Y", i, cY[k-1])
                            if i < cY[k-1]:
                                if i-cY[k-1] <= 5 and i-cY[k-1] > 0:
                                    cY.append(i-cY[k-1])
                                    print("Deu certo 2")
                                else:
                                    continue

                            elif cY[k-1] > i:
                                if cY[k-1] > i:
                                    if cY[k-1] - i <= 5 and cY[k-1]-i > 0:
                                        cY.append(cY[k-1]-i)
                                        print("Deu certo 3")
                                    else:
                                        continue
                        else:
                            print("Não deu certo mas vamo ve")
                            cX.append(j)
                            cY.append(i)
                            k += 1
        
                        print("Inseri no bagui", k, cX, cY, len(cX), len(cY))
                        coordenadas.write(frase)
                        frame_atual += 1
    

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    else:
        break
    frames += 1
    frame_atual = frames
 
plt.plot(cX, cY)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Teste!!')
coordenadas.close()
plt.show()

    
cap.release()