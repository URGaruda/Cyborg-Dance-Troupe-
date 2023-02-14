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
    def ajout_obstacle(self,o):
        """ Prends un obstacle o et l'ajoute dans l'arène """
        self.obstacles.append(o)
        print("Obstacle ajouté")
    def arene_update(self):
        self.robot.deplacement()
    def stop(self):
        self.robot.check_collision()
    


         

        