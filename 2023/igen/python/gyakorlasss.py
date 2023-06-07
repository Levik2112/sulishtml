#modul amiben van egy osztaly teglalap nevenami ket adatot tartalmaz hossz szel ket fugveny terulet kerulet szamitassal
#masik program ami hasznalja beker 5 teglalap adatot irjuk ki annak a teglalapnak az oldalait amelyik a legnagyobb teruletu,keruletu

class teglalap:
    def __init__(self,hosszusag,szelesseg):
        self.hosszusag=hosszusag
        self.szelesseg=szelesseg
    def terulet(self):
        
        print("A téglalap területe ",self.hosszusag*self.szelesseg,"cm")
    
    def kerulet(self):
        
        print("A téglalap kerülete",2*(self.hosszusag+self.szelesseg),"cm")
