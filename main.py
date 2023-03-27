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
    dexter=Robot()
    inter=Intermediaire(dexter)
    terrain=Arene(dexter,l_obstacle)
    ruby=ia.IA(inter,40.5,constantes.Vitesse)
    aff=Affichage(terrain)
    #simulation 
    ruby.start()
    dexter.start_time()
    while not ruby.stop() and not terrain.check_collision():
        terrain.arene_update()
        ruby.step()
        aff.updateAffichage(dexter,l_obstacle)

def make_carre():
    l_obstacle=[Obstacle(random.uniform(0,Arene.arene_longueur),random.uniform(0,Arene.arene_largeur),random.uniform(2.9,10))for i in range (10) ]
    dexter=Robot()
    inter=Intermediaire(dexter)

    terrain=Arene(dexter,l_obstacle)
    aff=Affichage(terrain)

    l_ia=[]
    for i in range(9):
        if(i%2==0):
            l_ia.append(ia.IA(inter,25.5,constantes.Vitesse) )
        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse ))
    ia_carre=ia_seq.IA_Seq(l_ia)
    ia_carre.start()
    dexter.start_time()
    while not ia_carre.stop() and not terrain.check_collision():
        terrain.arene_update()
        ia_carre.step()
        aff.updateAffichage(dexter,l_obstacle)
        aff.fenetre.update()
        
make_carre() 