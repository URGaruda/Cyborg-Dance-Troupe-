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

def initiate():
    global l_obstacle
    l_obstacle=[Obstacle(Arene.arene_longueur-20,Arene.arene_largeur-20,10) ]
    l_obstacle.append(Obstacle(20,Arene.arene_largeur-20,10))
    l_obstacle.append(Obstacle(Arene.arene_longueur-20,20,10))
    l_obstacle.append(Obstacle(20,20,10))

    global dexter
    dexter=Robot()
    dexter.x=200
    dexter.y=200
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

def create_hexagone(distance):
    global l_ia
    l_ia=[]
    l_ia.append(ia_tourner.Ia_Tourner(inter, 30, constantes.Vitesse))
    for i in range(6):
        
        l_ia.append(ia.IA(inter, distance, constantes.Vitesse))
        l_ia.append(ia_tourner.Ia_Tourner(inter, 60, constantes.Vitesse))
        
    ia_hex = ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia = ia_hex

def create_un(distance):
    l_ia = []
    l_ia.append(ia_tourner.Ia_Tourner(inter, 90, constantes.Vitesse))
    l_ia.append(ia.IA(inter, distance, constantes.Vitesse))
    l_ia.append(ia_tourner.Ia_Tourner(inter, -90, constantes.Vitesse))
    ia_line = ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia = ia_line

def create_zero(longueur, largeur):
    l_ia = []
    l_ia.append(ia_tourner.Ia_Tourner(inter, 90, constantes.Vitesse))
    for i in range(2):
        l_ia.append(ia.IA(inter, longueur, constantes.Vitesse))
        l_ia.append(ia_tourner.Ia_Tourner(inter, 90, constantes.Vitesse))
        l_ia.append(ia.IA(inter, largeur, constantes.Vitesse))
        l_ia.append(ia_tourner.Ia_Tourner(inter, 90, constantes.Vitesse))
    ia_rect = ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia = ia_rect




initiate()
create_zero(100,50)
main_ia.start()
dexter.start_time()
    
while not main_ia.stop() and not terrain.check_collision():
    
    terrain.arene_update()
    main_ia.step()
    aff.updateAffichage(dexter,l_obstacle)