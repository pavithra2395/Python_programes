import numpy as np
import cv2

img = cv2.imread('D:\\puppies\\puppy1.jpg')

img = cv2.line(img, (0,0), (255,255), (128,255,0), 5)
img = cv2.arrowedLine(img, (0,0), (255,255), (128,255,0), 5)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()