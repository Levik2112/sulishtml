
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
#print(helyes)

valaszok=[]
for e in adatok:
    valaszok.append(e.split(" "))

#print(valaszok)

print("2. feladat: A vetélkedőn {} versenyző indult!".format(str(len(valaszok))))

versenyzo=input("3. feladat: A versenyző azonosítója = ")

#1.lehetőség
versenyzoValasza=""
for e in valaszok:
    if e[0]==versenyzo:
        print(e[1]+"\t a versenyző válasza.")
        versenyzoValasza=e[1]
#2.lehetőség
#print("{} \t(a versenyző válasza)".format([e[1] for e in valaszok if e[0]==versenyzo[0]]))




print("4.feladat")
print(helyes+"\t a helyes megoldás.")
print(versenyzoValasza)

for sorszam,betu in enumerate(versenyzoValasza):
    #print(betu,str(sorszam))

    if betu==helyes[sorszam]:
        print("+",end="")
    else:
        print(" ",end="")

print("\t a versenyző helyes válaszai.")

feladat=int(input("5.feladat: A feladat sorszáma = "))

db=0
for e in valaszok:
    if e[1][feladat]==helyes[feladat]:
        db+=1

print("A feladatra {0} fő,a versenyzők {1}-a adott helyes választ!".format(db.db/len(valaszok)))
    
