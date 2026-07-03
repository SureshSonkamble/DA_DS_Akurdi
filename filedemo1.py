#Create file
'''try:
    f=open('suresh.txt','x')
    print("File create success..")
except Exception as e:
    print(e)'''
#Write data into file
try:
    #f=open('suresh.txt','w')
    #append data into file
    #f=open('suresh.txt','a')
    f.write(' 01-07-2026')
    print("File written success..")
    f.close()
except Exception as e:
    print(e)
