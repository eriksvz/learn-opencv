import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# img[200:300, 100:300] = 255, 0, 0
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 10)
cv2.rectangle(img, (5, 5), (250, 250), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (400, 50), 30, (255, 255, 0), cv2.FILLED)
cv2.putText(img, "eureka it works!", (100, 100), cv2.FONT_ITALIC, 1, (255, 255, 255))

cv2.imshow("Image", img)

cv2.waitKey(0)