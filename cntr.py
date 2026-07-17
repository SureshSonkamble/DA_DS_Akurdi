#constructor is get called when object is created
class Cntr:
    def __init__(self): #constructor
        print("This is constructor...")
    def __init__(self,name):
        self.name=name
        
    def cc(self):
        print("Name:=",self.name)
#Cntr.cc()
c=Cntr("Suresh") #object
c.cc()
