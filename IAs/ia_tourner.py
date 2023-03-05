from Robot_Arene_Obstacle.robot import Robot
import math
import time
from Robot_Arene_Obstacle.intermediaire import Intermediaire
class Ia_Tourner:
    """Fait tourner le robot à gauche de angle """
    def __init__(self,dexter,angle,vitesse):
        self.inter=dexter
        self.angle=math.radians(angle)
        self.vitesse=vitesse
        self.limite=False
    def start(self):
        self.a_tourner=0.0
        self.inter.tourner_gauche(self.vitesse)
    def step(self):
        self.a_tourner+=self.inter.get_angle()
        if((self.a_tourner/self.angle)*100>=75.0) and self.limite==False :
            self.inter.tourner_gauche(self.vitesse/2)
            self.limite=True
    def stop(self):
        return self.a_tourner>=self.angle
