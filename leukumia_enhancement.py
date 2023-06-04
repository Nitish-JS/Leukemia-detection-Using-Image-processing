import numpy as np
import cv2
import matplotlib.pyplot as plt


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


def contrastStretching(img, r1, r2, a, b, c):
    s1 = a*r1
    s2 = b*(r2-r1)+s1
    imgC = np.zeros((256, 256), dtype=np.int32)
    for i in range(0, 256):
        for j in range(0, 256):
            r = img[i, j]
            if r < r1:
                imgC[i, j] = a*r
            elif r > r1 and r < r2:
                imgC[i, j] = b*(r-r1) + s1
            else:
                imgC[i, j] = c*(r-r2) + s2

    imgC = imgC.astype(np.uint8)
    return imgC

def histeq(img):
    img=cv2.equalizeHist(img)
    return img
def enhancement(img1, img2):
    imgadd = cv2.add(img1, img2)
    imgsub = cv2.subtract(img1, img2)
    imgfinal = cv2.add(imgadd, imgsub)
    return imgfinal


img = cv2.imread('normal.jpg')
img = cv2.resize(img, (256, 256))
greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayscale1.jpg', greyImg)
contrast = contrastStretching(greyImg,20 , 150, 0.1, 1, 2)
cv2.imwrite('contrastStrechted1.jpg', contrast)
histo = histeq(contrast)
cv2.imwrite("histogramEqu1.jpg", histo)
median_filtered_histo = median_filter(histo, 3)  # using a 3x3 kernel
cv2.imwrite('median_filtered_histo1.jpg', median_filtered_histo)
median_filtered_contrast = median_filter(contrast, 3)  # using a 3x3 kernel
cv2.imwrite('median_filtered_contrast1.jpg', median_filtered_contrast)
imgEnhanced = enhancement(median_filtered_histo, median_filtered_contrast)
cv2.imwrite("Enhanced1.jpg",imgEnhanced)
