'''
CS204 Professor Chris Dancy
Stack ADT Implementation using Linked List
Student: Khoi Lam
'''

class _StackNode :
    '''
    Item is the data of a node and .next points to the next node
    '''
    def __init__(self, item, link):
        self.item = item
        self.next = link

class Stack:
    '''
    Top of the stack is initially None and the initial size is 0
    '''
    def __init__(self):
        self._top = None
        self._size = 0

    def peek(self):
        '''returning the item at the top of the stack without reducing the size of the stack '''
        if not self.is_empty():
            return self._top.item
        else:
            pass

    def push(self, item):
        ''' Method to push an item to top of a Stack'''
        if self.is_empty(): #this means that the stack is empty
            self._top = _StackNode(item, None)
            self._size += 1
        else:
            newnode = _StackNode(item, None)
            newnode.next = self._top
            self._top = newnode
            self._size += 1

    def pop(self):
        '''method to pop an item out of the top of the stack '''
        assert not self.is_empty()
        popped_node = self._top
        self._top = self._top.next
        popped_node.next = None
        self._size -= 1
        return popped_node.item

    def __len__(self):
        '''overwriting the len() function '''

        return self._size

    def is_empty(self):
        ''' Check if the stack is empty or not '''

        if self._top == None:
            return True
        return False
    def __str__(self):
        result = '['
        node = self._top
        if node != None:
            result+= str(node.item)
            node = node.next
            while node != None:
                result += ', ' + str(node.item)
                node = node.next
        return result + ']'
