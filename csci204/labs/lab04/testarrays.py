"""
The program tests the classes Array, Array2D, and Matrix

CSCI 204
2013 Fall
"""
from array204 import Array
from array204 import Array2D
from matrix204 import Matrix

# Test the creation of the Array object and its clear() method
print( 'testing arrays ...' )
a = Array( 10 )
a.clear( 0 )

print( 'clear array ...')
print( 'print 10 0s' )

for i in range( len( a ) ):
    print( a[i], ', ', end="" )
    if i+1 % 10 == 0:
        print()
print()


# Test the creation of the Array2D object and its clear() method
print( 'create a 2-D array 10X4 (initialized to 0s)' )
b = Array2D( 10, 4 )
b.clear( 0 )
for i in range( b.num_rows() ):
    for j in range( b.num_cols() ):
        print( b[ i, j ], ' ', end = "" )
    print()

# Test the clear() method with a different value
print( 'set all values to be 3' )
b.clear( 3 )
for i in range( b.num_rows() ):
    for j in range( b.num_cols() ):
        print( b[ i, j ], ' ', end = "" )
    print()


# Test the creation of the Matrix object and its scaleBy() method
c = Matrix( 2, 3 )
print( 'matrix element [1,2]: ', c[ 1, 2 ], ' (should be 0)' )
c[ 1, 2 ] =  4
c.scaleBy( 2 )
print( 'scaled matrix element [1,2]: ', c[ 1, 2 ], ' (should be 8)' )

# Test Matrix mutator (__setitem__) and its traspose() method
for i in range( c.num_rows() ):
    for j in range( c.num_cols() ):
        c[ i, j ] += i + j
d = Matrix( 3, 2 )
d = c.transpose()

print( 'original matrix: ' )
print( c )

print( 'transposed matrix: ' )
print( d )

# Test Matrix multiplication
print( 'matrix e = c X d : ' )
e = c * d
print( e )

# Test Matrix addition
print( 'matrix f = e + e : ' )
f = e + e
print( f )

# Test Matrix subtraction
print( 'matrix g = f - e : ' )
g = f - e
print( g )
