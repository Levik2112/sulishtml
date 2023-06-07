
class cb:
    def __init__(self,ora,perc,adas,nev):
        self.ora=ora
        self.perc=perc
        self.adas=adas
        self.nev=nev
    def __str__(self):
        return("Óra:{},perc: {}, adas: {},nev:{}".format(self.ora,self.perc,self.adas,self.nev))
    def AtszamolPercre():
        pass

adatok=[]
f=open("cb.txt")
for e in adatok:
    cb.append(e[0])
    cb.append(e[1])
    cb.append(e[2])
    cb.append(e[3])
for e in f:
    adatok.append(e.replace("\n","").split(";"))
f.close()
adatok.pop(0)
print(adatok)
print("3. feladat: Bejegyzések száma: {} db".format(len(adatok)))

nevek=[]
for e in adatok:
    nevek.append(e[3])
#print(nevek)
print("4. feladat")

for e in adatok:
    if e[2]=="4":
        print("Volt négy adást indító sofőr.")
        break
else:
    print("Nem volt négy adást indítós sofőr.")

nevBeker = input("5. feladat: Kérek egy nevet: ")
cbossz = []

for e in adatok:
    if e[3] == nevBeker:
        cbossz.append(int(e[2]))
ossz=sum(cbossz)

if nevBeker in nevek:
        print("{} {}x használta a CB-rádiót.".format(nevBeker, ossz))
else:
    print("Nincs ilyen sofőr!")
        
def AtszamolPerc():
    osszora=sum(adatok[0]*60+adatok[1]+adatok[2])


print("8.feladat")
soforokSzama=[]
for e in nevek:
    soforokSzama.append(e)
print(sum(soforokSzama))

f_uj=open("cb2.txt","w")
f_uj.write("igen")
f_uj.close()

