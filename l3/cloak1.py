import cv2
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('output video', frame)
        if cv2.waitKey(5) == ord('s'):
            cv2.imwrite("l3/images/background.png", frame)
            break

cap.release()
cv2.destroyAllWindows()