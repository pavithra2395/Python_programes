import numpy as np
import cv2

img = cv2.imread('D:\puppies\\puppy1.jpg', 1)

img = cv2.rectangle(img, (384,0), (510,128), (128,255,0), 5)
img = cv2.circle(img, (445, 60), 63, (0, 0, 255), -1)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()