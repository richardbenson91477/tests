#include <mpi.h>
#include <stdio.h>
#include <syslog.h>

int main (void) {
    MPI_Init(NULL, NULL);
    MPI_Finalize();
}

