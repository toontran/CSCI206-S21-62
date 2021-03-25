#include <stdio.h>
#include <time.h>

extern void add_second(struct tm *tm);
 
int main(void)
{
    time_t t = time(NULL);
    struct tm *tm = localtime(&t);
    int i; 

    printf ("it is now: %s\n", asctime(tm));

    for (i=0;i<2345;i++) add_second(tm);

    printf("%s\n", asctime(tm));
    return 0;
}
