from array204 import Array2D

class Matrix:
    # Create a matrix of size num_rows X num_cols initalized to 0
    def __init__( self, num_rows, num_cols ):
        self._the_grid = Array2D( num_rows, num_cols )
        self._the_grid.clear( None )
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

    # Set the value of element [i,j] toe the value of v3
    def __setitem__( self, ndx_tuple, v ):
        assert len( ndx_tuple ) == 2, "Invalid number of array subscripts."
        self._the_grid[ ndx_tuple[0], ndx_tuple[1] ] = v
    def __str__( self ):
        t=''
        for i in range(self.num_rows()):
            t += '\n'
            for j in range(self.num_cols()):
                t += (str(self[ i , j]) + ' ')

        return t
