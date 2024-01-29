"""
   This exercise asks students to write a recursive program to visit 
   a Unix direcory tree recursively starting from a giving directory. Print
   only the file name when visiting. 

   Students are not allowed to use the os.walk() method, which
   basically does the recursion.
 
   Date  : Fall 2013
   last-modified: Fall 2019
"""

import os, sys

def listDir ( startDir ):

    """ 
        listDir lists the contents of a starting directory
        and the contents of all its subdirectories recursively.
        
        Input:
           startDir - name of the starting directory
        Output: a complete list of contents of all subdirectories
    """

    # Set the starting directory and retrieve its contents
    path = startDir
    dirs = []

    # Check if the end of path is a forward slash
    if path[-1] == '/':
        path = path[:-1] # Then eliminate the slash

    # Check if a path is not a directory
    if not os.path.isdir( path ):
        print( os.path.basename( path ) )
    else:
        # Print the contents in this directory
        # Append directories into list dirs
        print( '--Entering {}'.format( os.path.basename(path) ) )
        for f in os.listdir( path ):
            # Convert it into a complete path, needed for 'isdir()'
            # 'v' will be needed to run 'isdir()' when recursive call is made
            print( f )            
            v = os.path.join( path, f )
            if os.path.isdir( v ):
                dirs.append(v)
        
        # listDir each path in list dirs
        for f in dirs:
            listDir( f )

        print( '--Leaving {}'.format( os.path.basename(path) ) )
		
## end of listDir()

### If you are running within Idle, comment the next six lines,
### then uncomment the statement with 'input()'
if __name__ == '__main__':
    if len( sys.argv ) != 2:
        print ( "Usage: python dirs.py dirname" )
        sys.exit()
    # Pick up the argument as the base directory
    basedir = sys.argv[1]

## uncomment the following line to use Idle, and indent the 
## line 'listDir( basedir )' properly
#basedir = input('Enter a starting directory or file : ')

    # Call listDir which lists directories and files recursively
    # The argument is the starting file(dir)
    listDir( basedir )

## end of program

