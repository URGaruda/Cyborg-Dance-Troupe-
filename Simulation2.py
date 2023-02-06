import math
import time 
from Vecteur import Vecteur
from Robot2 import Robot 
import random

class Obstacle : 
    def __init__(self,x,y,R):
        self.x=x
        self.y=y
        self.R=R

class Simulation : 
    Ymax=400.0 #en cm
    Xmax=355.0 #en cm 
    def __init__(self,x,y,dirX,dirY,temps,obstacle):
        self.dexter=Robot(x,y,25/2,60,dirX,dirY) #Je suppose ici que le Robot fait 25 cm de long et qu'il a un angle de vue de 60° . Vous pouvez les mettres en paramètres si vous préféré comme ça 
        self.liste_obstacle=obstacle
        self.pas_temps=temps
    
    def collision(self,vect):
        """ Determine si le Robot Dexter est où pas en collision avec un des obstacles du terrain """
        for obj in self.liste_obstacle :
            return not(math.sqrt(((obj.x-vect.x)**2)+((obj.y-vect.y)**2)) > obj.R+vect.R) # si y'a colision il renvoie vrai 
    
    def hors_terrain(self,robot):
        """ Prends un robot et vérifie s'il est toujours sur le terrain """
        return (robot.x<0.0 or robot.x >= Simulation.Xmax or robot.y < 0.0 or robot.y >= Simulation.Ymax )
            
    def senseur(self):
        """ Determine s'il y a un obstacle sur la direction du robot et renvoie le nombre de pas s'il l'a trouvé un
        obstacle ou sinon -1 s'il l'a rien trouvé """
        robot=self.dexter.copie() # crée une copie qui va faire des 
        pas=0
        while not(self.hors_terrain(robot)) :
            vect_v=self.dexter.dir.mult_par_un_scalaire((self.dexter.v*self.pas_temps))
            robot.x=vect_v.x
            robot.y=vect_v.y
            pas+=1
            if(self.collision(robot)):
                return pas 
        return -1 
    def update_position(self, time_delta):
        avg_speed = (self.dexter.left_wheel_speed + self.dexter.right_wheel_speed) / 2
        avg_speed = avg_speed / (2 * math.pi * self.dexter.wheel_radius)
        delta_x = avg_speed * math.cos(self.dexter.direction) * time_delta
        delta_y = avg_speed * math.sin(self.dexter.direction) * time_delta
        self.x += delta_x
        self.y += delta_y
        
        # Calculate the rotation using the formula for angular velocity
        angular_speed = (self.dexter.right_wheel_speed - self.dexter.left_wheel_speed) / (2 * math.pi * self.dexter.wheel_base)
        delta_direction = angular_speed * time_delta
        self.dexter.direction += delta_direction
    

for i in [] :
    print("aaah")
#tester la classe
"""        
try:
    sim=Simulation(104.29,145.96,2,56,24,0.10,[])
except ValueError as erreur :
    print(erreur)    
def update():
    sim=Simulation(124.29,196.96,4.2,3,8,0.20,[])
    sim.simulation_carre(10)
update()
"""


           
            




