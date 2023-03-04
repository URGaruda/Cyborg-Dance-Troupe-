from Robot_Arene_Obstacle.robot import Robot
import math
import time
from Robot_Arene_Obstacle.intermediaire import Intermediaire
class Ia_Tourner:
    """Fait tourner le robot à gauche de angle """
    def __init__(self,dexter,angle,vitesse):
        self.inter=Intermediaire(dexter)
        self.angle=math.radians(angle)
        self.vitesse=vitesse
    def start(self):
        self.a_tourner=0.0
        self.inter.tourner_gauche(self.vitesse,self.vitesse)
    def step(self):
        self.a_tourner+=self.inter.get_angle()
    def stop(self):
        return self.a_tourner>=self.angle
