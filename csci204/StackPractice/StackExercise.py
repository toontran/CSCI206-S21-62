class _StackNode:
    def __init__( self, item, link ):
        self.item = item
        self.next = link
        
class Stack:
    def __init__( self ):
        self._top = None
        self._size = 0

    def push( self, item ):
        ''' Method to push an item to the top of a Stack'''
        node = _StackNode(item, None)
        if self.is_empty():
            self._head = node # First node of the Stack 
            self._top = node
        else:
            self._top.next = node
        self._size += 1
        
    def pop( self ):
        ''' Method to pop an item from the top of a Stack'''
        top_item = self.peek()  # This takes care of empty stack
        
        if self._size == 1:
	        self._size -= 1
        else:
	        node = self._head
	        for i in range( self._size - 2	):
	            node = node.next
	        self._top = node
	        self._size -= 1
	   
        return top_item    
        
    def peek( self) :
        assert not self.is_empty(), 'Cannot peek at an empty Stack bruh'
        return self._top.item
        
    def is_empty( self ):
        if self._size == 0:
            return True
        
    def __len__( self ):
        return self._size
