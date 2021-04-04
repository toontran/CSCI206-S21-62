#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "stack.h"
#include "node.h"

struct stack *stack_create(){
    struct node *n;
    struct stack *s = (struct stack *)malloc(sizeof(n));
    s->top = NULL;
    return s;
}

int stack_empty(struct stack *s){
    if (s->top == NULL) return 1;
    return 0;
}

void stack_destroy(struct stack *s){
    struct node *p, *tmp;
    
    if (stack_empty(s)) (void)!realloc(s, 0); 
    // Loop through linked list and destroy
    else {
        p = s->top;
        while (p != NULL) {
            tmp = p;
            p = p->next;
            node_destroy(tmp);
        }
    }
}

void stack_push(struct stack* s, void* src, int size){
    struct node *new_node = node_create(src, size);
    new_node->next = s->top;
    s->top = new_node;
}

void stack_pop(struct stack* s, void* dest, int size){
    struct node *top_node;
    memcpy(dest, s->top->data, size);
    top_node = s->top;
    s->top = s->top->next;
    node_destroy(top_node); 
}