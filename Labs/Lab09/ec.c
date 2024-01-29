/* ec.c FACTORIAL test */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "bigint.h"

int main(int argc, char* argv[]){
  struct bigint *a = bigint_init("110010", 512); // 50
  struct bigint *b = bigint_init("", 512);

  char a_str[512];
  char b_str[512];

  bigint_hexstr(a_str, a);
  bigint_fact(b, a);      // a!, factorial
  bigint_hexstr(b_str, b);

  printf("   %s! = %s\n", a_str, b_str);
  free(a);
  free(b);

  return 0;
}
