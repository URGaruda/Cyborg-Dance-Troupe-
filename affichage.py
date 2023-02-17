from arene import Arene 
import math
import matplotlib.pyplot as plt
from robot import Robot 
import random
from tkinter import *
class Affichage() : 

    def __init__(self,arene):
        self.arene=arene
        self.fenetre=Tk()
        #self.fenetre.state('zoomed')
        self.acanvas= Canvas(self.fenetre,width = 1000, height = 1000 , bd=0, bg="white")
        self.acanvas.pack(padx=10,pady=10)
        self.liste_objet=[]
    def clear(self):
        self.acanvas.delete(self.liste_objet)
    def ok(self,robot,obstacles):
        ray_r=robot.rayon_robot
        self.liste_objet.append(self.acanvas.create_oval(robot.x+ray_r,robot.y+ray_r,robot.x-ray_r,robot.y-ray_r,fill='red'))
        for o in obstacles :
            self.acanvas.create_oval(o.x+o.rayon,o.y+o.rayon,o.x-o.rayon,o.y-o.rayon,fill='green')
    def updateAffichage(self,robot,obstacles):
        self.ok(robot,obstacles)
        self.clear()
    