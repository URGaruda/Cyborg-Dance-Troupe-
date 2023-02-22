import ia
import ia_tourner
import ia_seq
import random
from arene import Arene,Obstacle
from affichage import Affichage
import constantes
import time
from robot import Robot 

l_obstacle=[Obstacle(random.uniform(0,Arene.arene_longueur),random.uniform(0,Arene.arene_largeur),random.uniform(0.9,4))for i in range (30) ]
dexter=Robot()

terrain=Arene(dexter,l_obstacle)
ruby=ia.IA(dexter,30.5,constantes.Vitesse)
aff=Affichage(terrain)

l_ia=[]
for i in range(7):
    if(i%2==0):
        l_ia.append(ia.IA(dexter,5.5,constantes.Vitesse) )
    else:
       l_ia.append( ia_tourner.Ia_Tourner(dexter,90,constantes.Vitesse) )
ia_carre=ia_seq.IA_Seq(l_ia)


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
"""

