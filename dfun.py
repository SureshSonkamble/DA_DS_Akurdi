d = {
    "id": 101,
    "name": "Suresh",
    "marks": 85
}
print(d.keys())
print(d.items())
d.pop('id')#delete based on key
d.popitem()#delete last
print(d)
d["age"] = 25 #add data
d.update({"marks": 90})
print(d)
