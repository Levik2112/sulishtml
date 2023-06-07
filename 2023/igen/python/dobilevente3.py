import math
class ember:
    szulev=0
    magassag=0
    testsuly=0
    def __init__(self,szulev,magassag,testsuly):
        self.szulev=szulev
        self.magassag=magassag
        self.testsuly=testsuly


    def eletkor(self):
        print(2023-self.szulev)

    def tti(self):
        print(self.testsuly/(self.magassag*self.magassag))

ember1=ember(1990,210,160)
ember1.eletkor()
ember1.tti()

class diak(ember):
    osztalybetu=""
    def __init__(self,osztalybetu):
        self.osztalybetu=osztalybetu
        super().__init__(szulev)

    def osztalyszam(self):
        if self.szulev>19:
            print("Felnőttoktatás")
ember2=diak("B")
ember2.osztalyszam()
