#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include <pthread.h>

void *pi_thread (void *v);

const int THREADS_N = 4;
const uint64_t num_steps = 1e+9;
const double step = 1.0 / (double)num_steps;

typedef struct {
    int t_n;
    double t_total;
} t_data_t;

// a way to estimate π c/o https://www.youtube.com/watch?v=FQ1k_YpyG_A
int main () {
    pthread_t thread[THREADS_N];
    pthread_attr_t attr;

    pthread_attr_init (&attr);
    pthread_attr_setdetachstate (&attr, PTHREAD_CREATE_JOINABLE);

    t_data_t t_data[THREADS_N];

    for (int t_c = 0; t_c < THREADS_N; t_c++) {
        t_data[t_c].t_n = t_c;
        int res = pthread_create (&thread[t_c], &attr, pi_thread, &t_data[t_c]);
        if (res) {
            printf ("ERROR: pthread_create() returned %d\n", res);
            return -1;
        }
    }

    pthread_attr_destroy (&attr);

    double pi = 0.0;
    for (int t_c = 0; t_c < THREADS_N; t_c++) {
        int res = pthread_join (thread[t_c], NULL);
        if (res) {
            printf ("ERROR: pthread_join() returned %d\n", res);
            return -2;
        }
        pi += step * t_data[t_c].t_total;
    }

    const double pi_valid = 3.141592653589793238;
    printf ("%.16f %.16f\n", pi, pi_valid);
    return 0;
}

void *pi_thread (void *v) {
    t_data_t *t_data = (t_data_t *)v;

    t_data->t_total = 0.0;

    double x;
    for (uint64_t i = t_data->t_n; i < num_steps; i += THREADS_N) {
        x = (i + 0.5) * step;
        t_data->t_total += 4.0 / (1.0 + x * x);
    }

    pthread_exit(NULL);
}

