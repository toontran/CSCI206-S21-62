#ifndef STRNODE_H_
#define STRNODE_H_

#define STRLEN 100
struct strnode {
    char str[STRLEN+1];
    int length;
    struct strnode *next;
};

struct strnode *strnode_create(char *s, int length);
//$(CC) $(CFLAGS) strnode.o strnode_test.o

#endif
