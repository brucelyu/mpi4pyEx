#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : mpisum.py
# Author            : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
# Date              : 27.05.2021
# Last Modified Date: 27.05.2021
# Last Modified By  : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

orgdata = np.array([i + 1 for i in range(12)], dtype='i')
# tots = 0
comm.Bcast(orgdata, root=0)
s = 0
for i in range(len(orgdata)):
    if i % size != rank:
        continue
    s += orgdata[i]
print("The partial sum in core {:d} is {:d}".format(rank, s))
tots = comm.reduce(s, op=MPI.SUM, root=0)
if rank == 0:
    print("The total sum from 1 to 12 is {:d}.".format(tots),
          "The desired answer is {:d}".format((1+12)*6))
