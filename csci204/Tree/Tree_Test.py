'''
Tree Practice - Test

Tung Tran
'''
from BST import *


def main():
    # Creates a BST (binary search tree)
	print("Create binary search tree")
	new_root = BSTNode(6, "6")
	bst_insert(new_root, BSTNode(5, "5"))
	bst_insert(new_root, BSTNode(8, "8"))
	bst_insert(new_root, BSTNode(3, "3"))
	bst_insert(new_root, BSTNode(4, "4"))
	bst_insert(new_root, BSTNode(9, "9"))
	bst_insert(new_root, BSTNode(7, "7"))
	bst_insert(new_root, BSTNode(2, "2"))
	bst_insert(new_root, BSTNode(1, "1"))

	count = count_all_nodes(new_root)
	print("Print preorder")
	preorder(new_root)
	print("Print postorder")
	postorder(new_root)
	print("Print inorder")
	inorder(new_root)
	print("Print levelorder")
	levelorder(new_root)
	print("Count", count)

	print('Min', get_min(new_root))
	print('Max', get_max(new_root))

if __name__ == '__main__':
	main()
