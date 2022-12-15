import random
import math
l=[]
for i in range(10):
    szam=random.random()
    l.append(math.floor(szam*90)+10)
#print(l)

l=[]
for i in range(10):
    l.append(random.randint(10,99))
    
#print(l)


szamok=[]
for i in range(100):
    szamok.append((random.randint(-1000,1000)*3))
print(szamok)


#print(sum(szamok))  
szamok5=[]
for e in szamok:
    if e%5==0:
        szamok5.append(e)

print()
print()

#print(szamok5)


szamok5=[e for e in szamok5 if e%5==0]
#print(szamok5)

#167
#1666
#hattal ósztható,de 12vel (2*6) nem
#print(random.randrange(166,1667,2)*6)

#print((random.randint(83,832)*2+1 )* 6)

szavak=["alma","körte","barack","banón","dinnye","szőlő"]
#random.seed(1)
print(szavak[random.randint(0,len(szavak)-1)])
print(random.choice(szavak))

#[["alma",14],["körte",18],[]...]
print("-"*20)

nagylista=[]
for e in szavak:
    #print(e)
    kislista=[]
    kislista.append(e)
    kislista.append(random.randint(12,312))
    #print(kislista)
    nagylista.append(kislista)

print(nagylista)

for e in nagylista:
     print(e[0].ljust(10),"I" * e[1],e[1],"kg")
