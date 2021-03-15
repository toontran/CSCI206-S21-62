#include <stdio.h>
#define MAX_ITEMS 100

int collatz(int n)
{
    // implement this function to return
    // if n is 1: 1
    // if n is even: n / 2 
    // if n is odd: 3 * n + 1
    // checking for even/oddness in C is a debatable topic:
    // http://stackoverflow.com/questions/160930/how-do-i-check-if-an-integer-is-even-or-odd
    if (n % 2 == 0) return n / 2;
    else return (3 * n) + 1;
}

int find_length(int n)
{
    // TODO: implement a recursive function to count the number of
    // calls to collatz needed to reach 1 starting with n.
    // Note that you need to *count* the number of calls.
    // If the value of n is greater than 1, the find_length() function
    // would call the collatz function recursively.
    int length = 1;
    while (n!=1) {
        length += 1;
        n = collatz(n);
    }
        
    return length;
}

int main(void)
{
    int i;

    for (i = 1; i < MAX_ITEMS; i ++){
        printf ("%d ==> %d\n", i, find_length(i));
    }

    return 0;
}
