import numpy as np
import cv2 as cv

img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

while(1):
     cv.imshow('image', img)
     k = cv.waitKey(1) & oxFF
     if k == 27:
        break
cv.destroyAllWindows()
 