import cv2
import numpy as np

img = cv2.imread('cards.jpg')
width, height = 250, 350

pts1 = np.float32([[409, 88], [532, 140], [311, 249], [470, 333]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2. getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Warped Image", imgOutput)

cv2.waitKey(0)