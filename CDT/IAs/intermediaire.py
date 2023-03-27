from CDT.Simulation.robot import Robot
from CDT.Simulation.arene import Arene
import math
import CDT.Weiter.constantes as constantes 
import time 

"""Intermediaire entre les ia et le robot """
class Intermediaire :

    def __init__(self,robot):
        self.robot=robot
        self.tmp=0.0
        self.distanceP=0.0
        self.angleP=0
    def get_distance(self):
        return self.robot.distanceP

    def get_angle(self):
        return self.robot.angleP

    def tourner_gauche(self,vitesse):
        self.robot.set_vitesse(-vitesse,vitesse)
    def tourner_droite(self,vitesse):
        self.robot.set_vitesse(vitesse,-vitesse)
    def avancer(self,vitesseG,vitesseD):
        """Ajuste les vitesses afin que le robot puisse avancer """
        self.robot.set_vitesse(vitesseG,vitesseD)

    def start_time(self):
        self.tmp=time.time()

    def deplacement(self, delta_time):
        """
        Met à jour la position et l'orientation du robot en fonction des vitesses de ses roues.
        """
        #print(self.x," ",self.y)
        tmp_act=time.time()
        dt=tmp_act-self.tmp
        vitesse_moyenne = (self.robot.vitesse_roue_gauche + self.robot.vitesse_roue_droite) / 2 
        vitesse_moyenne = vitesse_moyenne / (2 * math.pi * self.robot.rayon_roue) #vitesse lineaire moyenne
        self.distanceP=vitesse_moyenne*dt
        delta_x = vitesse_moyenne * math.cos(self.robot.orientation) * dt 
        delta_y = vitesse_moyenne * math.sin(self.robot.orientation) * dt
        self.x += delta_x
        self.y += delta_y


        vitesse_angulaire = (self.robot.vitesse_roue_droite - self.robot.vitesse_roue_gauche) / (2 * math.pi * self.robot.distance_roues) #la vitesse de rotation du robot autour de son axe central
        delta_orientation = vitesse_angulaire * dt #calcule le changement d'orientation
        self.angleP=delta_orientation
        self.robot.orientation += delta_orientation #calcule la nouvelle orientation
        self.tmp=time.time()