#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include <omp.h>

const double pi_valid = 3.141592653589793238;
const int THREADS_N = 4;

// a way to estimate π c/o https://www.youtube.com/watch?v=FQ1k_YpyG_A
int main () {
    const uint64_t num_steps = 1e+9;
    const double step = 1.0 / (double)num_steps;
 
    omp_set_num_threads (THREADS_N);

    int t_n_shared;
    double t_total[THREADS_N];

    //omp_get_wtime ();
    #pragma omp parallel 
    {
        int t = omp_get_thread_num();
        int t_n = omp_get_num_threads();
        if (t == 0)
            t_n_shared = t_n;

        t_total[t] = 0.0;
        double x;
        for (uint64_t i = t; i < num_steps; i += t_n) {
            x = (i + 0.5) * step;
            t_total[t] += 4.0 / (1.0 + x * x);
        }
    }
    //printf ("%f\n", omp_get_wtime());
    printf ("%d threads\n", t_n_shared);

    double pi = 0.0;
    for (int c = 0; c < t_n_shared; c ++)
        pi += step * t_total[c];

    printf ("%.16f %.16f\n", pi, pi_valid);
    return 0;
}

