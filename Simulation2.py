import math
from Vecteur import Vecteur
from Robot2 import Robot 
from Obstacle import Obstacle

class Simulation : 
    Ymax=400 #en cm
    Xmax=355 #en cm 
    def __init__(self,x,y,v,dirX,dirY,temps,obstacle):
        self.dexter=Robot(x,y,v,25/2,60,dirX,dirY) #Je suppose ici que le Robot fait 25 cm de long et qu'il a un angle de vue de 60° . Vous pouvez les mettres en paramètres si vous préféré comme ça 
        self.liste_obstacle=obstacle
        self.pas_temps=temps

    
    
    