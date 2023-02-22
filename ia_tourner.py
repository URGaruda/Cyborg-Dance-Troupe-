from robot import Robot
import math
from arene import Arene
import time
from intermediaire import Intermediaire
class Ia_Tourner:
    """Fait tourner le robot à gauche de angle """
    def __init__(self,dexter,angle):
        self.inter=Intermediaire(dexter)
        self.angle=math.radians(angle)
    def start(self):
        self.a_tourner=0.0
        self.inter.tourner_gauche()
    def step(self):
        self.a_tourner+=self.inter.get_angle()
    def stop(self):
        if(self.a_tourner>self.angle):
            self.inter.avancer()
        return self.a_tourner>self.angle
