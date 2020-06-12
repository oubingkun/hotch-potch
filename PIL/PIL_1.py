import os
from PIL import Image,ImageEnhance
sources = os.path.join("C:/Users/Administrator/Desktop/tem2/","lena.jpg")
source_gif = os.path.join("C:/Users/Administrator/Desktop/tem2/","two.gif")
dst = os.path.dirname("C:/Users/Administrator/Desktop/tem2/")

im  = Image.open(sources)
print(im.format,im.size,im.mode)


"""
几何变换
"""
output = im.rotate(45)
output.show()
output = im.transpose(Image.FLIP_LEFT_RIGHT)
output = im.transpose(Image.FLIP_TOP_BOTTOM)
output = im.transpose(Image.ROTATE_90)
output = im.transpose(Image.ROTATE_180)
output = im.transpose(Image.ROTATE_270)
output.show()
output.save(dst + "dst.png")

"""
resize Image，对图片缩放
"""
re_size = (128,128)
im.thumbnail(re_size)
print(im.size)
im.show()

"""
图像增强
"""
enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contract")

"""
图像序列
"""
im_gif = Image.open(source_gif)
im_gif.seek(1)
try:
    while(1):
        im_gif.seek(im.tell() + 1)

except EOFError:
    pass
im_gif.show()


