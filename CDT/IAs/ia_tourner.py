import math
import time
class Ia_Tourner:
    """Fait tourner le robot à gauche de angle """
    def __init__(self,dexter,angle,vitesse):
        self.inter=dexter
        self.angle=math.radians(angle)
<<<<<<< HEAD
        self.vitesse=vitesse
=======
        self.vitesse=vitesse/7
>>>>>>> Dev
        self.limite=False
    def start(self):
        print("ok")
        self.a_tourner=0.0
<<<<<<< HEAD
        self.inter.tourner_gauche(self.vitesse/7)
    def step(self):
        print("angle :",self.a_tourner)
        self.a_tourner+=self.inter.get_angle()
        """
        if((self.a_tourner/self.angle)*100>=95.0) and self.limite==False :
            self.inter.tourner_gauche(self.vitesse/3)
            self.limite=True
        """
    def stop(self):
        return self.a_tourner>=self.angle
=======
        self.inter.tourner_gauche(self.vitesse)
    def step(self):
        #print("angle :",self.a_tourner)
        self.a_tourner+=self.inter.get_angle()
        if((self.a_tourner/self.angle)*100>=92.0) and self.limite==False : # à utiliser que si l'affichage est utilisé dans le main 
            self.inter.tourner_gauche(self.vitesse/75)
            self.limite=True
        
    def stop(self):
        return self.a_tourner>self.angle
>>>>>>> Dev
