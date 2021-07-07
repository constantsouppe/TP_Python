#-*-coding:Utf-8 -*

texte="els saucisses et saucissons secs sont dans le saloir"
lettres ={}

for c in texte :
    lettres[c] = lettres.get(c,0) + 1

print (lettres)

lettres_triees = []
for key, value in lettres.items() :
    lettres_triees.append(key,value)

print( lettres_triees)
lettres_triees.sort()
print(lettres_triees)