from robot import Robot 
import math
from arene import Arene
class IA:
    def __init__(self,robot,distance,arene):
        self.robot=robot
        self.distance=distance
        self.arene=arene
        self.parcouru=0.0

    def start(self):
        self.parcouru=0.0
    
    def step(self):
        print("voici le resultat",math.sqrt((self.robot.x-self.robot.historique[-1][0])**2+(self.robot.y-self.robot.historique[-1][1])**2 ))
        self.parcouru+=math.sqrt((self.robot.x-self.robot.historique[-1][0])**2+(self.robot.y-self.robot.historique[-1][1])**2 )
    def stop(self):
        if(self.parcouru>self.distance):
            print("Distance Parcouru")
        elif(self.arene.check_collision()):
            print("Il y a une collision ")
        else:
            print()
        return self.parcouru>self.distance or self.arene.check_collision()
