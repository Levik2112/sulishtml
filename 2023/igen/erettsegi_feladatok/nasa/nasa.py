def darabol(sor):
    lista=sor.split("*")
    temp=lista[-1].split(" ")
    lista.pop(-1)

    lista+=temp
    return lista
def ByteMeret(meret):
    if meret == "-":
        return 0
    else:
        return int(meret)

def Domain(nev):
    return not nev[-1] in "0123456789"
"""
    if nev[-1] in "0123456789":
        return False
    else:
        return True
"""
#print(darabol("rn3.swc.com*20/Jul/1995:12:55:04*GET /images/small.jpg*200 46573"))

naplo=[]
f=open("NASAlog.txt")
for e in f:
    naplo.append(darabol(e.strip()))
f.close()
#print(naplo[:10])

print("5. feladat: Kérések száma: {}".format(len(naplo)))

meretek=[]
for e in naplo:
    meretek.append(ByteMeret(e[4]))

print("6. feladat: Válaszok összes mérete: {} byte".format(sum(meretek)))

domainE=[]
for e in naplo:
    domainE.append(Domain(e[0]))
print("8. Feladat: Domain-es kérések: {:.2%}".format(domainE.count(True)/len(domainE)))

hibakodok=[]
for e in naplo:
    if e[3] not in hibakodok:
        hibakodok.append(e[3])

for e in hibakodok:
    temp=[]
    for o in naplo:
        if o[3]==e:
            temp.append(e)
    print(len(temp))




    
    
