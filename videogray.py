import cv2 
  
# reading the vedio 
source = cv2.VideoCapture('D:\\puppies\\misalignment\\MR192.mp4')
upper_left = (0, 0)
bottom_right = (600, 600) 

# running the loop 
while True: 
  
    # extracting the frames 
    ret, img = source.read() 
      
    # converting to gray-scale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.rectangle(img, upper_left, bottom_right, (100, 50, 200), 5)
    rect_img = img[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]
     
    
    #(thresh, blackAndWhiteImage) = cv2.threshold(gray, 100, 150, cv2.THRESH_BINARY)
    _, mask = cv2.threshold(rect_img, thresh=90, maxval=180, type=cv2.THRESH_BINARY)  
    #mask3 = cv2.cvtColor(rect_img, cv2.COLOR_GRAY2BGR)
    # displaying the video 
    #cv2.imshow("Live", gray) 
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    
    #Replacing the sketched image on Region of Interest
    img[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = mask
    #cv2.imshow("binary mask", mask)
    #cv2.imshow("3 channel mask", mask3)
    #cv2.imshow('Black white image', blackAndWhiteImage)
    #cv2.imshow('Original image',source)
    cv2.imshow('Gray image', gray)
    # exiting the loop 
    key = cv2.waitKey(1) 
    if key == ord("q"): 
        break
      
# closing the window 
cv2.destroyAllWindows() 
source.release()