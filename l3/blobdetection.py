# import cv2
# import numpy as np
# params = cv2.SimpleBlobDetector_Params()
# img = cv2.imread('l3/images/ellipses.jpeg', 0)

# params.filterByArea = True
# params.minArea = 50

# params.filterByCircularity = True
# params.minCircularity = 0.8

# params.filterByConvexity = True
# params.minConvexity = 0.2

# params.filterByInertia = True
# params.minInertiaRatio = 0.5

# detector = cv2.SimpleBlobDetector_create(params)
# keypoints = detector.detect(img)

# blank = np.zeros((1, 1))
# blobs = (img, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# cv2.imshow('detected blobs', blobs)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

img=cv2.imread('l3/images/ellipses.jpeg',0)

params=cv2.SimpleBlobDetector_Params()
params.filterByArea=True
params.minArea=50

params.filterByCircularity=True
params.minCircularity=0.8

params.filterByConvexity=True
params.minConvexity=0.2

params.filterByInertia=True
params.minInertiaRatio=0.5

detector=cv2.SimpleBlobDetector_create(params)
keypoints=detector.detect(img)

blank=np.zeros((1,1))
blobs=cv2.drawKeypoints(img,keypoints,blank,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('detected blobs:',blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()