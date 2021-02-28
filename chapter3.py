import cv2
import numpy as np

img = cv2.imread('lambo.jpg')
print(img.shape)

imgSmall = cv2.resize(img, (640, 480))
print(imgSmall.shape)

imgBig = cv2.resize(img, (1920, 1040))
print(imgBig.shape)

imgCropped = img[0:500, 500:1500]
cv2.imshow('lambo', img)
cv2.imshow('lambo resize', imgSmall)
cv2.imshow('lambo resize big', imgBig)
cv2.imshow('lambo Cropped :(', imgCropped)
cv2.waitKey(0)



