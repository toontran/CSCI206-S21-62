'''
Tree Practice - Binary Search Tree Class

Tung Tran
'''


class BSTNode:
		def __init__(self, key, data):
				self.key = key
				self.data = data
				self.left = None
				self.right = None

class BinarySTree:
		''' Framework for a Tree class'''
		def __init__(self):
				self.root = None
