import cv2

def main():

    imgpath = "D:\\puppies\\image1 (17).jpg"
    img = cv2.imread(imgpath, 1)
    
    print(type(img))

    print(img.dtype)
    print(img.shape)
    print(img.ndim)
    print(img.size)

    # outpath = "D:\\puppies\\out\\image1 (17).jpg"
    # cv2.namedWindow('Puppy', cv2.WINDOW_AUTOSIZE)
    # cv2.imshow('Puppy', img)
    # cv2.imwrite(outpath, img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 