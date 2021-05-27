#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : testgather.py
# Author            : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
# Date              : 27.05.2021
# Last Modified Date: 27.05.2021
# Last Modified By  : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

sendbuf = np.zeros(10, dtype='i') + rank
recvbuf = None
if rank == 0:
    recvbuf = np.empty([size, 10], dtype='i')
comm.Gather(sendbuf, recvbuf, root=0)
if rank == 0:
    for i in range(size):
        print(recvbuf[i,:])
