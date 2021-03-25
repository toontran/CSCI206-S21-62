CC=gcc
AS=as
CFLAGS=-Wall -Werror

all: primes2 counte matrix-sum time

is_prime.o: is_prime.s
	$(CC) $(CFLAGS) -c is_prime.s

primes2.o: primes2.c 
	$(CC) $(CFLAGS) -c primes2.c

primes2: primes2.o is_prime.o
	$(CC) $(CFLAGS) primes2.o is_prime.o -o primes2 

counte: counte.c counte.s
	$(CC) $(CFLAGS) counte.c counte.s -o counte

matrix-sum-main.o: matrix-sum-main.c
	$(CC) $(CFLAGS) -g -c matrix-sum-main.c

matrix-sum.o: matrix-sum.s
	$(CC) $(CFLAGS) -g -c  matrix-sum.s 

matrix-sum: matrix-sum-main.o matrix-sum.o
	$(CC) $(CFLAGS) matrix-sum-main.o matrix-sum.o -o matrix-sum
	
time: time.c time.s
	$(CC) $(CFLAGS) time.c time.s -o time
