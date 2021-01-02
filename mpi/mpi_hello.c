// c/o https://mpitutorial.com/tutorials/mpi-hello-world/
#include <mpi.h>
#include <stdio.h>
#include <syslog.h>

int main (void) {
    MPI_Init(NULL, NULL);

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    // Get the name of the processor
    char processor_name[MPI_MAX_PROCESSOR_NAME];
    int name_len;
    MPI_Get_processor_name(processor_name, &name_len);

    MPI_Barrier (MPI_COMM_WORLD);

    // Print off a hello world message
    syslog(0, "Hello world from processor %s, rank %d out of %d processors\n",
            processor_name, world_rank, world_size);
    printf("Hello world from processor %s, rank %d out of %d processors\n",
            processor_name, world_rank, world_size);

    // Finalize the MPI environment.
    MPI_Finalize();
}

