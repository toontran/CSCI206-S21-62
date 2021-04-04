CC=gcc
CFLAGS=-Wall -Werror
all: strnode_test node_test stack_test pcalc

strnode_test: strnode.o strnode_test.o strnode.h
node_test: node.o node_test.o node.h
stack_test: stack.o stack_test.o node.o stack.h node.h
pcalc: pcalc.o stack.o node.o stack.h node.h
	$(CC) $(CFLAGS) pcalc.o stack.o node.o stack.h node.h -o pcalc -lm


clean:
	rm -f strnode_test *.o 
	rm -f node_test *.o
