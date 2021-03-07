/* your name: Tung Tran
 * date/time of your lab section: 1:50pm
 * lab 04 - head.c
 * compile with:
 * notes: none
 */

// for O_RDONLY, etc.
#include "fileio.h"

//char buffer[MAXLINES][MAXBYTES+1];    // buffer to hold file data

int main(int argc, char* argv[])
{
    int readbytes = 1024;         // default to 10 bytesi
    char buffer[MAXLINES][MAXBYTES+1];    // buffer to hold file data
    int i;
    
    if (argc < 2){
        // missing required argument
        printf("Usage %s <filename> [<bytes>]\n", 
        argv[0]);
        exit(-1);
    }
    if (argc > 2){
        // process optional bytes argument
        readbytes = atoi(argv[2]);
        if (readbytes > MAXBYTES){            
            printf("bytes is too large, max supported value is %d!\n",
                    MAXBYTES);
            exit(-2);
        }
    }
    //read_file_lines(argv[1], readbytes);
    if (read_file_lines(argv[1], readbytes, buffer) >= 0){
        for (i=0;i<MAXLINES;i++) printf("%s", buffer[i]);
    } else {
        printf("Error: could not read file!\n");
        exit(-3);
    }
    return 0;
}


