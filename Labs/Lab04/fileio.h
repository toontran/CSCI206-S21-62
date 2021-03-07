#ifndef __fileio_h_
#define __fileio_h_

// for O_RDONLY, etc.
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXBYTES 1024
#define MAXLINES 10
 
//char buffer[MAXLINES][MAXBYTES+1];    // buffer to hold file data   
 
int read_file_bytes (char* filename, int bytes, char* buffer);

int read_file_lines(char* filename, int bytes, char (*buffer)[MAXBYTES+1]);
 
#endif

