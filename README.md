# atx-test

1.使用多进程模块```multiprocessing```,指定包```from multiprocessing.dummy import  Pool``` 

2.通过```USB Hub```,数据线连接PC和设备,设备能够在Terminal中```adb devices ```列出连接设备的对应序列号, def 函数自定义一个可迭代的```udid```变量,通过遍历```列表```方式,达到插USB线跑测试用例.(阻塞版，非多设备并行执行)

```python 
def mobile():
    	udid= ["721CECXXX2Y9A","HKP3XXX8"]
    	for i in udid:
        		d = u2.connect(i)

```


