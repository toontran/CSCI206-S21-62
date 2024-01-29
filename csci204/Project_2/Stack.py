class Stack:

    def __init__( self ):
        self._plist = []
    
    def __len__( self ):
        return len( self._plist )
        
    def __str__( self ):
        return str( self._plist )
        
    def peak( self ):
        if len(self._plist) == 0:
            return None
        return self._plist[-1]
        
    def pop( self ):
        assert len(self._plist) > 0, 'Empty Stack!'
        return self._plist.pop()
        
    def append( self, item ):
        return self._plist.append( item )
        
if __name__ == '__main__':
    s = _Stack()
    
    [s.append(x) for x in range(10)]
    print([s.pop() for x in range(3)])
    [s.append(x) for x in range(3)]
    
    for x in range(10):
        print(s.pop())
