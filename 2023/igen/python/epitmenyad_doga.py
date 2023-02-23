utcak=[]

f=open("utca.txt","r")
for egySor in f:
    utcak.append(egySor.replace("\n",""))
    
f.close()
print(utcak)
