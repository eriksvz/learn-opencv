import cv2
import numpy as np

img = cv2.imread('lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCasccade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

faces = faceCasccade.detectMultiScale(imgGray, 1.1, 4)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 12)

cv2.imshow('Result', img)

cv2.waitKey(0)