import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import time

name = sys.argv[1]
img = cv2.imread(name)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #transformando a imagem em nível de cinza
_, imgBinaria = cv2.threshold(gray, 235, 255, cv2.THRESH_BINARY) #seleciona apenas os pixels dentro do intervalo [250,255]

# plt.gray()
# plt.imshow(imgBinaria)
# plt.show()
# plt.imshow(img)
