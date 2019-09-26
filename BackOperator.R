# Polynomial
x<- seq(1,1.5, by = 0.1)
y<- 1+2*x+3*x*x
l<-length(x)
dtable<-array(0,dim= c(l,l+2))
dtable[,1]<-x
dtable[,2]<-y
for (i in 1:3){
 dtable [1:(l-i),(i+2)]<- diff(y,1,i)
}

round (dtable,2)



#Polynomial and Periodic 
x<-seq(1,2, by=0.1)
y<-1+2*x+3*x^2+2*sin(2*pi*x)
plot(y~x)



# Polynomial and periodic plus random error

x<-seq(1,2, by=0.1)
l<-length(x)
y<-1+2*x+3*x^2+ 2*sin(2*pi*x)+ rnorm(l,0,0.1)
dtable<-array(0,dim = c(l,l+2))
dtable[,1]<-x
dtable[,2]<-y
for(i in 1: (l-1)){
dtable[1:(l-i),(i+2)]<-diff(y,1,i)
}
round(dtable[,2:11], 2)
