#coding=utf-8
"""
https://www.jianshu.com/p/bae9e0b0a91c
"""
"""
循环队列，基于list
时间复杂度
现在假设我们的容积capacity为n，我们用enqueue方法n+1次，
才会触发一次resize，而一次resize，进行了n次操作，也就是
说，平均每次enqueue，我们执行的基本操作次数为： 
(n+1)+n/n+1 ≈ 2，enqueue操作的时间复杂度为O(1)，
同理，dequeue（出队）方法也是O(1)级别的时间复杂度

"""
class LoopQueue(object):
    def _init_(self,n=10):
        self.arr = [None] * (n+1) #浪费一个空间，arr实际大小为用户传入容量+1
        self.front = 0
        self.tail = 0
        self.size = 0

    def _str_(self):
        return str(self.arr)

    def _len_(self):
        return iter(self.arr)

    def _iter_(self):
        return iter(self.arr)

    #利用取余，判断队列为满
    def is_full(self):
        return (self.tail+1) % len(self.arr) == self.front


    #扩容，缩放容
    def resize(self,new_capacity):
        """
        当队列满时，以当前队列容积的2倍进行扩容（这里的容积指的是队列实际可存储的元素个数）
        当元素个数少于容积的1/4并且元素个数>1时，以当前队列容积的1/2倍进行扩容（也就是缩容）
        """
        new_arr = [None] * (new_capacity+1)
        for i in range(self.size):
            new_arr[i] = self.arr[(i+self.front) % len(self.arr)]

        self.arr = new_arr
        self.front = 0
        self.tail = self.size


