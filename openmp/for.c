// c/o https://en.wikipedia.org/wiki/OpenMP
#include <stdio.h>
#include <omp.h>

int main(int argc, char **argv) {
    int a[100000];

    // "embarrassingly parallel"
    #pragma omp parallel for
    for (int i = 0; i < 16; i++) {
        a[i] = i;
        printf ("%d\n", a[i]);
    }

    return 0;
}

