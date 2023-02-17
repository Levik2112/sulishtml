import haromszog

def ujabb(darab=3):
    haromszogek=[]
    for i in range(darab):
        haromszogek.append(haromszog.haromszog())

    for e in haromszogek:
        print("\ta={}, b={}, c={}".format(e[0],e[1],e[2]))
        #3,lista,3számmal l=[[1,2,3],[4,5,6],[7,8,9]]

    return haromszogek



def haromszogE(haromszogek):
    for e in haromszogek:
        if sum(e)-max(e)>max(e):
            print("Lehet háromszög")
        else:
            print("Nem lehet háromszög.")
                            
                            

#print(haromszog.haromszog())
    
h=ujabb(3)
haromszogE(h)

#hf:a mintában bevan sorszámozva,megkell csinánli a sorszámozást
