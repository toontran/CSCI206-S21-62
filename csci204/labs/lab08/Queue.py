'''
Tung Tran

CSCI 204'''
class Node:
  ''' Helper class for Queue '''
  def __init__( self, data, priority=0 ):
    self.priority = priority
    self.data = data
    self.next = None
  
  
class Queue:
  ''' Implement Queue with Linked List '''
  
  def __init__( self ):
    self._first = None
    self._last = None
    self._length = 0
    
  def __len__( self ):
    return self._length
    
  def enqueue( self, item ):
    '''
    Add item into Queue
    
    :param item: An item of any value (e.g. int, float, str)
    '''
    if self._length == 0:
      self._first = Node( item )
      self._last = self._first        # So that both would be the same object
    else:
      self._last.next = Node( item )
      self._last = self._last.next
    
    self._length += 1
    return
    
    
  def dequeue( self ):
    '''
    Return and Remove the first item
    
    :return: First item of the Queue
    '''
    if self._length == 0:
        print('Empty queue!')
        return None
    
    item = self._first.data
    self._first = self._first.next
    self._length -= 1
    
    return item
    
    
