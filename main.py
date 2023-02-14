import ia 
import random
from arene import Arene,Obstacle
from robot import Robot 
from affichage import Affichage 

l_obstacle=[Obstacle(random.uniform(0,100),random.uniform(0,100),random.uniform(0.3,1))for i in range (30) ]
dexter=Robot(55.56,26.78,0,0.3,0.05,0.2)
terrain=Arene(dexter,l_obstacle,0.0001)
ruby=ia.IA(dexter,10.5,terrain)
aff=Affichage(terrain)
ruby.start(5.4,9.7)
while not ruby.stop():
    terrain.arene_update()
    ruby.step()
    aff.updateAffichage(dexter,l_obstacle)
    

