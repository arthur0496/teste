import cv2
import numpy as np
import matplotlib.pyplot as plt
import time


img = cv2.imread('lixo2.jpg')
crop_img = img[1:420, 1:360]
cv2.imwrite('lixo2_420.jpg',crop_img)
# cv2.imshow("cropped", crop_img)
# cv2.waitKey(0)
# crop_img.save('./threshold.png')

# plt.gray()
# plt.imshow(imgBinaria)
# plt.show()
# plt.imshow(img)