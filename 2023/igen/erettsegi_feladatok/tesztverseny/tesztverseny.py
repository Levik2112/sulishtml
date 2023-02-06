

f=open("valaszok.txt","r")

adatok=f.read().split("\n")
#1megoldás
adatok.remove("")
#2megoldás
#adatok=adatok[:-1]
f.close()
#print(adatok)

helyes=adatok[0]
adatok.remove(helyes)

valaszok=[]
for e in adatok:
    valaszok.append(e.split(" "))

#print(valaszok)

