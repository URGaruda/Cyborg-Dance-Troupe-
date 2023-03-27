import math
import time
class Ia_Tourner:
    """Fait tourner le robot à gauche de angle """
    def __init__(self,dexter,angle,vitesse):
        self.inter=dexter
        self.angle=math.radians(angle)
        self.vitesse=vitesse
        self.limite=False
    def start(self):
        print("ok")
        self.a_tourner=0.0
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