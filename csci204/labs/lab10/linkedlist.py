class ListException(Exception):
    pass


class ListNode:
    def __init__( self, data ):
        self.data = data
        self.next = None
        
    def __str__( self ):
        return str( self.data )
        
    def __repr__( self ):
        return str( self.data )


class List:
    ''' Linked List '''

    def __init__( self ):
        self.head = None
        self.end = None
        self.size = 0
        
    def __len__( self ):
        return self.size
        
    def __iter__( self ):
        return _ListIterator( self )
        
    def insert( self, item, index ):
        if self.size == 0:
            self.append( item )
            return
            
        if index >= self.size:
            self.append( item )
        elif index <= 0:
            node = ListNode( item )
            prev_head = self.head
            self.head = node
            self.head.next = node
        else:
            i = 0
            node = self.head
            while i+1 != index:
                node = node.next
                i += 1
            curr_node = node.next
            node.next = ListNode( item )
            node.next.next = curr_node
        self.size += 1
        
    def append( self, item ):
        if self.size == 0:
            self.head = ListNode( item )
            self.end = self.head
            self.size = 1
            return 
            
        node = ListNode( item )
        self.end.next = node
        self.end = self.end.next
        
        self.size += 1
        
    def pop( self, index=None ):
        if index == None:
            index = self.size-1
        if index < 0 or index > self.size-1:
            return
            
        if index == 0:
            item = self.head.data
            self.head = self.head.next
        else:
            i = 0
            node = self.head
            while i+1 != index:
                node = node.next
                i += 1
            item = node.next.data
            node.next = node.next.next
        
        self.size -= 1
        return item
        
    def peek( self, index ):
        if index < 0 or index > self.size-1:
            raise ListException
    
        i = 0
        node = self.head
        while i != index:
            node = node.next
            i += 1
            
        return node.data


class _ListIterator:
    def __init__( self, a_structure ):
        self.a_structure = a_structure
        if isinstance(a_structure, List):
            self.head = a_structure.head
        else:
            self.head = a_structure[0]
        
        self.size = len(self.a_structure)
        self.running_idx = 0
            
    def __next__( self ):
        if self.running_idx == self.size:
            raise StopIteration
        elif self.running_idx == 0:
            self.running_idx += 1
            return self.head
    
        if self.head != 0:
            self.running_idx += 1
            self.head = self.head.next
            return self.head
        else:
            self.running_idx += 1
            self.head = self.a_structure[ self.running_idx ]
            return self.head
        
    def __iter__( self ):
        return self
  
  
  
  
def create_list(list_size):
    new_list = List()
    for i in range(list_size):
        new_list.append(i)
    return (new_list)

if __name__ == '__main__':
    new_list = create_list(10)
    new_list.append(12)
    print("Should be: 0 1 2 3 4 5 6 7 8 9 12")
    print(str(new_list.peek(10) == 12) + " - ")
    
    new_list.insert(25, 5)
    print("After insert @ 5, should be: 0 1 2 3 4 25 5 6 7 8 9 12")
    print("Peek @ 5 should be 25 " + str(new_list.peek(5) == 25) + " - ")
    new_list.pop()
    print("\nPeek @ 11 should result in exception.")
    try:
        new_list.peek(11)
        print(" - No exception.")
    except ListException:
        print(" - Exception.")
        
    for item in new_list:
        print( str(item), end=' ' )
    
