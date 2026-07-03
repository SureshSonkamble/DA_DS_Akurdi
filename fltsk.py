#read number of words from file
f=open('suresh.txt','r')
wd=f.read()
wrd=wd.split(" ")
print(wrd)
print("Total  lines:=",wd.count('\n')+1)
print("Total Word count:=",len(wrd))
print("Particular word count:=",wd.count('da'))
print("Total number of characters: =",len(wd))
dcnt=0
al=0
for i in wd:
    if(i.isdigit()):
        dcnt=dcnt+1
    if(not i.isalnum()):
        al=al+1
print("Number of digit:=",dcnt)
print("Number of Special character:=",al)
