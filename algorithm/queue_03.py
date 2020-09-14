""""""
"""
leetcode 225 队列实现栈，解2
push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
双队列实现栈，一个队列元素出队列，直到空队列，一个队列入
https://blog.csdn.net/weixin_43250623/article/details/88806625
https://blog.csdn.net/cy_believ/article/details/104612729
"""


class Stack:
    def _init_(self):
        self.queue = []
        self.back_queue = []

    def push(self, x):
        while len(self.queue) > 0:  # 主，不为空
            self.back_queue.append(self.queue.pop(0))
        self.queue.append(x)

        while len(self.back_queue) > 0: # 次，不为空
            self.queue.append(self.back_queue.pop(0))

    def pop(self):
        return self.queue.pop(0)


    def top(self):
        return self.queue[0]

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False


