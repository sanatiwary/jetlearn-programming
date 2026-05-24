import cv2
cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # rescaling factor = 1.3, minneighbors = 5
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 180, 190), 7)

        roiGray = gray[y: y + h, x: x + w]
        roiColor = frame[y: y + h, x: x + w]

        eyes = eyeCascade.detectMultiScale(roiGray, 1.3, 5)

        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roiColor, (ex, ey), (ex + ew, ey + eh), (165, 189, 190), 7)


    cv2.imshow('output', frame)
    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()