#include <stdio.h>
#include <stdlib.h>

struct c {
    int x;
    void (*print_x)(struct c *_c);
};

typedef void (* NEW_C)(struct c **__c, int x);
void new_c (struct c **__c, int x);

typedef void (* DEL_C)(struct c *_c);
void del_c (struct c *_c);

