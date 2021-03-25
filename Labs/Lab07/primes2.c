/* name: Tung Tran
 * time: 
 * real   0m19.074s
 *
 * user 0m18.792s
 *
 * sys  0m0.264s
 *
 */
//#include "prime2.s"
#include <stdio.h> 
#include <stdlib.h>
int is_prime(int n);

int main (int argc, char* argv[])
{
    int i, n = 0, maxnum=80;
    if (argc > 1){
        maxnum = atoi(argv[1]);
    }
	
    for (i = 2; n < maxnum; i++){
        if (is_prime(i)){
            printf("%7d", i);
            n++;
            if ((n % 10) == 0){
                printf("\n");
            }
        }
    }

    return 0;
}