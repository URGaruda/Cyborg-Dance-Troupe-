import CDT.IAs.ia as ia 
import CDT.IAs.ia_tourner as ia_tourner
import CDT.IAs.ia_seq as ia_seq 
import random
from CDT.Simulation.arene import Arene
from CDT.Simulation.obstacle import Obstacle
from CDT.Interfaces.affichage import Affichage
import CDT.Weiter.constantes as constantes 
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

def create_line(distance,b):
    global ruby
    ruby=ia.IA(inter,distance,constantes.Vitesse,b)
    global main_ia
    main_ia=ruby


def create_carre(distance):
    global l_ia
    for i in range(7):
        if(i%2==0):
            l_ia.append(ia.IA(inter,distance,constantes.Vitesse,True) )
        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse ,True))
    ia_carre=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_carre

def create_rectangle(longueur,largeur):
    global l_ia
    b=True
    for i in range(7):
        if(i%2==0):
            if(b):
                l_ia.append(ia.IA(inter,longueur,constantes.Vitesse,True) )
                b=False
            else:
                l_ia.append(ia.IA(inter,largeur,constantes.Vitesse,True) )
                b=True

        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse,True ))
    ia_rect=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_rect

def create_triangle_equilateral(distance):
    global l_ia
    l_ia.append(ia_tourner.Ia_Tourner(inter,60,constantes.Vitesse ,True))
    for i in range(5):
        if(i%2==0):
            l_ia.append(ia.IA(inter,distance,constantes.Vitesse,True) )
        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,120,constantes.Vitesse ,True))
    ia_equi=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_equi


def create_loop(ia,condition): #en phase de test 
    loop=ia_loop.IA_Loop(ia,condition)
    global main_ia
    main_ia=loop
"""
initiate(10)
create_carre(100)
main_ia.start()
dexter.start_time()

while not main_ia.stop() and not terrain.check_collision():
    
    terrain.arene_update()
    main_ia.step()
    aff.updateAffichage(dexter,l_obstacle)

l_obs=[Obstacle(124,155,5.5),Obstacle(174,155,5.5),Obstacle(124,205,5.5),Obstacle(174,205,5.5)]
"""
# tme solo 
#question 1.1
def initiate_sol(nb_obstacle):
    global l_obstacle
    #l_obstacle=[Obstacle(random.uniform(0,Arene.arene_longueur),random.uniform(0,Arene.arene_largeur),random.uniform(2.9,10))for i in range (nb_obstacle) ]
    l_obstacle=[Obstacle(124,155,5.5),Obstacle(174,155,5.5),Obstacle(124,205,5.5),Obstacle(174,205,5.5)]
    global dexter
    dexter=Robot()
    dexter.x=149
    dexter.y=175
    global inter
    inter=Intermediaire(dexter,l_obstacle)
    global terrain
    terrain=Arene(dexter,l_obstacle)
    global aff 
    aff=Affichage(terrain)

def create_hexagone(distance):
    global l_ia
    l_ia.append(ia_tourner.Ia_Tourner(inter,60,constantes.Vitesse ,True))
    for i in range(11):
        if(i%2==0):
            l_ia.append(ia.IA(inter,distance,constantes.Vitesse,True) )
        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,60,constantes.Vitesse,True ))
    ia_equi=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_equi

def create_1(distance):
    global l_ia
    l_ia.append(ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse ,True))
    l_ia.append(ia.IA(inter,distance,constantes.Vitesse,True) )
    ia_equi=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_equi

def create_0():
    longueur=70
    largeur=35
    global l_ia
    b=True
    for i in range(7):
        if(i%2==0):
            if(b):
                l_ia.append(ia.IA(inter,largeur,constantes.Vitesse,True) )
                b=False
            else:
                l_ia.append(ia.IA(inter,longueur,constantes.Vitesse,True) )
                b=True

        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse,True))
    ia_rect=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_rect

#question 2.3 
def create_0_1():
    longueur=70
    largeur=35
    global l_ia
    b=True
    for i in range(7):
        if(i%2==0):
            if(b):
                l_ia.append(ia.IA(inter,largeur,constantes.Vitesse,True) )
                b=False
            else:
                l_ia.append(ia.IA(inter,longueur,constantes.Vitesse,True) )
                b=True

        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse,True))

    l_ia.append( ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse,True))
    l_ia.append(ia.IA(inter,90,constantes.Vitesse,False))

    l_ia.append(ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse ,True))
    l_ia.append(ia.IA(inter,70,constantes.Vitesse,True) )
    ia_equi=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_equi
# question 2.5 
def create_bin(mot):
    global l_ia
    verif=0
    for i in mot :
        if i=="0" :
            verif=0
            longueur=70
            largeur=35
            b=True
            for i in range(7):
                if(i%2==0):
                    if(b):
                        l_ia.append(ia.IA(inter,largeur,constantes.Vitesse,True) )
                        b=False
                    else:
                        l_ia.append(ia.IA(inter,longueur,constantes.Vitesse,True) )
                        b=True

                else:
                    l_ia.append( ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse,True))  
        else :
            verif=1
            l_ia.append( ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse,False))
            l_ia.append(ia.IA(inter,70,constantes.Vitesse,True))
        if verif == 1 :
            l_ia.append(ia_tourner.Ia_Tourner(inter,180,constantes.Vitesse ,True))
            l_ia.append(ia.IA(inter,70,constantes.Vitesse,False))
            l_ia.append(ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse ,True))
            l_ia.append(ia.IA(inter,40,constantes.Vitesse,False)) 
        else :
            l_ia.append(ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse ,True))
            l_ia.append(ia.IA(inter,70,constantes.Vitesse,False))
    
    ia_equi=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_equi
        

        

"""
initiate(0)

#debut question 2.4    
create_0_1()
remonte=[]
remonte.append(ia_tourner.Ia_Tourner(inter,180,constantes.Vitesse ,True))
remonte.append(ia.IA(inter,70,constantes.Vitesse,False))
remonte.append(ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse ,True))
remonte.append(ia.IA(inter,40,constantes.Vitesse,False)) 
l_ia=main_ia.liste+remonte
ia_equi=ia_seq.IA_Seq(l_ia)
main_ia=ia_equi
loop=ia_loop.IA_Loop(main_ia,False)
main_ia=loop


main_ia.start()
dexter.start_time()
dexter.dessine(True)
ver=False
while not main_ia.stop() and not terrain.check_collision():
    main_ia.step()
    terrain.arene_update()
    aff.updateAffichage(dexter,l_obstacle)

#fin question 2.4 
"""
"""
initiate(0)
create_0()
main_ia.start()
dexter.start_time()
dexter.dessine(True)
while not main_ia.stop() and not terrain.check_collision():
    main_ia.step()
    terrain.arene_update()
    aff.updateAffichage(dexter,l_obstacle)

"""

#question 2.5 

initiate(0)
create_bin("100110")
main_ia.start()
dexter.start_time()
dexter.dessine(True)
while not main_ia.stop() and not terrain.check_collision():
    main_ia.step()
    terrain.arene_update()
    aff.updateAffichage(dexter,l_obstacle)