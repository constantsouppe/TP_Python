#-*-coding:Utf-8 -*

class Point:
    "Definition d'un point mathématique"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # (x,y)
        return "(" + str(self.x) + ", "+ str(self.y)")"

class Rectangle:
    "Definition d'une classe de rectangle"

    def __init__(self, hauteur, largeur, coin):
        self.largeur = largeur
        self.hauteur = hauteur
        self.coin = coin

    def perimetre(self):
        return self.largeur * 2 + self.hauteur * 2

    def aire(self):
        return self.largeur * self.hauteur

coin = Point(12, 27)
boite = Rectangle(50, 35, coin)
print ("le périmètre vaut :", boite.perimetre())
print("l'aire vaut:", boite.aire())