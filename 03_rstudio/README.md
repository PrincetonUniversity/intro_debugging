# Debugging in RStudio

Start RStudio on either [https://myadroit.princeton.edu](https://myadroit.princeton.edu)
or [https://mydella.princeton.edu](https://mydella.princeton.edu). Open the sample script `intro_debuggin/rstudio/myscript.R`
by choosing File then Open in the main menu.

![rstudio](https://tigress-web.princeton.edu/~jdh4/rstudio_two_frames.png)

Below is a simple R script:

```R
myfunc <- function(a) {
   b <- a^2
   return(b)
}

x <- c(2,5,3,9,8,11,6)
count <- 0
for (val in x) {
if(val %% 2 == 0)  count = count+1
}

cat("count: ", count, "\n")
cat("myfunc: ", myfunc(count))
```

After RStudio loads, choose File then Open and choose `intro_debuggin/rstudio/myscript.R`. Click on Source to run the script. It should output the following in the Console:

```
> source('~/myscript.R')
count:  3 
myfunc:  9
```

Next, insert a breakpoint on line 7 by putting the cursor on that line (maybe in middle of the count variable) then choose Debug and Toggle Breakpoint. Next, choose Source. Execution will be halted when the breakpoint is reached. Use the Debug menu to step through the code. See this guide on [Debugging with RStudio](https://support.rstudio.com/hc/en-us/articles/200713843?version=1.2.5033&mode=server) for details.
