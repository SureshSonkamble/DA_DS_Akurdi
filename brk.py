n=int(input("Enter number between 1 to 50:="))
for i in range(1,51):
    print(i)
    if(i==n):
        break
for i in range(1,51):
    if(i==n):
        print(i,"found")
        continue
    print(i)
