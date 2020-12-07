import cv2 
from matplotlib.patches import Rectangle

img = cv2.imread('D:\\puppies\\misalignment\\image1 (9).jpg')
height,width,depth = img.shape
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#cv2.rectangle(img,(width/2,height/2),200,1,thickness=-1)

masked_data = cv2.bitwise_and(img, img, mask=rectangle)

cv2.imshow("masked_data", masked_data)
cv2.waitKey(0)