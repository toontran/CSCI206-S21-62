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
            
    def bst_insert(self, root, new_node):
        if self.root == None:
            self.root = root
    
        if new_node.key <= root.key:
            if root.left == None:
                root.left = new_node
            else:
                self.bst_insert(root.left, new_node)
        else:
            if root.right == None:
                root.right = new_node
            else:
                self.bst_insert(root.right, new_node)
            
    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        '''Prints a preorder traversal'''
        if node is not None:
            before = self._preorder(node.left)
            after = self._preorder(node.right)
            return str(node.data) + ' ' + before + ' ' + after
        else:   
            return ''

    # 1, 2, 4, 3, 5, 7, 9, 8, 6
    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        '''Prints a postorder traversal'''
        if node is not None:
            before = self._postorder(node.left)
            after = self._postorder(node.right)
            return before + ' ' + after + ' ' + str(node.data)
        else:
            return ''

    # 1, 2, 3, 4, 5, 6, 7, 8, 9
    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        '''Returns the string of an inorder traversal'''
        if node is not None:
            before = self._inorder(node.left)
            after = self._inorder(node.right)
            return before + ' ' + str(node.data) + ' ' + after
        else:
            return ""
            
    def get_min(self):
        return self._get_min(self.root)

    def _get_min(self, node):
        ''' Return the smallest value in the BST'''
        if node.left is not None:
            return self._get_min(node.left)
        else:
            return node.data

    def get_max(self):
        return self._get_max(self.root)

    def _get_max(self, node):
        '''Returns the max of a BST'''
        if node.right is not None:
            return self._get_max(node.right)
        else:
            return node.data
            
    def _process_values_returned(self, count, is_found, 
            node_with_needed_value, count_before, count_after):
        ''' 
        Helper function, process the tail of recursive function _search  
        
        :param count: keep track of size
        :param is_found: keep track of value found status (too lazy to
                         write get_size)
        :param node_with_needed_value: keep the node needed to be found
                         (again, too lazy to do that)
        :param count_before: values returned by left node 
                         (including count, is_found, 
                         node_with_needed_value)
        :param count_after: values returned by right node
        :return: count, is_found, node_with_needed_value
        '''
            
        count += count_before[0]
        is_found = is_found or count_before[1]
        if node_with_needed_value == None and count_before[2] != None:
            node_with_needed_value = count_before[2]
        
        count += count_after[0]
        is_found = is_found or count_after[1]
        if node_with_needed_value == None and count_after[2] != None:
            node_with_needed_value = count_after[2]
            
        return count, is_found, node_with_needed_value
            
    def search(self, value):
        ''' Return true if the tree contains the value given'''
        return self._search(self.root, value)[1]

    def _search(self, node, value):
        count = 0
        is_found = False
        node_with_needed_value = None
        if node != None and node.data == value:
            is_found = True
            node_with_needed_value = node
        
        if node is not None:
            count = 1
            count_before = self._search(node.left, value)
            count_after = self._search(node.right, value)
            return self._process_values_returned(count, is_found,
                   node_with_needed_value, count_before, count_after)
        else:
            return 0, False, None         

    def get(self, target):
        ''' Returns the node object of a value'''
        return self._get(self.root, target)

    def _get(self, node, target):
        return self._search(node, target)[2]

    def get_size(self):
        ''' Returns the number of nodes in the tree'''
        return self._get_size(self.root)

    def _get_size(self, node):
        return self._search(node, 1)[0]
            
    def trim_bst(self, min_val, max_val):
        '''Keep only the nodes in a BST that are beteween
        min_val and max_val'''
        self._trim_bst(self.root, min_val, max_val)

    def _trim_bst(self, node, min_val, max_val):
        '''Traverse the tree
            If we encounter a key less than our min_val, disregard that
            Node and only keep right subtree of that node. IF we 
            encounter a key greater than our max_val, disregard 
            that Node and only keep left subtree of that node'''
        if node is not None:
            if node.left != None and node.left.key >= min_val:
                before = self._trim_bst(node.left, min_val, max_val)
            else:
                node.left = None
                before = ''
            if node.right != None and node.right.key <= max_val:
                after = self._trim_bst(node.right, min_val, max_val)
            else:
                node.right = None
                after = ''
            return before + ' ' + str(node.data) + ' ' + after
        else:
            return ""
                

    # You might need to change this definition!
    def is_bst(self, lastBSTNodeVal = -1):
        ''' Returns True if the tree is a BST '''
        # return True # CUZ IT'S A TRUE BST!
        inorder = _inorder_but_print_key(self, self.root)
        num = -2*10**9
        
        for ch in inorder:
            if ch == ' ':
                pass
            else:
                key = int(ch)
                if key >= num:
                    num = key
                else:
                    return False
        
        return True
        
    def _inorder_but_print_key(self, node):
        '''Returns the string of an inorder traversal'''
        if node is not None:
            before = self._inorder(node.left)
            after = self._inorder(node.right)
            return before + ' ' + str(node.key) + ' ' + after
        else:
            return ""
            
    def level_order(self):
        ''' Level order traversal '''
        return self._level_order([self.root])
        
    def _level_order(self, current_level_nodes, more=None, result=''):
        if current_level_nodes == []:
            return result

        next_level_nodes = []
        for node in current_level_nodes:
            result += node.data + ','
            if node.left != None:
                next_level_nodes.append(node.left)
            if node.right != None:
                next_level_nodes.append(node.right)
                
        return self._level_order(next_level_nodes, result=result)
        
    def remove(self, target):
        ''' Remove a target from a binary tree
        HINT: You'll need a find predecessor/successor function
        
        
        3 steps when target is found: 
                 Store left_node of target_node
                 Find the min_node of target.right
                 min_node.left = left_node
        '''
        assert self.root is not None, 'Tree doesn\'t have root!'
        
        parent = self.get_parent(target)
        
        if parent == True:
            # Remove root
            if self.root.right != None:
                left_node = self.root.left
                min_node = self._get_min_node(self.root.right)
                min_node.left = left_node
                # Reassign root
                self.root = self.root.right
            else:
                self.root = self.root.left
        elif parent == False:                # None target found
            return 
        else:                                # Target has parent
            left = parent.left
            right = parent.right
            is_left, target_node = self._left_or_right(left, right, target)

            if target_node.right != None:
                left_node = target_node.left
                min_node = self._get_min_node(target_node.right)
                min_node.left = left_node
            
                if is_left:
                    parent.left = target_node.right
                else:
                    parent.right = target_node.right
            else:
                if is_left:
                    parent.left = target_node.left
                else:
                    parent.right = target_node.left
                
    def _left_or_right(self, left, right, target):
        ''' Which child is the target? 
        
        :return: is_left: is the target left?
                 target_node: the target node itself
        '''
        if left.data == target:
            target_node = left
            is_left = True
        elif right.data == target:
            target_node = right
            is_left = False
        else:
            print('WTF, SumTingWong')
            return
        return is_left, target_node
    
           
    def _get_min_node(self, node):
        ''' Return the node with smallest value in the BST'''
        if node.left is not None:
            return self._get_min_node(node.left)
        else:
            return node
    
    def get_parent(self, target):
        ''' 
        Get parent of target 
        
        :param target: data of the target node
        :return: True if target is root, False if target is not found
                 Node object if target is found and is a child of 
                  a parent node
        '''
        if self.root.data == target:
            return True
            
        return self._get_parent(self.root, target)
        
    def _get_parent(self, node, target):
        left = False
        right = False
    
        if node.left is not None:
            if node.left.data == target:
                return node
            else:
                left = self._get_parent(node.left, target)
        
        if node.right is not None:
            if node.right.data == target:
                return node
            else:
                right = self._get_parent(node.right, target)
                
        if left == False and right == False:
            return False
        elif left != False:
            return left
        else:
            return right
            
            

            
        
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
