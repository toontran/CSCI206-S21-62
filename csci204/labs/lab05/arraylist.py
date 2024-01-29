from array204 import *
from ListException import ListException

class List:

    def __init__(self):
        self.__capacity = 2
        self.__size = 0
        self._array = Array(2)

    def __len__(self):
        return self.__size

    def __double_capacity(self):
        new_array = Array(self.__capacity*2)
        self.__capacity *= 2
        for i in range(len(self._array)):
            new_array[i] = self._array[i]
        self._array = new_array

    def insert(self, item, index):
        # Double capacity if capacity reached
        if self.__size == self.__capacity-1:
                self.__double_capacity()

        # Illegal indexes become last element of array or first
        if index > self.__size:
            index = self.__size + 1
        elif index < 0:
            index = 0

        num_of_elems_to_move = self.__size-index
        for i in range( num_of_elems_to_move ):
            self._array[ self.__size-i ] = self._array[ self.__size-i-1 ] # Propagate forward
            
        self._array[index] = item
        self.__size += 1
                
    def delete(self, index):
        for i in range( index, self.__size ):
            self._array[i] = self._array[i+1]
        self.__size -= 1

    def peek(self, index):
        if index >= self.__size or index < 0:
            raise ListException
        elif self.__size == 0 and index == 0:
            raise ListException
        else:
            return self._array[index]
        
