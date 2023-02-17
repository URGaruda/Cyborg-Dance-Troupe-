import robot
import math


class Save_Position :
    """Prend l'historique de position du robot"""
    def __init__(self):
        self.liste=[] #liste de tuple de position
    def get_position(self):
        return self.liste[-1]

    def last_distance(self): # retourne la distance du dernier deplacement du robot 
        return math.sqrt((self.liste[-1][0]-self.liste[-2][0])**2+(self.liste[-1][1]-self.liste[-2][1])**2 )
