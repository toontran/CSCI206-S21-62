CC=gcc
CFLAGS=-Wall -Werror

all: collatz

collatz.o: collatz.c 
	$(CC) $(CFLAGS) -c collatz.c

collatz: collatz.o 
	$(CC) $(CFLAGS) collatz.o -o collatz
	
