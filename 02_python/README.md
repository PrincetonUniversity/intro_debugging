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

One could also write the output to a file to avoid buffering of print statements. But the best approach is to use a debugger.

## Interactive Mode

Before working with a Python debugger let's explore interactive mode. When we run a Python script in the conventional way, a crash produces a stack trace and we are returned to command prompt:

```bash
$ ssh -X adroit
$ cd /scratch/network/<YourNetID>    # or /scratch/gpfs on Perseus, Della, Tiger
$ git clone https://github.com/PrincetonUniversity/intro_debugging
$ cd intro_debugging/02_python
$ module load anaconda3
```

Consider the following Python script:

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
  File "no_furniture.py", line 15, in <module>
    for item in items.sort():
AttributeError: 'NoneType' object has no attribute 'sort'
$
```

In Python's interactive mode, after the exception is raised and the [stack trace](https://en.wikipedia.org/wiki/Stack_trace) is produced, we land in the Python interpreter where we can inspect variables and attempt to understand the failure.

If you have a Python script that is crashing, you can enter interactive mode after the crash to inspect variables with the `-i` option. This allows you to enter interactive mode to inspect a stack trace when a script raises an exception:

```bash
$ python -i myscript.py 
Traceback (most recent call last):
  File "myscript.py", line 2, in <module>
    for item in items.sort():
TypeError: 'NoneType' object is not iterable
>>> items
['cat', 'dog', 'fish', 'rattlesnake']
>>> items.sort()
>>> exit()
$
```

## Using `breakpoint()`

One better than interactive mode is adding the line `breakpoint()` to stop execution before
some line and then inspect variables and step through the remaining code. This is essentially adding a breakpoint
or a point where execution should be halted so that the variables can be inspected.

Insert the following line anywhere in your code to halt execution and enter PDB:

```python
breakpoint()
```

Consider the following script (`mybreak.py`):

```python
def myfunc(x, y):
  z = min(x, y)
  return x**2 + y**2 + z**2

x = sum([1 for u in '4a9d9eeJz' if u.isalpha()])
y = 1 if x > 7 else -1

breakpoint()

print(myfunc(x, y))
```

We run the code and step through after hitting the breakpoint:

```bash
$ python mybreak.py 
> /home/jdh4/mybreak.py(10)<module>()
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
(Pdb) print(x)
6
(Pdb) print(y)
-1
(Pdb) step
--Call--
> /home/jdh4/mybreak.py(1)myfunc()
-> def myfunc(x, y):
(Pdb) step
> /home/jdh4/mybreak.py(2)myfunc()
-> z = min(x, y)
(Pdb) step
> /home/jdh4/mybreak.py(3)myfunc()
-> return x**2 + y**2 + z**2
(Pdb) print(z)
-1
(Pdb) step
--Return--
> /home/jdh4/mybreak.py(3)myfunc()->38
-> return x**2 + y**2 + z**2
(Pdb) step
38
--Return--
> /home/jdh4/mybreak.py(10)<module>()->None
-> print(myfunc(x, y))
(Pdb) step
```

Once the breakpoint is reached we can inspect the values of variables in the current stack frame and step through the code
using the `print` and `step` commands. In order to fully take advantage of `breakpoint()` we need to learn how to use PDB and that is covered next. Note that in Python 3.7 and beyond, you can use the built-in `breakpoint()` but ealier versions required `import pdb; pdb.set_trace()`.

See the `browser()` function in R for something analogous to Python's `breakpoint()`.

## PDB on the Command Line

PDB is the Python debug engine. It can be used directly on the command line or through an IDE like PyCharm or Spider.

```
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
```

Call the following `myscript.py`:

```python
items = ['cat', 'dog', 'rattlesnake', 'fish']
for item in items.sort():
    print(item)
```

```bash
$ module load anaconda3
$ python myscript.py
Traceback (most recent call last):
  File "myscript.py", line 2, in <module>
    for item in items.sort():
TypeError: 'NoneType' object is not iterable
```

```bash
$ python -m pdb myscript.py 
> /home/jdh4/pdb/myscript.py(1)<module>()
-> items = ['cat', 'dog', 'rattlesnake', 'fish']

(Pdb) step
> /home/jdh4/pdb/myscript.py(2)<module>()
-> for item in items.sort():

(Pdb) print(items)
['cat', 'dog', 'rattlesnake', 'fish']

(Pdb) step
TypeError: 'NoneType' object is not iterable
> /home/jdh4/pdb/myscript.py(2)<module>()
-> for item in items.sort():

(Pdb) print(item)
*** NameError: name 'item' is not defined

(Pdb) print(items)
['cat', 'dog', 'fish', 'rattlesnake']

(Pdb) print(items.sort())
None

(Pdb) quit
```

The list command shows breakpoints and the current line:

```
(Pdb) step
--Call--
> /home/jdh4/pdb/myscript.py(7)doubler()
-> def doubler(u):
(Pdb) list
  2  	  def __init__(self, u):
  3  	    self.u = u
  4  	  def mysquare(self):
  5  	    return self.u * self.u
  6  	
  7  ->	def doubler(u):
  8  	  return 2 * u
  9  	
 10 B	def make_tuple(u):
 11  	  return (u,)
```

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

Exercises:

- Set a breakpoint at line 22, run `cont` and inspect the values of `x` and `y` then `quit`.  
- Set a conditional breakpoint at line 24 where `i>6`. The type `break` to see all breakpoints. Run with `contd` and test that it worked by printing `i` then `quit`.  
- Use `display` to watch the product of `i` and `mysum` within the loop.  
- Set a breakpoint at line x then use `where` or equivalently `bt` to see the backtrace.  

## Using PDB on the HPC Clusters

Short debugging sessions using PDB can be carried out on the head node. For sessions that require more than 10 minutes, an interactive allocation via `salloc` should be used:

```bash
$ ssh della
$ salloc --nodes=1 --ntasks=1 --time=01:00:00 --mem=4G
$ module load anaconda3
$ python -m pdb myscript.py
```

## Debugging Jupyter Notebooks

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

## Using the PyCharm Debugger on the HPC Clusters

The video below explains how to run the PyCharm debugger on a TigerGPU node. The same procedure can be used for the other clusters.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=0XmZsfixAdw" target="_blank">
<img src="http://img.youtube.com/vi/0XmZsfixAdw/0.jpg" alt="PyCharm" width="640" height="360" border="0" /></a>

PyCharm for Linux is available [here](https://www.jetbrains.com/pycharm/download/#section=linux). While the video uses the Community Edition, you can get the professional edition for free by supplying your `.edu` email address.

## Multi-file Projects

Run the folling commands to see the failure then try to find the bug:

```bash
$ ssh adroit
$ git clone repo
$ cd intro_debugging/02_python/multi
$ module load anaconda3
$ python myscript
# this will give an error
```

## Advanced Cases

+ pybind11 or mixed language programming
+ parallel python


## Useful Links

[PDB on Python.org](https://docs.python.org/3/library/pdb.html)
