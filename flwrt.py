'''f=open('suresh.txt','a')
data=input("Entre data to be write file:=")
f.write(data)
f.close()
print("file write success..")'''

fr=open('suresh.txt','r')
#data=fr.read() #read all file data at once
#data=fr.readlines() #read all file data at once in single list
data=fr.readline() #read one line at a time
#data=fr.readline()
#data=fr.readline()
print(data)
