"""
"""
"""
leetcode 225 用list实现栈
"""
class Std_Stack(object):
    #init data structure
    def _init_(self):
        self._list = []

    #元素添加，进栈
    def push(self,x:int):
        self._list.append(x)

    #将元素从栈移除
    def pop(self):
        return self._list.pop()

    #返回栈顶元素
    def top(self):
        return self._list[-1]

    #空栈
    def empty(self):
        return self._list == []

xlen = []
xlen = Std_Stack()
xlen.push(1)
xlen.push(2)
print(xlen.pop())
print(xlen.pop())
print(xlen.pop())

