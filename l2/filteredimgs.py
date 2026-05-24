import cv2

img = cv2.imread('l2/images/cat.jpg', 1);
cv2.imshow('og img', img)

gaussian = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow('gaussian img', gaussian)

median = cv2.medianBlur(img, 5)
cv2.imshow('median blur', median)

bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('bilateral filter', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()