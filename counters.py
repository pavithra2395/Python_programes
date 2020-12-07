import cv2

import numpy as np

img = cv2.imread("D:\\puppies\\misalignment\\MR192.jpg")


contrast_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)

cv2.imshow('Original Image', img)

cv2.imshow('Contrast Image', contrast_img)

cv2.waitKey(0)