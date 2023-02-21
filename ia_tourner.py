from robot import Robot 
import math
from arene import Arene 
import time 
import constantes
class Ia_Tourner:
    """Fait tourner le robot de 90° soit à gauche si cote=0 ou à droite si cote=1 """
    def __init__(self,cote):
        self.cote=cote
        self.valide=False
    def start(self):
        self.a_tourner=0.0
        
    def step(self):
        pass
    def stop(self):
        if(self.valide):
            return True
        return False 
