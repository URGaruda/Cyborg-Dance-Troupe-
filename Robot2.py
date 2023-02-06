import math
import copy
from Vecteur import Vecteur 
class Robot :
    VMAX= 25 # vitesse maximale du robot en cm/s 
    def  __init__(self , x , y, R,theta ,direction , wheel_radius, wheel_base ):
        if theta < 0 or theta > 360:
            raise ValueError("L'angle doit être entre 0 et 360 degrés")
        self.x = x  #coordonnée x du robot
        self.y = y  #coordonnée y du robot  
        self.R = R  #Rayon du robot 
        self.theta = theta #angle de vue du robot  
        self.wheel_radius = wheel_radius  #rayon des roues 
        self.wheel_base = wheel_base # longueur entre les deux roues en cm 
        self.left_wheel_speed = 0 #vitesse de la roue gauche en cm/s
        self.right_wheel_speed = 0 #vitesse de la roue droite en cm/s
        self.direction = direction #direction du robot en radians 

    def copie(self):
        """Fait une copie du robot """
        robot=copy.copy(self)
        return robot

    def set_speeds(self, left_wheel_speed, right_wheel_speed):
        self.left_wheel_speed = left_wheel_speed
        self.right_wheel_speed = right_wheel_speed
    
    
    


"""
#tester la classe        
try:
    robot=Robot(1,1,20,10,50,5,3) 
    print(robot.dir.x,",",robot.dir.y)  
    robot.stop()
    print(robot.v)
    robot.acceleration(30)
    print(robot.v)
    robot.freinage(15)
    print(robot.v)
    robot2=robot.copie()
    print("c'est la copie")
    print(robot2.v)
    print(robot.dir.x,",",robot.dir.y) 
    
except ValueError as erreur :
    print(erreur) 
    robot.stop()
    print(robot.v)
    robot.acceleration(30)
    print(robot.v)
"""


