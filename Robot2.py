import math
import copy
from Vecteur import Vecteur 
class Robot :
    VMAX= 25 # vitesse maximale du robot en cm/s 
    def  __init__(self , x , y, R , theta , dirX,dirY ):
        if theta < 0 or theta > 360:
            raise ValueError("L'angle doit être entre 0 et 360 degrés")
        self.x = x  #coordonnée x du robot
        self.y = y  #coordonnée y du robot 
        self.vmoy = 0.0  #vitesse moyenne du robot en cm/s qui est calculé à partir des vitesses des 2 roues 
        self.R = R  #Rayon du robot 
        self.theta = theta #angle de vue du robot 
        self.l=11.5 # longueur entre les deux roues en cm  
        self.v1=0.0 #vitesse de la roue gauche en cm/s
        self.v2=0.0 #vitesse de la roue droite en cm/s 
        new_dir=Vecteur(dirX-x,dirY-y)
        norme_dir=new_dir.norme()
        self.dir=Vecteur((new_dir.x/norme_dir),(new_dir.y/norme_dir)) #direction du robot 

    def copie(self):
        """Fait une copie du robot """
        robot=copy.copy(self)
        return robot

    def setVitesse_A(self,v):
        """Initialise les vitesses des 2 roues du robot à la même vitesse """
        if v<0.0 or v>Robot.VMAX:
            raise ValueError("La vitesse doit etre entre 0 et {} ".format(Robot.VMAX))
        self.v1=v
        self.v2=v
    def setVitesse_B(self,v1,v2):
        if v1<0.0 or v2<0.0 or v1>Robot.VMAX or v2>Robot.VMAX:
            raise ValueError("La vitesse doit etre entre 0 et {} ".format(Robot.VMAX))
        self.v1=v1
        self.v2=v2 
    
    
    


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


