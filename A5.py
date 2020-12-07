import cv2
import numpy as np

def main():

    img1 = np.zeros((512, 512, 3), np.uint8)
    cv2.line(img1, (0, 99), (99, 0), (255, 0, 0), 2)
    cv2.rectangle(img1, (40, 60), (80, 70), (0, 255, 0), 1)

    cv2.imshow('Image', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()