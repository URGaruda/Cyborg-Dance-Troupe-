import math
import time 
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
    
    def collision(self,robot):
        """ Determine si le Robot Dexter est où pas en collision avec un des obstacles du terrain """
        for obj in self.liste_obstacle :
            return not(math.sqrt(((obj.x-robot.x)**2)+((obj.y-robot.y)**2)) > obj.R+robot.R) # si y'a colision il renvoie vrai 
    
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

        # Record the current position in history
        self.history.append((self.x, self.y))
    
    def marche_arrierre(self):
        self.dexter.set_speeds(-self.dexter.left_wheel_speed,-self.dexter.right_wheel_speed) #inverse la vitesse des deux roues pour faire une marche arrière 
    def simulation_carre(self,distance,time_delta):#prend une distance à parcourir 
        """ Fait faire un carré au robot dont les cotés sont égaux à la distance"""
        self.dexter.set_speeds(10, 10)
        get_dist=0.0
        state=0
        b=False # Variable qui permet de savoir si on a tourné dans la boucle 
        while not(self.collision(self.dexter) or self.hors_terrain(self.dexter) or state>4):
            if(get_dist>=distance):
                b=True
                self.dexter.set_speeds(-self.dexter.left_wheel_speed,self.dexter.right_wheel_speed)
                time_to_turn = math.pi / 2
                angular_speed = (self.dexter.right_wheel_speed - self.dexter.left_wheel_speed) / (2 * math.pi * self.dexter.wheel_base)
                turn_time = abs(time_to_turn / angular_speed) # Time needed to turn
                num_steps = int(turn_time / time_delta)
                i=0
                while i<num_steps :
                    self.update_position(time_delta)
                    self.dexter.history.append((self.dexter.x,self.dexter.y))
                    i+=1
                state+=1
            if(b):
                self.dexter.set_speeds(-self.dexter.left_wheel_speed,self.dexter.right_wheel_speed)
            self.update_position(time_delta)
            get_dist+=math.sqrt((self.dexter.x-self.dexter.history[len-2][0])**2+(self.dexter.y-self.dexter.history[len-2][1])**2) # ajout de la distance entre l'ancienne position et la nouvelle position 

            
    

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


           
            




