from arene import Arene 
import math
import matplotlib.pyplot as plt
from robot import Robot 
import random
class Affichage() : 

    def __init__(self,arene):
        self.arene=arene

    def updateAffichage(self,robot,obstacles):
        fig, ax = plt.subplots()
        l_obstacles=[plt.Circle((obs.x,obs.y),obs.rayon)for obs in obstacles]
        for o in l_obstacles:
            ax.add_patch(o)
        l_robot=[plt.Circle((robot.x,robot.y),robot.rayon_robot, color='r') ]
        for r in l_robot:
            ax.add_patch(r)
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        plt.show()
      