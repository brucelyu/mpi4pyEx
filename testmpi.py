#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : testmpi.py
# Author            : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
# Date              : 27.05.2021
# Last Modified Date: 27.05.2021
# Last Modified By  : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

task_list = range(12)
for i, task in enumerate(task_list):
    if i % size != rank:
        continue
    print("Task number {:d} being done by processor {:d} of total {:d}".format(i, rank, size))
