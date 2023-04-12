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
        self.distanceP=0.0
        self.angleP=0.0 

    
    def get_distance(self):
        # distance = nombre de tour * circonférence 
        left_position, right_position = self.robot.get_motor_position()
        left_distance = (left_position / 360.0) * self.robot.WHEEL_CIRCUMFERENCE # en mm 
        right_distance = (right_position / 360.0) * self.robot.WHEEL_CIRCUMFERENCE # en mm 
        distance_traveled = (left_distance + right_distance) / 2.0 # distance moyenne 
        self.distanceP += distance_traveled / 1000.0 # conversion en mètre 
        #print("Distance : ",self.distanceP)
        return self.distanceP 

    def get_angle(self):
        position_gauche, position_droite = self.robot.get_motor_position()
        angle = math.radians((position_gauche + position_droite) / 2)
        self.angleP+= angle
        #print("Angle: ",self.angleP)
        return self.angleP 
    
    def tourner_gauche(self,vitesse):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,-vitesse)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,vitesse)
    def tourner_droite(self,vitesse):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,vitesse)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,-vitesse)
    def avancer(self,vitesseG,vitesseD):
        """Ajuste les vitesses afin que le robot puisse avancer """
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,vitesseG)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,vitesseD)

    def start_time_dist(self):
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT,self.robot.read_encoders()[0])
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT,self.robot.read_encoders()[1])
    def start_time_angle(self):
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT,self.robot.read_encoders()[0])
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT,self.robot.read_encoders()[1])
        
    
    

