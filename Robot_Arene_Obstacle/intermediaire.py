from Robot_Arene_Obstacle.robot import Robot
from Robot_Arene_Obstacle.arene import Arene
import math
import Autres.constantes as constantes

"""Intermediaire entre les ia et le robot """
class Intermediaire :

    def __init__(self,robot):
        self.robot=robot
        self.x=constantes.x
        self.y=constantes.y
        self.distanceP=0.0
        self.angleP=0
    def get_distance(self):
        return self.distanceP

    def get_angle(self):
        return self.angleP
    
    def tourner_gauche(self,vitesse):
        self.robot.set_vitesse(-vitesse,vitesse)
    def tourner_droite(self,vitesse):
        self.robot.set_vitesse(vitesse,-vitesse)
    def avancer(self,vitesse):
        """Ajuste les vitesses afin que le robot puisse avancer """
        self.robot.set_vitesse(vitesse,vitesse)

    def deplacement(self, delta_time):
        """
        Met à jour la position et l'orientation du robot en fonction des vitesses de ses roues.
        """
        #print(self.x," ",self.y)
        vitesse_moyenne = (self.robot.vitesse_roue_gauche + self.robot.vitesse_roue_droite) / 2 
        vitesse_moyenne = vitesse_moyenne / (2 * math.pi * self.robot.rayon_roue) #vitesse lineaire moyenne
        self.distanceP=vitesse_moyenne*delta_time
        delta_x = vitesse_moyenne * math.cos(self.robot.orientation) * delta_time 
        delta_y = vitesse_moyenne * math.sin(self.robot.orientation) * delta_time 
        self.x += delta_x
        self.y += delta_y
        
        
        vitesse_angulaire = (self.robot.vitesse_roue_droite - self.robot.vitesse_roue_gauche) / (2 * math.pi * self.robot.distance_roues) #la vitesse de rotation du robot autour de son axe central
        delta_orientation = vitesse_angulaire * delta_time #calcule le changement d'orientation
        self.angleP=delta_orientation
        self.robot.orientation += delta_orientation #calcule la nouvelle orientation
    
