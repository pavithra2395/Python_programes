import cv2
import numpy as np

# Read the image and transform to HSV colorspace.
img = cv2.imread('D:\\puppies\\template_matching_based_classifier\\temp.jpg')
print(img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Extract the red text.
lower_red = np.array([0,150,50])
upper_red = np.array([40,255,255])
mask_red = cv2.inRange(hsv, lower_red, upper_red)

# Search for contours on the mask.
contours, hierarchy = cv2.findContours(mask_red,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# Create a new mask for further processing.
mask = np.ones(img.shape, np.uint8)*255

# Draw contours on the mask with size and ratio of borders for threshold (to remove other noises from the image).
for cnt in contours:
    size = cv2.contourArea(cnt)
    x,y,w,h = cv2.boundingRect(cnt)
    if 10000 > size > 50 and w*2.5 > h:
        cv2.drawContours(mask, [cnt], -1, (0,0,0), -1)

# Connect neighbour contours and select the biggest one (text).
kernel = np.ones((50,50),np.uint8)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
gray_op = cv2.cvtColor(opening, cv2.COLOR_BGR2GRAY)
_, threshold_op = cv2.threshold(gray_op, 150, 255, cv2.THRESH_BINARY_INV)
contours_op, hierarchy_op = cv2.findContours(threshold_op, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt = max(contours_op, key=cv2.contourArea)

# Create rotated rectangle to get the 4 points of the rectangle.
rect = cv2.contourArea(cnt)

# Create bounding and calculate the "lenght" of the text.
box = cv2.boxPoints(rect)
a, b, c, d = box = np.int0(box)
bound =[]
bound.append(a)
bound.append(b)
bound.append(c)
bound.append(d)
bound = np.array(bound)
(x1, y1) = (bound[:,0].min(), bound[:,1].min())
(x2, y2) = (bound[:,0].max(), bound[:,1].max())

# Draw the rectangle.
cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),1)

# Identify the room status.   
if x2 - x1 > 200:
    print('unoccupied')
else:
    print('occupied')

# Display the result
cv2.imshow('img', img)