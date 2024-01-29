"""Drive method in priority queue lab"""
import time       # for timing
import random     # for random numbers

"""Change to different implmenetation as needed"""
from PriorityQ import PriorityQueue as MyQueue
#from FastPriorityQ import FastPriorityQueue as MyQueue

def test_queue(q, name):
    """ Test your Queue. """

    outfname = name + '.txt'
    q.enqueue( 3, "Shampoo carpets" )
    q.enqueue( 7, "Empty trash" )
    q.enqueue( 8, "Water plants" )
    q.enqueue( 10, "Remove pencil sharpened shavings" )
    q.enqueue( 6, "Replace light bulb" )
    q.enqueue( 1, "Fix broken sink" )
    q.enqueue( 6, "Pet the dog" )
    q.enqueue( 9, "Clean coffee maker" )
    q.enqueue( 2, "Order cleaning supplies" )
    q.enqueue( 6, "Take a nap" )
    file = open( outfname, 'w' )
    while len(q) > 0:
        file.write( q.dequeue() + "\n" )
    file.close()
    print("Done creating", outfname)

def time_enqueue( q, name ):
    """Test how long it takes to complete the operations"""
    print("Testing time to enqueue.")
    start = time.time()
    for i in range( 10000 ):             # the number of items
        p = random.randint( 0, 10 )      # priority values
        v = random.randint( 0, 10000 )   # some random values
        q.enqueue( p, v )
    end = time.time()
    print( "Time to enqueue 10000 items in the", name, "is {0:.8f} us.".format( end - start ) )
    
def time_dequeue( q, name ):
    """Test how long it takes to complete the operations"""
    print("Testing time to dequeue.")
    
    for i in range( 10000 ):             # the number of items
        p = random.randint( 0, 10 )      # priority values
        v = random.randint( 0, 10000 )   # some random values
        q.enqueue( p, v )
        
    start = time.time()
    for i in range( 10000 ):             # the number of items
        q.dequeue()
    end = time.time()
    print( "Time to dequeue 10000 items in the", name, "is {0:.8f} us.".format( end - start ) )

def time_few_priorities( q, name ):
    """Test how long it takes to complete the operations"""
    print("Testing time to enqueue.")
    start = time.time()
    for i in range( 10000 ):             # the number of items
        p = random.randint( 0, 2 )      # priority values
        v = random.randint( 0, 10000 )   # some random values
        q.enqueue( p, v )
    end = time.time()
    print( "Time to enqueue 10000 items in the", name, "is {0:.8f} us.".format( end - start ) )
    
def time_interleaved_enq_deq( q, name, percentage ):
    """Test how long it takes to complete the operations"""
    print("Testing time to enqueue.")
    start = time.time()
    count = 100
    for i in range( 10000 ):             # the number of items
        p = random.randint( 0, 10 )      # priority values
        v = random.randint( 0, 10000 )   # some random values
        q.enqueue( p, v )
        count -= 1
        if count == 0:
            for i in range( percentage ):
                q.dequeue()
            count = 100
    end = time.time()
    print( "Time to enq deq 10000 items in the", name, "is {0:.8f} us.".format( end - start ) )
    
def time_enqueue_before_dequeue( q, name ):
    """Test how long it takes to complete the operations"""
    print("Testing time to enqueue.")
    start = time.time()
    for i in range( 10000 ):             # the number of items
        p = random.randint( 0, 10 )      # priority values
        v = random.randint( 0, 10000 )   # some random values
        q.enqueue( p, v )
        
    for i in range( 10000 ):             # the number of items
        q.dequeue()
        
    end = time.time()
    print( "Time to enq before deq 10000 items in the", name, "is {0:.8f} us.".format( end - start ) )
"""
Various tests follow.
We use a generic queue class MyQueue here. Change the 'import' statement
at the top of the program to a different queue implementation as needed.
"""

"""
Note that the string representation of the queue will be used in various
printing statements. Make sure you implement the __str__() method properly
before running the following tests.
"""
# test some basic operations
q = MyQueue()
test_queue( q, str(q) )

# test enqueue
q = MyQueue()
#time_enqueue( q, str(q) )

"""
Students have to implement the following methods, following the
lab instructions. Uncomment proper segments to test the method
that has been implemented.


# test dequeue
q = MyQueue()
time_dequeue( q, str(q) )

# test with fewer priority classes
q = MyQueue( 3 )
time_few_priorities( q, str(q) )
"""

# test interleaved enqueue and dequeue, the third parameter specifies
# the percentage of dequeue operations
q = MyQueue()
time_interleaved_enq_deq( q, str(q), 50 )

# test evenly distributed queue, but enqueues take place before dequeue
q = MyQueue()
time_enqueue_before_dequeue( q, str(q) )

