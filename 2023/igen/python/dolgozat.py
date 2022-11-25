#1,2
lista=[]
for i in range(1,9):
    lista.append(int(input("Kérek egy számot: ")))
print(lista)

#5,6,7
txt="Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."
vegjel=""
while vegjel!="end":
    vegjel=input("Kérek egy betűt: ")
    x=txt.count(vegjel)
    print("Ez a szó ennyiszer van meg " + str(x))
    if vegjel=="end":
        print("Vége")
lista2=[]
lista2.append(txt)
lista2.reverse()
print(lista2)



