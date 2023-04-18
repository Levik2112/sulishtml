class auto:
    szin,ajtokszama,marka,tipus=["",0,"",""]
    #indulaskor mondja azt hogy brrr,hangjelzes(kurt,duda=tütü),irányjlező=katkatkat,
    #leszarmazott amelyik bmw,indul=vrumm,iranyjelzo=néma,
    #mégegy class mercedes néven kürt=vmi mást,
    #3. auto audi miden tulajdonság ami eddig,check engine de ha megnyomjak a kurtot akkor bekapcsol

    def __init__(self,szin,ajtokszama,marka,tipus):
        self.szin=szin
        self.ajtokszama=ajtokszama
        self.marka=marka
        self.tipus=tipus

    def inditas(self):
        print("Brrr")
    def duda(self):
        print("Tütü")
teszt=auto("piros",3,"bmw","e34")
print(teszt.inditas())
print(teszt.duda())
