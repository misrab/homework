setwd("/Users/zachang/Desktop/Data_Science_Course/homework/ZacharyAng/Data")
#load libraries
library(lpSolve)
library(stringr)
library(plyr)
library(httr)
library(rjson)
library(ggplot2)
# Read the Data in ## 

fantasy_scores=c()

## This for loop performs the optimisation step for GW 8 to 26
for (i in 8:26){
df = read.csv(paste("Gameweek",i,"Predictions.csv"),header=T)


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
const_dir <- c("=", "=", "=", "=", rep("<=", (1+length(unique(df$team_name)))))

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
print(x)

# Store the data in a data frame and csv
pred_df= df[which(x$solution==1),]
write.csv(pred_df,file=paste("Optimised Predictions for Gameweek",i,".csv"))
pred_df$actual[which(pred_df$actual==max(pred_df$actual))] = pred_df$actual[which(pred_df$actual==max(pred_df$actual))]*2
fantasy_scores<-append(fantasy_scores,sum(pred_df$actual))
}

# Evaluating my results

my_own_scores=c(91,69,43,52,40,74,43,62,73,71,40,75,43,25,69,41,63,38,55) # This is how I performed over GW8 to GW26
average_scores=c(55,51,42,56,45,55,51,51,51,59,44,57,40,35,46,43,60,55,41) # 
scores<-data.frame(cumsum(fantasy_scores),cumsum(my_own_scores),cumsum(average_scores),row.names=8:26)
?data.frame
plot(8:26,cumsum(fantasy_scores),type="l",lwd=3,col="green",xlab="Gameweek",ylab="Cumulative Fantasy Scores",main="Fantasy Scores from Gameweek 8 to Gameweek 26",ylim=c(100,1400),xlim=c(5,34))
lines(8:26,cumsum(average_scores),lwd=3,col="magenta")
lines(8:26,cumsum(my_own_scores),lwd=3,col="blue")
legend(x=27,y=1200,legend=c("My Predictions","My Actual Scores","Average Scores"),col=c("green","blue","magenta"),xjust=0,lty=1,cex=0.65)

## See how many transfers I actually made 
Indmat=c()
for (i in 8:25){
	df1=read.csv(paste("Optimised Predictions for Gameweek",i,".csv"),header=T)
	df2=read.csv(paste("Optimised Predictions for Gameweek",i+1,".csv"),header=T)
	Indmat=append(Indmat,df1 %in% df2)
}
Indmat=matrix(Indmat,nrow=18,byrow=T)
14-rowSums(Indmat)