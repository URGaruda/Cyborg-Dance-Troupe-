#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# taille de la fenetre (carrée)
larg, long = 10, 10

# figure et limites des axes x et y
fig, ax = plt.subplots()
ax.set_xlim(0, larg)
ax.set_ylim(0, long)


def deplacement_possible(x,y,taille,liste_obstacle):
        if x < 0 or x >= taille or y < 0 or y >= taille or (x,y) in liste_obstacle :
            return False 
        else:
            return True
def creer_obstacle(n):
    l=[]
    for i in range(n):
        l.append((random.randint(0,larg),(random.randint(0,long))))
    return l 
lo=creer_obstacle(60) # liste d'obstacle  

def affiche_obstacle(l):
    for x,y in l:
        plt.scatter(x,y,c='r')   
         
class Robot:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        # créer le point qui représente le robot
        self.scat=ax.scatter(self.x, self.y)
class Roue:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.somme=self.x+self.y
    

    
    def avancer(self):
        direction_v = random.choice(["haut", "bas","rien"])
        direction_h = random.choice(["gauche", "droite","rien"])
        pos_x=self.x
        pos_y=self.y
        if direction_h=="gauche" :
            pos_x-=1
        else :
            if direction_h=="droite":
                pos_x+=1
        if direction_v=="haut":
            pos_y-=1
        else :
            if direction_v=="bas":
                pos_y+=1
        if(deplacement_possible(pos_x,pos_y,long,lo)) :
            self.x=pos_x
            self.y=pos_y

        # changer la position du point
        self.scat.set_offsets([[self.x, self.y]])

    

# simulation
cyborg = Robot(larg/2,long/2)
def update(frame):
    cyborg.avancer()
affiche_obstacle(lo)
ani = animation.FuncAnimation(fig, update, frames=range(100), repeat=False, interval=700)
plt.show()




