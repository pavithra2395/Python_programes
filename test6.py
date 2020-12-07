import numpy as np
import cv2

img = cv2.imread('D:\puppies\\puppy1.jpg', 1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Puppy', (10, 500), font, 6, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()