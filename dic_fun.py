d={
     "id":101,
     "name":"suresh",
     "city":"pune",
     "age":33
    }

for i in d:
    print(d[i])

print(d)
d.update({"city": "Nashik"})
d.update({"marks": 81})
print(d)
#add new data
d['mob']="8485070453"
print(d)
#pop(key)
d.pop("age")
d.popitem()#remove data from last
d.popitem()#remove data from last
print(d)
d.clear()
print(d)
del d
print(d)



