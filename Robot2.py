import math
import copy
from Vecteur import Vecteur 

class Robot:
    """
    Classe pour représenter un robot.

    Attributs:
        x (float): la position x du robot.
        y (float): la position y du robot.
        orientation (float): orientation du robot en radians.
        rayon_roue (float): le rayon des deux roues.
        distance_roues (float): la distance entre les deux roues du robot.
        vitesse_roue_gauche (float): vitesse angulaire de la roue gauche du robot en radians par seconde.
        vitesse_roue_droite (float): vitesse angulaire de la roue droite du robot en radians par seconde.
        historique (list): une liste de tuples de la position x, y du robot à chaque instant.
    """
    def __init__(self, x, y, orientation, rayon_roue, distance_roues):
        """
        Initialise un objet de la classe Robot avec les paramètres donnés.
        """
       
        self.x = x
        self.y = y
        self.orientation = orientation
        self.rayon_roue = rayon_roue
        self.distance_roues = distance_roues
        self.vitesse_roue_gauche = 0
        self.vitesse_roue_droite = 0
        self.historique = []
    
    def set_vitesse(self, vitesse_roue_gauche, vitesse_roue_droite):
        """
        Définit les vitesses de la roue gauche et droite du robot.
        """
        self.vitesse_roue_gauche = vitesse_roue_gauche
        self.vitesse_roue_droite = vitesse_roue_droite

    def update_position(self, delta_time):
        """
        Met à jour la position et l'orientation du robot en fonction des vitesses de ses roues.
        """
        vitesse_moyenne = (self.vitesse_roue_gauche + self.vitesse_roue_droite) / 2 #vitesse angulaire moyenne
        vitesse_moyenne = vitesse_moyenne / (2 * math.pi * self.rayon_roue) #vitesse lineaire moyenne
        delta_x = vitesse_moyenne * math.cos(self.orientation) * delta_time #trignometry
        delta_y = vitesse_moyenne * math.sin(self.orientation) * delta_time #trigonometry
        self.x += delta_x
        self.y += delta_y
        
        
        vitesse_angulaire = (self.vitesse_roue_droite - self.vitesse_roue_gauche) / (2 * math.pi * self.distance_roues) #la vitesse de rotation du robot autour de son axe central
        delta_orientation = vitesse_angulaire * delta_time #calcule le changement d'orientation
        self.orientation += delta_orientation #calcule la nouvelle orientation
        
        self.historique.append((self.x, self.y))

    def copie(self):
        """Fait une copie du robot """
        robot=copy.copy(self)
        return robot

    
    
    


"""
#tester la classe        
try:
    robot=Robot(1,1,20,10,50,5,3) 
    print(robot.dir.x,",",robot.dir.y)  
    robot.stop()
    print(robot.v)
    robot.acceleration(30)
    print(robot.v)
    robot.freinage(15)
    print(robot.v)
    robot2=robot.copie()
    print("c'est la copie")
    print(robot2.v)
    print(robot.dir.x,",",robot.dir.y) 
    
except ValueError as erreur :
    print(erreur) 
    robot.stop()
    print(robot.v)
    robot.acceleration(30)
    print(robot.v)
"""


