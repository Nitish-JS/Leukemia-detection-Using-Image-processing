import numpy as np
import cv2
import matplotlib.pyplot as plt

def thresholding(img, t):
    for i in range(0, 256):
        for j in range(0, 256):
            img[img > t] = 255
            img[img != 255] = 0
    return img

def dilation(img, mask):
    img = img.astype(np.float16)
    dilimg = np.zeros((256, 256), dtype=np.float16)
    for i in range(1, 255):
        for j in range(1, 255):
            imgtemp = img[i-1:i+2, j-1:j+2]
            res = np.multiply(imgtemp, mask)
            dilimg[i, j] = np.amax(res)
    dilimg = dilimg.astype(np.uint8)
    return dilimg

def erosion(img, mask):
    img = img.astype(np.float16)
    eroimg = np.zeros((256, 256), dtype=np.float16)
    for i in range(1, 255):
        for j in range(1, 255):
            imgtemp = img[i-1:i+2, j-1:j+2]
            res = []
            for k in range(0, 3):
                for m in range(0, 3):
                    if mask[k][m] == 1:
                        a = imgtemp[k, m]
                        res.append(a)
            eroimg[i, j] = np.amin(res)
    eroimg = eroimg.astype(np.uint8)
    return eroimg


def edgeDetection(img):
    imgS = img.astype(np.float16)
    sobx = [[-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]]
    sobx = np.array(sobx, np.float16)
    soby = [[-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]]
    soby = np.array(soby, np.float16)
    for i in range(1, 254):
        for j in range(1, 254):
            imgtemp = img[i-1:i+2, j-1:j+2]
            x = np.sum(np.multiply(sobx, imgtemp))
            y = np.sum(np.multiply(soby, imgtemp))
            pixvalue = np.sqrt(x**2 + y**2)
            imgS[i, j] = pixvalue
    imgS = imgS.astype(np.uint8)
    return imgS




def median_filter(img, kernel_size):
    padding = int((kernel_size - 1) / 2)
    img_pad = np.pad(
        img, ((padding, padding), (padding, padding)), mode='constant')
    filtered_img = np.zeros_like(img)

    for i in range(padding, img.shape[0] + padding):
        for j in range(padding, img.shape[1] + padding):
            patch = img_pad[i-padding:i+padding +
                            1, j-padding:j+padding+1].flatten()
            filtered_img[i-padding][j-padding] = np.median(patch)

    return filtered_img

img = cv2.imread('grayscale.jpg')
enhancedImg = cv2.imread('Enhanced.jpg')
Thresholded = thresholding(enhancedImg, 110)
cv2.imwrite('Thresholded.jpg', Thresholded)
mask = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
erodedImg = erosion(Thresholded, mask)
openedImg = dilation(erodedImg, mask)
cv2.imwrite("Opened.jpg",openedImg)
median_filtered_open = median_filter(openedImg, 10)
cv2.imwrite("FilteredOpen.jpg",median_filtered_open)
edgeDetectedImg=edgeDetection(median_filtered_open)
cv2.imwrite('edgeDetected1.jpg',edgeDetectedImg)
