setwd("/Users/zachang/Desktop/Data Science Course/homework/ZacharyAng/Project")
#load libraries
library(lpSolve)
library(stringr)

# Read the Data in ## 

df = read.csv("Gameweek 7 Predictions.csv",header=T)


#Create the constraints
num_gk = 2
num_def = 5
num_mid = 5
num_fwd = 3
max_cost = 100
# Create vectors to constrain by position
df$Goalkeeper = ifelse(df$type_name == "Goalkeeper", 1, 0)
df$Defender = ifelse(df$type_name == "Defender", 1, 0)
df$Midfielder = ifelse(df$type_name == "Midfielder", 1, 0)
df$Forward = ifelse(df$type_name == "Forward", 1, 0)
# Create vector to constrain by max number of players allowed per team
team_constraint = unlist(lapply(unique(df$team_name), function(x, df){
ifelse(df$team_name==x, 1, 0)
}, df=df))
df$cost_t1m = df$cost_t1/10
# next we need the constraint directions
const_dir <- c("=", "=", "=", "=", rep("<=", (1+length(unique(df$team_name))))

# The vector to optimize against
objective = df$predictions

# Put the complete matrix together
const_mat = matrix(c(df$Goalkeeper, df$Defender, df$Midfielder, df$Forward,
df$cost_t1m, team_constraint),
nrow=(5 + length(unique(df$team_name))),
byrow=TRUE)
const_rhs = c(num_gk, num_def, num_mid, num_fwd, max_cost, rep(3, length(unique(df$team_name))))
# And solve the linear system
x = lp ("max", objective, const_mat, const_dir, const_rhs, all.bin=TRUE, all.int=TRUE)
print(arrange(df[which(x$solution==1),], desc(Goalkeeper), desc(Defender), desc(Midfielder), desc(Forward), desc(predictions)))

