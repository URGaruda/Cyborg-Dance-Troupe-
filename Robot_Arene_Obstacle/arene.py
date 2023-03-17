import math 
from .robot import Robot
from .obstacle import Obstacle 
from random import *

class Arene() : 
    arene_longueur=400.0 #longueur de l'arène 
    arene_largeur=400.0 # largeur de l'arène 
    dt=0.1 #pas de temps de l'arène 
    """ La classe Arene a comme variables d'instances : robot un objet de type Robot , obstacles : une liste d'obstacles et dt : une variable qui est censé determiner le pas de temps entre chaque update """
    def __init__(self,inter,obstacles):
        self.inter=inter 
        self.obstacles=obstacles
    def check_collision(self):
        """
        Vérifie s'il y a une collision entre le robot et les bords de l'arène/ obstacle
        avec arene_x la longueur en x et arene_y la longueur en y 
        """
        # Vérifie une collision avec les bords de l'arène
        if self.inter.x - self.inter.robot.rayon_robot < 0 or self.inter.x + self.inter.robot.rayon_robot > self.arene_longueur:
            return True
        if self.inter.y - self.inter.robot.rayon_robot < 0 or self.inter.y + self.inter.robot.rayon_robot > self.arene_largeur:
            return True

        # Vérifie une collision avec les obstacles
        for obstacle in self.obstacles:
            distance = math.sqrt((self.inter.x - obstacle.x)**2 + (self.inter.y - obstacle.y)**2)
            if distance < self.inter.robot.rayon_robot + obstacle.rayon:
                return True

        return False
    
    def ajout_obstacle(self,o):
        """ Prends un obstacle o et l'ajoute dans l'arène """
        self.obstacles.append(o)
        print("Obstacle ajouté")
    def arene_update(self):
        self.inter.deplacement(self.dt)
    
