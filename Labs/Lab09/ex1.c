/* ex1.c */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "bigint.h"

int main(int argc, char* argv[]){
  struct bigint *a = bigint_init("1011", 4);
  char a_str[8];

  bigint_str(a_str, a);

  printf("%d, %s\n", a->N, a_str);

  free(a);

  return 0;
}
