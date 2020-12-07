import numpy as np
import cv2 

img = cv2.imread('D:\puppies\\puppy1.jpg', 1)

print (img.shape)
print(img.size)
print(img.dtype)
img1 = cv2.resize(img, (640, 480))
b,g,r = cv2.split(img1)
#print(b,g,r)


cv2.imshow('imge1', b)
cv2.imshow('imge2', g)
cv2.imshow('imge3', r)
cv2.waitKey(0)
cv2.destroyAllWindows()