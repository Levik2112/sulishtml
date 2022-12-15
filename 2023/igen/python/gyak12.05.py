import random

minimumErtek=int(input("Add meg,hogy hol kezdődjön: "))
maximumErtek=int(input("Add meg,hogy mennyi legyen a maximuma: "))
db=int(input("Add meg,hogy hány számot generáljunk: "))
lista=[]

for i in range(db):
    lista.append(random.randint(minimumErtek,maximumErtek))
print(lista)
#random=random.randint(minimumErtek,maximumErtek)
#print(random)


for e in lista:
    print(e, "*" * int(e//10))
