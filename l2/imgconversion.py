import cv2

img = cv2.imread('l2/images/cat.jpg', 1)
cv2.imshow('og img', img)

# grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('grey img', grey)

# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv image', hsv)

luv = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
cv2.imshow('luv image', luv)

hsvfull = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
cv2.imshow('hsv full image', hsvfull)

bgr = cv2.cvtColor(img, cv2.COLOR_BGR2BGR555)
cv2.imshow('bgr555 image', bgr)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('lab image', lab)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('rgb image', rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()