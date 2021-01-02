#include <unistd.h>

int main (void) {
    for (int c = 0; c < 3; c ++) {
        char l = 'a';
        write (1, &l, 1);
    }

    return 0;
}

