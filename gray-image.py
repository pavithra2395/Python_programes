import matplotlib, cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\\puppies\\misalinment\\batch_93_189.jpg', 0) 
img = np.array(img, dtype=np.uint8)
gray = (cv2.cvtColor(img, cv2.COLOR_GRAY2RGB))
cv2.imshow(gray)
cv2.waitKey() 
  
cv2.destroyAllWindows()