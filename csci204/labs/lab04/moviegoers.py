"""
This is an incomplete program. Students
will have to complete the program as lab exercises.

CSCI 204
2013 Fall
"""
import sys
from array204 import *  # Array and Array2D
from matrix204 import Matrix

class MovieGoers:

    def __init__( self, fileName ):
        # Create the MovieGoers object

        # Initialize data members
        # Completed for you
        self.movies = None   # a 1-D array
        self.people = None   # a 1-D array
        self.data   = None   # list to store raw data read from the file
        self.matrix = None   # Matrix
        self.interestMeasure = None # Matrix

        # Open the input file and read all lines from the file
        ## student work
        ## 1. Open a text file and read all the lines in the file
        f = open(fileName, 'r') 
        self.data = f.readlines()
            
        # Read information from the lines
        ## student work, using a method self.__read_data()
        ## 2. Parse the lines and read the first part of lines
        ##    into two 1-D arrays, self.movies and self.people
        self.__read_data()
        
        # Create matrix based on the data
        ## stduent work
        ## 3. Create the matrix object based on the sizes of the two
        ##    arrays, self.people and self.movies
        self.matrix = Matrix( len(self.people), len(self.movies) )
        

        # Read data into the matrix
        ## student work, using a method self.__read_matrix()
        ## 4. Read the rest of the data (rating matrix) into the self.matrix
        ##    just created.
        self.__read_matrix()

    def __read_data( self ):

        ## student work
        ## convert data from lines in self.data into useful information
        ## so the arrays needed for the matrix can be created
        ## this part reads movies and people
        # Movie
        self.num_movies = int( self.data[0] )
        self.movies = Array( self.num_movies )
        for i in range( 1, self.num_movies+1 ):
            self.movies[ i-1 ] = self.data[ i ]

        # People
        self.num_people = int( self.data[self.num_movies+1] )
        self.people = Array( self.num_people )
        # Including lines that have num of movies and people
        start_idx = self.num_movies + 2 
        end_idx = (self.num_movies+1) + self.num_people
        for i in range( start_idx, end_idx+1 ):
            self.people[ i-start_idx ] = self.data[ i ]

    def __read_matrix( self ):

        ## student work
        ## convert data from lines in self.data into useful information
        ## so the arrays needed for the matrix can be created
        ## this part reads rating matrix
        start_idx = self.num_movies + 2 + self.num_people
        for r in range( start_idx, len(self.data) ):
            nums = self.data[ r ].rstrip('\n').split(' ')
            for c in range( self.num_movies ):
                self.matrix[ r-start_idx, c ] = int( nums[c] )
                      
    def find_common( self ):

        ## student work
        ## this part transposes the rating matrix and
        ## multiply the rating matrix by its transpose
        ## to get the common interest measurement matrix.
        ## print your results.
        print( self.matrix * self.matrix.transpose() )

if __name__ == '__main__':
    if len( sys.argv ) != 2:
        inputfile = input("Name of input file: ")
    else:
        inputfile = sys.argv[1]

    m = MovieGoers( inputfile )
    m.find_common()
