def ado(adosav,alapterulet):
    ar=0
    alapterulet=int(alapterulet)
    if adosav=="A":
        ar= int(arak[0])*alapterulet
    elif adosav=="B":
        ar= int(arak[1])*alapterulet
    else:
        ar= int(arak[2])*alapterulet
    if ar>=10000:
        return ar
    else:
        return 0
    

hazak=[]
f=open("utca.txt")
for egySor in f:
    hazak.append(egySor.replace("\n","").split(" "))
    
f.close()
arak=hazak.pop(0)
#print(arak)

print("2.Feladat: {} telek szerepel.".format(len(hazak)))

adoBeker=input("3.feladat: Egy tulajdonos adószáma: ")
tulajdonok=[]
for e in hazak:
    if e[0]==adoBeker:
       #print("{} {}".format(e[1],e[2]))
        tulajdonok.append(e)
   

#tulajdonok=[e for e in hazak if e[0]==adoszam]
if len(tulajdonok)==0:
    print("Nem szerepel az adatállományban.")
else:
    for e in tulajdonok:
        print("{} utca {}".format(e[1],e[2]))


#print(ado("C",120))

hazakA=[e for e in hazak if e[3]=="A"]

hazakB=[]
for e in hazak:
    if e[3]=="B":
        hazakB.append(e)
hazakC=[e for e in hazak if e[3]=="C"]


for i in range(len(hazakA)):
    hazakA[i].append(ado(hazakA[i][3],hazakA[i][4]))


