import math
from Vecteur import Vecteur 
class Robot :
    VMAX= 50 
    def  __init__(self , x , y, v ,  R , theta , dirX,dirY ):
        if v<0 or v>Robot.VMAX:
            raise ValueError("La vitesse doit etre entre 0 et {} ".format(Robot.VMAX))
        if theta < 0 or theta > 360:
            raise ValueError("L'angle doit être entre 0 et 360 degrés")
        self.x = x
        self.y = y
        self.v = v
        self.R = R
        self.theta = theta
        new_dir=Vecteur(dirX-x,dirY-y)
        norme_dir=new_dir.norme()
        self.dir=Vecteur((new_dir.x/norme_dir),(new_dir.y/norme_dir))
        
        
#tester la classe        
try:
    robot=Robot(1,1,20,10,50,5,3) 
    print(robot.dir.x,",",robot.dir.y)  
except ValueError as erreur :
    print(erreur) 

