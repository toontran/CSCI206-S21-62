#ifndef _stack_h_
#define _stack_h_

#include "stack.h"

struct stack {
  struct node* top;
};

struct stack *stack_create();
int stack_empty(struct stack *s);
void stack_destroy(struct stack *s);
void stack_push(struct stack* s, void* src, int size);
void stack_pop(struct stack* s, void* dest, int size);

#endif
