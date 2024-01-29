/* ex4.c DIV test */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "bigint.h"

int main(int argc, char* argv[]){
  struct bigint *a = bigint_init("1001010", 16);  // 74 = dividend
  struct bigint *b = bigint_init("10101", 16);    // 21 = divisor
  struct bigint *quo = bigint_init("", 16);       // 0
  struct bigint *rem = bigint_init("", 16);       // 0

  char a_str[32];
  char b_str[32];
  char q_str[32];
  char r_str[32];

  bigint_str(a_str, a);
  bigint_str(b_str, b);

  bigint_div(quo, rem, a, b);    //74/21 = 3 R 11

  bigint_str(q_str, quo);
  bigint_str(r_str, rem);

  printf("DIV test\n");
  printf("   %s\n", a_str);
  printf("   --------- --------- = %s R %s \n", q_str, r_str);
  printf("   %s\n", b_str);

  free(a);
  free(b);
  free(quo);
  free(rem);

  return 0;
}
