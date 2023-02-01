import math
import time 
from Vecteur import Vecteur
from Robot2 import Robot 

class Obstacle : 
    def __init__(self,x,y,R):
        self.x=x
        self.y=y
        self.R=R

class Simulation : 
    Ymax=400.0 #en cm
    Xmax=355.0 #en cm 
    def __init__(self,x,y,v,dirX,dirY,temps,obstacle):
        self.dexter=Robot(x,y,v,25/2,60,dirX,dirY) #Je suppose ici que le Robot fait 25 cm de long et qu'il a un angle de vue de 60° . Vous pouvez les mettres en paramètres si vous préféré comme ça 
        self.liste_obstacle=obstacle
        self.pas_temps=temps
    
    def collision(self,vect):
        """ Determine si le Robot Dexter est où pas en collision avec un des obstacles du terrain """
        for obj in self.liste_obstacle :
            return not(math.sqrt(((obj.x-vect.x)**2)+((obj.y-vect.y)**2)) > obj.R+vect.R): # si y'a colision il renvoie vrai 
    
    def hors_terrain(self,robot):
        """ Prends un robot et vérifie s'il est toujours sur le terrain """
        if(robot.x<0.0 or robot.x >= Simulation.Xmax or robot.y < 0.0 or robot.y >= Simulation.Ymax ):
            return True 
        return False 
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

    def affichage(self):
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
    def simulation_carre(self,pas):
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
try:
    sim=Simulation(104.29,145.96,2,56,24,0.10,[])
except ValueError as erreur :
    print(erreur)    
def update():
    sim=Simulation(124.29,196.96,4.2,3,8,0.020,[])
    sim.simulation_carre(10)
update()

            
            




