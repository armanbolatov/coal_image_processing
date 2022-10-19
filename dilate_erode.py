import cv2
import numpy as np


def dilate_erode(image, kernel_size):
    '''
    Runs two morphological operations on the given image 
    (dilation and erosion) with the given kernel size
    '''
    kernel = np.ones((kernel_size, kernel_size), 'uint8')
    erode = cv2.erode(image, kernel, 1)
    dilate = cv2.dilate(erode, kernel, 1)
    return dilate


if __name__== '__main__':

    for file_name in range(1, 11):
        for type in ["after", "before"]:
            path = f"data/{file_name}/{type}/"
            manual = cv2.imread(path + "manual.bmp", 1)
            manual = cv2.cvtColor(manual, cv2.COLOR_BGR2GRAY)
            transformed = dilate_erode(manual, kernel_size=3)
            cv2.imwrite(path + "transformed.bmp", transformed)