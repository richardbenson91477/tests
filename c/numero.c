#include <stdio.h>
#include <ctype.h>

int main () {
    int c, n, t, t2;

    t2 = 0;
    while (1 < 2) {
        t = 0;

        while (EOF != (c = getchar())) {
            if (c == '\n')
                break;
            if (c == ' ')
                continue;

            c = tolower (c);
            n = c - 'a' + 1;
            printf ("%d ", n);
            t += n;
        }

        if (c != '\n')
            break;

        printf ("= %d\n", t);
        t2 += t;
    }

    printf ("total: %d\n", t2);
    return 0;
}

