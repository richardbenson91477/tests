#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <sys/select.h>

int main () {
    fd_set fds;
    struct timeval tv;
    int ires, c;
    char bin [256];

    for (;;) {
        tv.tv_sec = 0;
        tv.tv_usec = 100;
        FD_ZERO (&fds);
        FD_SET (0, &fds);
        if ((ires = select (1, &fds, NULL, NULL, &tv)) > 0) {
            if (! fgets (bin, sizeof(bin), stdin))
                break;
            bin[strlen (bin) - 1] = '\0';
            printf ("\nyou entered: %s\n", bin);
            fflush (stdout);
        }
        sleep (1);
        printf (".");
        fflush (stdout);
    }

    return 0;
}

