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
       
    def __init__(self,robot,obstacles):
        self.robot=robot
        self.obstacles=obstacles
        self.arene_longueur = 50.0
        self.arene_largeur = 50.0

    def check_collision(self):
        """
        Vérifie s'il y a une collision entre le robot et les bords de l'arène/ obstacle
        """
        # Vérifie une collision avec les bords de l'arène
        if self.robot.x - self.robot.rayon_robot < 0 or self.robot.x + self.robot.rayon_robot > self.arene_longueur :
            return True
        if self.robot.y - self.robot.rayon_robot < 0 or self.robot.y + self.robot.rayon_robot > self.arene_largeur :
            return True
        
        # Vérifie une collision avec les obstacles
        for obj in self.obstacles:
            if not(math.sqrt(((obj.x-self.robot.x)**2)+((obj.y-self.robot.y)**2)) > obj.rayon+self.robot.rayon_robot ): # si y'a colision il renvoie vrai
                return True
        
        return False

    def deplacement(self, delta_time):
        """
        Met à jour la position et l'orientation du robot en fonction des vitesses de ses roues.
        """
        vitesse_moyenne = (self.robot.vitesse_roue_gauche + self.robot.vitesse_roue_droite) / 2 
        vitesse_moyenne = vitesse_moyenne / (2 * math.pi * self.robot.rayon_roue) #vitesse lineaire moyenne
        delta_x = vitesse_moyenne * math.cos(self.robot.orientation) * delta_time 
        delta_y = vitesse_moyenne * math.sin(self.robot.orientation) * delta_time 
        self.robot.x += delta_x
        self.robot.y += delta_y
        
        
        vitesse_angulaire = (self.robot.vitesse_roue_droite - self.robot.vitesse_roue_gauche) / (2 * math.pi * self.robot.distance_roues) #la vitesse de rotation du robot autour de son axe central
        delta_orientation = vitesse_angulaire * delta_time #calcule le changement d'orientation
        self.robot.orientation += delta_orientation #calcule la nouvelle orientation
        
        self.robot.historique.append((self.robot.x, self.robot.y))

    
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
    
    
    def trace_cote_carre(self, vitesse, dt, taille_carre):
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
        self.robot.set_vitesse(vitesse, vitesse)
        duree = taille_carre / ((robot.vitesse_roue_gauche + robot.vitesse_roue_droite) / 2) * robot.rayon_roue * 2 * math.pi
        nombre_pas = int(duree / dt)
        #le robot trace un coté du carré
        for j in range(nombre_pas):
            self.deplacement(dt)
            if self.check_collision():
                self.robot.set_vitesse(0,0)
                return self.robot.historique

        
        self.robot.set_vitesse(vitesse, -vitesse) #pour pouvoir tourner
        angle = math.pi / 2
        vitesse_angulaire = (self.robot.vitesse_roue_droite - self.robot.vitesse_roue_gauche) / (2 * math.pi * self.robot.distance_roues)
        temps_tourner = abs(angle / vitesse_angulaire) #temps nécessaire pour finir le tour
        nombre_pas = int(temps_tourner / dt)
        #rotation du robot autour de son axe central
        for j in range(nombre_pas):
            self.deplacement(dt)

        return self.robot.historique
    
    def simulation_carre(self,distance,time_delta):#prend une distance à parcourir 
        """ Fait faire un carré au robot dont les cotés sont égaux à la distance"""
        self.robot.set_vitesse(10.5, 10.5)
        get_dist=0.0
        state=0
        b=False # Variable qui permet de savoir si on a tourné dans la boucle 
        while not(self.check_collision() or state>4):
            if(get_dist>=distance):
                b=True
                self.robot.set_vitesse(-self.robot.vitesse_roue_gauche,self.robot.vitesse_roue_droite)
                time_to_turn = math.pi / 2
                angular_speed = (self.robot.vitesse_roue_droite - self.robot.vitesse_roue_gauche) / (2 * math.pi * self.robot.distance_roues)
                turn_time = abs(time_to_turn / angular_speed) # Time needed to turn
                num_steps = int(turn_time / time_delta)
                i=0
                while i<num_steps :
                    self.deplacement(time_delta)
                    self.robot.historique.append((self.robot.x,self.robot.y))
                    i+=1
                state+=1
            if(b):
                self.robot.set_vitesse(-self.robot.vitesse_roue_gauche,self.robot.vitesse_roue_droite)
            self.deplacement(time_delta)
            get_dist+=math.sqrt((self.robot.x-self.robot.historique[len-2][0])**2+(self.robot.y-self.robot.historique[len-2][1])**2) # ajout de la distance entre l'ancienne position et la nouvelle position 
        return self.robot.historique 
    def affichage(self):
        fig, ax = plt.subplots()
        l_obstacles=[plt.Circle((obs.x,obs.y),obs.rayon)for obs in obstacles]
        for o in l_obstacles:
            ax.add_patch(o)
        l_robot=[plt.Circle((x, y), 0.9, color='r') for (x,y) in simulation_historique]
        for r in l_robot:
            ax.add_patch(r)
        ax.set_xlim(0, 50.0)
        ax.set_ylim(0, 50.0)
        plt.show()

robot = Robot(x=50, y=50, orientation=0, rayon_robot=0.3, rayon_roue=0.05, distance_roues=0.2) 
obstacles= [Obstacle(random.uniform(0,100),random.uniform(0,100),random.uniform(0.3,1))for i in range (50) ]
simulation=Simulation(robot,obstacles)

while True:
    simulation_historique = simulation.trace_cote_carre( 10, 0.0001, 10)
    print(simulation_historique)
    simulation.affichage() 
