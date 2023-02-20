from robot import Robot 
import math
from arene import Arene 
import time 
import ia
import ia_tourner 

class IA_Seq:
    def __init__(self,robot,arene,liste_ia):
        self.robot=robot
        self.arene=arene
        self.liste=liste_ia
        
    def start(self):
        self.cur=0

    def step(self):
        self.liste[self.cur].step()

    def stop(self):
        return self.cur>=len(self.liste)
    
    def update(self):
        """ fait la maj de l'ia actuelle de la liste  """
        if self.liste[self.cur].stop() :
            self.cur+=1
            self.liste[self.cur].start()
        