beszam=0

while beszam<2 or beszam>5:
    beszam= int(input("Adj meg egy sázmot 2 és 5 között: "))

autok=[]

for i in range(0,beszam):
    autok.append(input("Kérem a(z)"+ str(i+1)+ ". autó márkát: "))

print(autok)
