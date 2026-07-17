class Bank:#class
    __bal=10000 #var __private
    def viewbl(self,pin): #public
        if(pin==123):
            print("Balance:=",self.__bal)
        else:
            print("Invalid user")

p=int(input("Enter pint to view bal="))
b=Bank()
#print(b.bal)
b.viewbl(p)
#print(Bank.bal)
    

