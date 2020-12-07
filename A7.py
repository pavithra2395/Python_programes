import cv2
import numpy as np

def main():
    
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False


    while ret:

        ret; frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow("Original Webcam Feed", frame)
    if cv2.waitKey(1) == 27: #exit on ESC
        break

    cv2.destroyAllWindows()
    cap.release()
if __name__ == "__main__":
    main()