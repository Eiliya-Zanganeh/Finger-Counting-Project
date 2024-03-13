import cv2
from Modules.HandTracking import handTrackingModule as htm

wCam, hCam = 640, 480
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    count = detector.fingersUp(img)
    cv2.putText(img, str(count[0]), (45, 450), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow('img', img)
    cv2.waitKey(1)
