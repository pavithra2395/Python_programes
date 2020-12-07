import cv2

img = cv2.imread('D:\\puppies\\misalinment\\batch_93_189.jpg', 0)   
  
cv2.imshow('Grayscale', img) 
cv2.waitKey() 
  
cv2.destroyAllWindows() 