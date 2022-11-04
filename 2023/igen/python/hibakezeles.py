

lista=["bence","lászló","ferenc"]
lista.append("Oszkár")
try:   
    print(lista[3])
except:
    print("Valami nem jó")
else:
    print("Sikeres lefutás")
finally:
    print("ez a vége")
szam=""
while szam=="":
    try:    
        szam=int(input("kérek egy számot: "))
    except ValueError:
        print("Ez nem szám")
    except:
        print("Ismeretlen hiba")

print(szam)
