import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math

dir_img = 'F:/GitHub/atx-test/pycuda/test_imgs/'
image = mpimg.imread(dir_img + 'solidWhiteRight.jpg') #RGB
print('this image:',type(image),'with dimension:',image.shape)
plt.imshow(image)

img = 'F:/GitHub/atx-test/pycuda/test_imgs/solidWhiteRight.jpg'

def do_grayscale(img):
    '''
    灰度转换，返回只有一个颜色的单通道图像
    '''
    return cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

def canny(img,low_threashold,high_threshold):
    return cv2.Canny(img,low_threashold,high_threshold)

def do_gaussian_blur(img,kernel_size):
    return cv2.GaussianBlur(kernel_size,(kernel_size,0))


