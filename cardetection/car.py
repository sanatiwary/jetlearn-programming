import cv2

cap = cv2.VideoCapture('cardetection/video.avi')

carCascades = cv2.CascadeClassifier('cardetection/cars.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = carCascades.detectMultiScale(gray, 1.1, 3)
    for x, y, w, h in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 7)
    
    cv2.imshow('output', frame)
    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# import cv2

# cap=cv2.VideoCapture('video.avi')

# car_cascades=cv2.CascadeClassifier('cars.xml')

# while cap.isOpened():
#     ret,frame=cap.read()
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#     cars=car_cascades.detectMultiScale(gray,1.1,3)

#     for x,y,w,h in cars:
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)

#     cv2.imshow('output',frame)
#     if cv2.waitKey(5)==ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()