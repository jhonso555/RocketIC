import cv2
import numpy as np
from matplotlib import pyplot as plt
import xlswriter

workbook = xlswriter.Workbook('distancias.xlsx')
worksheet = workbok.add_worksheet()

numeros = (
    ['Velocidade', x]
    ['Distancia', x] 
    )
    
row = 0
col = 0

for item, cost in (numeros):
    worksheet.write(row, col,  , item)
    worksheet.write(row, col+1, cost)
    row += 1

worksheet.write (row, 0, 'resto')
worksheet.write (row, 1, '=SUM(B1:B4)')

workbook.close
