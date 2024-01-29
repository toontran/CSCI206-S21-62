/*
   Define a simple linked list node where each
   node holds an integer val and a pointer
   to the next node.

   the typedef makes "node" equal "struct node"
   so you don't have to type struct as often       */
typedef struct node {
	int val;
	struct node* next;
} node;

/* create and return a new node */
node* mk_node(int val);

/* de allocate all memory for a list. */
void ll_destroy(node* list);

/* append a node to a non-empty list */
void ll_append(node* list, node* new_node);

/* print the contents of the list */
void ll_print(const node* list);

/* check if lists are the same, meaning
   they contain the same values              */
int ll_equal(const node* a, const node* b);

/* returns 1 if there is a cycle (loop)
   else returns 0 */
int ll_has_cycle(node *head);
