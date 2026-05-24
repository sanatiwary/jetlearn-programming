import cv2

img = cv2.imread("images/cat.jpg", -1)
cv2.imshow("cat", img)

img = cv2.imread("images/cat.jpg", 0)
cv2.imshow("cat1", img)

k = cv2.waitKey(0)
if k == 27:
    location = "/Users/sana/Desktop/vsc/jetlearn/open cv/l1/images/catcopy.jpg"
    cv2.imwrite(location, img)
elif k == ord('s'):
    cv2.destroyAllWindows()