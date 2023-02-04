import math
import copy
from Vecteur import Vecteur 
class Robot :
    VMAX= 25 # vitesse maximale du robot en cm/s 
    def  __init__(self , x , y, R , theta , dirX,dirY ):
        if v<0 or v>Robot.VMAX:
            raise ValueError("La vitesse doit etre entre 0 et {} ".format(Robot.VMAX))
        if theta < 0 or theta > 360:
            raise ValueError("L'angle doit être entre 0 et 360 degrés")
        self.x = x  #coordonnée x du robot
        self.y = y  #coordonnée y du robot 
        self.vmoy = 0.0  #vitesse moyenne du robot en cm/s
        self.R = R  #Rayon du robot 
        self.theta = theta #angle de vue du robot 
        self.l=11.5 # longueur entre les deux roues en cm/s  
        self.v1=0.0 #vitesse de la roue gauche 
        self.v2=0.0 #vitesse de la roue droite 
        new_dir=Vecteur(dirX-x,dirY-y)
        norme_dir=new_dir.norme()
        self.dir=Vecteur((new_dir.x/norme_dir),(new_dir.y/norme_dir)) #direction du robot 

    def copie(self):
        """Fait une copie du robot """
        robot=copy.copy(self)
        return robot

    def stop(self):
        """ Met la vitesse du robot à 0 pour l'arrêter """
        self.v=0.0

    def acceleration(self,val):
        """ Augmente la vitesse v du robot d'une valeur val """
        self.v+=val

    def freinage(self,val):
        """ Reduit la vitesse v du robot d'une valeur val """
        self.v-=val


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


