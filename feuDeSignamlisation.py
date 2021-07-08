#-*-coding:Utf-8 -*

# 1) Définir une classe Feu_De_Signalisation pour décrire son fonctionnement.
class Feu_De_Signalisation :
    def __init__(self):
        self.index = 0
        self.couleur =["Vert", "Orange", "Rouge", "Orange clignotant"]


# 2) Le constructeur de la classe ( méthode __init__() ) initialise son état à "vert" par le biais d'un un index pour suivre cet enregistrement.
# 	Cet index sera initialisé à 0, utiliser une liste ["Vert", "Orange", "Rouge", "Orange Clignotant"]
    def afficher_état(self):
        return print(self.couleur[self.index])

    def Successeur(self):
        self.index +=1
        if self.index>2 :
            self.index=0

feu = Feu_De_Signalisation()

for i in range (60):
    feu.afficher_état()
    feu.Successeur()

# 3) La méthode successeur doit faire passer le feu d'une couleur à une autre en incrémentant l'index d'enregistrement modulo 3
# La méthode afficher_etat doit afficher l'état du feu de signalisation