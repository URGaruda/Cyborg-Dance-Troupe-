#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Robot:
    """Création d'un robot """
    def __init__(self,x,y,nom):
        """Variable qui defini"""
        self.x=x
        self.y=y
        self.nom=nom
    def getX(self):
        return self.x 
    def getY(self):
        return self.y 
    def setX(self,px):
        self.x=px 
    def setY(self,py):
        self.y=py 
    def presentation(self):
        print("Je suis ",self.nom," un robot et je suis en position (",self.x,",",self.y,")")


    