print("Normal flow 1")
a=2
b=0
print("Normal flow 2")
try:
    ad=a/b
    print(ad)
except ZeroDivisionError as z:
    print("Cannot divide by zero")
print("Normal flow 3")
print("Normal flow 1000")
