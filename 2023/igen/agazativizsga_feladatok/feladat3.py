def ido2mp():
    pass


eredmenyek=[]
#1.feladat
f=open("triatlon.txt","r")
for egySor in f:
    temp=egySor.replace("\n","").split(";")
    eredmenyek.append(temp)
f.close()

eredmenyek.pop(0)
#print(eredmenyek)


#2.feladat

print("2.Feladat: A versenyen {} induló volt.".format(len(eredmenyek)))

#3.feladat


