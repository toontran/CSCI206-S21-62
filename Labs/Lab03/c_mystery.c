/* Tung Tran
 * date/ 1:20 - 3:10
 * lab 02 - c_mystery.c
 * compile with: replicate mystery.asm
 * notes: none
 */
#include <stdio.h>
 
int main(void) 
{
    int x = 89;
    int s = 0;
    int i = 0;    

    do {
        s += i;
	i += 1;
    } while (i <= 10);

    x = s;    
 
    return 0;
}

