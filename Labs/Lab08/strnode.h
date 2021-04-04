#ifndef STRNODE_H_
#define STRNODE_H_

struct strnode {
    char str[101];
    int length;
    struct strnode *next;
};

struct strnode *strnode_create(char *s, int length);
//$(CC) $(CFLAGS) strnode.o strnode_test.o

#endif
