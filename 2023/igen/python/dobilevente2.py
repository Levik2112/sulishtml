
#1
szamlista=[]
for i in range(8):
    szamlista.append(int(input("Kérek egy számot: ")))
#2
print(szamlista)
#3
for i in range(len(szamlista)):
    print(szamlista[i],end=" ")
    if i%4==3:
       print()
#4
osszeg=sum(szamlista)
print("A számok összege:",osszeg)
#5
szoveg="Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."

#6,7
vegjel=""
while vegjel!="end":
    vegjel=input("Kérek egy betűt: ")
    szoveg2=szoveg.count(vegjel)
    print(szoveg2)
    
#formázás   
print()

#8
print(szoveg[::-1])

#formázás
print()

#9
print("A szöveg eddigi mérete:",len(szoveg))

#formázás
print()

szoveg=szoveg.replace("orna","")
print(szoveg)

#formázás
print()

print("A szöveg új mérete:",len(szoveg))

#10

def beker():
    karakter="asd"
    while len(karakter)!=1:
        karakter=(input("Kérek egy 3 jegyű karaktert: "))
        
beker()


listaszam=[[6,2],[5,4],[6,2],[4,6],[0,14],[2,10],[2,10],[3,6]]
for i in listaszam():
    print(i)
