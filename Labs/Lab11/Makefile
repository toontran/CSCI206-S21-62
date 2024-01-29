#CFLAGS=-g -Wall -Werror
#CFLAGS=-g -Wno-return-local-addr
CFLAGS=-g -Wall
cc=gcc

all: example ll_equal ll_cycle

example: example.o list.o
ll_equal: ll_equal.o list.o
ll_cycle: ll_cycle.o list.o

clean:
	rm -f *.o example ll_equal ll_cycle
