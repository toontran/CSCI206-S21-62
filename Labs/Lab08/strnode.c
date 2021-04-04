#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "strnode.h"

struct strnode *strnode_create(char *s, int length) {
  struct strnode *node;
  node = (struct strnode*) malloc(sizeof(node));
  strcpy(node->str, s);
  node->length = length;
  return node;
}