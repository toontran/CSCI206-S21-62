#include <stdio.h>
#include "list.h"

/* The main function exists just to test ll_equal.
   There are two tests. The second one will fail with
	 the given code.
	 Please find the error ll_equal and fix it!

	 Do not change this file (ll_equal.c)!	*/
int main(int argc, char** argv) {
	int i;

	// store pointers for a bunch of nodes, more than we need in fact.
	node *nodes[32] = {};

	// create 10 nodes and append them to the first node
	for (i=0; i<10; i++) {
		// all nodes have the same id, 42
		nodes[i] = mk_node(42);
		if (i > 0){
			// append node i onto the list started by node 0
			ll_append(nodes[0], nodes[i]);
		}
	}

	// should print [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]
	printf("The list of nodes: ");
	ll_print(nodes[0]);

	// should return 1 (true)
	printf("equal test 1 result = %d\n", ll_equal(nodes[0], nodes[0]));

	// should return 0 (false)
	// instead, it causes a Segmentation fault.
	printf("equal test 2 result = %d\n", ll_equal(nodes[0], nodes[2]));

	return 0;
}
