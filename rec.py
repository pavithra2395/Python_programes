# Python3 program to draw rectangle 
# shape on solid image 
import numpy as np 
import cv2 

img = cv2.imread('D:\\puppies\\misalignment\\MR192.jpg')
# Creating a black image with 3 
# channels RGB and unsigned int datatype 
#img = np.zeros((400, 400, 3), dtype = "uint8") 
  
# Creating rectangle 
cv2.rectangle(img, (992, 992), (564, 600), (0, 255, 0), 5) 

cv2.imshow('Image', img)  
#cv2.imshow('dark', img) 
  
# Allows us to see image 
# untill closed forcefully 
cv2.waitKey(0) 
cv2.destroyAllWindows() 