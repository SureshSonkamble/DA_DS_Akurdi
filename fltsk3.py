f=open("alldata.txt",'a')
dt=input("Enter a data")
f.write(dt)
f.close()

fr=open("alldata.txt",'r')
data=fr.read()
print(data)
sp=open("spl.txt",'a')
uc=open("uc.txt",'a')
lc=open("lc.txt",'a')
dg=open("dg.txt",'a')
for i in data:
    if(not i.isalnum()):
        sp.write(i)
    if(i.isdigit()):
         dg.write(i)
    if(i.isupper()):
         uc.write(i)
    if(i.islower()):
         lc.write(i)
sp.close()
uc.close()
lc.close()
dg.close()
print("Success...")




         
