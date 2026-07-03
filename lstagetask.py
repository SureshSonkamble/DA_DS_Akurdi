n=int(input("Enter a number of guest:="))
age=[]
c=[]
a=[]
s=[]
for i in range(n):
    ag=int(input("Enter a age:="))
    age.append(ag)
print(age)

for i in age:
    if(i>=60):
        s.append(i)
    if(i<60 and i>=18):
        a.append(i)
    if(i<18):
        c.append(i)
#print(age)
print("Child:=",len(c)," ",c)
print("Adult:=",len(a)," ",a)
print("Senior:=",len(s)," ",s)

