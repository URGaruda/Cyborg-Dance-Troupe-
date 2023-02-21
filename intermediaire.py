from robot import Robot
from arene import Arene
import math
import constantes

"""Intermediaire entre les ia et le robot """
class Intermediaire :

    def __init__(self,robot):
        self.robot=robot
    def get_distance(self):
        vitesse_moyenne = (self.robot.vitesse_roue_gauche + self.robot.vitesse_roue_droite) / 2 
        vitesse_moyenne = vitesse_moyenne / (2 * math.pi * self.robot.rayon_roue)
        return vitesse_moyenne * Arene.dt 

    def get_angle(self):
        vitesse_angulaire = (self.robot.vitesse_roue_droite - self.robot.vitesse_roue_gauche) / (2 * math.pi * self.robot.distance_roues) #la vitesse de rotation du robot autour de son axe central
        delta_orientation = vitesse_angulaire * Arene.dt #calcule le changement d'orientation
        return delta_orientation 

    



