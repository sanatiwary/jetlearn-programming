# import cv2
# import numpy as np

# # img = cv2.imread('l3/images/planets.jpeg', 1)
# img = cv2.imread('l3/images/cookie.jpeg', 1)
# output = img.copy()

# grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# grey = cv2.medianBlur(grey, 5)

# circles = cv2.HoughCircles(grey, cv2.HOUGH_GRADIENT, 1, 50, param1 = 50, param2 = 30, minRadius = 60, maxRadius = 500)
# detectedCircles = np.uint16(np.around(circles))

# for x, y, r in detectedCircles[0, :]:
#     cv2.circle(output, (x, y), r, (255, 255, 255), 4)
#     cv2.circle(output, (x, y), 2, (255, 255, 255), 4)

# cv2.imshow('output image', output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

img=cv2.imread('l3/images/planets.jpeg',1)
output=img.copy()

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,5)

circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,500,
param1=50,param2=30,minRadius=0,maxRadius=40)

detected_circles=np.uint16(np.around(circles))

for x,y,r in detected_circles[0,:]:
    cv2.circle(output,(x,y),r,(0,255,0),4)
    cv2.circle(output,(x,y),2,(0,255,255),4)

cv2.imshow('output image',output)

cv2.waitKey(0)
cv2.destroyAllWindows()