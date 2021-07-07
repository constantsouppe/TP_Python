#-*-coding:Utf-8 -*

#1. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est positif (>= 0) ou non, et affiche
#“positif” ou “négatif”.
#i_entier = int(input("veuillez saisir un nombre entier:\n"))
#if i_entier >= 0:
 #   print("ce nombre est postif")
#else :
 #   print("ce nombre est négatif")
#print(i_entier)

#2. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est strictement positif, nul ou strictement
#négatif, et affiche ce résultat.
# a=int(input("veuillez saisir un nombre entier"))
# if a>0 :
#     print("ce nombre est positif")
# elif a==0 :
#     print("ce nombre est nul")
# else :
#     print("ce nombre est négatif")


#3. Écrire un algorithme qui demande un réel à l’utilisateur et affiche sa valeur absolue (sans utiliser de fonction
#prédéfinie évidemment).
# b=float(input("veuillez saisir un nombre réel:\n"))
# if b>=0:
#     print (b)
# else :
#     print (-b)

#4. Écrire un algorithme qui demande un réel à l’utilisateur et l’arrondit à l’entier le plus proche (les x,5 seront arrondis
#à l’entier supérieur).
# c=float(input("veuillez entrer un nombre réel:\n"))
#
# if c>=0:
#     if int(c+0.5)>c :
#         print(int(c+1))
#     else :
#         print (int(c))
# if c<0:
#     if int(c-0.5)<c:
#         print(int(c-1))
#     else :
#         print (int(c))
#5. Écrire un algorithme qui demande le numéro d’un mois et affiche le nombre jours que comporte ce mois (sans tenir
#compte des années bissextiles).
# m=int(input("entrez le numéro d'un mois:\n"))
# l1=[1, 3, 5,7,8,10,12]
# l2=[4, 6, 9, 11]
# if m in l1 :
#     print("ce mois comporte 31 jours")
# elif m in l2 :
#     print("ce mois comporte 30 jours")
# elif m==2 :
#     print("ce mois comprte 28 jours")
# else :
#     print("va te faire foutre, cordialement la direction")

#6. Écrire un algorithme qui vérifie si une année est bissextile. On rappelle qu’il y a des années bissextiles tous les
#4 ans, mais la première année d’un siècle ne l’est pas (1800, 1900 n’étaient pas bissextiles) sauf tous les 400 ans
#"(2000 était une année bissextile).

# y=int(input("entrez le numéro d'une année"))
# if y%4 == 0 and y%100 != 0 :
#     print("cette année est bissextile")
# elif y%400 == 0 :
#     print("cette année est bissextile")
# else :
#     print("cette année n'est pas bissextile")

#7. Écrire un algorithme qui demande une date sous la forme de 2 nombres entiers (numéro du jour et numéro du mois)
#et affiche la saison (ex : 12/02; hiver). On supposera que le premier jour de la saison est toujours le 21.

j=int(input("entrez un numéro de jour: \n"))
m=int(input("entrez un numéro de mois : \n"))
if m==1 or m==2 or m==12 and j>=21 or m==3 and j<21 :
    print("on est en hiver")
elif m==4 or m==5 or m==3 and j>=21 or m==6 and j<21 :
    print("on est au printemps")
elif m==7 or m==8 or m==6 and j>=21 or m==9 and j<21 :
    print("on est en été")
elif m==10 or m==11 or m==9 and j>=21 or m==12 and j<21:
    print("on est en automne")
elif m>12 or j>31 :
    print("va te faire foutre cordialement la direction")