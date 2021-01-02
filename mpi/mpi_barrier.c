#include <mpi.h>
#include <stdio.h>
#include <syslog.h>

int main (void) {
    MPI_Init(NULL, NULL);
    MPI_Barrier(MPI_COMM_WORLD);
    MPI_Finalize();
}

