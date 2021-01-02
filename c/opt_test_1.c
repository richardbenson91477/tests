#include <unistd.h>

int main (void) {
    char l = 'a';
    for (int c = 0; c < 3; c ++) {
        write (1, &l, 1);
    }

    return 0;
}

