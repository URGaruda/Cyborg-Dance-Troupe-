import ia
import ia_tourner
import ia_seq
import random
from arene import Arene,Obstacle
from affichage import Affichage
import constantes
import variables
import time

l_obstacle=[Obstacle(random.uniform(0,Arene.arene_longueur),random.uniform(0,Arene.arene_largeur),random.uniform(0.9,4))for i in range (30) ]
variables.dexter.set_vitesse(constantes.Vitesse_Gauche,constantes.Vitesse_Droite)
terrain=Arene(variables.dexter,l_obstacle)
ruby=ia.IA(30.5)
aff=Affichage(terrain)

l_ia=[]
for i in range(7):
    if(i%2==0):
        l_ia.append(ia.IA(5.5) )
    else:
       l_ia.append( ia_tourner.Ia_Tourner(90) )
ia_carre=ia_seq.IA_Seq(l_ia)

"""
ruby.start()
while not ruby.stop() and not terrain.check_collision():
    terrain.arene_update()
    ruby.step()
    aff.updateAffichage(variables.dexter,l_obstacle)

    #time.sleep(0.2)
"""
ia_carre.start()
while not ia_carre.stop() and not terrain.check_collision():
    terrain.arene_update()
    ia_carre.update()
    ia_carre.step()
    aff.updateAffichage(variables.dexter,l_obstacle)
    aff.fenetre.update()


