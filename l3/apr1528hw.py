import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
text = "the dimensions of the video are " + str(width) + "x" + str(height)

while True:
    ret, frame = cap.read()
    cv2.putText(frame, text, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow('output', frame)
    if cv2.waitKey(0) == ord('s'):
        cv2.imwrite("imagecaptured.jpg", frame)
    if cv2.waitKey(0) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
