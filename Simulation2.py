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
    def avancer(self):
        """Fait avancer en ligne droite le robot """
        self.dexter.v1=(self.dexter.v1+self.dexter.v2)/2 #ajuste la vitesse des roues pour avoir un deplacdement en ligne droite 
        self.dexter.v2=self.dexter.v1 
        self.dexter.x=self.dexter.x
        v=self.dexter.v1 #Calcule la vitesse moyenne du robot 
        pc=v*self.pas_temps # valeur de la vitesse sur le pas de temps de la simulation 
        vect_v=self.dexter.dir.mult_par_un_scalaire(pc)
        self.dexter.x+=vect_v.x
        self.dexter.y+=vect_v.y

    def reculer(self):
        """Fait reculer le robot en ligne droite"""
        self.dexter.v1=(self.dexter.v1+self.dexter.v2)/2 #ajuste la vitesse des roues pour avoir un deplacdement en ligne droite 
        self.dexter.v2=self.dexter.v1 
        self.dexter.x=self.dexter.x
        v=self.dexter.v1 #Calcule la vitesse moyenne du robot 
        pc=(v*self.pas_temps) # valeur de la vitesse sur le pas de temps de la simulation 
        vect_v=self.dexter.dir.mult_par_un_scalaire(-pc)
        self.dexter.x+=vect_v.x
        self.dexter.y+=vect_v.y

    def simu_1(self,vit):
        """ Fait une simulation avec une vitesse vit initiale"""
        self.dexter.setVitesse_A(vit) #ajuste la vitesse du robot avant la simulation 
        while True : 
            print(self.dexter.x,",",self.dexter.y) 
            if(self.hors_terrain(self.dexter)):
                print("Dexter est sorti du terrain")
                break
            if(self.collision(Vecteur(self.dexter.x,self.dexter.y ))):
                print("Il y a eu collision")
                break 
            if(random.randint(1,15)>3):
                self.avancer()
                print("avance")
            else:
                self.reculer() 
                print("recule")
            
        

    def affichage(self): # essai d'affichage raté 
        print("+", end='')
        for j in range(int(self.Ymax)+1):
            print("-", end='')
        print("+\n")
        for i in range(int(self.Xmax)+1):
            print("|", end='')
            #for j in range(self.Ymax):
            print("|\n")
        print("+", end='')
        for j in range(int(self.Ymax)+1):
            print("-", end='')
        print("+\n")
    def simulation_carre(self,pas): # ancienne simulation 
        """ Fait faire un carré au robot de la distance "dist" au robot sur le terrain (0.0,Xmax) en x et (0.0,Ymax) """
        print(self.dexter.dir.x,",",self.dexter.dir.y)
        for i in range(4):
            vect_v=self.dexter.dir.mult_par_un_scalaire((self.dexter.v*self.pas_temps)) 
            for j in range(pas):
                print(self.dexter.x,",",self.dexter.y) 
                self.dexter.x+=vect_v.x
                self.dexter.y+=vect_v.y
                if(self.hors_terrain(self.dexter)):
                    print("Dexter est sorti du terrain")
                    return
                if(self.collision(Vecteur(self.dexter.x,self.dexter.y ))):
                    print("Il y a eu collision")
                    return 
                if(self.senseur()==1):
                    print("Obstacle à proximité")
                    time.sleep(1)
                    break 
                time.sleep(0.5)
            print("un tour s'est passé")
            self.dexter.dir.rotation_anti_horaire(math.pi/2)
            time.sleep(2)
        print("simulation fini")
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
sim=Simulation(324.29,96.96,6.32,1.45,0.20,[])
sim.simu_1(12.3)

           
            




