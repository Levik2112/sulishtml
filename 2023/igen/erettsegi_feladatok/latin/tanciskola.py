class tanc:
    def __init__(self,tanc,fiu,lany):
        self.tanc=tanc
        self.fiu=fiu
        self.lany=lany
    def __str__(self):
        return "Tánc: {}, lány: {}, fiú: {}".format(self.tanc,self.lany,self.fiu)

    def isVilma(self):
        #if self.lany=="Vilma":
         #   return True
       # else:
        #    return False
        return self.lany=="Vilma"

f=open("tancrend.txt")
sorok=[]
#2. megoldás
tancok2=[]
temp=[]
for e in f:
    sorok.append(e.strip())
    #2 megoldás
    if len(temp)<3:
        temp.append(e)
    else:
        tancok2.append(tanc(temp[0],temp[1],temp[2]))

#HF:ugyanezt a beolvasást egy más fajta módon megcsinálni
    
f.close()
#print(sorok)
print(sorok[:3])
#1 megoldás

tancok=[]
for i in range(len(sorok)//3):
    tancnev=sorok[1*3]
    lany=sorok[1*3+1]
    fiu=sorok[1*3+2]
    tancok.append(tanc(tancnev,lany,fiu))
#print(tancok)

print("2. Feladat")
print("első tánc: {},utolsó: {}".format(tancok[0].tanc,tancok[-1].tanc))

db=0
for egyTanc in tancok:
    if egyTanc.tanc=="samba":
        db+=1
print("Ennyi samba volt: {}".format(db))

print("Vilma ezekben szerepelt: ")
for egyTanc in tancok:
    if egyTanc.isVilma()==True:
        print(egyTanc.tanc)
