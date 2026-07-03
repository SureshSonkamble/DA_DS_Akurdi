n=int(input("Enter a number:"))
r=0
sm=0
while(n>0):
    r=n%10
    sm=sm+r
    n=n/10

print("Sum of digit:=",int(sm))    
