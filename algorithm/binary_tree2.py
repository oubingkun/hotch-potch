# coding=utf-8
"""
yield from形式
前序遍历
中序遍历
后序遍历
"""
"""
              4
           /     \
          3       5
         / \    /   \
        1  null null 7

"""
# yield from使用的一个经典场景：二叉树的遍历
# 利用 yield from 实现二叉树的遍历

# 结点
class Node:
	def __init__(self, key):
		self.key = key
		self.lchild = None
		self.rchild = None
		self.iterated = False
		self.father = None

	# 先序遍历
	def PreOrderTraverse(self):
		yield self.key
		if self.lchild is not None:
			yield from self.lchild.PreOrderTraverse()
		if self.rchild is not None:
			yield from self.rchild.PreOrderTraverse()
	# 中序遍历
	def InOrderTraverse(self):
		if self.lchild is not None:
			yield from self.lchild.InOrderTraverse()
		yield self.key
		if self.rchild is not None:
			yield from self.rchild.InOrderTraverse()
	# 后序遍历
	def PostOrderTraverse(self):
		if self.lchild is not None:
			yield from self.lchild.PostOrderTraverse()
		if self.rchild is not None:
			yield from self.rchild.PostOrderTraverse()
		yield self.key

# 二叉树
class Tree:
	def __init__(self):
		# 创建二叉树
		self.root = Node(4)
		self.root.lchild = Node(3)
		self.root.lchild.father = self.root
		self.root.rchild = Node(5)
		self.root.rchild.father = self.root
		self.root.lchild.lchild = Node(1)
		self.root.lchild.lchild.father = self.root.lchild
		self.root.rchild.rchild = Node(7)
		self.root.rchild.rchild.father = self.root.rchild
	# 先序遍历
	def PreOrderTraverse(self):
		yield from self.root.PreOrderTraverse()
	# 中序遍历
	def InOrderTraverse(self):
		yield from self.root.InOrderTraverse()
	# 后序遍历
	def PostOrderTraverse(self):
		yield from self.root.PostOrderTraverse()



binary_tree = Tree()
# 先序遍历
print("----先序遍历----")
it = binary_tree.PreOrderTraverse()
print(list(it))
# 中序遍历
print("----中序遍历----")
it = binary_tree.InOrderTraverse()
print(list(it))
# 后序序遍历
print("----后序遍历----")
it = binary_tree.PostOrderTraverse()
print(list(it))