#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt

def matriceCarre(n):
    return [[ 0 for j in range(n)] for i in range(n)]
    
def deplacementPossible(x,y,t):
        if x < 0 or x >= len(t) or y < 0 or y >= len(t) or t[x][y] != 0:
            return False 
        else:
            return True
class Robot:
    def __init__(self,x,y,nom):
        self.x=x
        self.y=y
        self.nom=nom
        self.positions = [] # Ajout d'une liste pour stocker les positions précédentes
         
    def deja_vu(self,x,y):
        for p in self.positions : 
            pos_x,pos_y=p 
            if pos_x==x and pos_y==y :
                return True 
        return False 
        
    def avancer(self,t):
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
        if(deplacementPossible(pos_x,pos_y,t)) :
            self.x=pos_x
            self.y=pos_y
            
        self.positions.append((self.x, self.y)) # Ajout de la position courante dans la liste
        

    def affichage(self):
        for position in self.positions:# afficher toutes les positions précédentes e
            plt.scatter(position[0], position[1], c='b')
        plt.scatter(self.x, self.y, c='r') # Afficher la position actuelle en rouge
        plt.title("Position de robot")
        plt.show()
        
    def simulation(n):
        t = matriceCarre(n)
        robot = Robot(0,0, "barry")
        for i in range(n):
            robot.avancer(t)
            
        robot.affichage()
        print("Voici les positions du robots ",robot.positions)
        print("Position actuelle: x =", robot.x, "y =", robot.y)

def simulations(k,n): # realise un ensemble k de simulations sur un matrice de taille n 
    for i in range(k):
        Robot.simulation(n)
simulations(5,20)
#Robot.simulation(20)



