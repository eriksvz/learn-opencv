import cv2
import numpy as np


img = cv2.imread('lena.png')
kernel = np.ones((5, 5), np.uint8)
imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (5, 5), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialate = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialate, kernel, iterations=1)

cv2.imshow('Gray image', imGray)
cv2.imshow('Blur image', imgBlur)
cv2.imshow('Canny image', imgCanny)
cv2.imshow('Normal image', img)
cv2.imshow('Dialated image', imgDialate)
cv2.imshow('Eroded image', imgEroded)

cv2.waitKey(0)