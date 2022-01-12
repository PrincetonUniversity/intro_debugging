packages <- c("microbenchmark","tidyverse","nycflights13","sqldf","dlnm","profvis")
install.packages(setdiff(packages, rownames(installed.packages())))  

library(microbenchmark)
library(tidyverse)
library(nycflights13)
library(sqldf)
library(dlnm)
library(profvis)

threshold <- 30

profvis({
  longest_delay <- c()
  record_delay <- c()
  for(i in 1:nrow(flights)){
    longest_delay <- max(longest_delay, flights$arr_delay[i])
    record_delay[i] <- flights$arr_delay[i] >= threshold & flights$arr_delay[i] >= longest_delay
  }
  flights <- cbind(flights, record_delay)
})