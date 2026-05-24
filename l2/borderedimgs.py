import cv2

img = cv2.imread('l2/images/cat.jpg', 1)
bimg = cv2.copyMakeBorder(img, 20, 50, 45, 10, cv2.BORDER_CONSTANT, value = (56, 120, 78))
rimg = cv2.copyMakeBorder(img, 50, 50, 10, 10, cv2.BORDER_REFLECT)
rimg2 = cv2.copyMakeBorder(img, 100, 230, 100, 75, cv2.BORDER_REFLECT101)


cv2.imshow('og img', img)
cv2.imshow('bordered img', bimg)
cv2.imshow('reflective img', rimg)
cv2.imshow('reflective img 2', rimg2)


cv2.waitKey(0)
cv2.destroyAllWindows()