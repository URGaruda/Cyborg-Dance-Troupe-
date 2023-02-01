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
        return math.sqrt((self.x**2) + (self.y**2))

    def p_scalaire(self,vecteur):
        return self.x*vecteur.x+self.y*vecteur.y
    

    #Creation d'une methode copie
    def copie(self,vecteur):
        new_vecteur= copy.copy(vecteur)
        return new_vecteur


    def mult_par_un_scalaire(self,k):
        vecteur=Vecteur(self.x,self.y)
        vecteur.x=k*(vecteur.x)
        vecteur.y=k*(vecteur.y)
        return vecteur
    
        
    def rotation_anti_horaire (self,angle):
        """ Rotation anti-horaire d'angle "angle" en radians """
        x= self.x * math.cos(angle) - self.y * math.sin(angle)
        y= self.x * math.sin(angle) + self.y * math.cos(angle)
        self.x=x
        self.y=y
    def rotation_horaire (self,angle):
        """ Rotation horaire d'angle "angle" en radians """
        x= self.x * math.cos(angle) + self.y * math.sin(angle)
        y= - self.x * math.sin(angle) + self.y * math.cos(angle)
        self.x=x
        self.y=y
    
    def angle_rotation(self,vecteur): # angle est dans l'intervalle 0 PI 
        val=self.p_scalaire(vecteur)/(vecteur.norme()*self.norme())
        return math.acos(val)
"""v1 = Vecteur(1, 2)
v2 = Vecteur(3, 4)
v3 = Vecteur(8,14)
v1.addition(x=1, y=1)
v1.addition(vecteur=v2)
v1.soustraction(x=1,y=1)
v1.soustraction(vecteur=v2)
v1.copie(v2)
print(v1.angle_rotation(v2))
print(v3.angle_rotation(v1))
print(v2.angle_rotation(v3))
v4=Vecteur(3,2)
v4.rotation(math.pi/2)
print(v4.x,",",v4.y)
v4.rotation(math.pi/2)
print(v4.x,",",v4.y)
print((v4.mult_par_un_scalaire(v4,5)).y)"""