from CDT.Simulation.robot import Robot
from CDT.Simulation.arene import Arene
import math
import CDT.Weiter.constantes as constantes
import time 

# 1 rad/s = 57.2958	deg/s 
class Inter_Robot:
    """Intermediaire entre le robot et les ia """
    def __init__(self,robot):
        self.robot=robot
        self.tmp=0.0
        self.distanceP=0.0
        self.angleP=0 

    
    def get_distance(self):
        return self.distanceP 

    def get_angle(self):
        return self.angleP 
    
    def tourner_gauche(self,vitesse):
        v_ang = (vitesse - (-vitesse)) / (2 * math.pi * constantes.Distance_Roues)
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,v_ang*57.2958)
    def tourner_droite(self,vitesse):
        v_ang = (-vitesse - vitesse) / (2 * math.pi * constantes.Distance_Roues)
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,v_ang*57.2958)
    def avancer(self,vitesseG,vitesseD):
        """Ajuste les vitesses afin que le robot puisse avancer """
        v_ang = (vitesseD - vitesseG) / (2 * math.pi * constantes.Distance_Roues)
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,v_ang*57.2958)

    def start_time(self):
        self.tmp=time.time()
        
    def get_distance_traveled(self):
        """ Calcule la distance en mètre qu'à parcouru le robot à chaque appel de get_motor_position """
        left_position, right_position = self.robot.get_motor_position()
        left_distance = (left_position / 360.0) * self.robot.WHEEL_CIRCUMFERENCE
        right_distance = (right_position / 360.0) * self.robot.WHEEL_CIRCUMFERENCE
        distance_traveled = (left_distance + right_distance) / 2.0 
        self.distanceP = distance_traveled / 1000.0 

    def get_angle(self):
        """Retourne l'angle en radians qu'a pris le robot"""
        position_gauche, position_droite = self.get_motor_position()
        angle = math.radians((position_gauche + position_droite) / 2)
        self.angleP= angle
    
    def update(self):
        """
        Met à jour la position et l'orientation du robot en fonction des vitesses de ses roues.
        """
        self.get_angle()
        self.get_distance_traveled()