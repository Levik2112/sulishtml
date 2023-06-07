import random
import modul
sorok=[]
f=open("szavak.txt")
for e in f:
    sorok.append(e.replace('"','').strip())
f.close()
#print(sorok)

sorok=sorok[0].split(", ")
#print(sorok)

szavak=[]
for e in sorok:
    szavak.append(modul.szo(e))
#print(szavak)
rejtett=random.choice(szavak)
print(rejtett.szo)
tippek=[]
while True:
    be=input("Kérek a tippet: ")
    tippek.append(be)
    if be == "stop":
        break
    vissza=rejtett.minta(be)
    

    print("Az eredmény: {}".format(vissza))
    if vissza==be:
        break
if tippek[-1]=="stop":
    pass
else:
    print("{} tippeléssel sikerült kitalálni.".format(len(tippek)))
