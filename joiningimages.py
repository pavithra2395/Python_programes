import cv2
import numpy as np
imgpath = "D:\\puppies\\image1 (16).jpg"
cv2.imread(imgpath)
#print(img)
imgHor = np.hstack((imgpath,imgpath))
#imgVer = np.vstack((img,img))

cv2.imshow = ("Horizontal",imgHor)
#cv2.imshow = ("Vertical",imgVer)
cv2.waitKey(0)
cv2.destroyAllWindows()