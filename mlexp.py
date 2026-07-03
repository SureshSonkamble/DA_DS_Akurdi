try:
    sm="suresh"
    print(snm)
except NameError as t:
    print(t)
try:
    s=[1,2,3]
    print(s[3])
except IndexError as i:
    print(i)
try:
    a=2
    b=0
    d=a/b
    print(d)
except ZeroDivisionError as z:
    print(z)
