#-*-coding:Utf-8 -*

# 1. Écrire un algorithme qui demande un entier positif, et le rejette tant que le nombre saisi n’est pas conforme.
# a= int(input("donner un entier positif"))
# while a <0 :
#     a = int(input("donner un entier positif"))
# print("c'est bien")
# 2. Écrire un algorithme qui demande 10 entiers, compte le nombre d’entiers positifs saisis, et affiche ce résultat.

# n=0
# for i in range(0,10,1) :
#     a=int(input ("entrez un entier:\n"))
#     if a>0 :
#         n=n+1
# print("il y a",n,"nombre positifs")
# 3. Écrire un algorithme qui demande des entiers positifs à l’utilisateur, les additionne, et qui s’arrête en affichant le
# résultat dès qu’un entier négatif est saisi.
# a=0
# b=0
# while a>=0 :
#     a=int(input("entrez un entier positif"))
#     if a>=0 :
#         b=b+a
# print("la somme de tout ces nombres vaut",b)

# 4. Modifier ce dernier algorithme pour afficher la moyenne de la série d’entiers positifs saisis.
m=0
i=0
a=0
b=0
while a>=0 :
    a=int(input("entrez un entier positif"))
    if a>=0 :
        i=i+1
        b=b+a
m=b/i
print("la somme de tout ces nombres vaut",b)
print("la moyenne de tout ces nombres vaut",m)