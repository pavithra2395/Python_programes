import numpy as np
import cv2

img = cv2.imread('C:\\Users\\lenovo\\Desktop\\puppies\\puppy1.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)
font = cv2.FONT_ITALIC
img = cv2.putText(img, 'OpenCv', (210, 210), font, 1, (255, 0, 255), 2, cv2.LINE_8)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()