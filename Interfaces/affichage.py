from Robot_Arene_Obstacle.arene import Arene 
import math
import matplotlib.pyplot as plt
import random
from tkinter import *
class Affichage() :

    def __init__(self,arene):
        self.arene=arene
        self.fenetre=Tk()
        #self.fenetre.state('zoomed')
        self.acanvas= Canvas(self.fenetre,width = Arene.arene_longueur*3, height = Arene.arene_largeur*3 , bd=0, bg="white")
        self.acanvas.pack(padx=10,pady=10)
        self.liste_objet=[]
        self.liste_fleche=[]
    def clear(self):
        self.acanvas.delete(ALL)
        self.liste_objet=[]

    def updateAffichage(self,inter,obstacles):
        ray_r=inter.robot.rayon_robot
        if len(self.liste_objet)>0:
            self.acanvas.delete(self.liste_objet[-1])
            self.liste_objet.pop()
        if len(self.liste_fleche)>0:
            self.acanvas.delete(self.liste_fleche[-1])
            self.liste_fleche.pop()
        self.liste_objet.append(self.acanvas.create_oval((inter.x + ray_r)*2.5, (inter.y + ray_r)*2.5,( inter.x - ray_r)*2.5, (inter.y - ray_r)*2.5, fill='red'))
        x1= inter.x *2.5
        y1 = inter.y *2.5
        x2 = x1 + + ray_r *2.5 * math.cos(inter.robot.orientation)
        y2 = y1 + + ray_r *2.5 * math.sin(inter.robot.orientation)
        self.liste_fleche.append(self.acanvas.create_line(x1,y1,x2,y2,arrow=LAST,fill='blue'))
        for o in obstacles:
            self.acanvas.create_oval((o.x + o.rayon)*2.5,(o.y + o.rayon)*2.5,(o.x - o.rayon)*2.5,( o.y - o.rayon)*2.5, fill='green')
        self.fenetre.update()
