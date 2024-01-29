#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

int main()
{
  struct stack* stack = stack_create();
  int i;
  float f = 1.0;

  printf("Stacking...\n");
  for (i=1; i <= 15; i++){
    printf("%f\n", f);
    stack_push(stack, &f, sizeof(float));
    f += 1.0;
  }

  printf("Unstacking...\n");
  while (!stack_empty(stack)){
    stack_pop(stack, &f, sizeof(float));
    printf("%f\n", f);
  }
  stack_destroy(stack);
  return 0;
}
