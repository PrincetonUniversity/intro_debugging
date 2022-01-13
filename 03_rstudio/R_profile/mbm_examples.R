packages <- c("microbenchmark","tidyverse","nycflights13","sqldf","dlnm")
install.packages(setdiff(packages, rownames(installed.packages())))  

library(microbenchmark)
library(tidyverse)
library(nycflights13)
library(sqldf)
library(dlnm)


my_mean <- function(x){
  sum = 0
  for(i in 1:length(x)){
    sum = sum + x[i]
  }
  return(sum/length(x))
}

x = runif(100)
data("chicagoNMMAPS")
temp_data <- chicagoNMMAPS$temp

test_bench <- microbenchmark(
  sqrt(x),
  x ^ 0.5,
  mean(temp_data),
  my_mean(temp_data)
)

temp_sorts = microbenchmark(
  auto = sort(temp_data),
  shell = sort(temp_data, method  = 'shell'),
  quick = sort(temp_data, method  = 'quick'),
  radix = sort(temp_data, method  = 'radix'),
  times=50
)
temp_sorts

mbm_flights = microbenchmark(
  base = aggregate(flights$arr_delay, by=list(flights$carrier), mean, na.rm=TRUE),
  sqldf = sqldf("SELECT carrier, avg(arr_delay) FROM flights GROUP BY carrier"),
  dplyr = flights %>% group_by(carrier) %>% summarize(mean(arr_delay, na.rm=TRUE), .groups = 'drop'),
  times=50
)
mbm_flights
