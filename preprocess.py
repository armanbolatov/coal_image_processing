import cv2
import numpy as np
from matplotlib import pyplot as plt


def crop_center(image):
    '''
    Given a binary image, deletes everything that lies
    outside of the circle inscribed in the image frame
    '''
    center = image.shape[0] // 2
    radius = int(center * 0.99)
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.circle(mask, (center, center), radius, 255, -1)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result


def clear_dots(image, min_area):
    '''
    Create connected components of a binary image and
    delete those which area is less than min_area
    '''
    nlabels, labels, stats, _ = \
        cv2.connectedComponentsWithStats(
            image=image,
            labels=None,
            stats=None,
            centroids=None,
            connectivity=8,
            ltype=cv2.CV_32S
        )
    result = np.zeros((labels.shape), np.uint8)
    areas = stats[:, cv2.CC_STAT_AREA]
    for i in range(1, nlabels):        
        if areas[i] >= min_area:
            result[labels == i] = 255
    return result


def process_image(image, size, alpha, C, min_area):
    '''
    Resizes the image to (size * size), and sequentially
    applies filters to the image with given hyperparameters
    '''
    resized = cv2.resize(image, (size, size))
    grayscaled = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
    bilatered = cv2.bilateralFilter(
        src=grayscaled,
        d=2,
        sigmaColor=75,
        sigmaSpace=75
    )
    brightened = cv2.convertScaleAbs(
        src=bilatered,
        alpha=alpha,
        beta=1
    )
    thresholded = cv2.adaptiveThreshold(
        src=brightened,
        maxValue=255,
	    adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
        thresholdType=cv2.THRESH_BINARY_INV,
        blockSize=25,
        C=C,
    )
    cropped = crop_center(thresholded)
    cleared = clear_dots(cropped, min_area)
    negated = cv2.bitwise_not(cleared)
    return negated
    

if __name__== '__main__':

    SIZE = 480

    when = "before"
    file_name = 10
    path = f"data/{file_name}/{when}/"
    original = cv2.imread(path + "original.jpg", 1)
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

    processed = process_image(
        image=original,
        size=SIZE,  
        alpha=1,
        C=8,
        min_area=10,
    ) 
    
    cv2.imwrite(path + "processed.bmp", processed)

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.subplot(1, 2, 2)
    plt.imshow(processed, cmap='gray')
    plt.show()