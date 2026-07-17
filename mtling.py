class Cntry:
    cntr="India"
class Gp(Cntry):
    snm="Sonkamble"
class Pp(Gp):
    pnm="Daulat"
class Cc(Pp):
    cnm="Suresh"
    def fullnm(self):
         #print(self.cnm)
         #print(self.cnm," ",self.pnm)
         print(self.cnm," ",self.pnm," ", self.snm," ", self.cntr)
c=Cc()
c.fullnm()
