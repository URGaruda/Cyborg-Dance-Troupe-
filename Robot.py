#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def matriceCarre(n):
    return [[ 0 for j in range(n)] for i in range(n)]

class Robot:
    """Création d'un robot """
    def __init__(self,x,y,nom):
        """Variable qui defini"""
        self.x=x
        self.y=y
        self.nom=nom
    def deplacementPossible(self,x,y,t):
        if(x>len(t) or y>len(t) or x<0 or y<0 ):
            return False 
        else:
            return True 
    def getX(self):
        return self.x 
    def getY(self):
        return self.y 
    def setX(self,px):
        self.x=px 
    def setY(self,py):
        self.y=py 
    def seDeplace(self,x,y,t):
        if(self.deplacementPossible(x,y,t)):
            self.x=x
            self.y=y
            print(self.nom,"s'est déplacé à la case ",x,",",y)
        
    def presentation(self):
        print("Je suis ",self.nom," un robot et je suis en position (",self.x,",",self.y,")")

m1=matriceCarre(15)
r1=Robot(5,7,"Barry")
r1.seDeplace(12,7,m1)
r1.presentation() 

    