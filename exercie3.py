#-*-coding:Utf-8 -*

#1) Créer une fonction qui creer_tableau2d(nb_lignes, nb_colonnes) et renvoi un tableau 2D (liste 2D)
print("\n Exemple d'utilisation de fonction pour 1) créer un tebleau 2d, 2) Initialiser un tableau 2d, 3) L'afficher")
x = int(input("entrez la vlaeur x:"))
b = int(input("entrez la valeur y:"))
l = int(input("entrez la largeur du rectangle:"))
h = int(input("entrez la hauteur du rectangle:"))
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
            tableau[x][y]=' '

def affiche_tableau2d(size_x, size_y, tableau):
    for x in range(size_x):
        for y in range ( size_y):
            print(tableau[x][y], end='')#l'option end =''permet d'éviter les retours à la ligne après chaque print
        print("\r")

def ligne(x_start, y_start, x_end, y_end):
    for y in range (y_start, y_end + 1):
        for x in range (x_start, x_end + 1):
            tableau[x][y]='*'
def rectangle(x, b, l, h, tableau):
    ligne(x,b,x+l,b)
    ligne(x,b+h,x+l,b+h)
    ligne(x,b,x,b+h)
    ligne(x+l,b,x+l,b+h)

tableau = creer_tableau2d(nb_lignes, nb_colonnes)
#print(tableau)
initialise_tableau2d(nb_lignes, nb_colonnes, tableau)
#print (tableau)
rectangle(x,b,l,h,tableau)
print(tableau)
affiche_tableau2d(nb_lignes, nb_colonnes, tableau)

#2) Créer une fonction initialise_tableau2d(nb_lignes, nb_colonnes, tableau) qui initialise le contenu à '*' pour chacun des éléments

#3) Créer une fonction affiche_tableau2d(nb_lignes, nb_colonnes, tableau) qui affiche le tableau à l'écran

#4.1) Créer une procédure ligne(x_start, y_start, x_end, y_end) qui va dessiner une ligne depuis les coordonnées (x_start, y_start) à (x_end, y_end)
		# nota: penser à vérifier en début de procédure que les conditions
		# x_end > x_start et y_end > y_start sont bien respectées (inverser respectivement x_end(/y_end) avec x_start(/y_start) si nécessaire)
	    # Tester la procédure et vérifier qu'une ligne est bien dessinée
	#4.2) Créer une procédure rectangle(x, y, l, h, tableau) qui utilise la procédure ligne(...) précédemment conçue pour dessiner un rectangle
		# Dessiner la ligne du bas en commençant à la position (x,y) jusqu’à (x+l, y)
		# Dessiner la ligne du haut en commençant à la position (x,y+h) jusqu’à (x+l, y+h)
		# Dessiner la barre verticale de gauche de (x, y) à (x, y+h)
		# Dessiner la barre verticale de droite de (x+l, y) à (x+l, y+h)
	    #  Tester la procédure et vérifier qu'un rectangle est bien dessiné