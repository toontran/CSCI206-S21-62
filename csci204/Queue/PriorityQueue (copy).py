'''
Priority Queue

Tung Tran
'''
class _Node:
  ''' Helper class for Queue '''
  def __init__( self, data ):
    self.data = data
    self.next = None
  
  def __len__( self ):
    return len( self.data )
  
class PriorityQueue:
  ''' Implement Queue with Linked List, this time Prioritized '''
  
  def __init__( self ):
    self._first = None
    self._last = None
    self._length = 0

  def __len__( self ):
    return self._length
    
  def enqueue( self, item ):
    '''
    Add item into Priority Queue
    
    :param item: A String
    '''
    if self._length == 0:
      self._first = _Node( item )
      self._last = self._first        # So that both would be the same object
    else:
      self._last.next = _Node( item )
      self._last = self._last.next
    
    self._length += 1
    return
    
    
  def dequeue( self ):
    '''
    Return and Remove the Highest priority item
    
    :return: Highest priority item of the Priority Queue
    '''
    assert self._length > 0, 'There\'s nothing in the Queue!'
    
    if self._length == 1:
        self._length -= 1
        return self._first.data
    
    highest_priority_node = self._first
    prev_highest_priority_node = None
    node = self._first.next
    prev_node = None
    
    # Find highest priority node (-1 because we start from index 1)
    for i in range( self._length-1 ):
    
        if len(highest_priority_node) < len(node):
            prev_highest_priority_node = prev_node
            highest_priority_node = node
       
        prev_node = node
        node = node.next 
    
    # Delete the node
    if prev_highest_priority_node == None:
        self._first = self._first.next
    else:
        prev_highest_priority_node.next = highest_priority_node.next
    
    self._length -= 1
    
    
    return highest_priority_node.data
    
    
if __name__ == '__main__':
    pQueue = PriorityQueue()
    pQueue.enqueue('adfasd')
    pQueue.enqueue('asdfa')
    
    for i in range(3):
        print(pQueue.dequeue())
    
    
