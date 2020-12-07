import cv2
import os

vid = cv2.VideoCapture("D:\\puppies\\videos\\videos\\video10\\video10.mp4")

if not os.path.exists('images'):
    os.makedirs('videos\\videos\\video10')

index = 0
while(True):
    ret, frame = vid.read()
    if not ret: 
        break
    name = "D:\\puppies\\videos\\videos\\video10\\"+ str(index) + '.jpg'
    if index%3==0:
        cv2.imwrite(name, frame)
    index += 1