#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main (void) {
    char *_b = malloc (2);
    strcpy (_b, "test");

    free (_b);
    strcpy (_b, "two");

    printf ("%s\n", _b);
    return 0;
}

