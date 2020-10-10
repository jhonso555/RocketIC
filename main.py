import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

#region / defining values
cap = cv2.VideoCapture('./src/Video_4.mp4')
data = open('coords.txt', 'w') #arquivo de coordenadas em Frame/posição em X/posição em Y para que possa ser utilizado no Excel posteriormente
data.write("F  |  X  |  Y\n")
frames = 1 #frame exato do vídeo
frame_atual = 1 #valor idêntico ao valor da variável frames para que as comparações sejam feitas frame a frame
k = 10 #constante das bases de dados
cX, cY = [], [] #vetores das posições onde o paraquedas é detectado no vídeo
tempoI = time.time() #contagem do tempo utilizado para a execução do programa
#endregion


#condicional para testar o funcionamento do vídeo
if (cap.isOpened() == False):
    print("Error opening video file")

while(frames <= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))): #enquanto o número de frames for menor que o número de frames totais, o algoritmo segue rodando
    #lendo o  vídeo
    ret, frame = cap.read()
    
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #transformação de cores
    
        #region // Color range and image processing 
        lower_red = np.array([150, 150, 200])
        upper_red = np.array([180, 255, 255])

        '''Range de cores detectados pela máscara
        caso a cor esteja dentro do valor estipulado, então
        o pixel será branco na máscara'''


        mask = cv2.inRange(hsv, lower_red, upper_red) #gerando a máscara

        cv2.imshow('Frame', frame) #mostrando o vídeo
        cv2.imshow('Mask', mask) #mostrando a máscara
        #endregion

        #region // object tracking and optimizing its position
        if frames % 4 == 0 and frames > 19: #varredura ocorre a cada 4 frames depois do frame 19
            for i in range(352): #352 é a altura do vídeo
                for j in range(640): #640 é a largura do vídeo
                    valor = mask[i][j] #variável valor é igual ao número da máscara naquele índice
                    if valor > 0 and frame_atual == frames: #comparando a cor do pixel e o frame atual
                        if len(cX) < 10 and len(cY) < 10: #criando uma base de dados para futuras comparações
                            cX.append(j)
                            cY.append(i)


                        elif len(cX) >= 10 and len(cY) >= 10: #comparando o tamanho das bases de dados
                            if (j > cX[k-1]) and (i > cY[k-1]): #comparando se o valor atual de X e Y são maiores que os valores do frame anterior para X e Y
                                
                                '''O cálculo de diferença é feito para que não
                                ocorra uma curva tão brusca ao gráfico final'''
                                
                                diffX = j-cX[k-1]
                                diffY = i-cY[k-1]

                                cX.append(cX[k-1] + (diffX/2))
                                cY.append(cY[k-1] + (diffY/2))

                                '''Caso os valores atuais de X e Y sejam maiores que os 
                                anteriores, então a diferença é anterior + ((atual-anterior)/2)'''

                                data.write("%d  |  %.1f  |  %.1f\n" % (frames, cX[k], cY[k])) #o valor calculado para os dois vetores (de X e de Y) são escritos no arquivo de coordenadas
                                k += 1
                                frame_atual += 1 #para que a comparação não ocorra novamente, o valor da variável aumenta, sendo diferente do valor do frame real

                            elif (cX[k-1] > j) and (cY[k-1] > i): #comparação contrária à comparação anterior
                                diffX = cX[k-1]-j
                                diffY = cY[k-1]-i


                                cX.append(j + (diffX/2))
                                cY.append(i + (diffY/2))

                                '''Cálculo caso o valor anterior seja maior que o atual
                                então o resultado é atual + ((anterior-atual)/2)'''
                                
                                data.write("%d  |  %.1f  |  %.1f\n" % (frames, cX[k], cY[k]))
                                k += 1
                                frame_atual += 1
                        

            np.savetxt('./data/' + str(frames) + '.txt', mask, fmt='%d') #salva, em texto, a matriz praticamente booleana, onde 0 é o ambiente e 255 é o paraquedas, também a cada 4 frames
        #endregion
    
        #condicional para fechar o programa
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    else:
        break

    frames += 1
    frame_atual = frames #restaurando o valor para o valor real do frame
 
tempoF = time.time()
delta = tempoF - tempoI
print(delta) #tempo de execução do programa

cY[0], cY[1] = 0, 0 #removendo os pontos de ruído no início do algoritmo

<<<<<<< HEAD
plt.plot(deltaTempo, cX, cY)
plt.title('Posição em Y por tempo')
=======
plt.plot(cX, cY) #amostragem do gráfico com base nos vetores de posição
>>>>>>> parent of a12a604... Um zilhão de alterações
plt.show()
data.close()
cap.release()