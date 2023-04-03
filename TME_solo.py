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
"Ex1Q3:Ajouter la fonction dessine dans robot"

"Ex2Q1:Crerr la fonction crerr_1 dans le main"
"Ex1Q2: Crerr la fonction creer_0 dans le main"
"Ex3Q1: Creer deux classe, 1 emeteur et un recepteur dans le fichier robot, ajouter la fonction get_signal qui renvoi le signal de l'emmeteur et la fonction recevoir qui recoit l'intensité du signal"
"Ex2 en general, j'ai modifié egalement les fichier ia et ia_tourner"
