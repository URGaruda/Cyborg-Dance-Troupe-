from robot import Robot 
import math
from arene import Arene 
import time 
import variables
class Ia_Tourner:
    """Fait tourner le robot à gauche de angle """
    def __init__(self,angle):
        self.angle=angle
    def start(self):
        self.a_tourner=0.0
        variables.inter.tourner_gauche()
    def step(self):
        self.a_tourner+=variables.inter.get_angle()
    def stop(self):
        return self.a_tourner>self.angle
