"""
Example showing how to use mpi4py for parallel programming
"""

from mpi4py import MPI

# Communication object
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = range(10)
    print("process{} bcast data {} to other processes".format(rank, data))
else:
    data = None

# Broadcast communication
data = comm.bcast(data, root=0)
print("process {} receive data {} ...".format(rank, data))

# Point to point communication
# comm.send(data, dest=target_process_rank, tag)
# comm.isend(data, dest=target_process_rank, tag)
# comm.recv(source, tag)
# For non build-in data structure, using capital method
