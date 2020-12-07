import numpy
import cv2

img = cv2.imread('D:\\puppies\\misalignment\\New folder\\MR192.jpg')

# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# out = cv2.VideoWriter('output.MOV',fourcc, 20.0, (640,480))
while(1):

    # read the frames
    _,frame = img.read()

    #Rect
    rec1 = cv2.rectangle(frame, (314, 211), (975, 557), (0, 0, 0), -1)
    #rec2 = cv2.rectangle(frame, (8, 342), (634, 476), (0, 0, 0), -1)
    #A line
    #cv2.line(frame, (500, 400), (640, 480),(0,255,0), 3)


    #cv2.putText(frame, "test!",(105, 105),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(225,0,0))
    out.write(frame)
    #if key pressed is 'Esc', exit the loop
    cv2.imshow('frame',frame)
    #cv2.imshow('rectangle',rec)
    if cv2.waitKey(33)== 27:
        break
out.release()

cv2.destroyAllWindows()