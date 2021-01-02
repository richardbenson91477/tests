#include <stdio.h>

int *getTwoReturnValues () {
    static int a[] = {3, 4};
    return a;
}

int main () {
    int *_ab = getTwoReturnValues ();
    int a = _ab[0], b = _ab[1];
    printf ("%d, %d\n", a, b);
    return 0;
}

