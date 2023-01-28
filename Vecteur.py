#Ajoute le module copy pour la méthode copie
import copy
import math

class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def addition(self, x=None, y=None, vecteur=None):
        if vecteur:
            self.x += vecteur.x
            self.y += vecteur.y
        else:
            self.x += x
            self.y += y
        return self 
    
    def soustraction(self, x=None, y=None, vecteur=None):
        if vecteur:
            self.x -= vecteur.x
            self.y -= vecteur.y
        else:
            self.x -= x
            self.y -= y
        return self

    def norme(self):
        return math.sqrt(self.x**2 + self.y**2)

    #Creation d'une methode copie
    def copie(self,vecteur):
        new_vecteur= copy.copy(vecteur)
        return new_vecteur


    def mult_par_un_scalaire(self,vecteur, k):
        vecteur.x=k*(vecteur.x)
        vecteur.y=k*(vecteur.y)
        return vecteur
v1 = Vecteur(1, 2)
v2 = Vecteur(3, 4)
v1.addition(x=1, y=1) 
v1.addition(vecteur=v2)
v1.soustraction(x=1,y=1)
v1.soustraction(vecteur=v2)
v1.copie(v2)
    
