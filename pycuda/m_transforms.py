#coding=utf-8
"""
形态转换，基于图像外形的简单操作，只作用于二进制图像，需要两个参数
:params ,原图，结构化元素（strutring element）或者Kernel
形态操作：
Erosion腐蚀
Dilation膨胀
Opening
Closing
Gradient

matplotlib是以RGB存儲
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

def erosion_transform():
    """
    腐蚀前景物体的边界，kernel以2D卷积遍历图像，原图像中，只有在kernel中所有像素为1的
    其像素为1，否则将为0（eroded）
      画图理解，其实结果就是前景物体的里临近边界的像素都抛弃了（变为0了）。
      根据kernel大小的不同，腐蚀的效果还不一样。这个方法还可以运用在移除白色小噪音、
      分离两个相连的物体上。
    :return:
    """
    img = cv2.imread("F:/GitHub/atx-test/pycuda/test_imgs/dragonwukong.jpg")
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(img,kernel,iterations=1)#interations表示腐蚀次数,次数越多，边缘缺失越严重

    plt.subplot(121),plt.imshow(img),plt.title("original")
    plt.subplot(122),plt.imshow(erosion),plt.title("erosion")
    plt.show()

def dilation_transform():
    """
    和腐蝕相反，在kernel裏的像素有一個為1，全部為0才為0
    前景物體增胖
    在噪音移除这个步骤中，可以先通过erosion移除噪音，
    然后通过dilation来补足缺失的边界。
    :return:
    """
    img = cv2.imread("F:/GitHub/atx-test/pycuda/test_imgs/dragonwukong.jpg")
    kernel = np.ones((3,3),np.uint8)
    erosion = cv2.dilate(img,kernel,iterations=1)

    plt.subplot(121),plt.imshow(img),plt.title("original")
    plt.subplot(122),plt.imshow(erosion),plt.title("erosion")
    plt.show()

#retangular kernel
def rectangular():
    """
    :return:
    """
    array = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    print(array)


#eliptical kernel
def elliptical():
    """
    :return:
    """
    array = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    print(array)

#cross-shaped kernel
def cross_shape():
    array = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
    print(array)


#Opening
def opening():
    img = cv2.imread("F:/GitHub/atx-test/pycuda/test_imgs/man01.jpg")
    kernel = np.ones((7,7),np.uint8)
    opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

    plt.subplot(121),plt.imshow(img),plt.title("original")
    plt.subplot(122),plt.imshow(opening),plt.title("opening")
    plt.show()

#Closing
def closing():
    img = cv2.imread("F:/GitHub/atx-test/pycuda/test_imgs/man01.jpg")
    kernel = np.ones((3,3),np.uint8)
    closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

    plt.subplot(121),plt.imshow(img),plt.title("original")
    plt.subplot(122),plt.imshow(closing),plt.title("closing")
    plt.show()

#morphlogical gradient
def gradient_transform():
    """
    全0为0，全1为0,kernel出现0.1的为1
    :return:
    """
    img = cv2.imread("F:/GitHub/atx-test/pycuda/test_imgs/man01.jpg")
    kernel = np.ones((3,3),np.uint8)
    gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

    plt.subplot(121), plt.imshow(img), plt.title("original")
    plt.subplot(122), plt.imshow(gradient), plt.title("gradient")
    plt.show()

if __name__ == '__main__':
    erosion_transform()
    dilation_transform()
    rectangular()
    elliptical()
    cross_shape()
    opening()
    closing()
    gradient_transform()
