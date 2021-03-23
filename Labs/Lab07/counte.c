#include <stdio.h>
#include <stdlib.h>
#define MAX_CHAR 100

int counte(char* s);

int main (int argc, char* argv[]) {
    char inp[MAX_CHAR];
    printf("Enter a string: ");
    fgets(inp, MAX_CHAR, stdin);
    printf("There are %d e's\n", counte(inp));    
    return 0;
}
