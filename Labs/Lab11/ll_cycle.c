#include <stdio.h>
#include "list.h"

void test_ll_has_cycle(void) {
	int i;

	/* ---------------- Test 1 ---------------- */
	/* a simple list of 4 nodes, no cycles */
	node *head = mk_node(0);
	for (i=1;i<3;i++)
	ll_append(head, mk_node(i));

	printf("Checking first list for cycles. There should be none, ll_has_cycle says it has %s cycle\n", ll_has_cycle(head)?"a":"no");

/* ---------------- Test 2 ---------------- */
/* a list where the last element loops to the begining of the list */
	head = mk_node(4);
	for (i=6;i<10;i++)
		ll_append(head, mk_node(i));
	node *loop = mk_node(10);
	loop->next = head;
	ll_append(head, loop);

	printf("Checking second list for cycles. There should be a cycle, ll_has_cycle says it has %s cycle\n", ll_has_cycle(head)?"a":"no");

	/* ---------------- Test 3 ---------------- */
	/* a list where a cycle is created in the middle of the list */
	head = mk_node(11);
	node* middle = NULL;
	for (i=11;i<17;i++){
		if (i==14){
			middle = mk_node(i);
			ll_append(head, middle);
		}
		else{
			ll_append(head, mk_node(i));
		}
	}
	loop = mk_node(17);
	loop->next = middle;
	ll_append(head, loop);

	printf("Checking third list for cycles. There should be a cycle, ll_has_cycle says it has %s cycle\n", ll_has_cycle(head)?"a":"no");

	/* ---------------- Test 4 ---------------- */
	/* a list with a single node that loops back to itself */
	head = mk_node(18);
	head->next = head;

	printf("Checking fourth list for cycles. There should be a cycle, ll_has_cycle says it has %s cycle\n", ll_has_cycle(head)?"a":"no");

	/* ---------------- Test 5 ---------------- */
	/* just a plain old list, no cycle */
	head = mk_node(19);
	for (i=19;i<22;i++)
		ll_append(head, mk_node(i));
	printf("Checking fifth list for cycles. There should be none, ll_has_cycle says it has %s cycle\n", ll_has_cycle(head)?"a":"no");

	/* ---------------- Test 6 ---------------- */
	/* the null list */
	printf("Checking length-zero list for cycles. There should be none, ll_has_cycle says it has %s cycle\n", ll_has_cycle(NULL)?"a":"no");
}

int main(void) {
  test_ll_has_cycle();
  return 0;
}
