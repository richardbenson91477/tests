#include <stdio.h>

int main () {
    int b[10] = {1,2,3,4,5,6,7,8,9,10};
    printf ("int b[10] = {1,2,3,4,5,6,7,8,9,10};\n");

    unsigned long sb = sizeof (b),\
        sb2 = sizeof ((char *)b),\
        sb3 = sizeof (b[0]),\
        sb4 = sizeof (*b);

    printf ("sizeof (b) = %ld\n", sb);
    printf ("sizeof ((char *)b) = %ld\n", sb2);
    printf ("sizeof (b[0] = %ld\n", sb3);
    printf ("sizeof (*b) = %ld\n", sb4);
    printf ("array length = sizeof (b) / sizeof (*b) = : %ld\n", sb / sb4);
}

