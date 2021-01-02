#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include <omp.h>

const double pi_valid = 3.141592653589793238;
const int THREADS_N = 4;

// a way to estimate π c/o https://www.youtube.com/watch?v=FQ1k_YpyG_A
int main () {
    int t_n_shared;
 
    omp_set_num_threads (THREADS_N);

    const uint64_t num_steps = 1e+9;
    const double step = 1.0 / (double)num_steps;
    double pi = 0.0;

    //omp_get_wtime ();
    #pragma omp parallel 
    {
        int t = omp_get_thread_num();
        int t_n = omp_get_num_threads();
        if (t == 0)
            t_n_shared = t_n;

        double x;
        double t_total = 0.0;
        for (uint64_t i = t; i < num_steps; i += t_n) {
            x = (i + 0.5) * step;
            t_total += 4.0 / (1.0 + x * x);
        }

        t_total = t_total * step;
        //#pragma omp barrier
        //#pragma omp critical
        #pragma omp atomic
        pi += t_total;
    }
    //printf ("%f\n", omp_get_wtime());
    printf ("%d threads\n", t_n_shared);

    printf ("%.16f %.16f\n", pi, pi_valid);
    return 0;
}

