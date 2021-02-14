
#include <stdio.h>
#include <string.h>
#include <ctype.h>
 
int main()
{
 
    char string[256];   // store input string
    int i;            	         // loop index
    int len;        	         // store input string length
 
    // this loop will read one line of input at a time
    // if EOF is reached, fgets() will return false, thus the loop will exit.
    while ( fgets(string, 256, stdin) ){
              
        /* convert the string here */
        len = strlen(string);
	for (i=0;i<len;i++) {
	    string[i] = toupper(string[i]);
	}             
        // print the result
        printf("%s", string);
    }
    
    // C main programs return an error code. Typically 0 means No errors.
    return 0;
}
                                                  
