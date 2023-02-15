import ia 
import random
from arene import Arene,Obstacle
from robot import Robot 
from affichage import Affichage 

l_obstacle=[Obstacle(random.uniform(0,100),random.uniform(0,100),random.uniform(0.3,1))for i in range (30) ]
dexter=Robot(55.56,56.78,0,0.3,0.05,0.2)
terrain=Arene(dexter,l_obstacle,0.01)
ruby=ia.IA(dexter,10.5,terrain)
aff=Affichage(terrain)
ruby.start(-10,-40)
i=0
while not ruby.stop():
    terrain.arene_update()
    ruby.step()
    """if(i%1000==0):
        aff.updateAffichage(dexter,l_obstacle)"""
    i+=1
    

