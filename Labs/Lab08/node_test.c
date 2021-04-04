#include <stdio.h>
#include <string.h>
#include "node.h"

// global variables (data segment)
struct node *n1, *n2, *n3, *p;

int main(int argc, char *argv[]) {

  // create strnodes
  n1 = node_create("hello", 6);
  n2 = node_create("there", 6);
  n3 = node_create("prof", 5);

  printf("node_test running...\n");

  // manually "link" the nodes together.
  n1->next = n2;
  n2->next = n3;
  n3->next = NULL;

  // p points to node n1 initially
  p = n1;

  while (p != NULL) {
    printf("str: %s - length: %zd\n", (char*)p->data, strlen((char*)p->data)); 
    p = p->next;
  }

  // deallocate
  node_destroy(n1);
  node_destroy(n2);
  node_destroy(n3);
    
  return 0;
}

