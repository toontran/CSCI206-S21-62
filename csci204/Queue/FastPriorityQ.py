""" Priority Queue lab: CSCI 204 """

from Queue import Queue

class FastPriorityQueue:
    """ This class implements a fast priority queue. Priorities are positive
        integers where the highest priority is zero. The lowest priority
        (highest number) must be known when the queue is initialized."""

    def __init__( self, min_priority = 15 ):
        """ The queue must have a known minimum priority.
            It is initialized to hold a list for each priority.
            The lists are each initialized to be empty. """
        prio_list_size = min_priority + 1
        self.prio_lists = [ None ] * prio_list_size
        for i in range(prio_list_size):
            self.prio_lists[i] = Queue()
            
        self._min_priority = min_priority
        self._size = 0

    def __str__( self ):
        """Return the name of the queue"""
        return 'Fast Priority Queue'

    def __len__( self ):
        """ Returns the number of items in the queue. """
        return self._size

    def enqueue( self, priority, item ):
        """ Enqueue the given item with the given priority. Precondition:
            0 <= priority <= least priority. """
        self.prio_lists[ priority ].enqueue( item )
        self._size += 1

    def dequeue(self):
        """ Dequeue and return the highest priority item. Returns None
            if the queue is empty. """
        if self._size == 0:
            return None
        else:
            for prio_list in self.prio_lists:
                if len( prio_list ) == 0:
                    continue
                else:
                    self._size -= 1
                    return prio_list.dequeue()
                
