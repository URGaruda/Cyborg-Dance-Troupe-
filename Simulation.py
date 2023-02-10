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

    '''def senseur(self):
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
        return -1 '''
    
    
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
        self.robot.set_vitesse(10.5, 10.5)
        get_dist=0.0
        state=0
        b=False # Variable qui permet de savoir si on a tourné dans la boucle 
        while not(self.robot.check_collision(self.arene_longueur,self.arene_largeur,self.obstacles) or state>4):
            if(get_dist>=distance):
                b=True
                self.robot.set_vitesse(-self.robot.vitesse_roue_gauche,self.robot.vitesse_roue_droite)
                time_to_turn = math.pi / 2
                angular_speed = (self.robot.vitesse_roue_droite - self.robot.vitesse_roue_gauche) / (2 * math.pi * self.robot.distance_roues)
                turn_time = abs(time_to_turn / angular_speed) # Time needed to turn
                num_steps = int(turn_time / time_delta)
                i=0
                while i<num_steps :
                    self.robot.deplacement(time_delta)
                    self.robot.historique.append((self.robot.x,self.robot.y))
                    i+=1
                state+=1
            if(b):
                self.robot.set_vitesse(-self.robot.vitesse_roue_gauche,self.robot.vitesse_roue_droite)
            self.robot.deplacement(time_delta)
            get_dist+=math.sqrt((self.robot.x-self.robot.historique[len-2][0])**2+(self.robot.y-self.robot.historique[len-2][1])**2) # ajout de la distance entre l'ancienne position et la nouvelle position 
        return self.robot.historique 
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


'''fig, ax = plt.subplots()
line, = ax.plot(*zip(*simulation_historique[:1]), '-o')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)

def update(frame):
    line.set_data(*zip(*simulation_historique[:frame +1]))
    return line,

ani = FuncAnimation(fig, update, frames=len(simulation_historique), interval=10, repeat=False)
plt.show()'''
