from robot import Robot 
import math
from arene import Arene 
import time 

class Ia_Tourner:
    """Fait tourner le robot de 90° soit à gauche si cote=0 ou à droite si cote=1 """
    def __init__(self,robot,cote,arene):
        self.robot=robot
        self.cote=cote
        self.arene=arene
        self.valide=False
    def start(self):
        if(self.cote==0):
            self.robot.set_vitesse(self.robot.vitesse_roue_gauche ,-(self.robot.vitesse_roue_droite))
        else:
            self.robot.set_vitesse(-(self.robot.vitesse_roue_gauche) ,self.robot.vitesse_roue_droite)
        
    def step(self):
        time.sleep(self.arene.dt)
        self.valide=True 
    def stop(self):
        if(self.valide):
            return True
        return False 
