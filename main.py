import IAs.ia as ia 
import IAs.ia_tourner as ia_tourner
import IAs.ia_seq as ia_seq 
import random
from Robot_Arene_Obstacle.arene import Arene
from Robot_Arene_Obstacle.obstacle import Obstacle
from Interfaces.affichage import Affichage
import Autres.constantes as constantes 
import time
from Robot_Arene_Obstacle.robot import Robot 
from threading import Thread 

l_obstacle=[Obstacle(random.uniform(0,Arene.arene_longueur),random.uniform(0,Arene.arene_largeur),random.uniform(2.9,10))for i in range (10) ]
dexter=Robot()

terrain=Arene(dexter,l_obstacle)
ruby=ia.IA(dexter,400.5,constantes.Vitesse)
aff=Affichage(terrain)

#thread_aff=Thread(target=aff.boucle_affichage(dexter,l_obstacle,ruby))
#thread_arene=Thread(target=terrain.boucle_arene(ruby))

l_ia=[]
for i in range(7):
    if(i%2==0):
        l_ia.append(ia.IA(dexter,55.5,constantes.Vitesse) )
    else:
       l_ia.append( ia_tourner.Ia_Tourner(dexter,90,constantes.Vitesse) )
ia_carre=ia_seq.IA_Seq(l_ia)



"""
ruby.start()
while not ruby.stop() and not terrain.check_collision():
    terrain.arene_update()
    ruby.step()
    aff.updateAffichage(dexter,l_obstacle)

    #time.sleep(0.2)
"""

ia_carre.start()
while not ia_carre.stop() and not terrain.check_collision():
    terrain.arene_update()
    ia_carre.step()
    aff.updateAffichage(dexter,l_obstacle)
    aff.fenetre.update()

