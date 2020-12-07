import cv2

img = cv2.imread('D:\puppies\picc.jpg')
height, width, _ = img.shape

#cutting image
roi = img[0: height, 120: width]

cv2.imshow("roi", roi)
cv2.imshow("IMG", img)
cv2.waitKey(0)
cv2.destroyAllWindows()