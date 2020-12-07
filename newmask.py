import cv2

import numpy as np

img = cv2.imread('D:\\puppies\\misalignment\\batch_84_1.jpg')

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray_img = cv2.medianBlur(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 3)

circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=50, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))

masking=np.full((img1.shape[0], img1.shape[1]),0,dtype=np.uint8)

for j in circles[0, :]:

    cv2.circle(masking, (j[0], j[1]), j[2], (255, 255, 255), -1)

    final_img = cv2.bitwise_or(img1, img1, masking=masking)