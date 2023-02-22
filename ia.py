from intermediaire import Intermediaire
import math
import variables
class IA:
    def __init__(self,dexter,distance):
        self.distance=distance
        self.parcouru=0.0
        self.inter=Intermediaire(dexter)
    def start(self):
        self.parcouru=0.0
    
    def step(self):
        #self.parcouru+=math.sqrt((self.robot.x-self.robot.historique[-1][0])**2+(self.robot.y-self.robot.historique[-1][1])**2 )
        self.parcouru+=variables.inter.get_distance()
    def stop(self):
        return self.parcouru>self.distance 
