from robot import Robot 
import math
from arene import Arene 
import time 
import variables
class Ia_Tourner:
    """Fait tourner le robot de 90° soit à gauche si cote=0 ou à droite si cote=1 """
    def __init__(self,angle):
        self.angle=angle
    def start(self):
        self.a_tourner=0.0
    def step(self):
        self.a_tourner+=variables.inter.get_angle()
    def stop(self):
        return self.a_tourner>self.angle
