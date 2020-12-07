import numpy as np
import cv2

img = cv2.imread('D:\puppies\K75T60.jpg')
#img = np.zeros((512, 512, 3), np.uint8)
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event, X, Y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[Y, X, 0]
        green = img[Y, X, 1]
        red = img[Y, X, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + '.'+ str(green)+ '.'+ str(red)
        cv2. putText(img, strBGR, (X,Y), font, 1, (255, 0, 255), 2)
        cv2.imshow('image', img)


cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()