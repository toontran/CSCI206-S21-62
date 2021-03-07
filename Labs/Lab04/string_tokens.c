//#include <stdio.h>
//#include <stdlib.h>
//#include <string.h>
#include "fileio.h"

int main(int argc, char *argv[])
{
    char *str1, *token;
    char *saveptr1;
    char * delim = " ;=$(){}#+,<>\"[]*'/!%&:\\\n\r\t";
    char buffer[MAXBYTES+1];
    int j;

    if (argc != 3) {
        fprintf(stderr, "Usage: %s filename num_tok\n",
                       argv[0]);
        exit(EXIT_FAILURE);
    }
    
    if (read_file_bytes(argv[1], MAXBYTES, buffer) < 0) {
        printf("Error: could not read file!\n");
        exit(-3);
    }

    for (j = 1, str1 = buffer; j<=atoi(argv[2]); j++, str1 = NULL) {
        token = strtok_r(str1, delim, &saveptr1);
        if (token == NULL)
            break;
        printf("%d: %s\n", j, token);

        //for (str2 = token; ; str2 = NULL) {
        //    subtoken = strtok_r(str2, argv[3], &saveptr2);
        //    if (subtoken == NULL)
        //        break;
        //   printf(" --> %s\n", subtoken);
        //}
    }
    
           exit(EXIT_SUCCESS);
}
