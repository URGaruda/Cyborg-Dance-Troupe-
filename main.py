import CDT.IAs.ia as ia 
import CDT.IAs.ia_tourner as ia_tourner
import CDT.IAs.ia_seq as ia_seq 
import random
from CDT.Simulation.arene import Arene
from CDT.Simulation.obstacle import Obstacle
from CDT.Interfaces.affichage import Affichage
import CDT.Weiter.constantes as constantes 
<<<<<<< HEAD
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
=======
import CDT.IAs.ia_loop as ia_loop 
import time
from CDT.Simulation.robot import Robot
from CDT.IAs.intermediaire import Intermediaire  
l_obstacle=[]
dexter=None
inter=None
terrain=None
aff=None
ruby=None
l_ia=[]
main_ia=None
def initiate(nb_obstacle):
    global l_obstacle
    l_obstacle=[Obstacle(random.uniform(0,Arene.arene_longueur),random.uniform(0,Arene.arene_largeur),random.uniform(2.9,10))for i in range (nb_obstacle) ]
    global dexter
    dexter=Robot()
    global inter
    inter=Intermediaire(dexter,l_obstacle)
    global terrain
    terrain=Arene(dexter,l_obstacle)
    global aff 
    aff=Affichage(terrain)

def create_line(distance):
    global ruby
    ruby=ia.IA(inter,distance,constantes.Vitesse)
    global main_ia
    main_ia=ruby


def create_carre(distance):
    global l_ia
    for i in range(7):
        if(i%2==0):
            l_ia.append(ia.IA(inter,distance,constantes.Vitesse) )
        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse ))
    ia_carre=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_carre

def create_rectangle(longueur,largeur):
    global l_ia
    b=True
    for i in range(7):
        if(i%2==0):
            if(b):
                l_ia.append(ia.IA(inter,longueur,constantes.Vitesse) )
                b=False
            else:
                l_ia.append(ia.IA(inter,largeur,constantes.Vitesse) )
                b=True

        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse ))
    ia_rect=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_rect

def create_triangle_equilateral(distance):
    global l_ia
    l_ia.append(ia_tourner.Ia_Tourner(inter,60,constantes.Vitesse ))
    for i in range(5):
        if(i%2==0):
            l_ia.append(ia.IA(inter,distance,constantes.Vitesse) )
        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,120,constantes.Vitesse ))
    ia_equi=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_equi


def create_loop(ia,condition): #en phase de test 
    loop=ia_loop.IA_Loop(ia,condition)
    global main_ia
    main_ia=loop

initiate(0)
create_triangle_equilateral(100)
main_ia.start()
dexter.start_time()
    
while not main_ia.stop() and not terrain.check_collision():
    
    terrain.arene_update()
    main_ia.step()
    aff.updateAffichage(dexter,l_obstacle)

>>>>>>> Dev
