#include <stdio.h>
#include <math.h>
#include <stdint.h>

// for reference
const double pi_valid = 3.141592653589793238;
const uint32_t PIES_N = 1;

// another not-so-optimal way to estimate π
int main () {
    // 5m37.71s @ 1e+11 -> 3.141592653 6085275
    // 0m34.14s @ 1e+10 -> 3.141592653 7882011
    // 0m03.42s @ 1e+9  -> 3.14159265 55892577
    const uint64_t iters = 1e+9;

    for (uint32_t pies = 0; pies < PIES_N; pies ++) {
        double total = 1.0;

        for (uint64_t c = 3, c2 = 5; c < iters; c += 4, c2 += 4) {
            total -= 1.0 / c;
            total += 1.0 / c2;
        }
        double pi = total * 4.0;
        printf ("%.16f %.16f\n", pi, pi_valid);

    }
    return 0;
}

