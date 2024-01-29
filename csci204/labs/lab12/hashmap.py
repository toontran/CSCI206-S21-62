"""Implementation of the Map ADT using closed hashing and a probe with 
double hashing.

This is an incomplete file, students will have to fill in the missing
parts to make the hash map work correctly.
"""

class HashMap :
  """ A closed hashing (one key per slot) with a double hashing
      probe (one hash function that maps into two different capacities)"""

  def __init__( self, capacity):                                     
    """Creates an empty map instance."""

    # Define the size of the table
    self.CAP = capacity

    # Create the data storage (empty hash table)
    self._array = [None] * self.CAP

    # how many items in the array
    self._size = 0
    
    # how many collisions so far
    self._collisions = 0
      
  def __len__( self ):
    """Returns the number of entries in the map."""
    return self._size

  def _hash1( self, key ):                               
    """The main hash function for mapping keys to table entries."""
    return abs( hash( key ) ) % len( self._array )
  
  def _hash2( self, key ):
    """ The second hash function used for backup."""
    return 1 + abs( hash( key ) ) % ( len( self._array ) - 2 )    
  
  def add( self, key, value ):
    """ If the key does not exist, adds a new entry to the map.
        If the key exists, update its value.
    """
    ## STUDENTS WILL COMPLETE THE REST OF THIS METHOD
    map_entry = _MapEntry(key, value)
    
    slot, contents = self._lookup(self._hash1, key)
    if contents == None:
        if slot == None:
            # Another key exists and we have to change hash function
            self._collisions += 1
        else:
            # The key does not exist -> just add
            self._array[slot] = map_entry
            self._size += 1    
            return
    else:
        # Key exists, update its value
        self._array[slot] = map_entry
        self._size += 1
        return
        
    slot, contents = self._lookup(self._hash2, key)
    if contents == None:
        if slot == None:
            #print("FATAL")
            # FATAL
            return
        else:
            # The key does not exist -> just add
            self._array[slot] = map_entry
            self._size += 1    
    else:
        # Key exists, update its value
        self._array[slot] = map_entry
        self._size += 1
            
      
  def peek( self, key ):
    """ Returns the value associated with the key or returns None."""
    slot,contents = self._lookup(self._hash1, key)
    if contents == None:
      slot,contents = self._lookup(self._hash2, key)
      
    if contents == None:
      return None
    else:
      return contents.value

  def _lookup(self, hashFunction, key):
    """ This function returns a tuple with two values.
        If the slot it should occupy contains the matching key, it 
        returns (slot, contents).
        If the slot it should occupy is empty it returns (slot,None).
        If the slot it should occupy has other contents, it returns 
        (None,None). """
    # Compute the slot.
    slot = hashFunction( key )
    contents = self._array[slot]
    
    ## STUDENTS WILL COMPLETE THE REST OF THIS METHOD
    if contents == None:
        return slot, None
    elif contents.key == key:
        return slot, contents
    elif contents.key != key:
        return None, None
    else:
        raise("Look up has something wrong!")
    
  def __iter__(self):
    """ Return an iterator for the hashmap. """
    ## STUDENTS WILL COMPLETE THE REST OF THIS METHOD
    for contents in self._array:
        if contents == None:
            continue
        else:
            yield contents.key
  
  def printStats( self ):
    """Print the number of items in the table and the total
    number of collisions due to insertion."""
    print( 'Entry count : ', self._size )
    print( 'Collision count : ', self._collisions )

  def remove( self, key ):
    """ Removes the entry associated with the key.
        If the key is not in the map, does nothing. """
    ## STUDENTS WILL COMPLETE THE REST OF THIS METHOD
    slot, contents = self._lookup(self._hash1, key)
    if contents == None:
        #The key does not match -> change hash function
            pass
    else:
        # Key exists, update its value
        self._array[slot] = None
        self._size -= 1
        return contents
        
    slot, contents = self._lookup(self._hash2, key)
    if contents == None:
        # Key does not match again, key doesn't exist
        print("Not in our Hash Table")   
    else:
        # Key exists, update its value
        self._array[slot] = None
        self._size -= 1
        return contents

# Storage class for holding a key/value pair.   
class _MapEntry :                       

  def __init__( self, key, value ):
    """Create the entry with key and value """
    self.key = key
    self.value = value 
  
  def __eq__( self, other ):
    """Overload __eq__ so key, value pairs can be compared using '==' """
    if other == None:
      return False
    return ( self.key == other.key and self.value == other.value )

## STUDENTS WILL PUT AN ITERATOR CLASS HERE.

