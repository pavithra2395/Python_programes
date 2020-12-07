
#!/usr/local/bin/python3
from PIL import Image
import numpy as np
import cv2

# Open the input image as numpy array
npImage=np.array(Image.open("D:\\puppies\\misalignment\\MR192.jpg"))
# Open the mask image as numpy array
#npMask=np.array(Image.open("mask2.jpg").convert("RGB"))
# _, mask = cv2.threshold(rect_img, thresh=90, maxval=180, type=cv2.THRESH_BINARY)  
# mask3 = cv2.cvtColor(rect_img, cv2.COLOR_GRAY2BGR)
# Make a binary array identifying where the mask is black
cond = npMask<128

# Select image or mask according to condition array
pixels=np.where(cond, npImage, npMask)

# Save resulting image
result=Image.fromarray(pixels)
result.save('result.png')

# img[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = mask3
#     #cv2.imshow("binary mask", mask3)
# cv2.imshow("3 channel mask", mask3)