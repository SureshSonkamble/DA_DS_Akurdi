'''t=(1,2,3,4,1,1,2,6,7,1,8,9)
print(t)
print(set(t))'''

s={1,2,99,3,7,'a',2.2,'b','z',3.3,'Z',1,1,'z'}
print(s)
s.add('suresh')
s.pop()
#s.clear()
#del s
s.update([100,200]) #add data
print(s)
print(s)
for i in s:
    print(i)
