import math
import matplotlib.pyplot as plt
from Robot2 import Robot 
import random


class Obstacle : 
    def __init__(self,x,y,rayon):
        self.x=x
        self.y=y
        self.rayon=rayon

class Simulation : 
       
    def __init__(self,obstacles):
        self.robot=Robot(x=0, y=0, orientation=0, rayon_robot=0.3, rayon_roue=0.05, distance_roues=0.2) 
        self.obstacles=obstacles
        self.arene_longueur = 100
        self.arene_largeur = 100
    
    def trace_cote_carre(self,robot, vitesse, dt, taille_carre):
        """
        Trace un coté du carré avec le robot et faire une rotation pour se préparer à tourner.
    
        Paramètres:
            robot (Robot): objet de la classe Robot.
            vitesse (float): valeur de vitesse angulaire appliquée au roues.
            dt (float): pas de temps de la simulation.
            taille_carre (float): taille du côté du carré en mètres.
        
        Retourne:
            list: une liste de tuples représentant la position x, y du robot à chaque instant.
        """
        robot.set_vitesse(vitesse, vitesse)
        duree = taille_carre / ((robot.vitesse_roue_gauche + robot.vitesse_roue_droite) / 2) * robot.rayon_roue * 2 * math.pi
        nombre_pas = int(duree / dt)
        #le robot trace un coté du carré
        for j in range(nombre_pas):
            robot.deplacement(dt)
            if robot.check_collision(self.arene_longueur,self.arene_largeur,self.obstacles):
                robot.set_vitesse(0,0)
                return robot.historique

        
        robot.set_vitesse(vitesse, -vitesse) #pour pouvoir tourner
        angle = math.pi / 2
        vitesse_angulaire = (robot.vitesse_roue_droite - robot.vitesse_roue_gauche) / (2 * math.pi * robot.distance_roues)
        temps_tourner = abs(angle / vitesse_angulaire) #temps nécessaire pour finir le tour
        nombre_pas = int(temps_tourner / dt)
        #rotation du robot autour de son axe central
        for j in range(nombre_pas):
            robot.deplacement(dt)

        return robot.historique
    
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

    def affichage(self):
        fig, ax = plt.subplots()
        l_obstacles=[plt.Circle((obs.x,obs.y),obs.rayon)for obs in obstacles]
        for o in l_obstacles:
            ax.add_patch(o)
        l_robot=[plt.Circle((x, y), 0.3, color='r') for (x,y) in simulation_historique]
        for r in l_robot:
            ax.add_patch(r)
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        plt.show()

robot = Robot(x=50, y=50, orientation=0, rayon_robot=0.3, rayon_roue=0.05, distance_roues=0.2) 
obstacles= [Obstacle(random.uniform(0,100),random.uniform(0,100),random.uniform(0.3,1))for i in range (50) ]
simulation=Simulation(obstacles)

while True:
    simulation_historique = simulation.trace_cote_carre(robot, 10, 0.0001, 10)
    simulation.affichage()

            
    



           
            




