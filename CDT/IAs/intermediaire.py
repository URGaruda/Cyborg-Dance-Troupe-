from CDT.Simulation.robot import Robot
from CDT.Simulation.arene import Arene
import math
import CDT.Weiter.constantes as constantes 
import time 

"""Intermediaire entre les ia et le robot """
class Intermediaire :

    def __init__(self,robot,obstacles):
        self.robot=robot
        self.tmp=0.0
        self.distanceP=0.0
        self.angleP=0
        self.obstacles=obstacles
        self.tmpD=0.0
        self.tmpA=0.0


    def start_time_dist(self):
        self.tmpD=time.time()
    def start_time_angle(self):
        self.tmpA=time.time()
    def get_distance(self):
        tmp_act=time.time()
        delta_time=tmp_act-self.tmpD
        vitesse_moyenne = (self.robot.vitesse_roue_gauche + self.robot.vitesse_roue_droite) / 2 
        vitesse_moyenne = vitesse_moyenne / (2 * math.pi * self.robot.rayon_roue)
        self.distanceP+=vitesse_moyenne *delta_time
        self.tmpD=time.time()
        print("Distance : %d",self.distanceP)
        return self.distanceP

    def get_angle(self):
        tmp_act=time.time()
        delta_time=tmp_act-self.tmpA
        vitesse_angulaire = (self.robot.vitesse_roue_droite - self.robot.vitesse_roue_gauche) / (2 * math.pi * self.robot.distance_roues)
        self.angleP+= vitesse_angulaire * delta_time
        self.tmpA=time.time()
        print("Angle: %d",self.angleP)
        return self.angleP
    
    def tourner_gauche(self,vitesse):
        self.robot.set_vitesse(-vitesse,vitesse)
    def tourner_droite(self,vitesse):
        self.robot.set_vitesse(vitesse,-vitesse)
    def avancer(self,vitesseG,vitesseD):
        """Ajuste les vitesses afin que le robot puisse avancer """
        self.robot.set_vitesse(vitesseG,vitesseD)


    