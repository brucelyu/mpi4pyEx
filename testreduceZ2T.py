#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : testreduceZ2T.py
# Author            : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
# Date              : 27.05.2021
# Last Modified Date: 27.05.2021
# Last Modified By  : Xinliang(Bruce) Lyu <lyu@issp.u-tokyo.ac.jp>
from mpi4py import MPI
from abeliantensors import TensorZ2

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

sendbuf = TensorZ2.zeros(shape=[[10]], qhape=[[0]], dirs=[1]) + rank
recvbuf = None
if rank == 0:
    recvbuf = TensorZ2.zeros(shape=[[10]], qhape=[[0]], dirs=[1])
recbuf = comm.allreduce(sendbuf)
if rank == 0:
    print(recvbuf)
