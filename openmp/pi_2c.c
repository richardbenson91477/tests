#include <stdio.h>
#include <math.h>
#include <stdint.h>

// for reference
const double pi_valid = 3.141592653589793238;

// a way to estimate π c/o https://www.youtube.com/watch?v=FQ1k_YpyG_A
int main () {
    const uint64_t num_steps = 1e+9;
    const double step = 1.0 / (double)num_steps;
    double total;

    #pragma omp parallel
    {
        double x;
        #pragma omp for reduction (+: total)
        for (uint64_t i = 0; i < num_steps; i ++) {
            x = (i + 0.5) * step;
            total += 4.0 / (1.0 + x * x);
        }
    }

    double pi = step * total;

    printf ("%.16f %.16f\n", pi, pi_valid);
    return 0;
}

