from hashmap import HashMap
import random

"""Test program for hashmap implementation.
First run some small tests to make sure basic operations in hashmap
work correctly. Then run a large test to examine the number of collisions
when different hash and collision resolution methods are used.

You must use the following command via terminal (on a unix system) for this to work:

PYTHONHASHSEED=1 python testhash.py

This is because (as of Python 3.3 for the current 3.6) the built-in hash function
uses a random seed by default. You can also set PYTHONHASHSEED to 1 as an environment
variable (e.g., in a bashsrc file), but this method allows programs that rely on
the built-in hash to stay a bit more secure by default.

**************
Last Updated:   27-Apr-2017, Prof. Chris Dancy
Updates:        Fixed a few bugs
"""

# Create a hashmap
my_map = HashMap(23) # capacity 23, a prime number

# Keys and values for testing
keys = [ 'Hi', 'a', 29, 12, 'b', 'c', 101, 'def', 6, 56, 30]
values = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# key 30 will be a fatal collision

# Set the seed so that we get a consistent answer
random.seed(5)

# Test insertion
print('Testing the add method')
print( 'You will not be able to see this succeed yet.')
for i in range( len( keys ) ):
    print( 'inserting key:', str(keys[ i]) +  ', value:', values[ i]  )
    my_map.add( keys[ i ], values[ i ] )    # (key, value) pair

# Test search
print('\nTesting the peek method (This will work after you write _lookup and add)')
print( 'key Hi should have value 0, it is', my_map.peek( 'Hi' ) )
print( 'key def should have value 7, it is', my_map.peek( 'def' ) )
print( 'key 12 should have value 3, it is', my_map.peek( 12 ) )
print( 'key 6 should have value 8, it is', my_map.peek( 6 ) )

# Test the iterator
print('\nTesting the iterator (This will work after you write the iterator)')
print( 'You should see a key,value pair for each one inserted (10 total).' )
print('You should NOT see a pair for [30,10] since it had a fatal collision.')
for v in my_map:
    print( '['+str(v) + ',' + str(my_map.peek(v)) + ']', end = ' ' )
print()

# Test removal
print('\nTesting the remove method (This will work after you write remove)')
my_map.remove( 3 ) # non existant
my_map.remove( 29 ) # a primary slot
my_map.remove( 'def' ) # a backup slot

print( 'You should no longer see [29,2] or [def,7] in the output (8 pairs total).')
for v in my_map:
    print( '[' + str(v) + ',' + str(my_map.peek(v)) + ']', end = ' ' )
print()

print('\nTesting the peek method again (This will work after you write remove)')
print( 'key Hi should have value 0, it is', my_map.peek( 'Hi' ) )
print( 'key def should be "None", it is', my_map.peek( 'def' ) )
print( 'key 12 should have value 3, it is', my_map.peek( 12 ) )
print( 'key 6 should have value 8, it is', my_map.peek( 6 ) )

# Test removal
print('\nTesting a combo of add and remove (This will work after you write remove)')
my_map.remove( 6 ) # a backup slot when the primary slot is empty

print( 'You should no longer see [6,8] in the output (7 pairs total).')
for v in my_map:
    print( '[' + str(v) + ',' + str(my_map.peek(v)) + ']', end = ' ' )
print()

# Print stats
print('\nTesting statistics (This will work after you count collisions)')
print( 'You should see 7 entries and 2 collisions.')
my_map.printStats()

# Now a large set of random data to test collisions
key = []
value = []
my_map = HashMap(23) # capacity 23, a prime number
for i in range ( 1200 ):     # Generate 1,200 pairs of key and value
    key.append( random.randint( 1, 1000000 ) )
    value.append( i )
    my_map.add( key[ i ], value[ i ] )

# Print stats
print('\nTesting statistics with small capacity (This will work after you count collisions)')
print( 'You should see 23 entries and 1185 collisions.')
print( len( key ), ' key/value pairs generated.' )
my_map.printStats()

# Now a large set of random data to test collisions
key = []
value = []
my_map = HashMap(1277) # capacity 1277, a prime number
for i in range ( 1200 ):     # Generate 1,200 pairs of key and value
    key.append( random.randint( 1, 1000000 ) )
    value.append( i )
    my_map.add( key[ i ], value[ i ] )

# Print stats
print('\nTesting statistics with large capacity (This will work after you count collisions)')
print( 'You should see 938 entries and around 484 collisions.')
print( len( key ), ' key/value pairs generated.' )
my_map.printStats()
