#from resourcesim import *

class _Node:
    def __init__( self, data ):
        self.data = data
        self.next = None

class Queue:
    
    def __init__( self, max_size=False ):
        
        self.max_size = max_size
        self._end = None
        self._top = None
        self._size = 0
        
    def __len__( self ):
        return self._size
        
    def is_empty( self ):
        return self._size == 0
        
    def enqueue( self, item ):
        if self.max_size != False and self._size >= self.max_size:
            return -1
            
        if self._size == 0:
            self._top = _Node( item )
            self._end = self._top
        else:
            self._end.next = _Node( item )
            self._end = self._end.next    
        self._size += 1
        
    def dequeue( self ):
        if self._size == 0:
            return None
    
        top = self._top.data
        self._top = self._top.next
        self._size -= 1
        
        if self._size == 0:
            self._end = None
               
        return top
        
    def peek( self ):
        return self._top
            
            
if __name__ == '__main__':
    mahQueue = Queue()
    mahQueue.enqueue(3)
    mahQueue.enqueue(5)
    print(mahQueue.dequeue())
    print(mahQueue.dequeue())
    print(mahQueue._end.data)
    
