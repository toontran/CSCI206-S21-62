/* ex3.c MULT test */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "bigint.h"

int main(int argc, char* argv[]){
  struct bigint *a = bigint_init("1001", 8);  // 9
  struct bigint *b = bigint_init("1100", 8);  // 12
  struct bigint *c = bigint_init("", 8);     // 0
  char a_str[16];
  char b_str[16];
  char c_str[16];

  bigint_str(a_str, a);
  bigint_str(b_str, b);

  bigint_mult(c, a, b);    // 9 * 12 = 108 = 0b1101100
  bigint_str(c_str, c);

  printf("MULT test\n");
  printf("   %s\n", a_str);
  printf("x  %s\n", b_str);
  printf("------------\n");
  printf("   %s\n", c_str);

  free(a);
  free(b);
  free(c);

  return 0;
}
