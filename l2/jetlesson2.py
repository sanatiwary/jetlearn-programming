# # erosion
# import cv2
# import numpy as np

# img = cv2.imread('images/cat.jpg', 1)
# kernel = np.ones((5, 5), np.uint8)
# erosion = cv2.erode(img, kernel)
# rsize = cv2.resize(erosion, (400, 400))

# cv2.imshow('erroded img', rsize)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# # resizing
# import cv2

# img = cv2.imread('images/road.jpg', 1)
# cv2.imshow('og img', img)

# rsize = cv2.resize(img, (100, 100))
# cv2.imshow('resized img', rsize)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# subtraction
import cv2

image1 = cv2.imread('images/input1.jpg', 1)
image2 = cv2.imread('images/input2.jpg', 1)

subtraction = cv2.subtract(image1, image2)

cv2.imshow("subtraction of imgs", subtraction)
cv2.waitKey(0)
cv2.destroyAllWindows()



# import cv2

# image1 = cv2.imread('images/input1.jpg', 1)
# image2 = cv2.imread('images/input2.jpg', 1)

# result = cv2.addWeighted(image1, 0.6, image2, 0.4, 0)
# resultb = cv2.addWeighted(image1, 0.9, image2, 0.9, 0)

# cv2.imshow('addition of imgs', result)
# cv2.imshow('addition of imgs w/ brightness', resultb)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# subtraction of images
