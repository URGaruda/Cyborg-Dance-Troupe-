from CDT.Robot_Arene_Obstacle.robot import Robot
from CDT.Robot_Arene_Obstacle.arene import Arene
import math
import CDT.Autres.constantes as constantes
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
        #self.robot.set_vitesse(-vitesse,vitesse)
        v_ang = (vitesse - (-vitesse)) / (2 * math.pi * constantes.Distance_Roues)
        self.robot.set_motor_dps(self._gpg.MOTOR_LEFT+self._gpg.MOTOR_RIGHT,v_ang*57.2958)
    def tourner_droite(self,vitesse):
        #self.robot.set_vitesse(vitesse,-vitesse)
        v_ang = (-vitesse - vitesse) / (2 * math.pi * constantes.Distance_Roues)
        self.robot.set_motor_dps(self._gpg.MOTOR_LEFT+self._gpg.MOTOR_RIGHT,v_ang*57.2958)
    def avancer(self,vitesseG,vitesseD):
        """Ajuste les vitesses afin que le robot puisse avancer """
        v_ang = (vitesseD - vitesseG) / (2 * math.pi * constantes.Distance_Roues)
        self.robot.set_motor_dps(self._gpg.MOTOR_LEFT+self._gpg.MOTOR_RIGHT,v_ang*57.2958)

    def start_time(self):
        self.tmp=time.time()
        
    def get_distance_traveled(self):
        """ Calcule la distance en mètre qu'à parcouru le robot à chaque appel de get_motor_position """
        left_position, right_position = self.robot.get_motor_position()
        left_distance = (left_position / 360.0) * self.robot.WHEEL_CIRCUMFERENCE
        right_distance = (right_position / 360.0) * self.robot.WHEEL_CIRCUMFERENCE
        distance_traveled = (left_distance + right_distance) / 2.0 
        self.distanceP = distance_traveled / 1000.0 

    def update(self):
        """
        Met à jour la position et l'orientation du robot en fonction des vitesses de ses roues.
        """
        tmp_act=time.time()
        dt=tmp_act-self.tmp # calcul du delta temps entre 2 updates
        mt_pos=self.get_motor_position() # récupère le couple du  degre de rotation des moteurs
        angleP=math.radians((mt_pos[0]+mt_pos[1])/2) # calcule l'angle moyen parcouru par le robot 
        
        self.angleP=angleP
        self.tmp=time.time()


