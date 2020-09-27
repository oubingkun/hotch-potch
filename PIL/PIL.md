* 几何变换
>Rotate
>m.rotate(angle) ⇒ image
im.rotate(angle,filter=NEAREST, expand=0) ⇒ image
>返回一个按照给定角度的顺时针围绕图像中心旋转后的图像拷贝。
>变量fliter是NEAREST、BILINEAR,BICUBIC
>如果省略该变量，或者图像模式为1或者P，则默认是NEAREST.
>变量expand，如果为True，表示输出图像足够大，可以装载旋转后的图片
>如果false或者缺省，就默认输出图像和输入图像尺寸一样大
```python
from PIL import Image
import os
sources_uinx = os.path.join("/home/oubingkun/图片/pil_img/","lena.jpg")
sources_ugif = os.path.join("/home/oubingkun/图片/pil_img/","qxz.gif")
im  = Image.open(sources_uinx)
print(im.format,im.size,im.mode)

im_45 = im.rotate(45,Image.NEAREST,1)
im_30 = im.rotate(30,1)
print(im_45.size,im_30.size)
im_45.show()
im_30.show()
```
* Thumbnail类
> im.thumbnail(size)
im.thumbnail(size, filter)
修改当前图像，使其包含一个自身的缩略图，该缩略图尺寸不大于给定的尺寸。
这个方法会计算一个合适的缩略图尺寸，使其符合当前图像的宽高比，调用方法draft()配置文件读取器，最后改变图像的尺寸。

变量filter应该是NEAREST、BILINEAR、BICUBIC或者ANTIALIAS之一。
如果省略该变量，则默认为NEAREST。注意：在当前PIL的版本中，滤波器bilinear和bicubic不能很好地适应缩略图产生。

用户应该使用ANTIALIAS，图像质量最好。如果处理速度比图像质量更重要，可以选用其他滤波器。
这个方法在原图上进行修改。如果用户不想修改原图，可以使用方法copy()拷贝一个图像。这个方法返回空。
```python
from PIL import Image
import os
sources_uinx = os.path.join("/home/oubingkun/图片/pil_img/","lena.jpg")
sources_ugif = os.path.join("/home/oubingkun/图片/pil_img/","qxz.gif")
im  = Image.open(sources_uinx)
im.thumbnail((100,100))
im.show()
```
* transform类
>im.transform(size,EXTENT, data) ⇒ image
im.transform(size, EXTENT, data, filter) ⇒ image
>im.transform(size, AFFINE, data) ⇒ image
im.transform(size, AFFINE,data, filter) ⇒ image 
>im.transform(size,QUAD, data) ⇒ image
im.transform(size, QUAD, data, filter) ⇒ image
>m.transform(size,QUAD, data) ⇒ image
im.transform(size, QUAD, data, filter) ⇒ image
>使用给定的尺寸生成一张新的图像，与原图有相同的模式，使用给定的转换方式将原图数据拷贝到新的图像中。在当前的PIL版本中，参数method为EXTENT（裁剪出一个矩形区域），AFFINE（仿射变换），QUAD（将正方形转换为矩形），
>MESH（一个操作映射多个正方形）或者PERSPECTIVE。变量filter定义了对原始图像中像素的滤波器。在当前的版本中，变量filter为NEAREST、BILINEAR、BICUBIC或者ANTIALIAS之一。如果忽略，或者图像模式为“1”或者“P”，该变量设置为NEAREST。
> 从图像中裁剪一个区域。变量data为指定输入图像中两个坐标点的4元组(x0,y0,x1,y1)。输出图像为这两个坐标点之间像素的采样结果。例如，如果输入图像的(x0,y0)为输出图像的（0，0）点，(x1,y1)则与变量size一样。
这个方法可以用于在当前图像中裁剪，放大，缩小或者镜像一个任意的长方形。它比方法crop()稍慢，但是与resize操作一样快。
>对当前的图像进行仿射变换，变换结果体现在给定尺寸的新图像中。变量data是一个6元组(a,b,c,d,e,f)，包含一个仿射变换矩阵的第一个两行。输出图像中的每一个像素（x，y），新值由输入图像的位置（ax+by+c, dx+ey+f）的像素产生，使用最接近的像素进行近似。这个方法用于原始图像的缩放、转换、旋转和裁剪。

>输入图像的一个四边形（通过四个角定义的区域）映射到给定尺寸的长方形。变量data是一个8元组(x0,y0,x1,y1,x2,y2,x3,y3)，它包括源四边形的左上，左下，右下和右上四个角。
```python
import os
from PIL import Image,ImageEnhance
sources_uinx = os.path.join("/home/oubingkun/图片/pil_img/","lena.jpg")
sources_ugif = os.path.join("/home/oubingkun/图片/pil_img/","qxz.gif")
im  = Image.open(sources_uinx)
print(im.format,im.size,im.mode)
out = im.transform((400,400),Image.EXTENT,(0,0,400,400))
out = im.transform ((512,512),Image.AFFINE,(1,2,3,2,1,4))
out = im.transform((400,400),Image.QUAD,(0,0,0,500,500,500,500,0))
out = im.transform((200,200),Image.PERSPECTIVE,(1,2,3,2,1,6,1,2))
print(out.size)
out.show()
```

* Transpose类
>im.transpose(method)⇒ image
>返回当前图像的翻转或者旋转的拷贝。变量method的取值为：FLIP_LEFT_RIGHT，FLIP_TOP_BOTTOM，ROTATE_90，ROTATE_180，或ROTATE_270。
```python
import os
from PIL import Image,ImageEnhance
sources_uinx = os.path.join("/home/oubingkun/图片/pil_img/","lena.jpg")
sources_ugif = os.path.join("/home/oubingkun/图片/pil_img/","qxz.gif")
im  = Image.open(sources_uinx)
output = im.roate(45)   #逆时针旋转45°
output = im.transpose(Image.FLIP_LEFT_RIGHT) #左右对换
output = im.transpose(Image.FLIP_TOP_BOTTOM) #上下对换
output = im.transpose(Image.ROTATE_90)  #旋转90°
output = im.transpose(Image.ROTATE_180) #旋转180°
output = im.transpose(Image.ROTATE_270) #旋转270°
output.show()

```
* Resize类
>对图片进行缩放
>返回改变尺寸的图像的拷贝。变量size是所要求的尺寸，是一个二元组：（width, height）。变量filter为NEAREST、BILINEAR、BICUBIC或者ANTIALIAS之一。如果忽略，或者图像模式为“1”或者“P”，该变量设置为NEAREST。
>在当前的版本中bilinear和bicubic滤波器不能很好地适应大比例的下采样（例如生成缩略图）。用户需要使用ANTIALIAS，除非速度比质量更重要
```python
import os
from PIL import Image,ImageEnhance
sources_uinx = os.path.join("/home/oubingkun/图片/pil_img/","lena.jpg")
sources_ugif = os.path.join("/home/oubingkun/图片/pil_img/","qxz.gif")
im  = Image.open(sources_uinx)
re = im.resize(200,200)
print(im.size)
re.show()
```
* Seek类,Tell类
>im.seek(frame)
在给定的文件序列中查找指定的帧，如果查找超越了序列的末尾，
则产生一个EOFError异常当文件序列被打开是，PIL自动指定到第0帧
>im.tell() integer
返回当前帧所处的位置，从0计算
```python
import os
from PIL import Image,ImageEnhance
sources_uinx = os.path.join("/home/oubingkun/图片/pil_img/","lena.jpg")
sources_ugif = os.path.join("/home/oubingkun/图片/pil_img/","qxz.gif")
im  = Image.open(sources_uinx)
im.seek(1)
print(im.tell())
im.show()
im.seek(8)
im.show()
print(im.tell())
```
```python
"""
序列迭代器类
"""
import os
from PIL import Image,ImageEnhance
sources_uinx = os.path.join("/home/oubingkun/图片/pil_img/","lena.jpg")
sources_ugif = os.path.join("/home/oubingkun/图片/pil_img/","qxz.gif")
im  = Image.open(sources_uinx)
class Sequence:
    def _init(self,im):
        self.im = im

    def _item(self,ix):
        try:
            if ix:
                self.im.seek(ix)
            return self.im

        except EOFError:
            raise IndexError

for ix in Sequence(im):
    im.show()
```
```python
"""
图像序列
"""
import os
from PIL import Image,ImageEnhance
sources_uinx = os.path.join("/home/oubingkun/图片/pil_img/","lena.jpg")
sources_ugif = os.path.join("/home/oubingkun/图片/pil_img/","qxz.gif")
im  = Image.open(sources_uinx)
im_gif = Image.open(sources_ugif)
im_gif.seek(1)
try:
    while(1):
        im_gif.seek(im.tell() + 1)

except EOFError:
    pass
im_gif.show()
```
