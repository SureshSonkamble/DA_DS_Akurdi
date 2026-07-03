try:
    a=2
    b=2
    d=a/b
    print(d)
    sm="suresh"
    print(sm)
    s=[1,2,3]
    print(s[1])
except NameError as nm:
    print(nm)
except IndexError as nm:
    print(nm)
except ZeroDivisionError as z:
    print(z)     
print("Normal flow")    
