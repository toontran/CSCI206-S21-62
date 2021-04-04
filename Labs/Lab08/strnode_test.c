#include <stdio.h>
#include <string.h>
#include "strnode.h"

// global variables (data segment)
struct strnode *n1, *n2, *n3, *p;

int main(int argc, char *argv[]) {

  // create strnodes
  n1 = strnode_create("hello", 5);
  n2 = strnode_create("there", 5);
  n3 = strnode_create("prof", 4);

  printf("strnode_test running...\n");

  // manually "link" the nodes together.
  n1->next = n2;
  n2->next = n3;
  n3->next = NULL;

  // p points to node n1 initially
  p = n1;

  while (p != NULL) {
    printf("str: %s - length: %d\n", p->str, p->length); 
    p = p->next;
  }

  return 0;
}

