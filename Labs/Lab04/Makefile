CC=gcc
CFLAGS=-Wall -Werror

all: head2 head3 string_tokens

head2: head2.o fileio.o
	$(CC) $(CFLAGS) head2.o fileio.o -o head2

head3: head3.o fileio.o
	$(CC) $(CFLAGS) head3.o fileio.o -o head3

fileio.o: fileio.c fileio.h
	$(CC) $(CFLAGS) -c fileio.c

head2.o: head2.c fileio.h
	$(CC) $(CFLAGS) -c head2.c
 
head3.o: head3.c fileio.h
	$(CC) $(CFLAGS) -c head3.c

string_tokens.o: string_tokens.c fileio.h
	$(CC) $(CFLAGS) -c string_tokens.c

string_tokens: string_tokens.o fileio.o
	$(CC) $(CFLAGS) string_tokens.o fileio.o -o string_tokens	
