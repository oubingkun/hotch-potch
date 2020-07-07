# conding=utf-8
import uiautomator2 as u2
from multiprocessing import Pool
import time


def initPool():
    print("初始化")


pool = Pool(processes=2, initializer=initPool, initargs=[])


def meizu():
    d1 = u2.connect("721CECXXX2Y9A")
    d1.app_start("com.xxx.xxx")
    time.sleep(5)
    d1.app_stop('com.xxx.xxx')


def lenovo():
    d2 = u2.connect("HKP3XXX8")
    d2.app_start("com.xxx.xxx")
    time.sleep(5)
    d2.app_stop('com.xxx.xxx')


if __name__ == "__main__":
    pool.apply_async(lenovo(), meizu())
    pool.close()
    pool.join()
