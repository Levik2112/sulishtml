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

print(szamok5)


szamok5=[e for e in szamok5 if e%5==0]
print(szamok5)
