nev=input("Kérek egy nevet:")
print("A " + nev + " neved irtad be.")

print("A {nev} nevet irtad be.".format(nev=nev))

if len(nev)<5:
    print("jó rövid név")
elif len(nev)>=10:
    print("Veri big név.")

be="nem végjel"
szavak=[]
while be!="":
    be=input("irj be valamit: ")
    szavak.append(be)
#szavak.remove("")
#szavak.pop(-1)
#szavak=szavak[:-1]
szavak=[]
print(szavak)
