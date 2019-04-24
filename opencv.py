import matplotlib.pyplot as plt
import numpy as np
import cv2

frame = cv2.imread('trash_on_water.jpg')
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
subtractor = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25, detectShadows=True)