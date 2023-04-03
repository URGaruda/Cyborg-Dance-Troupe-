import tkinter as tk
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
"Ex1Q1"
root = tk.Tk()
root.geometry("400x400")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

canvas.create_oval(195, 195, 205, 205, fill="black")

canvas.create_oval(10, 10, 20, 20, fill="orange")
canvas.create_oval(10, 380, 20, 390, fill="orange")
canvas.create_oval(380, 10, 390, 20, fill="orange")
canvas.create_oval(380, 380, 390, 390, fill="orange")

root.mainloop()

"Ex1Q2: Modifier le fill des obstacles en orange dans affichage"

"Ex2Q1:Je n'ai pas utilisé la fonction dessin mais la fonction create_rectangle qui se trouve dans mon main, pour que le dessin aille dans le bon sens, j'ai du modifier l'orientation qui se trouve dans les Constantes dans Weiter"
"Ex1Q2:Pareil que la 1ère sauf que j'ai du utliser la fonction create_line"
