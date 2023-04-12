class MyClass:
    x=5 
    def megnovel(self,mennyivel=1):
        self.x+=mennyivel


class kutya:
    nev,fajta,agresszivitas,kor,szin=["","",0,0,""]
    def __init__(self,nev,fajta,agresszivitas,kor,szin):
        self.nev=nev
        self.fajta=fajta
        self.agresszivitas=agresszivitas
        self.kor=kor
        self.szin=szin
    def ugat(self):
        print("vau-vau")
    def koszon(self):
        print("Vau-vau, {} vagyok.".format(self.nev))
    def talalkozas(self,masik):
        if self.agresszivitas>5 or masik.agresszivitas>5:
            #támadás
            if self.agresszivitas>=masik.agresszivitas:
                print("Megöllek kutya!")
            else:
                print("Ne bánts báttya")
        else:
            if self.agresszivitas>=masik.agresszivitas:
                print("Szevasz kutya!")
            else:
                print("Szia  báttya")
    def __str__(self):
        return "{}, {}({})".format(self.nev,self.fajta,self.kor)
            
class kotorek(kutya):
    def koszon(self):
        print("{} a nevem,kutyaság a mindenem!".format(self.nev))
        
    def __init__(self,nev,fajta,ag,kor,szin,szemszin):
        super().__init__(nev,fajta,ag,kor,szin)
        self.szemszin=szemszin
        

        
k1=kutya("bodri","puli",3,9,"fekete")
k2=kutya("morzsi","golden retriever",1,3,"világos barna")

kotor1=kotorek("Füles","tacskó",10,4,"barna","zöld")
print(kotor1.szemszin)
#print(k1.szemszin)

k1.ugat()
k1.koszon()
k2.koszon()
k2.talalkozas(k1)
k1.talalkozas(k2)
kotor1.koszon()
k1.talalkozas(kotor1)
print(k1)
print(kotor1)
"""
print(MyClass.x)

p1=MyClass()
print(p1.x)

p2=MyClass()
p2.x=6
print(p2.x)


p1.megnovel()
p1.megnovel(10)
print(p1.x)
""" 
