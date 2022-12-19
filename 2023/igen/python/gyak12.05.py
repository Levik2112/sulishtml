import random
import math

minimumErtek=int(input("Add meg,hogy hol kezdődjön: "))
maximumErtek=int(input("Add meg,hogy mennyi legyen a maximuma: "))
db=int(input("Add meg,hogy hány számot generáljunk: "))
lista=[]

for i in range(db):
    lista.append(random.randint(minimumErtek,maximumErtek))
print(lista)
#random=random.randint(minimumErtek,maximumErtek)
#print(random)

legnagyobb=max(lista)
egyseg=80//legnagyobb
for e in lista:
    print("*" * (e*egyseg))

#3 jegyű szám
szam=""
while len(szam)!=3:
    szam=(input("Kérek egy 3 jegyű számot: "))
szam=int(szam)
if szam%12==0:
    print("Osztható")
print(szam)


szoveg="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ac elit ultricies, accumsan quam non, egestas magna. Donec viverra sit amet est sed consequat. Maecenas fermentum ex ac nisi malesuada blandit. Quisque ac sodales purus. Sed ut turpis vitae justo maximus dapibus quis quis risus. In tristique urna id est lobortis, eu posuere diam ultrices. Phasellus non magna urna. Suspendisse urna tortor, vehicula sit amet enim a, ullamcorper rhoncus sapien. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce non dapibus tortor, vitae bibendum est."
print(len(szoveg.split(" ")))
print()
betu="i"
szoveg2=szoveg.replace(betu,betu.upper())
print(szoveg2)
