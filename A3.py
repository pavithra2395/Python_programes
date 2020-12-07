import cv2

def main():

    imgpath = "D:\\puppies\\image1 (17).jpg"
    img = cv2.imread(imgpath)

    cv2.namedWindow('Puppy', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Puppy', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows('Puppy')

if __name__ == "__main__":
    main()