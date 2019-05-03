import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt


name = sys.argv[1]
img = cv2.imread(name, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)[...,0]
# edges = cv2.Canny(gray, 10,30)    
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(32,32))
contrast = clahe.apply(blurred)
ret, thresh = cv2.threshold(contrast, 20, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)

# plt.imshow(thresh)
# plt.savefig('./threshold.png')