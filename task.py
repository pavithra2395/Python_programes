import cv2
import numpy as np

image = cv2.imread('C:\\Users\\lenovo\\Desktop\\puppies\\K75T60.jpg', -1)
print(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray)
cv2.resize(gray, resizee, Size(), 0.5, 0.5, interpolation=cv2.INTER_LINEAR);

resize = cv2.imwrite("C:\\Users\\lenovo\\Desktop\\puppies\\K75T60.jpg", resizedImage);
bwImage = imread("C:\\Users\\lenovo\\Desktop\\puppies\\K75T60.jpg");
threshold(bwImage, bwImage, 120, 255, CV_THRESH_BINARY);
imwrite("C:\\Users\\lenovo\\Desktop\\puppies\\K75T60.jpg", bwImage);
cv2.imshow("Original", rgbimage);
cv2.imshow("Resized", resizedimage);
cv2.imshow("Resized Binary", bwimage);
cv2.imshow("Image", image)
cv2.imshow('Gray image', gray)

cv2.waitKey()
cv2.destroyAllWindows()

