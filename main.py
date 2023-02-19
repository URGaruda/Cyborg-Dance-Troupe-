import ia 
import random
from arene import Arene,Obstacle
from robot import Robot 
from affichage import Affichage
import constantes 
import time

l_obstacle=[Obstacle(random.uniform(0,Arene.arene_longueur),random.uniform(0,Arene.arene_largeur),random.uniform(0.9,4))for i in range (30) ]
dexter=Robot()
terrain=Arene(dexter,l_obstacle,0.01)
ruby=ia.IA(dexter,20.5,terrain)
aff=Affichage(terrain)
ruby.start(constantes.Vitesse_Gauche,constantes.Vitesse_Droite)
i=0
while not ruby.stop():
    terrain.arene_update()
    ruby.step()
    """if(i%50==0):
        aff.updateAffichage(dexter,l_obstacle)
    i+=1"""
    aff.updateAffichage(dexter,l_obstacle)
    aff.fenetre.update()
    time.sleep(0.001)


