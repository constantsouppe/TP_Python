#-*-coding:Utf-8 -*

#1) Créer une fonction qui creer_tableau2d(nb_lignes, nb_colonnes) et renvoi un tableau 2D (liste 2D)
print("\n Exemple d'utilisation de fonction pour 1) créer un tebleau 2d, 2) Initialiser un tableau 2d, 3) L'afficher")

nb_colonnes = 50
nb_lignes = 10

def creer_tableau2d(nb_lignes, nb_colonnes):
    tableau =[]
    ligne=[0]*nb_colonnes
    for i in range (nb_lignes):
        tableau.append(ligne)
    return tableau

def initialise_tableau2d(size_x, size_y, tableau):
    for x in range(size_x):
        for y in range(size_y):
            tableau[x][y]='*'

def affiche_tableau2d(size_x, size_y, tableau):
    for x in range(size_x):
        for y in range ( size_y):
            print(tableau[x][y], end='')#l'option end =''permet d'éviter les retours à la ligne après chaque print
        print("\r")
tableau = creer_tableau2d(nb_lignes, nb_colonnes)
print(tableau)
initialise_tableau2d(nb_lignes, nb_colonnes, tableau)
print (tableau)
affiche_tableau2d(nb_lignes, nb_colonnes, tableau)

#2) Créer une fonction initialise_tableau2d(nb_lignes, nb_colonnes, tableau) qui initialise le contenu à '*' pour chacun des éléments

#3) Créer une fonction affiche_tableau2d(nb_lignes, nb_colonnes, tableau) qui affiche le tableau à l'écran