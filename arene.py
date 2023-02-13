import math 
from robot import Robot
from obstacle import Obstacle 
from random import *

class Arene : 
    arene_longueur=100.0 #longueur de l'arène 
    arene_largeur=100.0 # largeur de l'arène 
    """ La classe Arene a comme variables d'instances : robot un objet de type Robot , obstacles : une liste d'obstacles et dt : une variable qui est censé determiner le pas de temps entre chaque update """
    def __init__(self,robot,obstacles,dt):
        self.robot=robot 
        self.obstacles=obstacles
        self.dt=dt
    def ajout_obstacle(self,n,rayon):
        for i in rang(n):
            x=random.randint(0,self.arene_longueur)
            y=random.randint(0,self.arene_largeur)
            rayon = random.randint(1,10) 
            self.obstacles.append(Obstacle(x,y,rayon))
    def arene_update():
        self.robot.update_position(self.dt)
        return 

        