utcak=[]
#1feladat
f=open("utca.txt","r")
for egySor in f:
    utcak.append(egySor.replace("\n",""))
    
f.close()
utcak.pop(0)
#2feladat
print("2. feladat. A mintában {} telek szerepel.".format(len(utcak)))

#3feladat
adoszamBeker=input("3. feladat. Egy tulajdonos adószáma: ")
x=[]
for e in utcak:
   x.append(e.split(" "))

for e in x:
    if e[0]==adoszamBeker:
        print(e[1],e[2])
else:
    print("Nincs ilyen adószám")
   

