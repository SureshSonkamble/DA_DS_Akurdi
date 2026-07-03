import os
#create
f=open('cs.txt','w')
f.write('CoDingSeeKho')
print("File write success..")
f.close()
#read
fr=open('cs.txt','r')
data=fr.read()
print(data)

for i in range(1,11):
    path="Fldr"+str(i)
    os.makedirs(path) #Fldr1
    print(path+'test.txt')
    fw=open(path+'/test.txt','w')
    fw.write(data)
    
