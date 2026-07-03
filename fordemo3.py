#find number even and odd count between 1 to 100
e=0
o=0
for i in range(1,102):
    if(i%2==0):
        e=e+1
    else:
        o=o+1
print("Even :=",e)
print("Odd :=",o)  
