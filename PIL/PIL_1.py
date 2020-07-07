# coding=utf-8
import os
from PIL import Image, ImageEnhance

sources_uinx = os.path.join("/home/oubingkun/图片/pil_img/", "lena.jpg")
sources_ugif = os.path.join("/home/oubingkun/图片/pil_img/", "qxz.gif")
# dst_u= os.path.dirname("/home/oubingkun/图片/pil_img/")

sources_windows = os.path.join("C:/Users/Administrator/Desktop/tem2/", "lena.jpg")
sources_wgif = os.path.join("C:/Users/Administrator/Desktop/tem2/", "two.gif")
dst = os.path.dirname("C:/Users/Administrator/Desktop/tem2/")

im = Image.open(sources_uinx)

"""
图像增强
"""
enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contract")
