import cv2

# img = cv2.imread('lena.png')
# cv2.imshow('Output', img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture('test-video.mp4')
cap = cv2.VideoCapture(0)
# width
cap.set(3, 640)
# height
cap.set(4, 480)
# light
cap.set(10, 100)

while True:
    success, img = cap.read()
    if success:
        cv2.imshow('Video', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
