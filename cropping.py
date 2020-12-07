import numpy as np
import cv2
import glob
import os 


path = "D:\\puppies\\videos\\videos\\"
out = "D:\\puppies\\videos\\crop\\"

files = os.listdir(path)


print(files)
for file in files:
    file = path + file

    print(file)
    
    img = cv2.imread(file)

    y=0
    x=0
    h=576
    w=274
    crop = img[ 761:2105, 581:1181]
    crop = image[745:2041, 2329:2989]
    cv2.imwrite(out+file,file)

    cv2.imshow('Image', crop)

    cv2.waitKey(0)


