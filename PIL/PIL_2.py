#coding=utf-8
from PIL import Image
"""
图像过滤处理
Image类，getdata,pixel方法获得，所得到的像素都是0-255之间的整数
按照RGB排列，非BGR排列
整体是作为一个一个元祖
getdata返回的是一个能够访问当前图片所有像素点的迭代器
用buffer列表，通过.append()方式，可以将以255，进行取反
putdata将原本的image类对象img保存像素值替换
"""
def pic_filter():
    img = Image.open("/home/oubingkun/图片/pil_img/lena.jpg")
    buffer=[]
    for pixel in img.getdata():
        buffer.append((
            255 - pixel[0],
            255 - pixel[1],
            255 - pixel[2],)
        )
    """
    取数据putdata不再循环体，直接由之前的buffer就存储了
    """
    img.putdata(buffer)
    img.save("/home/oubingkun/图片/pil_img/pic_filter.jpg")

if __name__ == '__main__':
    pic_filter()
