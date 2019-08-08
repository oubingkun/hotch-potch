# atx-test

##### 说明

> 自动化多进程两个实验demo,都使用了多进程的pool.apply_async,demo1列举了两种函数,两种函数表示两台设备,demo2是把设备通过遍历```字典```,,简化.

##### demo1:简单函数版:

```python


def meizu():
    d1 = u2.connect("721CECRE22Y9A")
    d1.app_start("com.czur.scanpro")
    time.sleep(5)
    d1.app_stop('com.czur.scanpro')

def lenovo():
    d2 = u2.connect("HKP3AF68")
    d2.app_start("com.czur.scanpro")
    time.sleep(5)
    d2.app_stop('com.czur.scanpro')

```



demo2 遍历字典:

```python
#coding=utf-8
import uiautomator2 as u2 
from multiprocessing.dummy  import Pool as ThreadPool
import time

threadNum = 2

def meizu():
    udid= ["721CECRE22Y9A","HKP3AF68"]
    for i in udid:
        d = u2.connect(i)
        d.app_start("com.czur.scanpro")
        time.sleep(2)
        d.app_stop('com.czur.scanpro')

if __name__ == "__main__":

    pool = ThreadPool(threadNum)    
    pool.apply_async(meizu())
    pool.close()
    pool.join()
```

