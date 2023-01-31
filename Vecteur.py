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

    def p_scalaire(self,vecteur):
        return self.x*vecteur.x+self.y*vecteur.y
    

    #Creation d'une methode copie
    def copie(self,vecteur):
        new_vecteur= copy.copy(vecteur)
        return new_vecteur


    def mult_par_un_scalaire(self,vecteur, k):
        vecteur.x=k*(vecteur.x)
        vecteur.y=k*(vecteur.y)
        return vecteur
    
        
    def rotation (self,angle):
        angle= math.radians(angle)
        x= self.x * math.cos(angle) - self.y * math.sin(angle)
        y= self.x * math.sin(angle) + self.y * math.cos(angle)
        self.x=x
        self.y=y

"""v1 = Vecteur(1, 2)
v2 = Vecteur(3, 4)
v1.addition(x=1, y=1) 
print(v1.x,",",v1.y)
v1.addition(vecteur=v2)
print(v1.x,",",v1.y)
v1.soustraction(x=1,y=1)
print(v1.x,",",v1.y)
v1.soustraction(vecteur=v2)
print(v1.x,",",v1.y)
v3=v1.copie(v2)
print(v3.x,",",v3.y)
v1=v1.mult_par_un_scalaire(v1,5)  
print(" ")
print(v1.x,",",v1.y)"""
v4=Vecteur(3.0,2.0)
v4.rotation(math.pi/2)
#print(math.radians(math.pi/2))
print(v4.x,",",v4.y)
v4.rotation((math.pi/2))
print(v4.x,",",v4.y)
"""v4.rotation(math.pi/2)
print(v4.x,",",v4.y)"""