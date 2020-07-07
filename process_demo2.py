# coding=utf-8
import uiautomator2 as u2
from multiprocessing.dummy import Pool as ThreadPool
import time

threadNum = 2


def meizu():
    udid = ["721CECXXX2Y9A", "HKP3XXX8"]
    for i in udid:
        d = u2.connect(i)
        d.app_start("com.xxx.xxx")
        time.sleep(2)
        d.app_stop('com.xxx.xxx')


if __name__ == "__main__":
    pool = ThreadPool(threadNum)
    pool.apply_async(meizu())
    pool.close()
    pool.join()
