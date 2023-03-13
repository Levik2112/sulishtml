#Gyakorlás 2023.03.07

def oszlopBe(hanyadik):
    oszlop=[]
    for e in tabla:
        oszlop.append(e[hanyadik-1])

    return oszlop

gyumolcsok=["alma","banán","körte","barac","szőlő","licsi","eper"]
print(f"Ennyi gyümölcs van: {len(gyumolcsok)}")
print(gyumolcsok[3])
#gyumolcsok[3]+="k"
#gyumolcsok[3]="barack"

print(gyumolcsok.index("barac"))
#gyumolcsok[gyumolcsok.index("barac")]+="k"
index=gyumolcsok.index("barac")
gyumolcsok[index]+="k"

print(gyumolcsok[3])


print("5 betűnél kisebb gyümölcs:")

rovid=[]
for i in range (len(gyumolcsok)):
    if len(gyumolcsok[i])<5:
        rovid.append((gyumolcsok[i]))

print(rovid)


rovid=[]
for e in gyumolcsok:
    if len(e)<5:
        rovid.append(e)

print(rovid)

rovid=[e for e in  gyumolcsok if len(e)<5]
print(rovid)

rovid=[]
i=0
while i<len(gyumolcsok):  
    if len(gyumolcsok[i])<5:
            rovid.append(gyumolcsok[i])
    i+=1
print(rovid)
rovid=[]
i=0
while True:
    print(i)
    if len(gyumolcsok[i])<5:
        rovid.append(gyumolcsok[i])
    if len(gyumolcsok)-1==i:
        break
    i+=1

print(gyumolcsok[:2])
print(gyumolcsok[-2:])
print(gyumolcsok[len(gyumolcsok)-2:])
print(gyumolcsok[1:len(gyumolcsok)-1])



paratlan=gyumolcsok[1::2]
print(paratlan)
paros=gyumolcsok[::2]
print(paros)

masolat=gyumolcsok
masolat.reverse()
print(", ".join(masolat))
print(", ".join(masolat[::-1]))

tabla=[]
for i in range(20):
    sor=[]
    for k in range(10):
        sor.append((i+1)*(k+1))
    tabla.append(sor)
#print(tabla[0])
oszlop=[]
for e in tabla:
    #print(e)
    oszlop.append(e[0])
print(oszlop)


print(oszlopBe(5))
print(oszlopBe(10))
        
