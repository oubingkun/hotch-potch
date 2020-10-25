#coding=utf-8
"""
image blurring(image smoothing)
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#均值滤波
def average_filter():
    """
    均值滤波
    均值滤波器来卷积图像，通过取得所有图像的像素再kernal area的平均值，
    并且用该平均值来取代central element
    :param cv2.blur()
    :param cv2.boxfilter()
    指定一个5x5均值滤波器内核
    """
    img = cv2.imread("f:/github/atx-test/pycuda/test_imgs/solidwhiteright.jpg")
    blur = cv2.blur(img,(5,5))
    plt.subplot(121),plt.imshow(img),plt.title("orignal")
    plt.subplot(122),plt.imshow(blur),plt.title("blurred")
    plt.show()

#高斯滤波
def gaussian_filter():
    """
    移除gaussian noise
    数字图像中高斯噪声主要来源是在采集过程中产生的，由于光照不足和高温造成的传感器噪声，
    以及传输，电子电路噪声，在数字图像处理中，可以使用空间滤波器来减少高斯噪声，但在平滑图像中，
    不良的结果可能会导致细尺度图像边缘和细节的模糊，因为它们也对应于阻塞的高频。
    传统的消除噪声的空间滤波技术包括：平均（卷积）滤波、中值滤波和高斯平滑。
    :param gaussian kernel
    """
    img  = cv2.imread("f:/github/atx-test/pycuda/test_imgs/solidwhiteright.jpg")
    blur = cv2.GaussianBlur(img,(5,5),0)
    plt.subplot(121),plt.imshow(img),plt.title("Original")
    plt.subplot(122),plt.imshow(blur),plt.title("Gaussianed")
    plt.show()

#中值滤波
def median_filter():
    """
    cv2.medianBlur()替代所有像素值的中值，并且在central pixel中用中值去替代它
    中值对处理salt-and pepper noise非常有效，区别Gaussian and box filters的是
    中值滤波器中替代图像中值可能是原图的像素值，kernel size必须是正奇数
    :return:
    """
    img = cv2.imread("f:/github/atx-test/pycuda/test_imgs/solidwhiteright.jpg")
    blur = cv2.medianBlur(img,5)#kernel不是矩阵，是单纯数值
    plt.subplot(121),plt.imshow(img),plt.title("Original")
    plt.subplot(122),plt.imshow(blur),plt.title("medianBlur")
    plt.show()

#双边滤波
def bilateral_filter():
    img = cv2.imread("f:/github/atx-test/pycuda/test_imgs/solidwhiteright.jpg")
    blur = cv2.bilateralFilter(img,9,75,75)
    plt.subplot(121),plt.imshow(img),plt.title("Original")
    plt.subplot(122),plt.imshow(blur),plt.title("bilateral blured")
    plt.show()

if __name__ == '__main__':
    average_filter()
    gaussian_filter()
    median_filter()
    bilateral_filter()


