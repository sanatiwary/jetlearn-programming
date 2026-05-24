import cv2

img = cv2.imread("l1/images/road.jpg")

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

img = cv2.line(img, (30, 30), (240, 350), (94, 4, 3), 10)
img = cv2.arrowedLine(img, (250, 30), (300, 500), (8, 7, 102), 20)
img = cv2.rectangle(img, (350, 50), (500, 350), (24, 40, 13), -1)
img = cv2.circle(img, (800, 800), 500, (70, 0, 36), -1)
img = cv2.putText(img, 'lesson 3 - shapes using OPEN CV', (200, 1200), font, 4, (255, 255, 255), 10)

resize = cv2.resize(img, (500, 500))
cv2.imshow("shapes", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()