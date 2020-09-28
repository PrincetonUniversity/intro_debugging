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
