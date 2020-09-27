#coding=utf-8
from collections import deque

"""
demo binary tree
把节点看做是对象，通过类似链表连接节点
            E
           /  \
          A    G
           \    \
            C    F
           / \
          B   D
"""

#二叉树模型初始化
class BinaryTree(object):
    def _init_(self,rootP):
        self.rootP = rootP
        self.Child_left = None
        self.Child_right = None

#Create
a = BinaryTree("A")
b = BinaryTree("B")
c = BinaryTree("C")
d = BinaryTree("D")
e = BinaryTree("E")
f = BinaryTree("F")
g = BinaryTree("G")

#根
root = e

#构造各节点关系
e.Child_left = a
e.Child_right = g
a.Child_right = c
c.Child_left = b
c.Child_right = d
g.Child_right = f

"""
前序遍历
root->child_l->child_r
tree:root of tree
"""
def pre_tra(tree):
    if tree:
        print(tree.rootP,end=',')
        pre_tra(tree.Child_left)
        pre_tra(tree.Child_right)

"""
中序遍历
child_l->root->child_r
"""
def in_tra(tree):
    if tree:
        in_tra(tree.Child_left)
        print(tree.rootP, end='')
        in_tra(tree.Child_right)
"""
后序遍历
child_r->child_l->root
"""
def back_tra(tree):
    if tree:
        back_tra(tree.Child_right)
        back_tra(tree.Child_left)
        print(tree.rootP,end='')

"""
层次遍历
deque队列
E->A,G->C,F->B-D
"""
def level_tra(tree):
    queue = deque()     #创建一个deque队列对象
    queue.append(tree)  #把root加入队列
    while len(queue):   #保证队列不为空
        node = queue.popleft()
        print(tree.rootP,end='')
        if node.Child_left:
            level_tra(node.Child_left)
        if node.Child_right:
            level_tra(node.Child_right)

