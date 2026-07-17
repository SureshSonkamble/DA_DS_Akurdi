class Prnt:
    p=100
    def pp(self):
        print("This is parent class")

class Cld(Prnt):#inherit
    def cc(self):
        print("This is child class")

#p=Prnt()
#p.pp()
c=Cld()
c.cc()
c.pp()
print(c.p)
