# Debugging Python

## A Word on Print Statements

Print statements are an example of "worst practices" when it comes to debugging. Our hope is that you will learn to use a debugger but if not then at least use print statements effectively. The  mistake that people make is not understanding that Python print statements are buffered by default. This means that output is not printed instantaneously. If a crash occurs shortly after a print statement, the printed output may never be seen. So don't debug like this:

```
print(myvar)
```

Instead, force unbuffered output:

```
print(myvar, flush=True)
```

One could also use `python -u myscript.py` which forces stdin, stdout and stderr to be unbuffered or even write the output to a file to avoid buffering of print statements. But the best approach is to use a debugger.

## Interactive Mode

Before working with a Python debugger let's explore interactive mode. When we run a Python script in the conventional way, a crash produces a stack trace and we are returned to command prompt:

```bash
$ ssh -X adroit
$ cd /scratch/network/<YourNetID>    # or /scratch/gpfs on Perseus, Della, Tiger
$ git clone https://github.com/PrincetonUniversity/intro_debugging
$ cd intro_debugging/02_python
$ module load anaconda3
```

Consider the following Python script (`no_furniture.py`):

```python
"""This script should print a list of non-furniture objects in
   alphabetical order.""" 

def remove_furniture(items):
  furniture = {'couch', 'table', 'desk', 'chair'}
  items_furniture_removed = [item for item in items if item not in furniture]
  return items_furniture_removed

# input list of items
items = ['book', 'pencil', 'desk', 'door']

# remove furniture objects from items
items = remove_furniture(items)

# print remaining items in alphabetical order
for item in items.sort():
  print(item)
```

Try running this script with the following commands:

```bash
$ python no_furniture.py 
Traceback (most recent call last):
  File "no_furniture.py", line 16, in <module>
    for item in items.sort():
TypeError: 'NoneType' object is not iterable
$
```

In Python's interactive mode, after the exception is raised and the [stack trace](https://en.wikipedia.org/wiki/Stack_trace) is produced, we land in the Python interpreter where we can inspect variables and attempt to understand the failure.

If you have a Python script that is crashing, you can enter interactive mode after the crash to inspect variables with the `-i` option. This allows you to enter interactive mode to inspect a stack trace when a script raises an exception:

```bash
$ python -i no_furniture.py 
Traceback (most recent call last):
  File "no_furniture.py", line 16, in <module>
    for item in items.sort():
TypeError: 'NoneType' object is not iterable
>>> items
['book', 'door', 'pencil']
>>> items.sort() 
>>> help(list.sort)  # we see sort is in-place so it returns None  
>>> exit()
$
```

To correct the code we use the following line:

```python
for item in sorted(items):
```

## Using `breakpoint()`

One better than interactive mode is adding the line `breakpoint()` to stop execution before
some line and then inspect variables and step through the remaining code. This is essentially adding a breakpoint
or a point where execution should be halted so that the variables can be inspected.

Consider the following code snippet (`mybreak.py`):

```python
def myfunc(x, y):
  z = min(x, y)
  return x**2 + y**2 + z**2

x = sum([1 for u in '4a9d9eeJz' if u.isalpha()])
y = 1 if x > 7 else -1

print(myfunc(x, y))
```

Insert the following line before `print(myfunc(x, y))` to halt execution and enter the PDB debugger:

```python
breakpoint()
```

Your script should now look like this:

```python
def myfunc(x, y):
  z = min(x, y)
  return x**2 + y**2 + z**2

x = sum([1 for u in '4a9d9eeJz' if u.isalpha()])
y = 1 if x > 7 else -1

breakpoint()

print(myfunc(x, y))
```

Run the code and step through after hitting the breakpoint:

```bash
$ python mybreak.py 
> /home/ceisgrub/mybreak.py(10)<module>()
-> print(myfunc(x, y))
(Pdb) ll
  1  	def myfunc(x, y):
  2  	  z = min(x, y)
  3  	  return x**2 + y**2 + z**2
  4  	
  5  	x = sum([1 for u in '4a9d9eeJz' if u.isalpha()])
  6  	y = 1 if x > 7 else -1
  7  	
  8  	breakpoint()
  9  	
 10  ->	print(myfunc(x, y))
(Pdb) x
6
(Pdb) y
-1
(Pdb) step
--Call--
> /home/ceisgrub/mybreak.py(1)myfunc()
-> def myfunc(x, y):
(Pdb) step
> /home/ceisgrub/mybreak.py(2)myfunc()
-> z = min(x, y)
(Pdb) step
> /home/ceisgrub/mybreak.py(3)myfunc()
-> return x**2 + y**2 + z**2
(Pdb) z
-1
(Pdb) step
--Return--
> /home/ceisgrub/mybreak.py(3)myfunc()->38
-> return x**2 + y**2 + z**2
(Pdb) step
38
--Return--
> /home/ceisgrub/mybreak.py(10)<module>()->None
-> print(myfunc(x, y))
(Pdb) step
```

Once the breakpoint is reached we can inspect the values of variables in the current stack frame and step through the code
using the `print` and `step` commands. In order to fully take advantage of `breakpoint()` we need to learn how to use PDB and that is covered next. Note that in Python 3.7 and beyond, you can use the built-in `breakpoint()` but ealier versions required `import pdb; pdb.set_trace()`.

See the `browser()` function in R for something analogous to Python's `breakpoint()`.

## Command Line Debugging with PDB

PDB is the Python debug engine. It can be used directly on the command line or through an IDE like PyCharm or Spider.

Use this command to run a Python script under PDB:

```bash
$ python -m pdb <myscript.py>
```

Consider the following code (`multifile.py`):

```python
"""There is no bug in this code."""

from MyShapes import RightTriangle

def myfunc1(x, y , z):
  mymin = min(x, y, z)
  mymax = max(x, y, z)
  return mymin * mymax

def myfunc2(x, y, mysum):
  z = myfunc1(x, y, mysum)
  return -z**2

x = sum([1 for u in '4a9d9eeJz' if u.isalpha()])
y = 1 if x > 7 else -1

mysum = 0
for i in range(10):
  mysum += i

print("myfunc2 = ", myfunc2(x, y, mysum))

mytriangle = RightTriangle(2.5, 7.0)
print("triangle area = ", mytriangle.area())
```
The contents of `MyShapes.py` are:

```python
class RightTriangle(object):
  def __init__(self, base, height):
    self.base = base
    self.height = height
  def area(self):
    return 0.5 * self.base * self.height
```

Run the above script under the PDB debugger:

```bash
$ python -m pdb multifile.py 
> /home/ceisgrub/multifile.py(1)<module>()
-> """There is no bug in this code."""
(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb

(Pdb) ll
  1  ->	"""There is no bug in this code."""
  2  	
  3  	from MyShapes import RightTriangle
  4  	
  5  	def myfunc1(x, y , z):
  6  	  mymin = min(x, y, z)
  7  	  mymax = max(x, y, z)
  8  	  return mymin * mymax
  9  	
 10  	def myfunc2(x, y, mysum):
 11  	  z = myfunc1(x, y, mysum)
 12  	  return -z**2
 13  	
 14  	x = sum([1 for u in '4a9d9eeJz' if u.isalpha()])
 15  	y = 1 if x > 7 else -1
 16  	
 17  	mysum = 0
 18  	for i in range(10):
 19  	  mysum += i
 20  	
 21  	print("myfunc2 = ", myfunc2(x, y, mysum))
 22  	
 23  	mytriangle = RightTriangle(2.5, 7.0)
 24  	print("triangle area = ", mytriangle.area())
 
(Pdb) break 17
Breakpoint 1 at /home/ceisgrub/multifile.py:17

(Pdb) continue
> /home/ceisgrub/multifile.py(17)<module>()
-> mysum = 0
(Pdb) x
6
(Pdb) y
-1

(Pdb) step
> /home/ceisgrub/multifile.py(18)<module>()
-> for i in range(10):
(Pdb) step
> /home/ceisgrub/multifile.py(19)<module>()
-> mysum += i
(Pdb) step
> /home/ceisgrub/multifile.py(18)<module>()
-> for i in range(10):
(Pdb) step
> /home/ceisgrub/multifile.py(19)<module>()
-> mysum += i
(Pdb) step
> /home/ceisgrub/multifile.py(18)<module>()
-> for i in range(10):
(Pdb) i, mysum
(1, 1)

(Pdb) until 21
> /home/ceisgrub/multifile.py(21)<module>()
-> print("myfunc2 = ", myfunc2(x, y, mysum))

(Pdb) next
myfunc2 =  -2025
> /home/ceisgrub/multifile.py(23)<module>()
-> mytriangle = RightTriangle(2.5, 7.0)

(Pdb) next
> /home/ceisgrub/multifile.py(24)<module>()
-> print("triangle area = ", mytriangle.area())
(Pdb) step
--Call--
> /home/ceisgrub/MyShapes.py(5)area()
-> def area(self):
(Pdb) step
> /home/ceisgrub/MyShapes.py(6)area()
-> return 0.5 * self.base * self.height
(Pdb) step
--Return--
> /home/ceisgrub/MyShapes.py(6)area()->8.75
-> return 0.5 * self.base * self.height
(Pdb) step
triangle area =  8.75
--Return--
> /home/ceisgrub/multifile.py(24)<module>()->None
-> print("triangle area = ", mytriangle.area())
(Pdb) step
--Return--
> <string>(1)<module>()->None
(Pdb) step
> /usr/licensed/anaconda3/2019.10/lib/python3.7/bdb.py(589)run()
-> self.quitting = True
(Pdb) step
The program finished and will be restarted
> /home/ceisgrub/multifile.py(1)<module>()
-> """There is no bug in this code."""

(Pdb) quit
```

Exercises:

- Set a breakpoint at line 17, run `cont` and inspect the values of `x` and `y` then `quit`.  
- Set a breakpoint at line 21, run `cont` then `step` then `quit`. Repeat using `next` instead of `step`.
- Set a conditional breakpoint at line 19 where `i>6` (see `help break`). Use the `break` command to see all breakpoints. Run with `cont` and test that it worked by printing `i` then `quit`.  
- Set a breakpoint at line 7, run `cont` then run `where` to see the backtrace then `quit`.  
- Set a breakpoint at line 6 in MyShapes.py (i.e., `break MyShapes:6`), run `cont` then `step` to the finish.
- Set a breakpoint at line 17, run `cont`. Use `display` to watch the product of `i` and `mysum` within the loop (see `help display`).  

Below are some common commands for PDB:

```
(Pdb) help break
b(reak) [ ([filename:]lineno | function) [, condition] ]
        Without argument, list all breaks.

        With a line number argument, set a break at this line in the
        current file.  With a function name, set a break at the first
        executable line of that function.  If a second argument is
        present, it is a string specifying an expression which must
        evaluate to true before the breakpoint is honored.

        The line number may be prefixed with a filename and a colon,
        to specify a breakpoint in another file (probably one that
        hasn't been loaded yet).  The file is searched for on
        sys.path; the .py suffix may be omitted.

(Pdb) help cont
c(ont(inue))
        Continue execution, only stop when a breakpoint is encountered.

(Pdb) help step
s(tep)
        Execute the current line, stop at the first possible occasion
        (either in a function that is called or in the current
        function).
        
(Pdb) help next
n(ext)
        Continue execution until the next line in the current function
        is reached or it returns.

(Pdb) help p
p expression
        Print the value of the expression.

(Pdb) help list
l(ist) [first [,last] | .]

        List source code for the current file.  Without arguments,
        list 11 lines around the current line or continue the previous
        listing.  With . as argument, list 11 lines around the current
        line.  With one argument, list 11 lines starting at that line.
        With two arguments, list the given range; if the second
        argument is less than the first, it is a count.

        The current line in the current frame is indicated by "->".
        If an exception is being debugged, the line where the
        exception was originally raised or propagated is indicated by
        ">>", if it differs from the current line.
        
(Pdb) help return        
r(eturn)
        Continue execution until the current function returns.

(Pdb) help where
w(here)
        Print a stack trace, with the most recent frame at the bottom.
        An arrow indicates the "current frame", which determines the
        context of most commands.  'bt' is an alias for this command.
        
(Pdb) help until
unt(il) [lineno]
        Without argument, continue execution until the line with a
        number greater than the current one is reached.  With a line
        number, continue execution until a line with a number greater
        or equal to that is reached.  In both cases, also stop when
        the current frame returns.
        
(Pdb) help display
display [expression]

        Display the value of the expression if it changed, each time execution
        stops in the current frame.

        Without expression, list all display expressions for the current frame.
```

## Using PDB on the HPC Clusters

Short debugging sessions using PDB can be carried out on the head node. For sessions that require more than 10 minutes, an interactive allocation via `salloc` should be used:

```bash
$ ssh della
$ salloc --nodes=1 --ntasks=1 --time=01:00:00 --mem=4G
$ module load anaconda3
$ python -m pdb myscript.py
```

## pudb

For a terminal-based GUI try [pudb](https://github.com/inducer/pudb):

```
$ conda activate myenv
$ conda install -c conda-forge pudb
$ python -m pudb myscript.py
```

## Debugging Jupyter Notebooks

Jupyter notebooks are available on either [https://myadroit.princeton.edu](https://myadroit.princeton.edu)
or [https://mydella.princeton.edu](https://mydella.princeton.edu).

If you encounter an error then put `%debug` in a cell to use iPDB. 

![jupyter](https://tigress-web.princeton.edu/~jdh4/jupyter_debug.png)

```
%debug:
    ::
    
      %debug [--breakpoint FILE:LINE] [statement [statement ...]]
    
    Activate the interactive debugger.
    
    This magic command support two ways of activating debugger.
    One is to activate debugger before executing code.  This way, you
    can set a break point, to step through the code from the point.
    You can use this mode by giving statements to execute and optionally
    a breakpoint.
    
    The other one is to activate debugger in post-mortem mode.  You can
    activate this mode simply running %debug without any argument.
    If an exception has just occurred, this lets you inspect its stack
    frames interactively.  Note that this will always work only on the last
    traceback that occurred, so you must call this quickly after an
    exception that you wish to inspect has fired, because if another one
    occurs, it clobbers the previous one.
    
    If you want IPython to automatically do this on every exception, see
    the %pdb magic for more details.
    
    .. versionchanged:: 7.3
        When running code, user variables are no longer expanded,
        the magic line is always left unmodified.
    
    positional arguments:
      statement             Code to run in debugger. You can omit this in cell
                            magic mode.
    
    optional arguments:
      --breakpoint <FILE:LINE>, -b <FILE:LINE>
                            Set break point at LINE in FILE.
```

Note that you can use `nbconvert` to convert a Jupyter notebook to a flat Python script. On can then use the debugger in PyCharm, for example, to do more advanced debugging.

## PyCharm

A popular Python IDE is [PyCharm](https://www.jetbrains.com/pycharm/). Try running the code above using PyCharm's graphical debugger interface. Note that PyCharm will create two directories: `PycharmProjects/ .PyCharmCE2019.3/`

## Using the PyCharm Debugger on the HPC Clusters

The video below explains how to run the PyCharm debugger on a TigerGPU node. The same procedure can be used for the other clusters.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=0XmZsfixAdw" target="_blank">
<img src="http://img.youtube.com/vi/0XmZsfixAdw/0.jpg" alt="PyCharm" width="640" height="360" border="0" /></a>

PyCharm for Linux is available [here](https://www.jetbrains.com/pycharm/download/#section=linux). While the video uses the Community Edition, you can get the professional edition for free by supplying your `.edu` email address.

## Debugging parallel codes

See [this page](https://researchcomputing.princeton.edu/mpi4py) then:

```
[jdh4@tigergpu mpi4py]$ salloc -N 1 -n 3 -t 5
[jdh4@tigergpu mpi4py]$ module load anaconda3 openmpi/gcc/3.1.3/64
[jdh4@tiger-h20c1n11 mpi4py]$ conda activate fast-mpi4py
(fast-mpi4py) [jdh4@tiger-h20c1n11 mpi4py]$ srun python -m pdb hello_world.py
> /home/jdh4/mpi4py/hello_world.py(6)<module>()
-> from mpi4py import MPI
> /home/jdh4/mpi4py/hello_world.py(6)<module>()
-> from mpi4py import MPI
> /home/jdh4/mpi4py/hello_world.py(6)<module>()
-> from mpi4py import MPI
next
(Pdb) > /home/jdh4/mpi4py/hello_world.py(7)<module>()
-> import sys
(Pdb) > /home/jdh4/mpi4py/hello_world.py(7)<module>()
-> import sys
(Pdb) > /home/jdh4/mpi4py/hello_world.py(7)<module>()
-> import sys
next
(Pdb) > /home/jdh4/mpi4py/hello_world.py(9)<module>()
-> def print_hello(rank, size, name):
(Pdb) > /home/jdh4/mpi4py/hello_world.py(9)<module>()
-> def print_hello(rank, size, name):
(Pdb) > /home/jdh4/mpi4py/hello_world.py(9)<module>()
-> def print_hello(rank, size, name):
next
(Pdb) > /home/jdh4/mpi4py/hello_world.py(13)<module>()
-> if __name__ == "__main__":
(Pdb) > /home/jdh4/mpi4py/hello_world.py(13)<module>()
-> if __name__ == "__main__":
(Pdb) > /home/jdh4/mpi4py/hello_world.py(13)<module>()
-> if __name__ == "__main__":
next
(Pdb) > /home/jdh4/mpi4py/hello_world.py(14)<module>()
-> size = MPI.COMM_WORLD.Get_size()
(Pdb) > /home/jdh4/mpi4py/hello_world.py(14)<module>()
-> size = MPI.COMM_WORLD.Get_size()
(Pdb) > /home/jdh4/mpi4py/hello_world.py(14)<module>()
-> size = MPI.COMM_WORLD.Get_size()
next
(Pdb) > /home/jdh4/mpi4py/hello_world.py(15)<module>()
-> rank = MPI.COMM_WORLD.Get_rank()
(Pdb) > /home/jdh4/mpi4py/hello_world.py(15)<module>()
-> rank = MPI.COMM_WORLD.Get_rank()
(Pdb) > /home/jdh4/mpi4py/hello_world.py(15)<module>()
-> rank = MPI.COMM_WORLD.Get_rank()
next
(Pdb) > /home/jdh4/mpi4py/hello_world.py(16)<module>()
-> name = MPI.Get_processor_name()
(Pdb) > /home/jdh4/mpi4py/hello_world.py(16)<module>()
-> name = MPI.Get_processor_name()
(Pdb) > /home/jdh4/mpi4py/hello_world.py(16)<module>()
-> name = MPI.Get_processor_name()
print(size)
(Pdb) 3
(Pdb) 3
(Pdb) 3
print(rank)
(Pdb) 0
(Pdb) 1
(Pdb) 2
next
(Pdb) > /home/jdh4/mpi4py/hello_world.py(18)<module>()
-> print_hello(rank, size, name)
(Pdb) > /home/jdh4/mpi4py/hello_world.py(18)<module>()
-> print_hello(rank, size, name)
(Pdb) > /home/jdh4/mpi4py/hello_world.py(18)<module>()
-> print_hello(rank, size, name)
quit
```

## PDB in Color

Make a Conda environment with the `ipython` and `ipdb` packages then:

```
$ ipython -m ipdb run_graph_net_nv.py
```

## Useful Links

[PDB on Python.org](https://docs.python.org/3/library/pdb.html)
