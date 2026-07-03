import os
try:
    os.makedirs('Test')
    print("Folder create success..")
except Exception as e:
    print(e)
f=open("Test/test.txt",'x')

#create 10 folder
'''try:
    for i in range(1,50):
        os.makedirs('Test'+str(i))
        print(i)
except Exception as e:
    print(e)  '''  
