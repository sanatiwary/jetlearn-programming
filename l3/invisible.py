import cv2
import numpy as np

background = cv2.imread('l3/images/background.png')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # red1 = np.array([0, 120, 70])
        # redU =np.array([10, 255, 255])

        green1 = np.array([50, 50, 50])
        greenU =np.array([70, 255, 255])

        mask1 = cv2.inRange(hsvFrame, green1, greenU)

        # red1 = np.array([170, 120, 70])
        # redU = np.array([180, 255, 255])

        green1 = np.array([130, 50, 50])
        greenU = np.array([150, 255, 255])


        mask2 = cv2.inRange(hsvFrame, green1, greenU)

        redMask = mask1 + mask2
        redMask = cv2.morphologyEx(redMask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 10)
        redMask = cv2.morphologyEx(redMask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations = 1)

        part1 = cv2.bitwise_and(background, background, mask = redMask)
        redFree = cv2.bitwise_not(redMask)
        part2 = cv2.bitwise_and(frame, frame, mask = redFree)
        final = part1 + part2

        cv2.imshow('output', final)
        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
