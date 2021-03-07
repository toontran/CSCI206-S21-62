/* Tung Tran
 * date/ 1:20 - 3:10
 * lab 04 - calc.c
 * compile with: 
 * notes: none
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int main(int argc, char* argv[]) 
{
    int i = 0;
    float result = 0;

    if ((argc < 3)) {
        printf("Usage: ./calc <operation> <arguments..>\n");
        return 0;
    }

    for (i=2; i < argc; i++) {
        if (strcmp(argv[1], "add") == 0) {
            result += atof(argv[i]);       
        } else if (strcmp(argv[1], "mult") == 0) {
            if (result == 0) result = 1;
            result *= atof(argv[i]);
        } else if (strcmp(argv[1], "div") == 0) {
            if (i == 2) {
                result = atof(argv[i]);
            } else if (i == 3) {
                result /= atof(argv[i]);
            } else {
                printf("Invalid arguments: div only takes 2 arguments\n");
                return 1;
            }
        } else if (strcmp(argv[1], "len") == 0) {
            result += strlen(argv[i]);
        } else {
            printf("Unsupported function, try: add, mult, div, or len\n");
            return 1;
        }               
    }

    printf("%.6f\n", result);
     
    return 0;
}

