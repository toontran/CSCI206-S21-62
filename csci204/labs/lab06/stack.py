""" CSCI204 Stack lab
Last Modified by: Prof. Dancy, Mar-2017
"""

from array204 import *

class MyStack:
    """ Implement this Stack ADT using an Array to hold elements.
    """

    def __init__( self ):
        """ Initialize an empty stack.
        Initial capacity should be 2, size should be zero, all items
        in the array should be None. """
        self.__capacity = 2
        self.__size = 0
        self.__array = Array( 2 )
        
    def __len__( self ):
        return len(self.__array)
        
    def __str__( self ):
        result = ''
        result += '['
        for i in range(self.__size):
            result += str(self.__array[i]) + ','
        result += ']'
        return result

    def is_empty( self ):
        """ Is the stack empty?
        Returns True if the stack is empty; False otherwise. """
        if self.__size == 0:
            return True
        return False

    def __expand__(self):
        """ Stack is full, expand the capacity. """
        self.__capacity *= 2
        new_array = Array( self.__capacity )
        for i in range( len(self.__array) ):
            new_array[ i ] = self.__array[ i ]
        self.__array = new_array            
        
    def push( self, item ):
        """ Push the item onto the top of the stack. """
        if self.__capacity == self.__size:
            self.__expand__()
        
        self.__array[ self.__size ] = item
        self.__size += 1

    def pop( self ):
        """ Pop the top item off the stack and return it. """
        self.__size -= 1
        return self.__array[ self.__size ] # Because we just reduced the size 

    def top( self ):
        """ Return the top item on the stack (does not change the stack). """
        return self.__array[ self.__size-1 ]

