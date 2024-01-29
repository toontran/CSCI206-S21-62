from BST import *

def count_all_nodes(root):
    count = 0
    if root is not None:
        count += 1
        count += count_all_nodes(root.left)
        count += count_all_nodes(root.right)
    return count

def main():
    # Creates a BST (biinary search tree)
	print("Create binary search tree")
	new_root = BSTNode(6, "6")
	new_tree = BinarySTree()
	new_tree.bst_insert(new_root, BSTNode(5, "5"))
	new_tree.bst_insert(new_root, BSTNode(8, "8"))
	new_tree.bst_insert(new_root, BSTNode(3, "3"))
	new_tree.bst_insert(new_root, BSTNode(4, "4"))
	new_tree.bst_insert(new_root, BSTNode(9, "9"))
	new_tree.bst_insert(new_root, BSTNode(7, "7"))
	new_tree.bst_insert(new_root, BSTNode(2, "2"))
	new_tree.bst_insert(new_root, BSTNode(1, "1"))
    
	count = count_all_nodes(new_root)
	print("Print preorder")
	print(new_tree._preorder(new_root))
	print("Print postorder")
	print(new_tree._postorder(new_root))
	print("Print inorder")
	print(new_tree._inorder(new_root))
	'''
	print("Print levelorder")
	new_tree.levelorder(new_root)
	'''
	print("Count", count)

	print('Min', new_tree._get_min(new_root))
	print('Max', new_tree._get_max(new_root))
	
	print('Is 1 in BST? ', new_tree.search('1'))
	print('Is 9 in BST? ', new_tree.search('9'))
	print('Is 0 in BST? ', new_tree.search('0'))
	
	print('Get node 1: ', new_tree.get('1').data)
	print('Get node 0: ', new_tree.get('0'))
	
	print('Get size: ', new_tree.get_size())
	
	new_tree.trim_bst(2, 8)
	print(new_tree._preorder(new_root))
	
	# Just trimmed the 9 and 1 out, adding back in
	new_tree.bst_insert(new_root, BSTNode(9, "9"))
	new_tree.bst_insert(new_root, BSTNode(1, "1"))
	
	print(new_tree._level_order([new_root], more=None))
	
	print('Parent of 3 is: ', new_tree.get_parent('3').key)
	
	print('Original: ', new_tree.inorder())
	print('Remove 5:')
	new_tree.remove('5')
	print(new_tree._inorder(new_root))
	print('Remove 8:')
	new_tree.remove('8')
	print(new_tree._inorder(new_root))
	
	

if __name__ == '__main__':
	main()
