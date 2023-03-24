from CDT.IAs.inter_robot import Inter_Robot
from CDT.Weiter.robotmockup import Robotmockup 
import CDT.IAs.ia as ia 
import CDT.IAs.ia_tourner as ia_tourner
import CDT.IAs.ia_seq as ia_seq 
import random
from CDT.Simulation.arene import Arene
from CDT.Simulation.obstacle import Obstacle
from CDT.Interfaces.affichage import Affichage
import CDT.Weiter.constantes as constantes 
import time
from CDT.Simulation.robot import Robot
from CDT.IAs.intermediaire import Intermediaire  


def make_line():
    l_obstacle=[Obstacle(random.uniform(0,Arene.arene_longueur),random.uniform(0,Arene.arene_largeur),random.uniform(2.9,10))for i in range (10) ]
    dexter=Robotmockup(252,96)
    inter=Inter_Robot(dexter)
    terrain=Arene(dexter,l_obstacle)
    ruby=ia.IA(inter,40.5,constantes.Vitesse)
    #simulation 
    ruby.start()
    #dexter.start_time()
    while not ruby.stop() and not terrain.check_collision():
        terrain.arene_update()
        ruby.step()

print("ça commence")       
make_line()
print("c'est fini")
