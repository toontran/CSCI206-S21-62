""" Priority Queue lab: CSCI 204 """

""" This class implements a linked priority queue with a head.
        Priorities are positive integers where the highest priority
        is zero. This queue is a linked list.
        Assume the base class Queue has been implemented as
        linked list."""

from Queue import Queue
from Queue import Node

class PriorityQueue( Queue ):

    def __init__( self, minPriority = 15 ):
        """Initialize the queue with a default number of priority classes."""
        super().__init__()
        self.minPriority = minPriority

    def __str__( self ):
        """Return the name of the queue"""
        return 'Priority Queue'

    def enqueue( self, priority, item ):
        """Insert an item with priority at the right place."""
        new_node = Node( item, priority=priority )
        
        # Deal with edge cases
        if self._length == 0:
            self._first = new_node
            self._length += 1
            return
        elif self._length == 1:
            if priority >= self._first.priority:
                self._first.next = new_node
            else:
                node = self._first
                self._first = new_node
                self._first.next = node
            self._length += 1
            return
        
        # If higher priority is met, connect node to new_node
        # and new_node to node.next
        node = self._first
        
        # Edge case: greatest priority
        if priority < node.priority:
            self._first = new_node
            self._first.next = node
            self._length += 1
            return
            
        # Actual insertion
        for i in range( self._length-1 ):
            next_node = node.next
            # If next_node has lower priority
            if priority < next_node.priority:
                node.next = new_node
                new_node.next = next_node
                self._length += 1
                return
            node = node.next  
            
        # No lower priority => lowest priority
        node.next = new_node
        self._length += 1

    def dequeue( self ):
        """Remove the item with most preferred priority."""
        return super().dequeue()


"""This class should implement nodes for a singly linked list with a priority."""    
