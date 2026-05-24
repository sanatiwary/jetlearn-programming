import cv2

img = cv2.imread("images/cat.jpg", 1)

cv2.rectangle(img, (40, 40), (100, 100), (255, 255, 255), 2)
cv2.line(img, (40, 40), (70, 20), (255, 255, 255), 2)
cv2.line(img, (100, 40), (70, 20), (255, 255, 255), 2)

cv2.imshow("cat", img)

cv2.waitKey(0)
cv2.destroyAllWindows()