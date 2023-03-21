
f=open("felfedezesek.csv")
elemek=[]
for e in f:
    elemek.append((e.replace("\n","").split(";")))
f.close()

elemek.pop(0)
print(f"3.Feladat:Elemek száma: {len(elemek)}")

okor=[e for e in elemek if e[0]=="Ókor"]
#print(len(okor))
print(f"4.Feladat:Felfedezések száma az ókorban: {len(okor)}")

while True:
    vegyjel=input("5.Feladat:Kérek egy vegyjegyet: ").lower()           
    if len(vegyjel)<3 and len(vegyjel)>0:
        jo=True
        for i in range(len(vegyjel)):
            if not(vegyjel[i]>="a" and vegyjel[i]<="z"):
                jo=False
        if jo:
            break
#print(vegyjel)
                
kereset=[e for e in elemek if e[2].lower()==vegyjel]
if kereset==[]:
    print("Nincs ilyen elem!")
else:
    print()
print(kereset)
