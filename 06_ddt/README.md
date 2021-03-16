# ARM DDT

[DDT](https://developer.arm.com/tools-and-software/server-and-hpc/debug-and-profile/arm-forge/arm-ddt) is a graphical debugger produced by ARM as part of ARM Forge. It is based on GDB. DDT can be used for serial, parallel and GPU codes.

## Serial Code

Here is the code that we encountered previously:

```c++
#include <iostream>

int doubler(int num) {
  return 2 * num;
}

void myfunc(double* x, int N) {
  double y = x[0] * x[1];
  x[2] = y;
}

int main(int argc, char* argv[]) {

  int mynum = 42;
  std::cout << mynum << " doubled is " << doubler(mynum) << std::endl;

  size_t N = 5;
  double x[5] = {10, 20, 30, 40, 50};
  myfunc(x, N);
  std::cout << "myfunc produced: " << x[2] << std::endl;

  int A[N][N];
  for (int i=0; i < N; i++)
    for (int j=0; j < N; j++) {
      A[i][j] = i * j + i + j;
      if (i == j) std::cout << "diagonal element of A[i][j]: " << A[i][j] << std::endl;
  }

  int mysum = 0;
  for (int i=0; i < 10; i++)
    mysum = mysum + i;
  std::cout << "mysum = " << mysum << std::endl;
 
  return 0;
}
```

Run the executable using DDT:

```bash
$ ssh -X adroit
$ git clone https://github.com/PrincetonUniversity/intro_debugging
$ cd intro_debugging/05_gdb
$ g++ -g -O0 -o serial_cpp serial.cpp
$ salloc --nodes=1 --ntasks=1 --time=05:00 --x11
$ module load ddt/20.0.1
$ ddt
```

## Hello World MPI Program

Follow the procedure below to run a simple MPI job under the DDT debugger:

```bash
$ ssh -X adroit
$ git clone https://github.com/PrincetonUniversity/hpc_beginning_workshop
$ cd hpc_beginning_workshop/RC_example_jobs/cxx/parallel
$ module load intel/19.1/64/19.1.1.217 intel-mpi/intel/2019.7/64
$ mpicxx -g -O0 hello_world_mpi.cpp
$ module load ddt/20.0.1
$ ddt
# choose "Run and debug a program" then complete the form similar to below
```

![DDT screen](https://tigress-web.princeton.edu/~jdh4/ddt_mpi_hello_world.png)

There is a Fortran 90 version in `hpc_beginning_workshop/RC_example_jobs/parallel_fortran`.

On Stellar and Traverse, set the MPI/UPC Implementation to "SLURM (generic)" in the System Settings by choosing "Change..." from the main window.

## CUDA Kernels

DDT can be used to debug CUDA kernel functions. Here is the setup:

```bash
$ ssh -X <YourNetID>@adroit.princeton.edu  # tigergpu or traverse
$ git clone https://github.com/PrincetonUniversity/hpc_beginning_workshop
$ cd hpc_beginning_workshop/RC_example_jobs/simple_gpu_kernel
$ salloc -N 1 -n 1 -t 10 --gres=gpu:1 --x11
$ module load cudatoolkit/10.1
$ nvcc -g -G hello_world_gpu.cu
$ module load ddt/20.0.1
$ export ALLINEA_FORCE_CUDA_VERSION=10.1
$ ddt
# check cuda, uncheck "submit to queue", and click on "Run"
```

The `-g` debugging flag is for CPU code while the `-G` flag is for GPU code. `-G` turns off compiler optimizations. Note that as of February 2020 CUDA Toolkit 10.2 is not supported.
