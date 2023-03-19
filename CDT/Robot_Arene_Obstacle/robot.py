import math
import CDT.Autres.constantes as constantes 
class Robot:
    """
    Classe pour représenter un robot.
    Attributs:
        x (float): la position x du robot.
        y (float): la position y du robot.
        orientation (float): orientation du robot en radians.
        rayon_robot(float): le rayon du robot.
        rayon_roue (float): le rayon des deux roues.
        distance_roues (float): la distance entre les deux roues du robot.
        vitesse_roue_gauche (float): vitesse angulaire de la roue gauche du robot en radians par seconde.
        vitesse_roue_droite (float): vitesse angulaire de la roue droite du robot en radians par seconde.
        historique (list): une liste de tuples de la position x, y du robot à chaque instant.
    """
    def __init__(self):
        """
        Initialise un objet de la classe Robot avec les paramètres donnés.
        """
       
        self.orientation = constantes.Orientation
        self.rayon_robot=constantes.Rayon_Robot
        self.rayon_roue = constantes.Rayon_Roue
        self.distance_roues = constantes.Distance_Roues
        self.vitesse_roue_gauche = 0.0
        self.vitesse_roue_droite = 0.0
        
    
    def set_vitesse(self, vitesse_roue_gauche, vitesse_roue_droite):
        """
        Définit les vitesses de la roue gauche et droite du robot.
        """
        self.vitesse_roue_gauche = vitesse_roue_gauche
        self.vitesse_roue_droite = vitesse_roue_droite

    def deplacement(self, delta_time):
        """
        Met à jour la position et l'orientation du robot en fonction des vitesses de ses roues.
        """
        print(self.x," ",self.y)
        vitesse_moyenne = (self.vitesse_roue_gauche + self.vitesse_roue_droite) / 2 
        vitesse_moyenne = vitesse_moyenne / (2 * math.pi * self.rayon_roue) #vitesse lineaire moyenne
        delta_x = vitesse_moyenne * math.cos(self.orientation) * delta_time 
        delta_y = vitesse_moyenne * math.sin(self.orientation) * delta_time 
        self.x += delta_x
        self.y += delta_y
        
        
        vitesse_angulaire = (self.vitesse_roue_droite - self.vitesse_roue_gauche) / (2 * math.pi * self.distance_roues) #la vitesse de rotation du robot autour de son axe central
        delta_orientation = vitesse_angulaire * delta_time #calcule le changement d'orientation
        self.orientation += delta_orientation #calcule la nouvelle orientation
    