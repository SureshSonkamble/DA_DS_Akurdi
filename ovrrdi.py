class Prnt:
    prty="$78787"
    def marry(self):
        print("ABC")

class Cld(Prnt):
    pass
    def marry(self):#override
        print("Laxmi")
c=Cld()
print(c.prty)
c.marry()
