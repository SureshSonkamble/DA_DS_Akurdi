class Pp1():
    def p1(self):
        print("This is parent 1")
class Pp2():
    def p2(self):
        print("This is parent 2")
class Cld(Pp1,Pp2):
    def cc(self):
        print("This is child class")
c=Cld()
c.cc()
c.p1()
c.p2()
#Cld.cc()
