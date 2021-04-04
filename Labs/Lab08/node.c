#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "node.h"

struct node *node_create(void *data, int size) {
  struct node *node;
  node = (struct node*) malloc(sizeof(node));
  node->data = malloc(size);
  memcpy(node->data, data, size);
  return node;
}

void node_destroy(struct node *n) {
  // Ignore unused result warning:
  // https://stackoverflow.com/questions/40576003/ignoring-warning-wunused-result
  (void)!realloc(n->data, 0);
  (void)!realloc(n, 0); 
}