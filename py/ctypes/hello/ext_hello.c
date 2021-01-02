#include <stdio.h>
#include <stdlib.h>

int ext_hello (const char *n, char *s) {
    printf ("in ext_hello\n");
	sprintf (s, "Hello, %s!\n", n);
	return 0;
}

