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
import time


class FileStats:
    
    def __init__(self, maxSize=0, minSize=sys.maxsize, oldestTime=time.time(), newestTime=0):
        self.maxSize = maxSize
        self.minSize = minSize
        self.oldestTime = oldestTime
        self.newestTime = newestTime
    
    def printResults(self):
        print('maximum size of files : ', self.maxSize)
        print('minimum size of files : ', self.minSize)
        print('oldest time : ', time.asctime( time.localtime(self.oldestTime) ))
        print('newest time : ', time.asctime( time.localtime(self.newestTime) ))

    def update(self, path):
        stats = os.lstat(path)
        
        if stats.st_size < self.minSize:
            self.minSize = stats.st_size
        if stats.st_size > self.maxSize:
            self.maxSize = stats.st_size

        if stats.st_mtime < self.oldestTime:
            self.oldestTime = stats.st_mtime
        if stats.st_mtime > self.newestTime:
            self.newestTime = stats.st_mtime


def listDir ( startDir, MahFileStats ):

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
        for f in os.listdir( path ):
            # Convert it into a complete path, needed for 'isdir()'
            # 'v' will be needed to run 'isdir()' when recursive call is made           
            v = os.path.join( path, f )
            if os.path.isdir( v ):
                dirs.append( v )
            elif os.path.isfile( v ):
                MahFileStats.update(v)
        
        # listDir in each of path in list dirs
        for f in dirs:
            listDir( f, MahFileStats )

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
    # Create object FileStats
    MahFileStats = FileStats()
    # Call listDir which lists directories and files recursively
    # The argument is the starting file(dir)
    listDir( basedir, MahFileStats )
    MahFileStats.printResults()

## end of program

