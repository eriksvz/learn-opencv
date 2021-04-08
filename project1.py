import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# width
cap.set(3, 640)
# height
cap.set(4, 480)
# light
cap.set(10, 100)

# sun
# h_min, h_max, s_min, s_max, v_min, v_max
# orange
# 0      33     114    255    250    255
# blue
# 70     117    46     255    161    255
# yellow
# 26     38     45     255    216    255

# artificial light

# h_min, h_max, s_min, s_max, v_min, v_max
# orange
# 0      5      173    255    227    255
# blue
# 79     137    26     255    50     255
# green
# 33     80     26     255    50     255

# h_min, s_min, v_min, h_max, s_max, v_max
myColors = [[0, 173, 227, 5, 255, 255],
            [79, 26, 50, 137, 255, 255],
            [33, 26, 50, 80, 255, 255]]
# colors in bgr format
colorvalues = [
    [0, 170, 255],
    [255, 140, 25],
    [102, 204, 0]
]

points = []  # [x, y, colorId]


def findcolors(imgResult, colors, colorvalues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask, imgResult)
        cv2.circle(imgResult, (x, y), 10, colorvalues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
    return newPoints


def getContours(img, img_countours):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(img, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx_polygon = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx_polygon)
    return x + w // 2, y


def drawOnCanvas(imgResult, points, colorvalues):
    for point in points:
        cv2.circle(imgResult, (point[0], point[1]), 10, colorvalues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    if success:
        # cv2.imshow('Camera', img)
        # cv2.imshow('result', imgResult)
        imgResult = img.copy()
        newPoints = findcolors(imgResult, myColors, colorvalues)
        if len(newPoints) != 0:
            for newP in newPoints:
                points.append(newP)
        if len(newPoints) != 0:
            drawOnCanvas(imgResult, points, colorvalues)

        cv2.imshow('Result', imgResult)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
