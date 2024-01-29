class _Node_Linked:
        ''' Helper class for class _Linked_List '''
        def __init__(self, item):
                self.item = item
                self.next = None
                
        def next(self, other_node):
                self.next = other_node
                

class Linked_List:
        ''' Helper class for Inventory creation '''
        def __init__(self):
                self._head = None
                self._top = None
                self._size = 0
                
        def __len__(self):
                return self._size
                
        def __str__(self):                        
                result = '['
                node = self._head
                while node != None:
                        result += str(node.item) + ', '
                        node = node.next
                result += ']'
                return result
                
        def delete(self, item):
                assert self._size > 0, 'Inventory is empty!'
                
                node = self._head
                
                if node.item == item:
                        self._head = self._head.next
                        self._size -= 1
                        return item
                
                while node.next != None and node.next.item != item:
                        node = node.next
                        
                if node.next == None:
                        return
                        
                item = node.next.item
                node.next = node.next.next
                self._size -= 1
                return item
        
        def append(self, item):
                if self._size == 0:
                        self._top = _Node_Linked(item)
                        self._head = self._top
                else:
                        self._top.next = _Node_Linked(item)
                        self._top = self._top.next        
                self._size += 1
                
        def has_item(self, item):
                node = self._head
                while node != None:
                        if node.item == item:
                                return True
                        node = node.next
                return False
                
        def get_head(self):
                return self._head
                
        def peak(self):
                return self._top
                
                
if __name__ == '__main__':
        ll = Linked_List()
        [ll.append(x) for x in range(10)]
        print(ll)
        print('ll has 5? ', ll.has_item(5))
        print([ll.delete(9-x) for x in range(10)])
        print(ll)
                
