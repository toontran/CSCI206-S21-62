#include <stdio.h>
#include "list.h"

int main(int argc, char* argv[]){

  int i;
  node* head = mk_node(1);

  for (i=0; i<8; i++) {
    ll_append(head, mk_node(i+10));
  }

  ll_print(head);

  
  return 0;
}
