import ia 
import ia_tourner
import ia_seq 
import random
from arene import Arene,Obstacle
from robot import Robot 
from affichage import Affichage
import constantes 
import time

l_obstacle=[Obstacle(random.uniform(0,Arene.arene_longueur),random.uniform(0,Arene.arene_largeur),random.uniform(0.9,4))for i in range (30) ]
dexter=Robot()
dexter.set_vitesse(constantes.Vitesse_Gauche,constantes.Vitesse_Droite)
terrain=Arene(dexter,l_obstacle,0.01)
ruby=ia.IA(dexter,20.5,terrain)
aff=Affichage(terrain)
l_ia=[]
for i in range(7):
    if(i%2==0):
        l_ia.append(ia.IA(dexter,10.5,terrain) )
    else:
       l_ia.append( ia_tourner.Ia_Tourner(dexter,0,terrain) ) 
ia_carre=ia_seq.IA_Seq(dexter,terrain,l_ia)
ruby.start()
i=0

while not ruby.stop():
    terrain.arene_update()
    ruby.step()
    aff.updateAffichage(dexter,l_obstacle)
    aff.fenetre.update()
    #time.sleep(0.2)
"""
ia_carre.start() 
while not ia_carre.stop():
    terrain.arene_update()
    ia_carre.update()
    ia_carre.step()
    aff.updateAffichage(dexter,l_obstacle)
    aff.fenetre.update()

    time.sleep(0.001)
"""

