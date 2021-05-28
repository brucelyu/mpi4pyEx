#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : mpifun.py
# Author            : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
# Date              : 28.05.2021
# Last Modified Date: 28.05.2021
# Last Modified By  : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
"""
Define functions that runs parallel
"""


def sumdata(orgdata, comm=None):
    if comm is None:
        s = 0
        for ele in orgdata:
            s += ele
    else:
        rank = comm.rank
        size = comm.size
        # comm.Bcast(orgdata, root=0)
        s = 0
        for i, ele in enumerate(orgdata):
            if i % size == rank:
                s += ele
        print("The partial sum in core {:d} is {:d}.".format(rank, s))
        s = comm.allreduce(s)
    return s

if __name__ == "__main__":
    from mpi4py import MPI
    import numpy as np
    import time

    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size
    orgdata = np.array([i + 1 for i in range(12)], dtype='i')
    if rank == 0:
        print("We are now using {:d} cores!".format(size))
    startT = time.time()
    totalsum = sumdata(orgdata, comm)
    endT = time.time()
    if rank == 0:
        print("The return of total sum in rank {:d} is {:d}.".format(rank, totalsum))
        print("The sum should be {:d}".format((1+12)*6))
        print("The running time is {:f}".format(endT - startT))

