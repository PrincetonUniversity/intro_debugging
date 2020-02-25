# GDB on the Command Line

The GNU project has produced its free and open source debugger called GDB. It is a powerful tool that is used by many IDE's
and GUI's including DDT. It can be used for C/C++ and Fortran as well as other languages. We work on the command line here because it is always available to us even on supercomputing sites. Graphics are nice but you may encounter times when they cannot be used or the data rates is too slow to transfer graphics.

## Example

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

For production jobs we would compile the code as follows:

```
$ g++ -O3 -Wall -W -DNDEBUG -ffast-math -fwhole-program -march=native -mtune=native -o serial_cpp serial.cpp
$ ./serial_cpp
```

Note that when developing code you consider adding even more warning options such as `-Wconversion -Wshadow -Wcast-qual -Wwrite-strings`.

For debugging the next step is to recompile the code with the `-g` debug flag and compiler optimizations turned off:

```
$ cd intro_debugging/05_gdb
$ g++ -g -O0 -o serial_cpp serial.cpp
```

For GCC one may consider also using `-Og` which produces as much optimization as possible without interfering with debugging. If compiling with `-g -O0` makes a bug go away then it suggests that compiler optimizations may be the cause of the problem.

Note that the file size of the executable increases when include `-g`. This is due the inclusion of the debugging symbols or source code into the executable.

Let's run the executable under the GDB debugger:

```bash
$ gdb serial_cxx
GNU gdb (GDB) Red Hat Enterprise Linux 7.6.1-115.el7
...
Reading symbols from /home/jdh4/serial_cxx...done.
(gdb) list
5	}
6	
7	void myfunc(double* x, int N) {
8	  double y = x[0] * x[1];
9	  x[2] = y;
10	}
11	
12	int main(int argc, char* argv[]) {
13	
14	  int mynum = 42;

(gdb) break 14
Breakpoint 1 at 0x4008df: file serial_cxx.cpp, line 14.

(gdb) run
Starting program: /home/jdh4/serial_cxx 

Breakpoint 1, main (argc=1, argv=0x7fffffffdef8) at serial_cxx.cpp:14
14	  int mynum = 42;
Missing separate debuginfos, use: debuginfo-install glibc-2.17-292.el7.x86_64 libgcc-4.8.5-39.el7.x86_64 libstdc++-4.8.5-39.el7.x86_64

(gdb) list
9	  x[2] = y;
10	}
11	
12	int main(int argc, char* argv[]) {
13	
14	  int mynum = 42;
15	  std::cout << mynum << " doubled is " << doubler(mynum) << std::endl;
16	
17	  size_t N = 5;
18	  double x[5] = {10, 20, 30, 40, 50};

(gdb) step
15	  std::cout << mynum << " doubled is " << doubler(mynum) << std::endl;

(gdb) 
doubler (num=42) at serial_cxx.cpp:4
4	  return 2 * num;

(gdb) 
5	}

(gdb) 
42 doubled is 84
main (argc=1, argv=0x7fffffffdef8) at serial_cxx.cpp:17
17	  size_t N = 5;
...
```

The most common GDB commands are:

+ help - Show help info about a command, e.g., `(gdb) help breakpoints`
+ file - Used if you start `gdb` without giving it an executable, e.g., `(gdb) file mycode`
+ run - Run the executable under the debugger, e.g., `(gdb) run`
+ backtrace - Show the calling function and it inputs
+ break - Set a breakpoint at a function or by &lt;file&gt;:&lt;line&gt;, e.g., `(gdb) break energy.cpp:42`
+ info breakpoints - Shows information about all declared breakpoints
+ where - Similar to backtrace but works in the middle of the program
+ delete - Delete a breakpoint, e.g., `(gdb) delete 3`
+ continue - Proceed to the next breakpoint (must be used after `run` has been called)
+ finish - Run until the current function is finished
+ until - Continue execution until loop is finished
+ condition - Add a condition to a breakpoint, e.g., `(gdb) condition 1 x==10`
+ step - Step into the next line of code (i.e., execute the next line)
+ next - Same as step but will not follow functions, etc. (i.e., treat line as one instruction)
+ watch - Watchpoints pause the program when a watched variable changes, e.g., `(gdb) watch x`
+ set - Set a variable to a value, e.g., `(gdb) set var y=1`
+ print - Print out variables, e.g., `(gdb) print x`
+ list - Print out lines in the source code around a line number, e.g., `(gdb) list 42`
+ [enter] - Hitting the [enter] key will execute the most recent previous command
+ quit - Quit `gdb`

## A Newer Version of GDB

Load the `rh/devtoolset/8` module if you need a recent version of `gdb`, for example:

```
$ ssh adroit
$ gdb --version
GNU gdb (GDB) Red Hat Enterprise Linux 7.6.1-115.el7
...
$ module load rh/devtoolset/8
$ gdb --version
GNU gdb (GDB) Red Hat Enterprise Linux 8.2-3.el7
...
```

## Tips and GUIs

For Emacs users, try using gdb by typing  M-x gdb. GDB is used by many graphical frontends and we cover this next.

## Producing Core Files

In some cases it is nice to produce core files when a program crashes. A core files stores all the memory associated with the running job at the time of the crash. These can be inspected in post. By default core files are not generated. To enable them one must enter this command in your Slurm script or ~/.bashrc file: `ulimit -c unlimited`

```bash
$ ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 766691
max locked memory       (kbytes, -l) unlimited
max memory size         (kbytes, -m) unlimited
open files                      (-n) 5120
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) unlimited
cpu time               (seconds, -t) unlimited
max user processes              (-u) 4096
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
```

GDB can be used to inspect core files.

## GDB Tutorials

+ [GDB Cheat Sheet](http://www.yolinux.com/TUTORIALS/GDB-Commands.html)  
+ [Debuggin Under Unix](https://www.cs.cmu.edu/~gilpin/tutorial/)   
+ [A Walkthrough with Examples](https://www.cs.umd.edu/~srhuang/teaching/cmsc212/gdb-tutorial-handout.pdf)
+ [Description of Common Commands](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=13&ved=2ahUKEwjKwYLd8rDnAhUOlXIEHSYjBNgQFjAMegQIAhAB&url=https%3A%2F%2Fweb.eecs.umich.edu%2F~sugih%2Fpointers%2Fsummary.html&usg=AOvVaw2cdI0D3acP_2CQ_-SII44B)
