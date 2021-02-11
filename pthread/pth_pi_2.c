#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include <pthread.h>

void *pi_thread (void *v);

const uint64_t num_steps = 1e+9;
const double step = 1.0 / (double)num_steps;
const int THREADS_N = 4;

// a way to estimate π c/o https://www.youtube.com/watch?v=FQ1k_YpyG_A
int main () {
    pthread_t thread[THREADS_N];
    pthread_attr_t attr;

    pthread_attr_init (&attr);
    pthread_attr_setdetachstate (&attr, PTHREAD_CREATE_JOINABLE);

    for (int t_c = 0; t_c < THREADS_N; t_c++) {
        int res = pthread_create (&thread[t_c], &attr, pi_thread, (void *)&t_c);
        if (res) {
            printf ("ERROR: pthread_create() returned %d\n", res);
            return -1;
        }
    }

    pthread_attr_destroy (&attr);

    double pi = 0.0;
    for (int t_c = 0; t_c < THREADS_N; t_c++) {
        double *t_total;
        int res = pthread_join (thread[t_c], (void **)&t_total);
        if (res) {
            printf ("ERROR: pthread_join() returned %d\n", res);
            return -2;
        }
        pi += step * *t_total;
    }

    const double pi_valid = 3.141592653589793238;
    printf ("%.16f %.16f\n", pi, pi_valid);
    return 0;
}

void *pi_thread (void *v) {
    int t_start = *(int *)v;
    double t_total = 0.0;

    double x;
    for (uint64_t i = t_start; i < num_steps; i += THREADS_N) {
        x = (i + 0.5) * step;
        t_total += 4.0 / (1.0 + x * x);
    }

    pthread_exit((void *)&t_total);
}

