l=[45,23,11,7,6,3,3,62,89,9,3,4,66,98,12,34,3]
print("Count:=",l.count(3))
print(len(l))
#max number from list
mx=l[0]#45
mn=l[0]#45
for i in l:
    if(mx<i):
        mx=i
    if(mn>i):
        mn=i    
print("Max:=",mx)
print("Min:=",mn)

'''sm=0
for i in l:
    sm=sm+i
print("Sum:=",sm)  '''  
   
