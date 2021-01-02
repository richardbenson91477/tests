#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include "to_utf8.h"

int main (int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "usage: %s utf8-hex\n", argv[0]);
        return 1;
    }
 
    uint8_t b[4];
    uint8_t bn = to_utf8 (strtol(argv[1], NULL, 0), b);
    if (! bn) {
        fprintf(stderr, "error: 0 bytes output\n");
        return 2;
    }
    for (uint8_t c = 0; c < bn; c ++)
        putchar(b[c]);

    putchar ('\n');
    return 0;
}

