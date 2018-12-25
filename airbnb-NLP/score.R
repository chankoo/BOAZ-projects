
############################
###### DTM Per Review ######
############################

data = read.csv("DTM.csv",stringsAsFactors = F)
rating = read.csv("ratings.csv",stringsAsFactors = F)

Xtr = as.matrix(data[,-1])
ytr = rating$X0

elastic = cv.glmnet(Xtr, ytr, alpha=0.5)
coef = c(coef(elastic)[,1])


DTM = data[1:1000,-1]
Dtopic = topic[,-1]
Dcoef = as.numeric(coef[-1])
write.csv(Dcoef,"coef.csv")

DT.Dc = matrix(nrow=1000,ncol=599)

for (i in 1:1000) {
  for (j in 1:599) {
    
    DT.Dc[i,j] = DTM[i,j] * Dcoef[j]
    
  }
}
library(dplyr)
Dtopic = as.matrix(Dtopic)
Sent.Score = DT.Dc %*% Dtopic
room.1 = data.frame(Sent.Score[1:8,])
room.2 = data.frame(Sent.Score[9:25,])
room.3 = data.frame(Sent.Score[26:118,])
mm = data.frame(room.1)

for (i in 1:nrow(room.3)) {
  assign(paste("x", i, sep=""), scale(as.numeric(room.3[i,]))[,1])
}
room3 = data.frame(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,
                   x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30)
room3[,30]=rep(0,6)
apply(room1,1,mean)
apply(room2,1,mean)
apply(room3,1,mean)


############################
###### DTM Per Room ######
############################

options("scipen" = 100)
data = read.csv("Dresult.csv",stringsAsFactors = F)
data = data[,-1]
apply(data, 2, mean) 

s.data = data.frame(scale(data))
dfmax <- apply(s.data, 2, max)  
dfmin <- apply(s.data, 2, min)  
p.data = as.data.frame(rbind(dfmax, dfmin, s.data[2670,]))

radarchart(p.data)
library(fmsb)
radarchart( p.data  , axistype=1 ,
            #custom polygon
            pcol=rgb(0.2,0.5,0.5,0.9) , pfcol=rgb(0.2,0.5,0.5,0.5) , plwd=3 ,
            #custom the grid
            cglcol="grey", cglty=1, axislabcol="grey", caxislabels=seq(0,20,5), cglwd=0.8,
            #custom labels
            vlcex=1,
            title = c("radar chart of Room 2670")
)
