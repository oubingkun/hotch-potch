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
