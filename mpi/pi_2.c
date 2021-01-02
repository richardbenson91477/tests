#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include <mpi.h>

const double pi_valid = 3.141592653589793238;

int main () {
    const uint64_t num_steps = 1e+9;
    const double step = 1.0 / (double)num_steps;
 
    MPI_Init(NULL, NULL);

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    MPI_Barrier (MPI_COMM_WORLD);

    double total = 0.0;
    double x;
    for (uint64_t i = world_rank; i < num_steps; i += world_size) {
        x = (i + 0.5) * step;
        total += 4.0 / (1.0 + x * x);
    }

    double pi;
    MPI_Reduce (&total, &pi, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    MPI_Finalize();

    if (! world_rank) {
        pi *= step;
        printf ("%.16f %.16f\n", pi, pi_valid);
    }

    return 0;
}

