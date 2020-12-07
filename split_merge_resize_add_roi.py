import numpy as np
import cv2

img = cv2.imread("D:\\puppies\\image1 (1).jpg")

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()