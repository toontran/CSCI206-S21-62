CC=gcc
CFLAGS=-Wall -Werror

all: primes2 counte

is_prime.o: is_prime.s
	$(CC) $(CFLAGS) -c is_prime.s

primes2.o: primes2.c 
	$(CC) $(CFLAGS) -c primes2.c

primes2: primes2.o is_prime.o
	$(CC) $(CFLAGS) primes2.o is_prime.o -o primes2 

counte: counte.c counte.s
	$(CC) $(CFLAGS) counte.c counte.s -o counte
