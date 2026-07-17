from abc import ABC, abstractmethod
class Payment(ABC): #inherit
    def payinfo(self):
        print("Pay EMI")        
    @abstractmethod   
    def pay():
        pass
class user3(Payment):
    def pay(self):
        print("Credit Card payment")
u3=user3()
u3.payinfo()
u3.pay()
class user2(Payment):
    def pay(self):
        print("Cash Payment")
u2=user2()
u2.payinfo()
u2.pay()


    
class user1(Payment):
    def pay(self):
        print("Online Payment")
u1=user1()
u1.payinfo()
u1.pay()





        
#p=Payment()
#p.payinfo()
