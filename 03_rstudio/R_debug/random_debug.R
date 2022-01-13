a=as.numeric(Sys.time())
set.seed(a)

n.sim = 100 # number of simulations

cts = rep(0, n.sim) # counts of dice casts

x = NULL # container for the current cast total

# Simulates casting a pair of dice and returns the total
cast_dice_pair <- function() {
  x = c(sample(2:6,1) + sample(1:6,1))
  return(x)
}

## Estimate how many throws of 2 s sided dice are need to get a specific number 
## between 2-12
for (i in 1:n.sim) {
  target <- sample(2:12, 1)
  cat("Simulation: ", i, "\n")
  repeat {
      # cat("Repeat of sim: ", i, "\n")
      x = cast_dice_pair()
      cts[i] = cts[i] + 1
      if(x %in% c(target)){ # new target of the repeat loop
        break
      }
    }
  }

mean_casts = mean(cts)
cat("Average number of casts: ", mean_casts, "\n")
