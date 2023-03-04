from Robot_Arene_Obstacle.intermediaire import Intermediaire
import math

class IA:
    def __init__(self,dexter,distance,vitesse):
        self.distance=distance
        self.parcouru=0.0
        self.inter=dexter
        self.vitesse=vitesse
    def start(self):
        self.parcouru=0.0
        self.inter.avancer(self.vitesse)
    def step(self):
        self.parcouru+=self.inter.get_distance()
    def stop(self):
        return self.parcouru>=self.distance 
