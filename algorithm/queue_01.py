"""
Queue:FIFO
LifoQueue:LIFO
PriorityQueue:优先队列，级别越低，越优先
deque：双边队列
"""
"""
队列可以并发的派多个线程，对排列的线程处理，并切每个需要处理线程
只需要将请求的数据放入队列容器的内存中，线程不需要等待，当排列完毕处
理完数据后，线程在准时来取数据即可。请求数据的线程只与这个队列容器存
在关系，处理数据的线程down掉不会影响到请求数据的线程，队列会派给其
他线程处理这分数据，它实现了解耦，提高效率。队列内会有一个有顺序的容
器，列表与这个容器是有区别的，列表中数据虽然是排列的，但数据被取走后
还会保留，而队列中这个容器的数据被取后将不会保留。当必须在多个线程之
间安全地交换信息时，队列在线程编程中特别有用。

"""
from queue import Queue,LifoQueue,PriorityQueue
from collections import deque
import time
import threading
"""
FIFO，maxsize设置队列中，数据上限，小于或等于0则不限制，容器大于
这个数则阻塞，直到队列中的数被清除
"""
def FIFO_Que():
    q= Queue(maxsize=0)
    #写入队列数据
    q.put(0)
    q.put(1)
    q.put(2)

    #输出当前队列所有数据
    print(q.queue)
    #删除队列数据，并返回该数据
    q.get()
    #再次输出所有队列数据
    print(q.queue)

# r = FIFO_Que()
# print(r)

"""
LIFO后进先出，与栈类似
"""
def LIFO_Que():
    lq = LifoQueue(maxsize=0)

    #队列写入数据
    lq.put(0)
    lq.put(1)
    lq.put(2)

    #输出队列所有数据
    print(lq.queue)
    #删除队尾数据，并返回数据
    lq.get()
    #再次输出所有数据
    print(lq.queue)

# x = LIFO_Que()
# print(x)

"""
双边队列
"""
def Deq_Que():
    dq = deque(['a','b'])

    #增加数据到队尾
    dq.append('c')
    #增加数据到队左
    dq.appendleft('d')
    #输出队列所有数据
    print(dq)
    #移除队尾，并返回
    print(dq.pop())
    #移除队左，并返回
    print(dq.popleft())

# j = Deq_Que()
# print(j)

"""
生产消费者模型
"""
q = Queue(maxsize=0)
def product(name):
    count = 1
    while True:
        q.put('步枪{}'.format(count))
        print('{}生产步枪{}支'.format(name,count))
        count+=1
        time.sleep(0.3)

def cousume(name):
    while True:
        print('{}装备了{}'.format(name,q.get()))
        time.sleep(0.3)

        q.task_done()

#部队线程
p1 = threading.Thread(target=product,args=('张三',))
p2 = threading.Thread(target=cousume,args=('李四',))
p3 = threading.Thread(target=cousume,args=('王五',))

p1.start()
p2.start()
p3.start()
