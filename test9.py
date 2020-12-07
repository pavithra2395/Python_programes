import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event, X, Y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(X,'.', Y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(X) + '.'+ str(Y)
        cv2. putText(img, strXY, (X,Y), font, 1, (0, 0, 255), 2)
        cv2.imshow('image', img)

img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
