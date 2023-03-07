#Gyakorlás 2023.03.07

gyumolcsok=["alma","banán","körte","barac","szőlő"]
print(f"Ennyi gyümölcs van: {len(gyumolcsok)}")
print(gyumolcsok[3])
#gyumolcsok[3]+="k"
#gyumolcsok[3]="barack"

print(gyumolcsok.index("barac"))
#gyumolcsok[gyumolcsok.index("barac")]+="k"
index=gyumolcsok.index("barac")
gyumolcsok[index]+="k"

print(gyumolcsok[3])

print("5 betűnél kisebb gyümölcs")
for i in range (len(gyumolcsok)):
    if len(gyumolcsok[i])<5:
        print(gyumolcsok[i])
