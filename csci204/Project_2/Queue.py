
class Queue:
    ''' Implement Queue using Circular Array '''
    
    def __init__( self, max_size ):
        self._array = [None] * max_size
        self._first = 1 # Index
        self._last = 0
        self._size = 0
        
    def __len__( self ):
        return self._size
        
    def enqueue( self, item ):
        assert self._size < len(self._array), 'Queue Overflow!'
        
        self._last = (self._last+1) % len(self._array)
        self._array[ self._last ] = item
        
        self._size += 1
        
    def dequeue( self ):
        assert self._size > 0, 'Nothing in Queue!'
        
        item = self._array[ self._first ]
        self._first = (self._first+1) % len(self._array)
        
        self._size -= 1
        
        return item
        
        
if __name__ == '__main__':
    queue = Queue(10)
    [queue.enqueue(x) for x in range(10)]
    print( [queue.dequeue() for x in range(len(queue)-3)] )
    [queue.enqueue(x) for x in range(3)]
    print( [queue.dequeue() for x in range(6)] )
