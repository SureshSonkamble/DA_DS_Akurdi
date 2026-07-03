import random
rn=random.randint(1, 10)
c=0
while(c<3):
    c=c+1
    un=int(input("Enter a number between 1 to 10 to be guess:="))
    if(rn==un):
        print("Number Guess Correct")
    else:
        print("Wrong Number")
    if(rn>un):
        print("Number is too small")
    else:
       print("Number is too high")
