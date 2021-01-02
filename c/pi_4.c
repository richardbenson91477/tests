#include <stdio.h>
#include <math.h>
#include <stdint.h>

// for reference
const double pi_valid = 3.141592653589793238;
const uint32_t PIES_N = 1;

// another not-so-optimal way to estimate π
int main () {
    const uint64_t iters = 1e+9;

    for (uint32_t pies = 0; pies < PIES_N; pies ++) {
        double total = 0.0;

        for (uint64_t c = 1; c < iters; c++) {
            total += 1.0 / (c * c);
        }
        double pi = sqrt(total * 6.0);
        printf ("%.16f %.16f\n", pi, pi_valid);

    }
    return 0;
}

