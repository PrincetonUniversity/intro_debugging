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

profvis({
  snail_sort <- function(x){
    n<-length(x)
    for(j in 1:(n-1)){
      for(i in 1:(n-j)){
        if(x[i]>x[i+1]){
          temp<-x[i]
          x[i]<-x[i+1]
          x[i+1]<-temp
        }
      }
    }
    return(x)
  }
  sort_search <- function(search_list, query){
    sorted_list <- snail_sort(search_list)
    for(j in 1:(length(sorted_list)-1)){
      if(query == sorted_list[j]){
        return(1)
      }
    }
    return(0)
  }
  search_list<-sample(1:10000,1000)
  query_list<-sample(1:10000,100)
  found_ctr <- 0
  for(i in 1:(length(query_list)-1)){
    if(sort_search(search_list, query_list[i]) == 1)
      found_ctr = found_ctr + 1
  }
  cat('Elements found:', found_ctr, '\n')
})