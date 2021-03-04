import cv2
import numpy as np


def empty(a):
    pass


trackBars = 'Track Bars'

path = 'lambo.jpg'
cv2.namedWindow(trackBars)
cv2.resizeWindow(trackBars, 1024, 240)
cv2.createTrackbar('Hue Min', trackBars, 0, 179, empty)
cv2.createTrackbar('Hue Max', trackBars, 48, 179, empty)
cv2.createTrackbar('Saturation Min', trackBars, 104, 255, empty)
cv2.createTrackbar('Saturation Max', trackBars, 255, 255, empty)
cv2.createTrackbar('Value Min', trackBars, 182, 255, empty)
cv2.createTrackbar('Value Max', trackBars, 255, 255, empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min', trackBars)
    h_max = cv2.getTrackbarPos('Hue Max', trackBars)
    s_min = cv2.getTrackbarPos('Saturation Min', trackBars)
    s_max = cv2.getTrackbarPos('Saturation Max', trackBars)
    v_min = cv2.getTrackbarPos('Value Min', trackBars)
    v_max = cv2.getTrackbarPos('Value Max', trackBars)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    print(h_min, h_max, s_min, s_max, v_min, v_max)

    # cv2.imshow('Original', img)
    # cv2.imshow('HSV', imgHSV)
    cv2.imshow('Modified', mask)
    cv2.imshow('Result', imgResult)
    cv2.waitKey(1)

#0 48 104 255 182 255
