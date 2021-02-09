#include <stdio.h>

int main (void) {
    printf("Hey C, does ((0.7 + 0.2) + 0.1) == (0.7 + (0.2 + 0.1))?\n");
    int b_ = ((0.7 + 0.2) + 0.1) == (0.7 + (0.2 + 0.1));
    printf("C says: %s\n", b_ ? "True" : "False");

    if (! b_) {
        printf ("womp womp\n");
    } else {
        printf ("You got it?! Good job\n");
    }

    return 0;
}

