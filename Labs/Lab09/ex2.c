/* ex2.c ADD test */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "bigint.h"

int main(int argc, char* argv[]){
  struct bigint *a = bigint_init("1001", 8);  // 9
  struct bigint *b = bigint_init("1100", 8);  // 12
  struct bigint *c = bigint_init("", 8);      // 0
  char a_str[16];
  char b_str[16];
  char c_str[16];

  bigint_str(a_str, a);
  bigint_str(b_str, b);

  bigint_add(c, a, b);     // 21 = 10101
  bigint_str(c_str, c);

  printf("ADD test\n");
  printf("   %s\n", a_str);
  printf("+  %s\n", b_str);
  printf("------------\n");
  printf("   %s\n", c_str);

  free(a);
  free(b);
  free(c);

  return 0;
}
