#1feladat
tancok=[]
f=open("tancrend.txt","r")
for egySor in f:
    tancok.append(egySor.replace("\n",""))
    
f.close()
#2feladat
#ancok.split(" ")
print(tancok)
print("Az első tánc {} volt,a második a {}".format(tancok[0][0],tancok[-3]))

#3feladat
print("A samba-t ennyi pár mutatta be {}".format(tancok.count("samba")))


        
