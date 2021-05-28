# mpi4pyEx
## Some sample codes for how to use the package `mpi4py`
- `testmpi.py` The simplest template of parallelling tasks using a for loop.
- `testgather.py` A example of how to gather NumPy arrays using `MPI.COMM_WORLD.Gather` method. Slightly adapted from the official documentation.
- `testreduce.py` A example of how to reduece NumPy arrays using `MPI.COMM_WORLD.Reduce` method.
- `testreduceZ2T.py` A example of how to reduce a general python object using `MPI.COMM_WORLD.reduce` method. Here we use the class TensorZ2 in [abeliantensors](https://github.com/mhauru/abeliantensors) as a specific example. Notice it is not an ordinary type, very useful if you are interested in tensor network calculations. See `mpisum.py` for a more elementary example of how to reduce a general python object.
- `mpisum.py` A more elementary example of how to reduce a general python object using `MPI.COMM_WORLD.reduce` method.
- `mpifun.py` An example of how to parallel a function. Use `MPI.COMM_WORLD.allreduce` before return the value.

## Useful resources
- A [short tutorial](https://nyu-cds.github.io/python-mpi/) about parallel computing by New York University.
- The official [documentation](https://mpi4py.readthedocs.io/en/stable/) (Not very well written though). Contain some useful examples, but lack of detailed explanations.
