import cv2
import matplotlib.pyplot as plt

def main():

    path = "D:\\puppies\\image1 (17).jpg"

    imgpath1 = path + "gray21.512.tiff"

    img = cv2.imread(imgpath1, 1)

    plt.imshow(img)
    plt.title('Original Image')
    plt.show()

if __name__ == "__main__":
    main()