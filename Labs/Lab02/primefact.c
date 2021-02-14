/* Tung Tran
 * date/ 1:20 - 3:10
 * lab 02 - primefact.c
 * compile with: make primefact
 * notes: none
 */
#include <stdio.h>
 
int main(void) 
{
    int n = 2147483645;
    int i = 2;
     
    while (i <= n) {
	if (n % i == 0) {
	    printf("%d\n", i);
	    n = n / i;
	} else i = i + 1;
    }
 
    return 0;
}

