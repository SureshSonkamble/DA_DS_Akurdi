class Prnt1:
    def pp1(self):
        print("This is parent 1 ")
class Cld1(Prnt1):
    def c1(self):
        print("This is child 1 ")
class Cld2(Prnt1):
    def c2(self):
        print("This is child 2")
cc1=Cld1()
cc1.c1()
cc1.pp1()
cc2=Cld2()
cc2.c2()
cc2.pp1()
