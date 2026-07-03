try:
    l=[1,2,3]
    print(l[5])
    sm="Suresh"
    print(sm)
    n=2/0
    print(n)
except NameError  as n:
        print(n)
except IndexError  as i:
        print(i)
except Exception as e:
    print(e)
