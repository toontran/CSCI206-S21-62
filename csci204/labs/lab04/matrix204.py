"""
This is a partial implementation of the Matrix ADT using a 2-D array. Students
will have to complete this class before other lab exercises.

The code is from the textboook "Data Structures and Algorithms Using Python"
by Rance D. Necaise

CSCI 204
Fall 2013

Students need to modify this file according to the lab description
"""
from array204 import Array2D

class Matrix:
    # Create a matrix of size num_rows X num_cols initalized to 0
    def __init__( self, num_rows, num_cols ):
        self._the_grid = Array2D( num_rows, num_cols )
        self._the_grid.clear( 0 )


    # Return the number of rows in the matrix
    def num_rows( self ):
        return self._the_grid.num_rows()

    # Return the number of colums in the matrix
    def num_cols( self ):
        return self._the_grid.num_cols()

    # Return the value of element at (i, j): x[i, j]
    def __getitem__( self, ndx_tuple ):
        assert len( ndx_tuple ) == 2, "Invalid number of array subscripts."
        return self._the_grid[ ndx_tuple[0], ndx_tuple[1] ]

    # Set the value of element [i,j] toe the value of v
    def __setitem__( self, ndx_tuple, v ):
        assert len( ndx_tuple ) == 2, "Invalid number of array subscripts."
        self._the_grid[ ndx_tuple[0], ndx_tuple[1] ] = v

    # Scale the matrix by the given scalar
    def scaleBy( self, scalar ):
        for r in range( self.num_rows() ):
            for c in range( self.num_cols() ):
                self[ r, c ] *= scalar

    # Create and returns a new matrix that is the result from matrix addition
    def __add__( self, rhs_matrix ):
        assert rhs_matrix.num_rows() == self.num_rows() and \
            rhs_matrix.num_cols() == self.num_cols(), \
            "Matrix size not compatible in the two matrices."

        new_matrix = Matrix( self.num_rows(), self.num_cols() )
        for r in range( self.num_rows() ):
            for c in range( self.num_cols() ):
                new_matrix[ r, c ] = self[ r, c ] + rhs_matrix[ r, c ]

        return new_matrix

######### The following operations will be implemented by students #######
######### as a set of lab exercises.                               #######


    # Create and return a new matrix that is the transpose of the original
    def transpose( self ):
        new_matrix = Matrix( self.num_cols(), self.num_rows() )
        for r in range( self.num_cols() ):
            for c in range( self.num_rows() ):
                new_matrix[ r, c ] = self[ c, r ]
        return new_matrix

    # Return a string form
    def __str__( self ):
        result = ''
        for r in range( self.num_rows() ):
            for c in range( self.num_cols() ):
                result += str( self[ r, c ] ) + ' '
            result += '\n'
        return result

    # Create and return a new matrix that results from matrix subtraction
    # Basically like the addition method
    def __sub__( self, rhs_matrix ):
        assert rhs_matrix.num_rows() == self.num_rows() and \
            rhs_matrix.num_cols() == self.num_cols(), \
            "Matrix size not compatible in the two matrices."

        new_matrix = Matrix( self.num_rows(), self.num_cols() )
        for r in range( self.num_rows() ):
            for c in range( self.num_cols() ):
                new_matrix[ r, c ] = self[ r, c ] - rhs_matrix[ r, c ]

        return new_matrix

    # Create and return a new matrix that results from matrix multiplication
    def __mul__( self, rhs_matrix ):
        assert  self.num_cols() == rhs_matrix.num_rows(), \
               "Matrix size not compatible in the two matrices."

        new_matrix = Matrix( self.num_rows(), rhs_matrix.num_cols() )
        for r in range( self.num_rows() ):
            for c in range( rhs_matrix.num_cols() ):

                # Sum of multiples
                new_matrix[ r, c ] = 0
                for elem in range( self.num_cols() ):
                    new_matrix[ r, c ] += self[ r, elem ] * \
                                          rhs_matrix[ elem, c ]

        return new_matrix
