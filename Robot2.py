import math

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
    def __init__(self, x, y, orientation, rayon_robot, rayon_roue, distance_roues):
        """
        Initialise un objet de la classe Robot avec les paramètres donnés.
        """
       
        self.x = x
        self.y = y
        self.orientation = orientation
        self.rayon_robot=rayon_robot
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

    
    
    
    
    




