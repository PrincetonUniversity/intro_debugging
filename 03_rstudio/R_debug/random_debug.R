a=as.numeric(Sys.time())
set.seed(a)

n.sim = 1000 # number of simulations

cts = rep(0, n.sim) # counts of dice casts

x = NULL # container for the current cast total

cast_dice_pair <- function() {
  x = c(sample(1:1,1) + sample(1:6,1))
  return(x)
}

for (i in 1:n.sim) {
  cat("sim: ", i, "\n")
  start = cast_dice_pair()
  cts[i] = cts[i] + 1 # update of cast counts
  x = start
  if(x %in% c(2,3,4,5,6)){ # initial target totals
    next} # stop the game if this total is casted
  
  repeat {
      cat("Repeat of sim: ", i, "\n")
      x = cast_dice_pair()
      cts[i] = cts[i] + 1
      if(x %in% c(12)){ # new target of the repeat loop
        break
      }
    }
  }

mean(cts)
