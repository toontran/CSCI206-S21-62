#include "fileio.h"

int read_file_bytes (char* filename, int bytes, char* buffer)
/*
 * Reads byte data from a file and appends a null terminator (byte value of zero, 0).
 * 
 *  filename: full path and filename to read from.
 *  bytes: maximum number of bytes to read.
 *  buffer: where to put the read data (note need bytes+1!).
 *  Return value: number of bytes read or -1 on error.
 */
{
    // your code here
    FILE *file_ptr = fopen(filename, "r");
    int bytes_read = fread(buffer, 1, bytes * sizeof(char), file_ptr); 
    buffer[bytes_read] = '\0';
    return bytes_read;
}

int read_file_lines(char* filename, int bytes, char (*buffer)[MAXBYTES+1]) {
    //char buffer[MAXLINES][MAXBYTES+1];    // buffer to hold file data    
    FILE *file_ptr = fopen(filename, "r");
    int lines_read = 0;
    printf("%s", buffer[0]);
    while (lines_read < MAXLINES && fgets(buffer[lines_read], bytes, file_ptr)) 
        lines_read += 1;
    return lines_read;
}
   
