adatok=[]
f=open("snooker.txt")
for e in f:
    e=e.replace("\n","").split(";")
    adatok.append(e)
f.close()
mezonevek=adatok.pop(0)
#print(mezonevek)

print("3. feladat: A világranglistán {} versenyző szerepel.".format(len(adatok)))

fizetes = []
for x in adatok:
    fizetes.append(int(x[3]))
összeg=sum(fizetes)
atlag=összeg/len(fizetes)



print("4. feladat: A versenyzők átlagosan {:.2f} fontot kerestek.".format(atlag))
kinaipenz=[]
for kinai in adatok:
    if kinai[2]=="Kína":
        kinaipenz.append(int(kinai[3]))
legjobb=max(kinaipenz)

for e in adatok:
    #print(e[3])
    if e[3]==str(legjobb):
        print("5. feladat: A legjobban kereső kínai versenyző:\n Helyezés: {}\n Név: {} \n Ország: {} \n Nyeremény összege: {} Ft".format(e[0],e[1],e[2],e[3]))
    
for e in adatok:
    if e[2] =="Norvégia":
        print("6. feladat: A versenyzők között van norvég versenyző.")


kinai=0
anglia=0
wales=0
skocia=0
for fo in adatok:
    if fo[2]=="Skócia":
        skocia+=1
    if fo[2]=="Kína":
        kinai+=1
    if fo[2]=="Anglia":
        anglia+=1
    if fo[2]=="Wales":
        wales+=1

print("7. feladat: Statisztika \n \tKína - {} fő \n \tAnglia - {} fő \n \tWales - {} fő \n \tSkócia - {} fő".format(kinai,anglia,wales,skocia))
