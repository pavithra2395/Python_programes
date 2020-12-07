import cv2 as cv

vid = cv.VideoCapture('D:\\puppies\\misalignment\\batch_84_1.jpg', cv.IMREAD_COLOR)
im_gray = cv.cvtColor(im_color, cv.COLOR_BGR2GRAY)

_, mask = cv.threshold(im_gray, thresh=80, maxval=150, type=cv.THRESH_BINARY)
im_thresh_gray = cv.bitwise_and(im_gray, mask)

mask3 = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)

im_thresh_color = cv.bitwise_and(im_color, mask3)

cv.imshow("original image", im_color)
cv.imshow("binary mask", mask)
cv.imshow("3 channel mask", mask3)
cv.imshow("im_thresh_gray", im_thresh_gray)
cv.imshow("im_thresh_color", im_thresh_color)
cv.waitKey(0)