""" Quicksort and Efficiency lab, CSCI 204 """

from random import *
from statistics import median

counter = 0


def quicksort( myList, first, last ):
    """ Sort the given list using the quicksort algorithm. Sorts the
        portion of the list between the first and last indices (inclusive).
    """
    # Count key comparisons
    global counter
    
    if first == 0 and last == len(myList)-1:
        counter = 0
    
    # base case: done when the indices touch or overlap.
    if first >= last: return

    # recursive case: partition the myList and recurse on both sides
    split = partition( myList, first, last )
    quicksort( myList, first, split-1 )
    quicksort( myList, split+1, last )

def partition( myList, first, last ):
    """ Partition the given list into two parts. The first part will
        contain smaller values, the second part will contain larger values.
        There will be a pivot value between them. Partitions the
        portion of the list between the first and last indices (inclusive).
        Return the index of the pivot element.
    """
    # We will track to index of the last number we found for the 'small' side.
    # We starts out with: "pivot, smalls, lastSmall, larges, unchecked".
    # Every time we find a small value in the unchecked section, we swap it
    # with the first large and label it as the new lastSmall.
    # In the end, we will have: "pivot, smalls, lastSmall, larges"
    # and we will swap the pivot and the lastSmall so the order is
    # "smalls, pivot, larges".
    
    # Count key comparison
    global counter

    lastSmall = first

    # Seperate the list into "pivot, smalls, lastSmall, larges".
    for i in range( first+1, last+1 ): # first+1 ... last (inclusive)
        # if myList[i] is small, swap it onto the 'small' side.
        counter += 1
        if myList[ i ] <= myList[ first ]:
            lastSmall = lastSmall + 1
            swap( myList, lastSmall, i )

    # Swap the pivot with lastSmall to get "smalls, pivot, larges".
    swap( myList, first, lastSmall )

    # Return the location of the pivot
    return lastSmall
    
def quicksortm( myList, first, last ):
    """ Faster quicksort """
    # Count key comparisons
    global counter
    
    if first == 0 and last == len(myList)-1:
        counter = 0
    
    # base case: done when the indices touch or overlap.
    if first >= last: return

    # recursive case: partition the myList and recurse on both sides
    split = partitionm( myList, first, last )
    quicksortm( myList, first, split-1 )
    quicksortm( myList, split+1, last )

def partitionm( myList, first, last ):
    """ Partition """    
    # Count key comparison
    global counter

    lastSmall = first
    
    median = find_median( myList, first, last)
    swap( myList, first, median )

    # Seperate the list into "pivot, smalls, lastSmall, larges".
    for i in range( first+1, last+1 ): # first+1 ... last (inclusive)
        # if myList[i] is small, swap it onto the 'small' side.
        counter += 1
        if myList[ i ] <= myList[ first ]:
            lastSmall = lastSmall + 1
            swap( myList, lastSmall, i )

    # Swap the pivot with lastSmall to get "smalls, pivot, larges".
    swap( myList, first, lastSmall )

    # Return the location of the pivot
    return lastSmall

def swap( myList, first, second ):
    """ Swap the items at the first and second indices in the given list.
        Assumes the indices are legal and occupied in the list.
    """
    tmp = myList[ first ]
    myList[ first ] = myList[ second ]
    myList[ second ] = tmp
    
def find_median( arr, first, last ):
    mid = (first + last)//2
    if arr[last] < arr[first]:
        swap(arr, first, last)        
    if arr[mid] < arr[first]:
        swap(arr, mid, first)
    if arr[last] < arr[mid]:
        swap(arr, last, mid)
    return mid

def main():
    
    # Task 1
    test_list = [randint(0,10) for x in range(10)]
    print(test_list)
    
    quicksort(test_list, 0, 9)
    print(test_list)
    
    test_list_sorted = [x for x in range(10)]
    print(test_list_sorted)
    quicksort(test_list, 0, 9)
    print(test_list_sorted)
    
    
    # Task 2
    outru = open('outrm', 'w')
    outsu = open('outsm', 'w')
    
    for i in range(3, 15):
        test_list = [randint(0, 20000) for x in range(2**i)]
        quicksortm( test_list, 0, len(test_list)-1 )
        print( 2**i, counter )
        outru.write( '{} {}\n'.format(len(test_list), counter) )
        
    test_list_sorted = [x for x in range(2**14)]
    quicksortm( test_list_sorted, 0, len(test_list_sorted)-1 )
    print( len(test_list_sorted), counter )
    outsu.write( '{} {}'.format(len(test_list_sorted), counter) )
    
    outru.close()
    outsu.close()
    print( "Done" )

main()





""" Controls the creation of lists, calling of quicksort, and data output.

                    ____________Lab Hints____________
        Recall that the exponent operator in Python 3.5 is ** so 2**3 is 8.

        You might want to use either a global variable or a class attribute to count key comparisons.

        Use a list comprehension to get a list of all the sizes you need to test.

        Use randint(from,to_inclusive), such as randint(0,20000) to get random integers between 0 and 20,000.

        Use range(to_exclusive) to get sorted integers. Convert the resulting iterator
        into a list using list().

        Because Python 3.2 has a maximum depth for the recursive calls it allows, you
        will only be able to test sizes 2^3..2^9 for the sorted, unmodified. You can test
        the full 2^3..2^14 for the other three cases.

        You should write seperate code to generate all four cases since you will need to
        run them repeatedly. (Do not delete code for one case to write the next one).

        Write the output for your four cases into the four files using the open(), write(),
        and close() methods. If you need to print a line break, remember that \n is a
        newline character.

        Print a test run of 10 numbers to standard output for each case to make sure your
        Quicksort is still actually sorting. (use the numbers 0..9 for both the random and
        sorted so you can eyeball the results and know they are ok).
"""
