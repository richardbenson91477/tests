#include "c.h"

void print_x(struct c *_c) {
    printf("_c->x = %d\n", _c->x);
}

void new_c(struct c **__c, int x) {
    *__c = malloc(sizeof(struct c));
    (*__c)->x = x;
    (*__c)->print_x = print_x;
}

void del_c(struct c *_c) {
    free(_c);
}

