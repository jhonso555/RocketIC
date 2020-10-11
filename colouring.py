import os
os.system('cls')
print("\t\t\t****Select color range****\nBlue:\t\t110, 50, 50 Lower\t130, 255, 255 Upper\nPink Red:\t150, 150, 200 Lower\t180, 255, 255 Upper\n")
r1 = int(input("R low: "))
g1 = int(input("G low: "))
b1 = int(input("B low: "))

r2 = int(input("R up: "))
g2 = int(input("G up: "))
b2 = int(input("B up: "))

arquivo = open('testes.txt', 'a')
arquivo.write('Low\t' + str(r1) + ' ' + str(g1) + ' ' + str(b1) + '\nUpp\t' + str(r2) + ' ' + str(g2) + ' ' + str(b2) + '\n\n')
arquivo.close()