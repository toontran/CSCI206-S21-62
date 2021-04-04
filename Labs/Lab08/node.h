#ifndef NODE_H_
#define NODE_H_

#define STRLEN 100
struct node {
    void* data;
    struct node *next;
};

struct node *node_create(void *data, int size);
void node_destroy(struct node *n);

#endif
